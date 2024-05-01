import datetime
import enum
import json
import os
import tempfile

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QMutex, Qt, QProcess, QTimer
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QTableWidgetItem, QPushButton, QMessageBox

from .py_ui import Ui_InspectSHM
from .InspectSHM_AddInt import InspectSHM_AddInt
from .InspectSHM_AddFloat import InspectSHM_AddFloat
from .InspectSHM_AddBool import InspectSHM_AddBool
from .InspectSHM_AddString import InspectSHM_AddString


class InspectSHM(QtWidgets.QMainWindow, Ui_InspectSHM):
    closed = QtCore.Signal()

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
            f"{self.name_prefix}DO": {},
            f"{self.name_prefix}DI": {},
            f"{self.name_prefix}AO": {},
            f"{self.name_prefix}AI": {},
        }

        self.__setup_add_buttons()

        self.spinbox_interval.valueChanged.connect(lambda x: self.slider_interval.setValue(x))
        self.slider_interval.valueChanged.connect(lambda x: self.spinbox_interval.setValue(x))
        self.slider_interval.valueChanged.connect(lambda x: self.timer.setInterval(x))

        self.auto_refresh.stateChanged.connect(self.on_checkbox_autorefresh_clicked)

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

        data["cfg_line"] = cfg_line
        data["value_widget"] = value_widget
        data["endian_widget"] = endian_widget
        data["time_widget"] = time_widget
        self.shm_format_cfg[f"{self.name_prefix}{register}"][identifier] = data
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

        do_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg[f"{self.name_prefix}DO"].values()]
        di_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg[f"{self.name_prefix}DI"].values()]
        ao_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg[f"{self.name_prefix}AO"].values()]
        ai_cfg_lines = [x["cfg_line"] for x in self.shm_format_cfg[f"{self.name_prefix}AI"].values()]

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

                cfg_data = self.shm_format_cfg[shm_name][name]
                value_widget = cfg_data["value_widget"]
                endian_widget = cfg_data["endian_widget"]
                time_widget = cfg_data["time_widget"]

                if data_type.startswith("int"):
                    endian = element["endian"] if "endian" in element else None
                    value = f"{raw_value:d}"
                elif data_type.startswith("uint"):
                    endian = element["endian"] if "endian" in element else None
                    format_char = name.split('_')[1]
                    match format_char:
                        case 'u':
                            value = f"{raw_value:u}"
                        case 'x':
                            value = f"0x{raw_value:x}"
                        case 'o':
                            value = f"0x{raw_value:o}"
                        case 'b':
                            value = f"0x{raw_value:b}"
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
        del self.shm_format_cfg[f"{self.name_prefix}{row_widget.register}"][row_widget.identifier]
        self.data_table.removeRow(i)
        self.exec_mutex.unlock()

    def closeEvent(self, event):
        super(InspectSHM, self).closeEvent(event)
        self.timer.stop()
        if self.add_window:
            self.add_window.close()
        self.closed.emit()
