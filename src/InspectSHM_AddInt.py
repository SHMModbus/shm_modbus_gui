from PySide6 import QtWidgets, QtCore

from .py_ui import Ui_InspectSHMAddInt


class InspectSHM_AddInt(QtWidgets.QWidget, Ui_InspectSHMAddInt):
    closed = QtCore.Signal()
    add_cfg = QtCore.Signal(tuple)

    def __init__(self, num_AO: int, num_AI: int, id: int) -> None:
        super(InspectSHM_AddInt, self).__init__()
        self.setupUi(self)

        self.num_AO = num_AO
        self.num_AI = num_AI
        self.id = id

        self.address.setMaximum(num_AO - 1)
        self.address_dec.setMaximum(num_AO - 1)

        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.size_1_lo.clicked.connect(lambda: self.on_size_changed(1))
        self.size_1_hi.clicked.connect(lambda: self.on_size_changed(1))
        self.size_2.clicked.connect(lambda: self.on_size_changed(2))
        self.size_4.clicked.connect(lambda: self.on_size_changed(4))
        self.size_8.clicked.connect(lambda: self.on_size_changed(8))

        self.button_add.clicked.connect(self.on_button_add)

    def set_addr_max(self, size):
        num_regs = self.num_AO if self.reg_AO.isChecked() else self.num_AI

        addr_max = num_regs - (size + 1) // 2
        self.address.setMaximum(addr_max)
        self.address_dec.setMaximum(addr_max)

    def on_size_changed(self, size: int):
        assert size in [1, 2, 4, 8]

        self.endian_little.setEnabled(size > 1)
        self.endian_big.setEnabled(size > 1)
        self.endian_reversed.setEnabled(size > 2)

        self.set_addr_max(size)

    def on_reg_changed(self):
        if self.size_1_lo.isChecked() or self.size_1_hi.isChecked():
            size = 1
        elif self.size_2.isChecked():
            size = 2
        elif self.size_4.isChecked():
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

        if self.size_1_lo.isChecked():
            size = 8
        elif self.size_1_hi.isChecked():
            size = 8
            shm_addr += 1
        elif self.size_2.isChecked():
            size = 16
        elif self.size_4.isChecked():
            size = 32
        elif self.size_8.isChecked():
            size = 64
        else:
            raise RuntimeError("No size radio button checked")

        data_type_char = 'u'
        if self.type_signed.isChecked():
            data_type_char = 'i'
            format_char = 'd'
        elif self.type_unsigned.isChecked():
            format_char = 'u'
        elif self.type_hex.isChecked():
            format_char = 'x'
        elif self.type_oct.isChecked():
            format_char = 'o'
        elif self.type_bin.isChecked():
            format_char = 'b'
        else:
            raise RuntimeError("No type radio button is checked")

        endian = ''
        if size > 8:
            endian += 'l' if self.endian_little else 'b'
        if size > 16 and self.endian_reversed.isChecked():
            endian += 'r'

        cfg_string = f"{shm_addr},{data_type_char}{size}{endian},int_{format_char}_{self.id}"
        self.add_cfg.emit(
            (
                cfg_string,
                {
                   "name": self.name.text(),
                },
                register,
                f"0x{register_addr:04x}",
                f"{size}",
                "int"
            )
        )
        self.close()

    def closeEvent(self, event) -> None:
        super(InspectSHM_AddInt, self).closeEvent(event)
        self.closed.emit()
