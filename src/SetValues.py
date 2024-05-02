import enum

from PySide6 import QtWidgets, QtCore

from .SetValues_AddFloat import SetValues_AddFloat
from .SetValues_AddInt import SetValues_AddInt
from .SetValues_AddBool import SetValues_AddBool
from .py_ui import Ui_SetValues


class SetValues(QtWidgets.QMainWindow, Ui_SetValues):
    closed = QtCore.Signal()

    class TableCols(enum.IntEnum):
        NAME = 0
        REGISTER = 1
        ADDR = 2
        TYPE = 3
        SIZE = 4
        ENDIAN = 5
        VALUE = 6
        BTN_CHANGE_VALUE = 7
        TIME = 8
        BTN_APPLY = 9
        BTN_DELETE = 10

    def __init__(self, name_prefix: str, num_DO: int, num_DI: int, num_AO: int, num_AI: int,
                 semaphore: str | None = None) -> None:
        super(SetValues, self).__init__()
        self.setupUi(self)

        self.name_prefix = name_prefix
        self.num_DO = num_DO
        self.num_DI = num_DI
        self.num_AO = num_AO
        self.num_AI = num_AI
        self.semaphore = semaphore

        self.add_window = None

        self.__setup_buttons()
        self.__setup_actions()

    def __setup_buttons(self) -> None:
        self.button_add_int.clicked.connect(self.on_button_add_int)
        self.button_add_bool.clicked.connect(self.on_button_add_bool)
        self.button_add_float.clicked.connect(self.on_button_add_float)
        self.button_apply_all.clicked.connect(self.on_button_apply_all)

    def __setup_actions(self) -> None:
        self.actionsave_config.triggered.connect(self.on_actions_save)
        self.actionload_config.triggered.connect(self.on_action_load)

    def add_done(self):
        self.setEnabled(True)
        self.add_window = None

    def __add_cfg(self, name: str, register: str, addr: int, data_type: str | None, size: str, endian: str | None, value: str, input_regex: str | None):
        print(f"{name},{register},{addr},{data_type},{size},{endian},{value},{input_regex}")
        cfg_line = f"{register}:{addr}:{value}"
        if data_type and endian:
            cfg_line += f"{data_type}{size}{endian}"
        print(cfg_line)

        # TODO store confif

        # TODO create table entry

    def on_button_add_int(self) -> None:
        self.setEnabled(False)
        if self.add_window:
            raise RuntimeError("Internal Error: add_window exists")
        self.add_window = SetValues_AddInt(self.num_AO, self.num_AI)
        self.add_window.closed.connect(self.add_done)
        # TODO
        #self.add_window.add_cfg.connect(self.__add_cfg)
        self.add_window.show()

    def on_button_add_bool(self) -> None:
        self.setEnabled(False)
        if self.add_window:
            raise RuntimeError("Internal Error: add_window exists")
        self.add_window = SetValues_AddBool(self.num_DO, self.num_DI)
        self.add_window.closed.connect(self.add_done)
        self.add_window.add_cfg.connect(self.__add_cfg)
        self.add_window.show()

    def on_button_add_float(self) -> None:
        self.setEnabled(False)
        if self.add_window:
            raise RuntimeError("Internal Error: add_window exists")
        self.add_window = SetValues_AddFloat(self.num_AO, self.num_AI)
        self.add_window.closed.connect(self.add_done)
        # TODO
        # self.add_window.add_cfg.connect(self.__add_cfg)
        self.add_window.show()

    def on_button_apply_all(self) -> None:
        pass

    def on_actions_save(self) -> None:
        pass

    def on_action_load(self) -> None:
        pass
