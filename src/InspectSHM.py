import csv
import datetime
import enum
import hashlib
import json
import os
import tempfile

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QMutex, Qt, QProcess, QTimer
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox, QFileDialog

from .py_ui import Ui_InspectSHM
from .InspectSHM_AddInt import InspectSHM_AddInt
from .InspectSHM_AddFloat import InspectSHM_AddFloat
from .InspectSHM_AddBool import InspectSHM_AddBool
from .InspectSHM_AddString import InspectSHM_AddString


class InspectSHM(QtWidgets.QMainWindow, Ui_InspectSHM):
    closed = QtCore.Signal(str)

    class TableCols(enum.IntEnum):
        NAME = 0
        REGISTER = 1
        ADDR = 2
        TYPE = 3
        SIZE = 4
        ENDIAN = 5
        VALUE = 6
        TIME = 7
        BUTTON = 8

    def __init__(self, name_prefix: str, num_DO: int, num_DI: int, num_AO: int, num_AI: int,
                 semaphore: str | None = None) -> None:
        super(InspectSHM, self).__init__()
        self.setupUi(self)

        self.name_prefix = name_prefix
        self.num_AI = num_AI
        self.num_AO = num_AO
        self.num_DI = num_DI
        self.num_DO = num_DO
        self.next_id = 0
        self.semaphore = semaphore

        self.add_window = None

        self.exec_mutex = QMutex()
        self.fixed_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)

        # auto refresh timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.execute)

        self.shm_format_cfg = {
            "DO": {},
            "DI": {},
            "AO": {},
            "AI": {},
        }

        self.shm_format_widgets = {
            "DO": {},
            "DI": {},
            "AO": {},
            "AI": {},
        }

        self.shm_sizes = {
            "DO": num_DO,
            "DI": num_DI,
            "AO": num_AO * 2,
            "AI": num_AI * 2,
        }

        self.setWindowTitle(f"{self.windowTitle()} {self.name_prefix}*")

        self.__setup_add_buttons()

        self.spinbox_interval.valueChanged.connect(lambda x: self.slider_interval.setValue(x))
        self.slider_interval.valueChanged.connect(lambda x: self.spinbox_interval.setValue(x))
        self.slider_interval.valueChanged.connect(lambda x: self.timer.setInterval(x))

        self.auto_refresh.stateChanged.connect(self.on_checkbox_autorefresh_clicked)

        self.actionLoad_config.triggered.connect(self.load_config)
        self.actionSave_config.triggered.connect(self.save_config)
        self.actionExport_values.triggered.connect(self.save_values)

    def add_row(self, name: str, register: str, reg_addr: str, type_str: str, size: str, identifier: str):
        self.data_table.setSortingEnabled(False)

        current_row = self.data_table.rowCount()
        self.data_table.setRowCount(current_row + 1)

        self.data_table.setItem(current_row, int(self.TableCols.NAME), QTableWidgetItem(name))
        self.data_table.setItem(current_row, int(self.TableCols.REGISTER), QTableWidgetItem(register))
        addr_widget = QTableWidgetItem(reg_addr)
        addr_widget.setFont(self.fixed_font)
        addr_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.ADDR), addr_widget)
        self.data_table.setItem(current_row, int(self.TableCols.TYPE), QTableWidgetItem(type_str))
        size_widget = QTableWidgetItem(size)
        size_widget.setFont(self.fixed_font)
        size_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.SIZE), size_widget)
        endian_widget = QTableWidgetItem("####")
        self.data_table.setItem(current_row, int(self.TableCols.ENDIAN), endian_widget)
        value_widget = QTableWidgetItem("#####")
        value_widget.setFont(self.fixed_font)
        value_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.VALUE), value_widget)
        time_widget = QTableWidgetItem("#####")
        self.data_table.setItem(current_row, int(self.TableCols.TIME), time_widget)

        value_widget.register = register
        value_widget.identifier = identifier

        delete_button = QPushButton()
        delete_button.setText("del")
        delete_button.clicked.connect(lambda: self.delete_row(value_widget))
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON), delete_button)

        self.data_table.setSortingEnabled(True)

        return value_widget, endian_widget, time_widget

    def __add_cfg(self, cfg: tuple[str, dict, str, str, str, str]):
        self.exec_mutex.lock()
        cfg_line = cfg[0]
        data = cfg[1]
        register = cfg[2]
        reg_addr = cfg[3]
        size = cfg[4]
        type_str = cfg[5]
        name = data["name"]
        identifier = cfg_line.split(',', maxsplit=2)[-1]

        # add table entry
        value_widget, endian_widget, time_widget = self.add_row(name, register, reg_addr, type_str, size, identifier)

        data["cfg_line"] = cfg_line
        data["reg_addr"] = reg_addr
        data["size"] = size
        data["type_str"] = type_str
        self.shm_format_cfg[f"{register}"][identifier] = data
        self.shm_format_widgets[f"{register}"][identifier] = {
            "value_widget": value_widget,
            "endian_widget": endian_widget,
            "time_widget": time_widget,
        }
        self.exec_mutex.unlock()

    def __setup_add_buttons(self):
        def add_done():
            self.setEnabled(True)
            self.add_window = None

        def on_button_add_int():
            self.setEnabled(False)
            if self.add_window:
                raise RuntimeError("Internal Error: add_window exists")
            self.add_window = InspectSHM_AddInt(self.num_AO, self.num_AI, self.next_id)
            self.add_window.closed.connect(add_done)
            self.add_window.add_cfg.connect(self.__add_cfg)
            self.add_window.show()
            self.next_id += 1

        def on_button_add_float():
            self.setEnabled(False)
            if self.add_window:
                raise RuntimeError("Internal Error: add_window exists")
            self.add_window = InspectSHM_AddFloat(self.num_AO, self.num_AI, self.next_id)
            self.add_window.closed.connect(add_done)
            self.add_window.add_cfg.connect(self.__add_cfg)
            self.add_window.show()
            self.next_id += 1

        def on_button_add_bool():
            self.setEnabled(False)
            if self.add_window:
                raise RuntimeError("Internal Error: add_window exists")
            self.add_window = InspectSHM_AddBool(self.num_DO, self.num_DI, self.num_AO, self.num_AI, self.next_id)
            self.add_window.closed.connect(add_done)
            self.add_window.add_cfg.connect(self.__add_cfg)
            self.add_window.show()
            self.next_id += 1

        def on_button_add_string():
            self.setEnabled(False)
            if self.add_window:
                raise RuntimeError("Internal Error: add_window exists")
            self.add_window = InspectSHM_AddString(self.num_AO, self.num_AI, self.next_id)
            self.add_window.closed.connect(add_done)
            self.add_window.add_cfg.connect(self.__add_cfg)
            self.add_window.show()
            self.next_id += 1

        self.button_add_int.clicked.connect(on_button_add_int)
        self.button_add_float.clicked.connect(on_button_add_float)
        self.button_add_bool.clicked.connect(on_button_add_bool)
        self.button_add_char_array.clicked.connect(on_button_add_string)
        self.button_refresh.clicked.connect(self.execute)

    def on_checkbox_autorefresh_clicked(self, state: int):
        if state != 0:
            self.timer.start(self.spinbox_interval.value())
        else:
            self.timer.stop()

    def execute(self):
        self.exec_mutex.lock()
        self.data_table.setSortingEnabled(False)

        do_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg["DO"].values()]
        di_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg["DI"].values()]
        ao_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg["AO"].values()]
        ai_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg["AI"].values()]

        cfg_files = {}

        if len(do_cfg_lines) > 0:
            with tempfile.NamedTemporaryFile(delete=False, mode='w', prefix="shm-modbus-gui", suffix="DO") as f:
                for line in do_cfg_lines:
                    print(line, file=f)
                cfg_files[f"{self.name_prefix}DO"] = f

        if len(di_cfg_lines) > 0:
            with tempfile.NamedTemporaryFile(delete=False, mode='w', prefix="shm-modbus-gui", suffix="DI") as f:
                for line in di_cfg_lines:
                    print(line, file=f)
                cfg_files[f"{self.name_prefix}DI"] = f

        if len(ao_cfg_lines) > 0:
            with tempfile.NamedTemporaryFile(delete=False, mode='w', prefix="shm-modbus-gui", suffix="AO") as f:
                for line in ao_cfg_lines:
                    print(line, file=f)
                cfg_files[f"{self.name_prefix}AO"] = f

        if len(ai_cfg_lines) > 0:
            with tempfile.NamedTemporaryFile(delete=False, mode='w', prefix="shm-modbus-gui", suffix="AI") as f:
                for line in ai_cfg_lines:
                    print(line, file=f)
                cfg_files[f"{self.name_prefix}AI"] = f

        if len(cfg_files) > 0:
            cmd_args = []
            if self.semaphore:
                cmd_args.append("--semaphore")
                cmd_args.append(self.semaphore)

            for shm_name, tmp_file in cfg_files.items():
                cmd_args.append(shm_name)
                cmd_args.append(tmp_file.name)

            process = QProcess()
            process.start("shm-format", cmd_args)

            if process.waitForFinished(min(self.slider_interval.value() * 0.8, 1000)):
                if process.exitCode() != 0:
                    self.timer.stop()
                    stderr = bytes(process.readAllStandardError()).decode("utf-8")
                    QMessageBox.warning(self, "shm-format failed", stderr)
                else:
                    try:
                        self.apply_shm_format_json(bytes(process.readAllStandardOutput()).decode("utf-8"))
                    except Exception as e:
                        QMessageBox.warning(self, f"failed to parse", f"failed to parse shm-format data:\n{type(e).__name__}\n{e}")
            else:
                process.kill()

            for tmp_file in cfg_files.values():
                os.unlink(tmp_file.name)

        self.data_table.setSortingEnabled(True)
        self.exec_mutex.unlock()

    def apply_shm_format_json(self, json_data: str):
        data = json.loads(json_data)

        time = datetime.datetime.fromtimestamp(data["time"]).strftime('%Y-%m-%d %H:%M:%S')

        for shm_name, shm_data in data["shm_data"].items():
            for element in shm_data["data"]:
                name: str = element["name"]
                raw_value = element["data"]
                data_type: str = element["type"]

                cfg_data = self.shm_format_cfg[shm_name[len(self.name_prefix):]][name]
                cfg_widgets = self.shm_format_widgets[shm_name[len(self.name_prefix):]][name]
                value_widget = cfg_widgets["value_widget"]
                endian_widget = cfg_widgets["endian_widget"]
                time_widget = cfg_widgets["time_widget"]

                if data_type.startswith("int"):
                    endian = element["endian"] if "endian" in element else None
                    value = f"{raw_value:d}"
                elif data_type.startswith("uint"):
                    endian = element["endian"] if "endian" in element else None
                    format_char = name.split('_')[1]
                    match format_char:
                        case 'u':
                            value = f"{raw_value}"
                        case 'x':
                            value = f"0x{raw_value:x}"
                        case 'o':
                            value = f"0o{raw_value:o}"
                        case 'b':
                            value = f"0b{raw_value:b}"
                        case _:
                            raise RuntimeError(f"Unknown int format: {format_char}")
                elif data_type.startswith("float") or data_type.startswith("double"):
                    endian = element["endian"]
                    format_char = name.split('_')[1]
                    match format_char:
                        case 'f':
                            value = f"{raw_value}"
                        case 'e':
                            value = f"{raw_value:e}"
                        case _:
                            raise RuntimeError(f"Unknown float format: {format_char}")
                elif data_type.startswith("bool"):
                    endian = None
                    value = cfg_data['true'] if raw_value else cfg_data['false']
                elif data_type.startswith("string"):
                    endian = None
                    value = raw_value
                else:
                    raise RuntimeError(f"Unknown data type: {data_type}")

                value_widget.setText(value)
                endian_widget.setText(endian)
                time_widget.setText(time)

    def delete_row(self, row_widget: QTableWidgetItem):
        self.exec_mutex.lock()
        i = row_widget.row()
        del self.shm_format_cfg[f"{row_widget.register}"][row_widget.identifier]
        del self.shm_format_widgets[f"{row_widget.register}"][row_widget.identifier]
        self.data_table.removeRow(i)
        self.exec_mutex.unlock()

    def closeEvent(self, event):
        self.exec_mutex.lock()
        super(InspectSHM, self).closeEvent(event)
        self.timer.stop()
        if self.add_window:
            self.add_window.close()
        self.closed.emit(self.name_prefix)
        self.exec_mutex.unlock()

    def save_config(self):
        file_name, _ = QFileDialog.getSaveFileName(self, caption="Save config")
        if len(file_name) <= 0:
            return

        cfg_json = json.dumps(self.shm_format_cfg)
        cfg_hash = hashlib.sha256(cfg_json.encode("utf-8")).hexdigest()
        try:
            with open(file_name, 'w') as f:
                print(cfg_hash, file=f)
                print(cfg_json, file=f)
        except Exception as e:
            QMessageBox.warning(self, "Failed to write config", f"{e}")

    def load_config(self):
        file_name, _ = QFileDialog.getOpenFileName(self, caption="Load config")
        if len(file_name) <= 0:
            return

        try:
            with open(file_name, 'r') as f:
                cfg_lines = [x.strip() for x in f.readlines()]
        except Exception as e:
            QMessageBox.warning(self, "Failed to read config", f"{e}")
            return

        if len(cfg_lines) != 2:
            QMessageBox.warning(self, "Invalid file", f"Content of selected file is invalid.")
            return

        cfg_hash_file = cfg_lines[0]
        cfg_json = cfg_lines[1]

        cfg_hash = hashlib.sha256(cfg_json.encode("utf-8")).hexdigest()
        if cfg_hash_file != cfg_hash:
            QMessageBox.warning(self, "Invalid file", f"Content hash is invalid.")
            return

        loaded_cfg = json.loads(cfg_json)

        # check config
        try:
            for reg, reg_data in loaded_cfg.items():
                shm_size = self.shm_sizes[reg]
                for entry in reg_data.values():
                    cfg_line = entry["cfg_line"]
                    size_str = entry["size"]
                    size = 1 if size_str == "bit" else int(size_str) / 8
                    addr = int(cfg_line.split(',')[0].split(':')[0])
                    if addr + size > shm_size:
                        QMessageBox.warning(self, "Invalid file",
                                            f"Config check failed: Shared memory {self.name_prefix}{reg} "
                                            f"is to small to apply this configuration.")
                        return

        except Exception as e:
            QMessageBox.warning(self, "Invalid file", f"Config check failed:\n{type(e).__name__}\n{e}")
            return

        # TODO check if entries in table, if yes: ask user to save
        if self.data_table.rowCount() > 0:
            pass

        # clear table
        self.data_table.setRowCount(0)

        # apply config
        self.shm_format_cfg = loaded_cfg

        # create table entries
        self.shm_format_widgets = {
            "DO": {},
            "DI": {},
            "AO": {},
            "AI": {},
        }

        for register, reg_entry in self.shm_format_cfg.items():
            for identifier, entry_values in reg_entry.items():
                name = entry_values["name"]
                reg_addr = entry_values["reg_addr"]
                type_str = entry_values["type_str"]
                size = entry_values["size"]

                value_widget, endian_widget, time_widget = self.add_row(name, register, reg_addr, type_str, size,
                                                                        identifier)

                self.shm_format_widgets[f"{register}"][identifier] = {
                    "value_widget": value_widget,
                    "endian_widget": endian_widget,
                    "time_widget": time_widget,
                }

    def save_values(self):
        file_name, _ = QFileDialog.getSaveFileName(self, caption="Save values", filter="*.csv")

        if len(file_name) == 0:
            return

        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            header = ["name", "register", "address", "data type", "size", "value", "time"]

            writer.writerow(header)

            self.exec_mutex.lock()
            self.data_table.setSortingEnabled(False)

            for row in range(self.data_table.rowCount()):
                writer.writerow([
                    self.data_table.item(row, int(self.TableCols.NAME)).text(),
                    self.data_table.item(row, int(self.TableCols.REGISTER)).text(),
                    self.data_table.item(row, int(self.TableCols.ADDR)).text(),
                    self.data_table.item(row, int(self.TableCols.TYPE)).text(),
                    self.data_table.item(row, int(self.TableCols.SIZE)).text(),
                    self.data_table.item(row, int(self.TableCols.VALUE)).text(),
                    self.data_table.item(row, int(self.TableCols.TIME)).text(),
                ])

            self.data_table.setSortingEnabled(True)
            self.exec_mutex.unlock()
