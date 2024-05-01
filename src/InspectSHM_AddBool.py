from PySide6 import QtWidgets, QtCore

from .py_ui import Ui_InspectSHMAddBool


class InspectSHM_AddBool(QtWidgets.QWidget, Ui_InspectSHMAddBool):
    closed = QtCore.Signal()
    add_cfg = QtCore.Signal(tuple)

    def __init__(self, num_DO: int, num_DI: int, num_AO: int, num_AI: int, id: int) -> None:
        super(InspectSHM_AddBool, self).__init__()
        self.setupUi(self)

        self.num_DO = num_DO
        self.num_DI = num_DI
        self.num_AO = num_AO
        self.num_AI = num_AI
        self.id = id

        self.address.setMaximum(num_DO - 1)
        self.address_dec.setMaximum(num_DO - 1)

        self.address.valueChanged.connect(lambda x: self.address_dec.setValue(x))
        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))

        self.button_add.clicked.connect(self.on_button_add)

        self.reg_DO.clicked.connect(self.on_reg_DO)
        self.reg_DI.clicked.connect(self.on_reg_DI)
        self.reg_AO.clicked.connect(self.on_reg_AO)
        self.reg_AI.clicked.connect(self.on_reg_AI)

    def set_addr_max(self, num_regs):
        addr_max = num_regs - 1
        self.address.setMaximum(addr_max)
        self.address_dec.setMaximum(addr_max)

    def on_reg_DO(self):
        self.set_addr_max(self.num_DO)
        self.bit.setEnabled(False)
        self.bit.setValue(0)
        self.endian_big.setEnabled(False)
        self.endian_little.setEnabled(False)

    def on_reg_DI(self):
        self.set_addr_max(self.num_DI)
        self.bit.setEnabled(False)
        self.bit.setValue(0)
        self.endian_big.setEnabled(False)
        self.endian_little.setEnabled(False)

    def on_reg_AO(self):
        self.set_addr_max(self.num_AO)
        self.bit.setEnabled(True)
        self.endian_big.setEnabled(True)
        self.endian_little.setEnabled(True)

    def on_reg_AI(self):
        self.set_addr_max(self.num_AI)
        self.bit.setEnabled(True)
        self.endian_big.setEnabled(True)
        self.endian_little.setEnabled(True)

    def on_button_add(self):
        register_addr = self.address.value()
        shm_addr = register_addr
        register_bit = 0
        bit = 0

        if self.reg_DO.isChecked():
            register = "DO"
        elif self.reg_DI.isChecked():
            register = "DI"
        else:
            register = "AO" if self.reg_AO.isChecked() else "AI"
            shm_addr *= 2

            register_bit = self.bit.value()
            bit = register_bit
            little_endian = self.endian_little.isChecked()

            if bit > 7:
                bit -= 8
                if little_endian:
                    shm_addr += 1
            else:
                if not little_endian:
                    shm_addr += 1

        cfg_string = f"{shm_addr}:{bit},b,bool_X_{self.id}"
        self.add_cfg.emit(
            (
                cfg_string,
                {
                    "name": self.name.text(),
                    "true": self.true_text.text(),
                    "false": self.false_text.text(),
                },
                register,
                f"0x{register_addr:04x}:{register_bit}",
                "bit",
                "bool"
            )
        )
        self.close()

    def closeEvent(self, event) -> None:
        super(InspectSHM_AddBool, self).closeEvent(event)
        self.closed.emit()
