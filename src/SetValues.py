import enum

from PySide6 import QtWidgets, QtCore

from src.py_ui import Ui_SetValues


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

    def on_button_add_int(self) -> None:
        pass

    def on_button_add_bool(self) -> None:
        pass

    def on_button_add_float(self) -> None:
        pass

    def on_button_apply_all(self) -> None:
        pass

    def on_actions_save(self) -> None:
        pass

    def on_action_load(self) -> None:
        pass
