from PySide6 import QtWidgets, QtCore

from .py_ui import Ui_SetValuesAddBool


class SetValues_AddBool(QtWidgets.QWidget, Ui_SetValuesAddBool):
    closed = QtCore.Signal()
    # name, register, addr, data_type, size, endian, value, input_regex
    add_cfg = QtCore.Signal(str, str, int, str, int, str, str, str)

    def __init__(self, num_DO: int, num_DI: int) -> None:
        super(SetValues_AddBool, self).__init__()
        self.setupUi(self)

        self.num_DO = num_DO
        self.num_DI = num_DI

        self.address.setMaximum(num_DO - 1)
        self.address_dec.setMaximum(num_DO - 1)

        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.button_add.clicked.connect(self.on_button_add)

        self.reg_DO.clicked.connect(lambda: self.set_addr_max(self.num_DO))
        self.reg_DI.clicked.connect(lambda: self.set_addr_max(self.num_DI))

    def set_addr_max(self, num_regs):
        addr_max = num_regs - 1
        self.address.setMaximum(addr_max)
        self.address_dec.setMaximum(addr_max)

    def on_button_add(self):
        name = self.name.text()
        register = "DO" if self.reg_DO.isChecked() else "DI"
        addr = self.address.value()
        data_type = None
        size = 0
        endian = None
        value = "0"
        input_regex = None

        self.add_cfg.emit(name, register, addr, data_type, size, endian, value, input_regex)

        self.close()

    def closeEvent(self, event) -> None:
        super(SetValues_AddBool, self).closeEvent(event)
        self.closed.emit()
