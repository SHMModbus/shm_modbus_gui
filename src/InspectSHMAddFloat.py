from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QMessageBox
from enum import Enum

from py_ui import Ui_InspectSHMAddFloat


class DisplayType(Enum):
    FIXED = 0
    SCIENTIFIC = 1


class Register(Enum):
    AO = 0
    AI = 1


class InspectSHMFloat:

    def __init__(self, address: int, size: int, display_type: DisplayType, little_endian: bool,
                 reversed_registers: bool, name: str, register: Register) -> None:
        self.name = name
        self.address = address
        self.size = size
        self.display_type = display_type
        self.little_endian = little_endian
        self.reversed_registers = reversed_registers
        self.register = register

    def __format__(self, format_spec: any) -> str:
        return (f">>{self.name};{self.register};0x{self.address:04x};{self.size};{self.display_type};"
                f"{'little' if self.little_endian else 'big'}{'-reversed' if self.reversed_registers else ''}<<")


class InspectSHMAddFloat(QtWidgets.QWidget, Ui_InspectSHMAddFloat):
    closed = QtCore.Signal()
    add = QtCore.Signal(InspectSHMFloat)

    def __init__(self, shm_size_AO: int, shm_size_AI: int):
        super(InspectSHMAddFloat, self).__init__()
        self.setupUi(self)

        if shm_size_AO < 0:
            raise RuntimeError("shm_size_AO must not be negative")

        if shm_size_AI < 0:
            raise RuntimeError("shm_size_AI must not be negative")

        self.shm_size_AO = shm_size_AO
        self.shm_size_AI = shm_size_AI

        if self.shm_size_AO + self.shm_size_AI == 0:
            self.setDisabled(True)
            QMessageBox.warning(self, "No registers", "Cannot add float: Number of AI and AO registers is 0.")
            raise RuntimeWarning("No registers")

        if self.shm_size_AO == 0:
            self.reg_AO.setEnabled(False)
            self.reg_AI.setChecked(True)

        if self.shm_size_AI == 0:
            self.reg_AI.setEnabled(False)
            self.reg_AO.setChecked(True)

        self.address.setMaximum(self.shm_size_AO - 4)
        self.address_dec.setMaximum(self.shm_size_AO - 4)
        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.reg_AO.clicked.connect(self.on_reg_ao)
        self.reg_AI.clicked.connect(self.on_reg_ai)

        self.size_4.clicked.connect(lambda: self.on_size_i(4))
        self.size_8.clicked.connect(lambda: self.on_size_i(8))

        self.button_add.clicked.connect(self.on_add_clicked)

    def on_reg_ao(self):
        self.address.setMaximum(self.shm_size_AO - 1)
        self.address_dec.setMaximum(self.shm_size_AO - 1)

    def on_reg_ai(self):
        self.address.setMaximum(self.shm_size_AI - 1)
        self.address_dec.setMaximum(self.shm_size_AI - 1)

    def on_size_i(self, i):
        reg_size = self.shm_size_AO if self.reg_AO.isChecked() else self.shm_size_AI
        self.address.setMaximum(reg_size - i)
        self.address_dec.setMaximum(reg_size - i)

    def on_add_clicked(self):
        if self.size_4.isChecked():
            size = 4
        elif self.size_8.isChecked():
            size = 8
        else:
            raise RuntimeError("Floaternal error: no size radio button checked")

        if self.type_fixed.isChecked():
            display_type = DisplayType.FIXED
        elif self.type_scientific.isChecked():
            display_type = DisplayType.SCIENTIFIC
        else:
            raise RuntimeError("Floaternal error: no display type radio button checked")

        little_endian = self.endian_little.isChecked() or not self.endian_little.isEnabled()
        reversed_registers = self.endian_reversed.isChecked() and self.endian_reversed.isEnabled()

        self.add.emit(InspectSHMFloat(self.address.value(), size, display_type, little_endian,
                                      reversed_registers, self.name.text(),
                                      Register.AI if self.reg_AI.isChecked() else Register.AO))
        self.close()

    def closeEvent(self, event):
        super(InspectSHMAddFloat, self).closeEvent(event)
        self.closed.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = InspectSHMAddFloat(16, 32)
    window.closed.connect(lambda: print("window closed"))
    window.add.connect(lambda x: print(f"{x}"))
    window.show()

    app.exec()
