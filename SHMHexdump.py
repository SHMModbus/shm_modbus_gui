from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QProcess
from PySide6.QtGui import QFontDatabase, QTextCursor
from PySide6.QtWidgets import QMessageBox

from py_ui import Ui_ShmHexdump


class SHMHexdump(QtWidgets.QMainWindow, Ui_ShmHexdump):
    closed = QtCore.Signal()

    def __init__(self, shm_name: str, num_registers: int, register_size: int, semaphore: str | None = None) -> None:
        super(SHMHexdump, self).__init__()
        self.setupUi(self)

        self.shm_name = shm_name
        self.num_registers = num_registers
        self.register_size = register_size
        self.shm_size = num_registers * register_size
        self.semaphore = semaphore

        self.setWindowTitle(f"hexdump {self.shm_name}")

        self.offset.setMaximum(num_registers - 1)
        self.offset.setValue(0)
        self.registers.setMaximum(num_registers)
        self.registers.setValue(num_registers)

        self.spinbox_interval.setMaximum(self.slider_interval.maximum())
        self.spinbox_interval.setMinimum(self.slider_interval.minimum())
        self.spinbox_interval.setSingleStep(self.slider_interval.singleStep())
        self.spinbox_interval.setValue(self.slider_interval.value())

        fixed_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.hexdump_text.setFont(fixed_font)

        # ui actions
        self.button_refresh.clicked.connect(self.execute)
        self.slider_interval.valueChanged.connect(lambda value: self.spinbox_interval.setValue(value))
        self.spinbox_interval.valueChanged.connect(lambda value: self.slider_interval.setValue(value))

        def on_offset_value_changed(value: int):
            new_max = self.num_registers - value
            self.registers.setMaximum(new_max)
            if new_max < self.registers.value():
                self.registers.setValue(new_max)

        self.offset.valueChanged.connect(on_offset_value_changed)

        def on_registers_value_changed(value: int):
            new_max = self.num_registers - value
            self.offset.setMaximum(new_max)
            if new_max < self.offset.value():
                self.offset.setValue(new_max)

        self.registers.valueChanged.connect(on_registers_value_changed)

        def on_checkbox_autorefresh_clicked(state: int):
            if state != 0:
                QMessageBox.critical(self, "Not Implemented", "This feature is not yet implemented.")
                self.checkbox_autorefresh.setChecked(False)

        self.checkbox_autorefresh.stateChanged.connect(on_checkbox_autorefresh_clicked)

        # create hexdump
        self.execute()

    def execute(self):
        size = self.registers.value() * self.register_size
        offset = self.offset.value() * self.register_size
        sem_cmd = f" -s {self.semaphore}" if self.semaphore else ""
        command = f"dump-shm --bytes {size} --offset {offset} {self.shm_name}{sem_cmd} | hexdump -C -v"

        process = QProcess()
        process.start("bash", ["-c", command])
        if process.waitForFinished(min(self.slider_interval.value() * 0.8, 1000)):
            self.hexdump_text.clear()
            self.hexdump_text.insertPlainText(bytes(process.readAllStandardError()).decode("utf-8"))
            self.hexdump_text.moveCursor(QTextCursor.End)
            self.hexdump_text.insertPlainText(bytes(process.readAllStandardOutput()).decode("utf-8"))
        else:
            process.kill()
            self.hexdump_text.clear()
            self.hexdump_text.insertPlainText("COMMAND TIMEOUT")

    def closeEvent(self, event):
        super(SHMHexdump, self).closeEvent(event)
        self.closed.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = SHMHexdump("modbus_AO", 2 ** 16, 2)
    window.closed.connect(lambda: print("window closed"))
    window.show()

    app.exec()
