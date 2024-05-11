from PySide6 import QtWidgets, QtCore

from .py_ui import Ui_InspectSHMAddString


class InspectSHM_AddString(QtWidgets.QWidget, Ui_InspectSHMAddString):
    closed = QtCore.Signal()
    add_cfg = QtCore.Signal(tuple)

    def __init__(self, num_AO: int, num_AI: int, id: int) -> None:
        super(InspectSHM_AddString, self).__init__()
        self.setupUi(self)

        self.num_AO = num_AO
        self.num_AI = num_AI
        self.id = id

        self.address.setMaximum(num_AO - 1)
        self.address_dec.setMaximum(num_AO - 1)
        self.length.setMaximum(num_AO * 2)

        self.address_dec.valueChanged.connect(lambda x: self.address.setValue(x))
        self.address.valueChanged.connect(self.on_addr_value_changed)
        self.length.valueChanged.connect(self.on_length_value_changed)
        self.reg_AO.clicked.connect(self.on_reg_changed)
        self.reg_AI.clicked.connect(self.on_reg_changed)

        self.button_add.clicked.connect(self.on_button_add)

    def on_addr_value_changed(self, value):
        num_regs = self.num_AO if self.reg_AO.isChecked() else self.num_AI
        self.address_dec.setValue(value)
        self.length.setMaximum(num_regs * 2 - value)

    def on_length_value_changed(self, value):
        num_regs = self.num_AO if self.reg_AO.isChecked() else self.num_AI
        max_addr = num_regs - (value + 1) // 2
        self.address.setMaximum(max_addr)
        self.address_dec.setMaximum(max_addr)

    def on_reg_changed(self):
        num_regs = self.num_AO if self.reg_AO.isChecked() else self.num_AI
        self.length.setMaximum(num_regs * 2)
        length = self.length.value()
        max_addr = num_regs - (length + 1) // 2
        self.address.setMaximum(max_addr)
        self.address_dec.setMaximum(max_addr)

    def on_button_add(self):
        register = "AO" if self.reg_AO.isChecked() else "AI"

        register_addr = self.address.value()
        shm_addr = register_addr * 2

        length = self.length.value()

        cfg_string = f"{shm_addr},s{length},string_{self.id}"
        self.add_cfg.emit(
            (
                cfg_string,
                {
                    "name": self.name.text(),
                },
                register,
                f"0x{register_addr:04x}",
                f"{length}",
                "string"
            )
        )
        self.close()

    def closeEvent(self, event) -> None:
        super(InspectSHM_AddString, self).closeEvent(event)
        self.closed.emit()
