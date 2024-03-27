from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox

from .py_ui import Ui_RandomizeShm


class SHMRandom(QtWidgets.QWidget, Ui_RandomizeShm):
    closed = QtCore.Signal()

    def __init__(self, shm_name: str, num_registers: int, register_size: int, bitmask: int | None = None,
                 semaphore: str | None = None):
        super(SHMRandom, self).__init__()
        self.setupUi(self)

        self.shm_name = shm_name
        self.num_registers = num_registers
        self.register_size = register_size
        self.shm_size = num_registers * register_size
        self.bitmask = bitmask
        self.semaphore = semaphore

        self.setWindowTitle(f"randomize {self.shm_name}")

        self.offset.setMaximum(num_registers - 1)
        self.offset.setValue(0)
        self.registers.setMaximum(num_registers)
        self.registers.setValue(num_registers)

        self.spinbox_interval.setMaximum(self.slider_interval.maximum())
        self.spinbox_interval.setMinimum(self.slider_interval.minimum())
        self.spinbox_interval.setSingleStep(self.slider_interval.singleStep())
        self.spinbox_interval.setValue(self.slider_interval.value())

        # ui actions
        self.button_start.clicked.connect(self.on_button_start_clicked)
        self.button_once.clicked.connect(self.on_button_once_clicked)
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

        # internal variables
        self.process: QtCore.QProcess | None = None
        self.active: bool = False

    def __get_cmd(self):
        cmd = [
            "-n",
            self.shm_name,
            "-a",
            f"{self.register_size}",
            "-o",
            f"{self.offset.value()}",
            "-e",
            f"{self.registers.value()}",
        ]

        if self.semaphore:
            cmd.append("--semaphore")
            cmd.append(self.semaphore)

        if self.bitmask:
            cmd.append("-m")
            cmd.append(f"{self.bitmask:x}")

        return cmd

    def __options_enable(self, enable: bool) -> None:
        self.spinbox_interval.setEnabled(enable)
        self.slider_interval.setEnabled(enable)
        self.offset.setEnabled(enable)
        self.registers.setEnabled(enable)

    def on_button_start_clicked(self) -> None:
        if not self.active:
            self.__options_enable(False)
            self.button_once.setEnabled(False)
            self.button_start.setText("Stop")
            self.active = True

            cmd = self.__get_cmd()
            cmd += ["-i", f"{self.spinbox_interval.value()}"]

            self.process = QtCore.QProcess()
            self.process.finished.connect(self.on_process_finished)
            self.process.start("shared-mem-random", cmd)

            if not self.process.waitForStarted(min(self.slider_interval.value() * 0.8, 1000)):
                self.process.kill()
                QMessageBox.warning(self, "Command Timeout", "Execution of command shared-mem-random timed out")
        else:
            self.process.terminate()

    def on_button_once_clicked(self) -> None:
        self.button_start.setEnabled(False)
        self.button_once.setEnabled(False)
        self.__options_enable(False)

        cmd = self.__get_cmd()
        cmd += ["-l", "1"]

        self.process = QtCore.QProcess()
        self.process.finished.connect(self.on_process_finished)
        self.process.start("shared-mem-random", cmd)

        if not self.process.waitForFinished(1000):
            self.process.kill()
            QMessageBox.warning(self, "Command Timeout", "Execution of command shared-mem-random timed out")

    def on_process_finished(self, exit_code) -> None:
        self.button_start.setEnabled(True)
        self.button_once.setEnabled(True)
        self.button_start.setText("Start")
        self.__options_enable(True)
        self.active = False
        if exit_code != 0:
            stderr = bytes(self.process.readAllStandardError()).decode("utf-8")
            QMessageBox.warning(self, "Command Failed",
                                f"Execution of command shared-mem-random failed (exit code: {exit_code}):\n {stderr}")

    def closeEvent(self, event):
        super(SHMRandom, self).closeEvent(event)
        self.closed.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = SHMRandom("modbus_AO", 2 ** 16, 2, semaphore="modbus")
    window.closed.connect(lambda: print("window closed"))
    window.show()

    app.exec()
