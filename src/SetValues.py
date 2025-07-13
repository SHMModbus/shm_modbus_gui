import enum
import hashlib
import json
from datetime import datetime

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt, QMutex, QProcess
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QInputDialog, QMessageBox, QFileDialog

from .SetValues_AddFloat import SetValues_AddFloat
from .SetValues_AddInt import SetValues_AddInt
from .SetValues_AddBool import SetValues_AddBool
from .py_ui import Ui_SetValues


class SetValuesEntry:
    fixed_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)

    class TableCols(enum.IntEnum):
        NAME = 0
        REGISTER = 1
        ADDR = 2
        TYPE = 3
        SIZE = 4
        ENDIAN = 5
        VALUE = 6
        BUTTON_EDIT = 7
        TIME = 8
        BUTTON_APPLY = 9
        BUTTON_DELETE = 10

    class ValueType(enum.IntEnum):
        BOOL = 0,
        INT = 1,
        FLOAT = 2,

    def __init__(self, index, parent, prefix: str, value: str, suffix: str, name: str, register: str, addr: str,
                 size: int,
                 endian_str: str, value_type: ValueType, type_str: str):
        self.index = index
        self.parent = parent
        self.data_table = parent.data_table
        self.prefix = prefix
        self.value = value
        self.suffix = suffix
        self.name = name
        self.register = register
        self.addr = addr
        self.size = size
        self.endian_str = endian_str
        self.value_type = value_type
        self.type_str = type_str

        self.value_widget = None
        self.time_widget = None

        self.create_table_entry()

    def create_table_entry(self) -> None:
        self.data_table.setSortingEnabled(False)

        current_row = self.data_table.rowCount()
        self.data_table.setRowCount(current_row + 1)

        self.data_table.setItem(current_row, int(self.TableCols.NAME), QTableWidgetItem(self.name))
        self.data_table.setItem(current_row, int(self.TableCols.REGISTER), QTableWidgetItem(self.register))
        addr_widget = QTableWidgetItem(self.addr)
        addr_widget.setFont(self.fixed_font)
        addr_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.ADDR), addr_widget)
        self.data_table.setItem(current_row, int(self.TableCols.TYPE), QTableWidgetItem(self.type_str))
        size_widget = QTableWidgetItem(f"{self.size}" if self.size > 0 else "")
        size_widget.setFont(self.fixed_font)
        size_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.SIZE), size_widget)
        self.data_table.setItem(current_row, int(self.TableCols.ENDIAN), QTableWidgetItem(self.endian_str))
        self.value_widget = QTableWidgetItem(self.value)
        self.value_widget.setFont(self.fixed_font)
        self.value_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.VALUE), self.value_widget)
        self.time_widget = QTableWidgetItem("#####")
        self.data_table.setItem(current_row, int(self.TableCols.TIME), self.time_widget)

        delete_button = QPushButton()
        delete_button.setText("del")
        delete_button.clicked.connect(self.destroy)
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON_DELETE), delete_button)

        edit_button = QPushButton()
        edit_button.setText("edit")
        edit_button.clicked.connect(self.edit_value)
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON_EDIT), edit_button)

        apply_button = QPushButton()
        apply_button.setText("apply")
        apply_button.clicked.connect(lambda: self.parent.execute(self.index))
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON_APPLY), apply_button)

        self.data_table.setSortingEnabled(True)

    def destroy(self):
        self.parent.exec_mutex.lock()
        self.data_table.setSortingEnabled(False)
        i = self.value_widget.row()
        self.data_table.removeRow(i)
        self.data_table.setSortingEnabled(True)
        self.parent.delete_cfg(self.index)
        self.parent.exec_mutex.unlock()

    def get_command(self) -> str:
        return f"{self.prefix}{self.value}{self.suffix}"

    def set_time(self, time_str):
        self.time_widget.setText(time_str)

    def edit_value(self):
        ok = False
        value = None
        match self.value_type:
            case self.ValueType.BOOL:
                value, ok = QInputDialog.getInt(self.parent, "Edit Bool", "Bool value: ", value=int(self.value),
                                                minValue=0, maxValue=1)
            case self.ValueType.INT:
                if self.suffix[1] == "i":
                    min_value = max(-((2 ** self.size) / 2), -2147483647)
                    max_value = min((2 ** self.size) / 2 - 1, 2147483647)
                else:
                    min_value = 0
                    max_value = min(2 ** self.size - 1, 2147483647)

                value, ok = QInputDialog.getInt(self.parent, "Edit Integer", "Integer value: ", value=int(self.value),
                                                minValue=min_value, maxValue=max_value)

            case self.ValueType.FLOAT:
                value, ok = QInputDialog.getDouble(self.parent, "Edit Float", "Float value: ", value=float(self.value),
                                                   decimals=4)

        if ok:
            self.value = f"{value}"
            self.value_widget.setText(self.value)

    def to_json_dict(self) -> dict:
        return {
            "name": self.name,
            "prefix": self.prefix,
            "value": self.value,
            "suffix": self.suffix,
            "register": self.register,
            "addr": self.addr,
            "size": self.size,
            "endian_str": self.endian_str,
            "value_type": self.value_type.value,
            "type_str": self.type_str
        }

    @classmethod
    def from_json_dict(cls, index, parent, json_dict: dict):
        expected_keys = [
            ("name", str),
            ("prefix", str),
            ("value", str),
            ("suffix", str),
            ("register", str),
            ("addr", str),
            ("size", int),
            ("endian_str", str),
            ("value_type", int),
            ("type_str", str),
        ]

        for key, dtype in expected_keys:
            if key not in json_dict:
                raise RuntimeError(f"missing key '{key}'")
            if not isinstance(json_dict[key], dtype):
                raise RuntimeError(f"key '{key}' has invalid data type")

        return cls(index, parent, json_dict["prefix"], json_dict["value"], json_dict["suffix"], json_dict["name"],
                   json_dict["register"], json_dict["addr"], json_dict["size"], json_dict["endian_str"],
                   SetValuesEntry.ValueType(json_dict["value_type"]), json_dict["type_str"])


    @classmethod
    def create(cls, index, parent, prefix: str, value: str, suffix: str, name: str, register: str, addr: str,
               size: int,
               endian_str: str,
               value_type: ValueType,
               type_str: str):
        return cls(index, parent, prefix, value, suffix, name, register, addr, size, endian_str, value_type, type_str)


class SetValues(QtWidgets.QMainWindow, Ui_SetValues):
    closed = QtCore.Signal(str)

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

        self.cfg_index = 0
        self.cfg_data = {}

        self.exec_mutex = QMutex()

        self.setWindowTitle(f"{self.windowTitle()} {self.name_prefix}*")

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

    def __add_cfg(self, name: str, register: str, addr: int, data_type: str | None, size: int, endian: str | None,
                  value: str, emitter: QtWidgets.QWidget, endian_str: str, type_str: str):
        if isinstance(emitter, SetValues_AddBool):
            value_type = SetValuesEntry.ValueType.BOOL
        elif isinstance(emitter, SetValues_AddInt):
            value_type = SetValuesEntry.ValueType.INT
        else:
            value_type = SetValuesEntry.ValueType.FLOAT

        self.exec_mutex.lock()
        self.cfg_data[self.cfg_index] = SetValuesEntry.create(self.cfg_index, self, f"{register}:{addr}:", f"{value}",
                                                              f":{data_type}{size}{endian}" if data_type and endian else "",
                                                              name, register, f"0x{addr:04x}", size, endian_str,
                                                              value_type, type_str)
        self.exec_mutex.unlock()
        self.cfg_index += 1

    def on_button_add_int(self) -> None:
        self.setEnabled(False)
        if self.add_window:
            raise RuntimeError("Internal Error: add_window exists")
        self.add_window = SetValues_AddInt(self.num_AO, self.num_AI)
        self.add_window.closed.connect(self.add_done)
        self.add_window.add_cfg.connect(self.__add_cfg)
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
        self.add_window.add_cfg.connect(self.__add_cfg)
        self.add_window.show()

    def on_button_apply_all(self) -> None:
        self.execute(None)

    def on_actions_save(self) -> None:
        file_name, _ = QFileDialog.getSaveFileName(self, caption="Save config")
        if len(file_name) <= 0:
            return

        self.exec_mutex.lock()

        json_data = []
        for cfg in self.cfg_data.values():
            json_data.append(cfg.to_json_dict())

        json_str = json.dumps(json_data)
        cfg_hash = hashlib.sha256(json_str.encode("utf-8")).hexdigest()

        try:
            with open(file_name, 'w') as f:
                print(cfg_hash, file=f)
                print(json_str, file=f)
        except Exception as e:
            QMessageBox.warning(self, "Failed to write config", f"{e}")

        self.exec_mutex.unlock()

    def on_action_load(self) -> None:
        file_name, _ = QFileDialog.getOpenFileName(self, caption="Load config")
        if len(file_name) <= 0:
            return

        self.exec_mutex.lock()

        try:
            with open(file_name, 'r') as f:
                cfg_lines = [x.strip() for x in f.readlines()]
        except Exception as e:
            QMessageBox.warning(self, "Failed to read config", f"{e}")
            self.exec_mutex.unlock()
            return

        if len(cfg_lines) != 2:
            QMessageBox.warning(self, "Invalid file", f"Content of selected file is invalid.")
            self.exec_mutex.unlock()
            return

        cfg_hash_file = cfg_lines[0]
        cfg_json = cfg_lines[1]

        cfg_hash = hashlib.sha256(cfg_json.encode("utf-8")).hexdigest()
        if cfg_hash_file != cfg_hash:
            QMessageBox.warning(self, "Invalid file", f"Content hash is invalid.")
            self.exec_mutex.unlock()
            return

        loaded_cfg = json.loads(cfg_json)
        if not isinstance(loaded_cfg, list):
            QMessageBox.warning(self, "Invalid file", f"Content of selected file is invalid: expected a list.")
            self.exec_mutex.unlock()
            return

        # TODO check if entries in table, if yes: ask user to save
        if self.data_table.rowCount() > 0:
            pass

        # clear table and config
        self.data_table.setRowCount(0)
        self.cfg_index = len(loaded_cfg)
        self.cfg_data = {}

        for i, cfg in enumerate(loaded_cfg):
            try:
                self.cfg_data[i] = SetValuesEntry.from_json_dict(i, self, cfg)
            except RuntimeError as e:
                QMessageBox.warning(self, "Failed to load config", f"index: {i}\n{e}")
                continue

        self.exec_mutex.unlock()

    def delete_cfg(self, index: int):
        del self.cfg_data[index]

    def execute(self, index: int | None):
        self.exec_mutex.lock()
        command_list = []
        if index:
            command_list.append(self.cfg_data[index].get_command())
        else:
            for cfg in self.cfg_data.values():
                command_list.append(cfg.get_command())

        if len(command_list) == 0:
            self.exec_mutex.unlock()
            return

        cmd_args = ['-n', f'{self.name_prefix}', '--pid', '0']
        if self.semaphore:
            cmd_args.append('--semaphore')
            cmd_args.append(f'{self.semaphore}')
            cmd_args.append('--semaphore-timeout')
            cmd_args.append('1')

        process = QProcess()
        process.start("stdin-to-modbus-shm", cmd_args)
        if process.waitForStarted(1000):
            process.write("\n".join(command_list).encode())
            process.closeWriteChannel()
            if process.waitForFinished(1000):
                if process.exitCode() != 0:
                    stderr = bytes(process.readAllStandardError()).decode("utf-8")
                    QMessageBox.warning(self, "stdin-to-modbus-shm failed", stderr)
                else:
                    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                    if index:
                        self.cfg_data[index].set_time(time)
                    else:
                        for cfg in self.cfg_data.values():
                            cfg.set_time(time)
            else:
                process.terminate()
        else:
            process.terminate()

        self.exec_mutex.unlock()

    def closeEvent(self, event):
        super(SetValues, self).closeEvent(event)
        if self.add_window:
            self.add_window.close()
        self.closed.emit(self.name_prefix)
