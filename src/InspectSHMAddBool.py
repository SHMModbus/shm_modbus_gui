from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox
from enum import Enum

from py_ui import Ui_InspectSHMAddBool


class Register(Enum):
    AO = 0
    AI = 1
    DO = 2
    DI = 3


class InspectSHMBool:

    def __init__(self, address: int, bit: int, true_str: str, false_str: str, little_endian: bool, name: str,
                 register: Register) -> None:
        self.name = name
        self.address = address
        self.bit = bit
        self.true_str = true_str
        self.false_str = false_str
        self.little_endian = little_endian
        self.register = register

    def __format__(self, format_spec: any) -> str:
        return (f">>{self.name};{self.register};0x{self.address:04x}:{self.bit};{self.true_str};{self.false_str};"
                f"{'little' if self.little_endian else 'big'}<<")


class InspectSHMAddBool(QtWidgets.QWidget, Ui_InspectSHMAddBool):
    closed = QtCore.Signal()
    add = QtCore.Signal(InspectSHMBool)

    def __init__(self, shm_size_DO: int, shm_size_DI: int, shm_size_AO: int, shm_size_AI: int):
        super(InspectSHMAddBool, self).__init__()
        self.setupUi(self)

        if shm_size_DO < 0:
            raise RuntimeError("shm_size_DO must not be negative")

        if shm_size_DI < 0:
            raise RuntimeError("shm_size_DI must not be negative")

        if shm_size_AO < 0:
            raise RuntimeError("shm_size_AO must not be negative")

        if shm_size_AI < 0:
            raise RuntimeError("shm_size_AI must not be negative")

        self.shm_size_DO = shm_size_DO
        self.shm_size_DI = shm_size_DI
        self.shm_size_AO = shm_size_AO
        self.shm_size_AI = shm_size_AI

        if self.shm_size_AO + self.shm_size_AI == 0:
            self.setDisabled(True)
            QMessageBox.warning(self, "No registers", "Cannot add bool: Number of DO, DI, AI and AO registers is 0.")
            raise RuntimeWarning("No registers")

        if self.shm_size_DO == 0:
            self.reg_DO.setEnabled(False)
            self.reg_DI.setChecked(True)

        if self.shm_size_DI == 0:
            self.reg_DI.setEnabled(False)
            self.reg_AO.setChecked(True)

        if self.shm_size_AO == 0:
            self.reg_AO.setEnabled(False)
            self.reg_AI.setChecked(True)

        self.address.setMaximum(self.shm_size_AO - 1)
        self.address_dec.setMaximum(self.shm_size_AO - 1)
        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.reg_DO.clicked.connect(self.on_reg_d)
        self.reg_DI.clicked.connect(self.on_reg_d)

        self.reg_AO.clicked.connect(self.on_reg_a)
        self.reg_AI.clicked.connect(self.on_reg_a)

        self.button_add.clicked.connect(self.on_add_clicked)

    def on_reg_d(self):
        self.bit.setValue(0)
        self.bit.setDisabled(True)
        self.endian_little.setEnabled(False)
        self.endian_big.setEnabled(False)

    def on_reg_a(self):
        self.bit.setMaximum(15)
        self.bit.setEnabled(True)
        self.endian_little.setEnabled(True)
        self.endian_big.setEnabled(True)

    def on_add_clicked(self):
        address = self.address.value()

        if self.reg_DO.isChecked():
            register = Register.DO
        elif self.reg_DI.isChecked():
            register = Register.DI
        elif self.reg_AO.isChecked():
            register = Register.AO
        elif self.reg_AI.isChecked():
            register = Register.AI
        else:
            raise RuntimeError("No register radio button selected")

        bit = self.bit.value()
        name = self.name.text()

        true_str = self.true_text.text()
        false_str = self.false_text.text()

        little_endian = self.endian_little.isChecked() or not self.endian_little.isEnabled()

        self.add.emit(InspectSHMBool(address, bit, true_str, false_str, little_endian, name, register))
        self.close()

    def closeEvent(self, event):
        super(InspectSHMAddBool, self).closeEvent(event)
        self.closed.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = InspectSHMAddBool(16, 20, 24, 28)
    window.closed.connect(lambda: print("window closed"))
    window.add.connect(lambda x: print(f"{x}"))
    window.show()

    app.exec()
