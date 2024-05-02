from PySide6 import QtWidgets, QtCore

from .py_ui import Ui_SetValuesAddFloat


class SetValues_AddFloat(QtWidgets.QWidget, Ui_SetValuesAddFloat):
    closed = QtCore.Signal()
    add_cfg = QtCore.Signal(tuple)

    def __init__(self, num_AO: int, num_AI: int) -> None:
        super(SetValues_AddFloat, self).__init__()
        self.setupUi(self)

        self.num_AO = num_AO
        self.num_AI = num_AI

        self.address.setMaximum(num_AO - 1)
        self.address_dec.setMaximum(num_AO - 1)

        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.size_4.clicked.connect(lambda: self.on_size_changed(4))
        self.size_8.clicked.connect(lambda: self.on_size_changed(8))

        self.button_add.clicked.connect(self.on_button_add)

    def set_addr_max(self, size):
        num_regs = self.num_AO if self.reg_AO.isChecked() else self.num_AI

        addr_max = num_regs - (size + 1) // 2
        self.address.setMaximum(addr_max)
        self.address_dec.setMaximum(addr_max)

    def on_size_changed(self, size: int):
        assert size in [4, 8]
        self.set_addr_max(size)

    def on_reg_changed(self):
        if self.size_4.isChecked():
            size = 4
        elif self.size_8.isChecked():
            size = 8
        else:
            raise RuntimeError("No size radio button checked")

        self.set_addr_max(size)

    def on_button_add(self):
        register = "AO" if self.reg_AO.isChecked() else "AI"

        register_addr = self.address.value()
        shm_addr = register_addr * 2

        size = 32 if self.size_4.isChecked() else 64

        endian = 'l' if self.endian_little.isChecked() else 'b'
        if self.endian_reversed.isChecked():
            endian += 'r'

        # TODO emit signal

        self.close()

    def closeEvent(self, event) -> None:
        super(SetValues_AddFloat, self).closeEvent(event)
        self.closed.emit()
