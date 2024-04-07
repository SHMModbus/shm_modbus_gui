from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox
from enum import Enum

from py_ui import Ui_InspectSHMAddCharArray


class Register(Enum):
    AO = 0
    AI = 1


class InspectSHMCharArray:

    def __init__(self, address: int, size: int, name: str, register: Register) -> None:
        self.name = name
        self.address = address
        self.size = size
        self.register = register

    def __format__(self, format_spec: any) -> str:
        return f">>{self.name};{self.register};0x{self.address:04x};{self.size}<<"


class InspectSHMAddCharArray(QtWidgets.QWidget, Ui_InspectSHMAddCharArray):
    closed = QtCore.Signal()
    add = QtCore.Signal(InspectSHMCharArray)

    def __init__(self, shm_size_AO: int, shm_size_AI: int):
        super(InspectSHMAddCharArray, self).__init__()
        self.setupUi(self)

        if shm_size_AO < 0:
            raise RuntimeError("shm_size_AO must not be negative")

        if shm_size_AI < 0:
            raise RuntimeError("shm_size_AI must not be negative")

        self.shm_size_AO = shm_size_AO
        self.shm_size_AI = shm_size_AI

        if self.shm_size_AO + self.shm_size_AI == 0:
            self.setDisabled(True)
            QMessageBox.warning(self, "No registers", "Cannot add char array: Number of AI and AO registers is 0.")
            raise RuntimeWarning("No registers")

        if self.shm_size_AO == 0:
            self.reg_AO.setEnabled(False)
            self.reg_AI.setChecked(True)

        if self.shm_size_AI == 0:
            self.reg_AI.setEnabled(False)
            self.reg_AO.setChecked(True)

        self.address.setMaximum(self.shm_size_AO - 1)
        self.address_dec.setMaximum(self.shm_size_AO - 1)
        self.length.setMaximum(self.shm_size_AO)
        self.length.setMinimum(1)
        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.reg_AO.clicked.connect(self.on_reg_ao)
        self.reg_AI.clicked.connect(self.on_reg_ai)

        self.address.valueChanged.connect(self.on_addr_changed)
        self.length.valueChanged.connect(self.on_length_changed)

        self.button_add.clicked.connect(self.on_add_clicked)

    def on_reg_ao(self):
        self.address.setMaximum(max(0, self.shm_size_AO - self.length.value()))
        self.address_dec.setMaximum(max(0, self.shm_size_AO - self.length.value()))

        if self.length.value() > self.shm_size_AO:
            self.length.setValue(self.shm_size_AO)

    def on_reg_ai(self) -> None:
        self.address.setMaximum(max(0, self.shm_size_AI - self.length.value()))
        self.address_dec.setMaximum(max(0, self.shm_size_AI - self.length.value()))

        if self.length.value() > self.shm_size_AI:
            self.length.setValue(self.shm_size_AI)

    def on_addr_changed(self, value: int) -> None:
        reg_size = self.shm_size_AO if self.reg_AO.isChecked() else self.shm_size_AI
        self.length.setMaximum(reg_size - value)

    def on_length_changed(self, value: int) -> None:
        reg_size = self.shm_size_AO if self.reg_AO.isChecked() else self.shm_size_AI
        self.address.setMaximum(reg_size - value)
        self.address_dec.setMaximum(reg_size - value)

    def on_add_clicked(self):
        self.add.emit(InspectSHMCharArray(self.address.value(), self.length.value(), self.name.text(),
                                          Register.AI if self.reg_AI.isChecked() else Register.AO))
        self.close()

    def closeEvent(self, event):
        super(InspectSHMAddCharArray, self).closeEvent(event)
        self.closed.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = InspectSHMAddCharArray(16, 32)
    window.closed.connect(lambda: print("window closed"))
    window.add.connect(lambda x: print(f"{x}"))
    window.show()

    app.exec()
