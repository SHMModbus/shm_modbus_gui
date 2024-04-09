from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import QTableWidgetItem, QPushButton
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QTimer, QMutex, QProcess, Qt
import enum
import struct

from py_ui import Ui_InspectSHM

import InspectSHMAddInt
import InspectSHMAddFloat
import InspectSHMAddBool
import InspectSHMAddCharArray


def oct_size(num_bytes: int) -> int:
    match num_bytes:
        case 1:
            return 3
        case 2:
            return 6
        case 4:
            return 11
        case 8:
            return 22


def dec_size(num_bytes: int) -> int:
    match num_bytes:
        case 1:
            return 3
        case 2:
            return 5
        case 4:
            return 10
        case 8:
            return 19


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
        BUTTON = 7

    def __init__(self, shm_name: str, shm_size_do: int, shm_size_di: int, shm_size_ao: int, shm_size_ai: int,
                 semaphore: str | None = None) -> None:
        super(InspectSHM, self).__init__()
        self.setupUi(self)

        self.shm_name = shm_name
        self.shm_size_do = shm_size_do
        self.shm_size_di = shm_size_di
        self.shm_size_ao = shm_size_ao
        self.shm_size_ai = shm_size_ai
        self.semaphore = semaphore

        self.command_window = None

        self.fixed_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)

        self.timer = QTimer()
        self.timer.timeout.connect(self.execute)

        def timer_start_stop(state):
            if state != 0:
                self.timer.start(self.spinbox_interval.value())
            else:
                self.timer.stop()

        self.auto_refresh.clicked.connect(timer_start_stop)

        def on_slider_interval_value_changed(value: int):
            self.spinbox_interval.setValue(value)
            self.timer.setInterval(value)

        self.slider_interval.valueChanged.connect(on_slider_interval_value_changed)

        def on_spinbox_interval_value_changed(value: int):
            self.slider_interval.setValue(value)

        self.spinbox_interval.valueChanged.connect(on_spinbox_interval_value_changed)

        # execution mutex
        self.exec_mutex = QMutex()

        # buttons
        self.button_refresh.clicked.connect(self.execute)
        self.button_add_int.clicked.connect(self.button_add_int_click)
        self.button_add_float.clicked.connect(self.button_add_float_click)
        self.button_add_bool.clicked.connect(self.button_add_bool_click)
        self.button_add_char_array.clicked.connect(self.button_add_char_array_click)

    def button_add_int_click(self):
        self.command_window = InspectSHMAddInt.InspectSHMAddInt(self.shm_size_ao, self.shm_size_ai)
        self.command_window.add.connect(self.add_int)
        self.command_window.closed.connect(self.command_window_closed)
        self.command_window.show()
        self.setDisabled(True)

    def button_add_float_click(self):
        self.command_window = InspectSHMAddFloat.InspectSHMAddFloat(self.shm_size_ao, self.shm_size_ai)
        self.command_window.add.connect(self.add_float)
        self.command_window.closed.connect(self.command_window_closed)
        self.command_window.show()
        self.setDisabled(True)

    def button_add_char_array_click(self):
        self.command_window = InspectSHMAddCharArray.InspectSHMAddCharArray(self.shm_size_ao, self.shm_size_ai)
        self.command_window.add.connect(self.add_char_arr)
        self.command_window.closed.connect(self.command_window_closed)
        self.command_window.show()
        self.setDisabled(True)

    def button_add_bool_click(self):
        self.command_window = InspectSHMAddBool.InspectSHMAddBool(self.shm_size_do, self.shm_size_di,
                                                                  self.shm_size_ao, self.shm_size_ai)
        self.command_window.add.connect(self.add_bool)
        self.command_window.closed.connect(self.command_window_closed)
        self.command_window.show()
        self.setDisabled(True)

    def add_row(self):
        current_row = self.data_table.rowCount()
        self.data_table.setRowCount(current_row + 1)
        return current_row

    def add_int(self, data: InspectSHMAddInt.InspectSHMInt):
        print(f"add_int: {data}")

        self.exec_mutex.lock()

        current_row = self.add_row()

        name_widget = QTableWidgetItem(data.name)
        name_widget.inspect_data = data

        self.data_table.setItem(current_row, int(self.TableCols.NAME), name_widget)
        self.data_table.setItem(current_row, int(self.TableCols.REGISTER), QTableWidgetItem(data.register.name))
        self.data_table.setItem(current_row, int(self.TableCols.ADDR), QTableWidgetItem(f"0x{data.address:04x}"))
        self.data_table.setItem(current_row, int(self.TableCols.TYPE), QTableWidgetItem(f"int ({data.display_type.name.lower()})"))
        self.data_table.setItem(current_row, int(self.TableCols.SIZE), QTableWidgetItem(f"{data.size}"))
        self.data_table.setItem(current_row, int(self.TableCols.ENDIAN), QTableWidgetItem(
            f"{'little' if data.little_endian else 'big'}{' (reversed)' if data.reversed_registers else ''}"))
        value_widget = QTableWidgetItem("#####")
        value_widget.setFont(self.fixed_font)
        value_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.VALUE), value_widget)

        delete_button = QPushButton()
        delete_button.setText("del")
        delete_button.clicked.connect(lambda: self.delete_row(name_widget))
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON), delete_button)

        self.exec_mutex.unlock()

    def add_float(self, data: InspectSHMAddFloat.InspectSHMFloat):
        print(f"add_float: {data}")
        self.exec_mutex.lock()

        current_row = self.add_row()

        name_widget = QTableWidgetItem(data.name)
        name_widget.inspect_data = data

        self.data_table.setItem(current_row, int(self.TableCols.NAME), name_widget)
        self.data_table.setItem(current_row, int(self.TableCols.REGISTER), QTableWidgetItem(data.register.name))
        self.data_table.setItem(current_row, int(self.TableCols.ADDR), QTableWidgetItem(f"0x{data.address:04x}"))
        self.data_table.setItem(current_row, int(self.TableCols.TYPE), QTableWidgetItem(f"float ({data.display_type.name.lower()})"))
        self.data_table.setItem(current_row, int(self.TableCols.SIZE), QTableWidgetItem(f"{data.size}"))
        self.data_table.setItem(current_row, int(self.TableCols.ENDIAN), QTableWidgetItem(
            f"{'little' if data.little_endian else 'big'}{' (reversed)' if data.reversed_registers else ''}"))
        value_widget = QTableWidgetItem("#####")
        value_widget.setFont(self.fixed_font)
        value_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.VALUE), value_widget)

        delete_button = QPushButton()
        delete_button.setText("del")
        delete_button.clicked.connect(lambda: self.delete_row(name_widget))
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON), delete_button)

        self.exec_mutex.unlock()

    def add_bool(self, data: InspectSHMAddBool.InspectSHMBool):
        print(f"add_bool: {data}")
        self.exec_mutex.lock()

        current_row = self.add_row()

        name_widget = QTableWidgetItem(data.name)
        name_widget.inspect_data = data

        self.data_table.setItem(current_row, int(self.TableCols.NAME), name_widget)
        self.data_table.setItem(current_row, int(self.TableCols.REGISTER), QTableWidgetItem(data.register.name))
        self.data_table.setItem(current_row, int(self.TableCols.ADDR), QTableWidgetItem(f"0x{data.address:04x}:{data.bit}"))
        self.data_table.setItem(current_row, int(self.TableCols.TYPE), QTableWidgetItem("bool"))
        self.data_table.setItem(current_row, int(self.TableCols.SIZE), QTableWidgetItem("bit"))
        self.data_table.setItem(current_row, int(self.TableCols.ENDIAN), QTableWidgetItem(
            f"{'little' if data.little_endian else 'big'}"))
        value_widget = QTableWidgetItem("#####")
        value_widget.setFont(self.fixed_font)
        value_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.VALUE), value_widget)

        delete_button = QPushButton()
        delete_button.setText("del")
        delete_button.clicked.connect(lambda: self.delete_row(name_widget))
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON), delete_button)

        self.exec_mutex.unlock()

    def add_char_arr(self, data: InspectSHMAddCharArray.InspectSHMCharArray):
        print(f"add_char_arr: {data}")
        self.exec_mutex.lock()

        current_row = self.add_row()

        name_widget = QTableWidgetItem(data.name)
        name_widget.inspect_data = data

        self.data_table.setItem(current_row, int(self.TableCols.NAME), name_widget)
        self.data_table.setItem(current_row, int(self.TableCols.REGISTER), QTableWidgetItem(data.register.name))
        self.data_table.setItem(current_row, int(self.TableCols.ADDR), QTableWidgetItem(f"0x{data.address:04x}"))
        self.data_table.setItem(current_row, int(self.TableCols.TYPE), QTableWidgetItem("char[]"))
        self.data_table.setItem(current_row, int(self.TableCols.SIZE), QTableWidgetItem(f"{data.size}"))
        self.data_table.setItem(current_row, int(self.TableCols.ENDIAN), QTableWidgetItem("---"))
        value_widget = QTableWidgetItem("#####")
        value_widget.setFont(self.fixed_font)
        value_widget.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.data_table.setItem(current_row, int(self.TableCols.VALUE), value_widget)

        delete_button = QPushButton()
        delete_button.setText("del")
        delete_button.clicked.connect(lambda: self.delete_row(name_widget))
        self.data_table.setCellWidget(current_row, int(self.TableCols.BUTTON), delete_button)

        self.exec_mutex.unlock()

    def delete_row(self, row_widget):
        self.exec_mutex.lock()
        i = row_widget.row()
        print(f"delete row {i}: {row_widget.inspect_data}")
        self.data_table.removeRow(i)
        self.exec_mutex.unlock()

    def command_window_closed(self):
        self.setEnabled(True)

    def execute(self):
        self.exec_mutex.lock()

        shm_data = {}
        for reg in ("DO", "DI", "AO", "AI"):
            shm_name = f"{self.shm_name}{reg}"
            cmd_args = []
            if self.semaphore:
                cmd_args += ['-s', self.semaphore]
            cmd_args.append(shm_name)
            process = QProcess()
            process.start("dump-shm", cmd_args)
            if process.waitForFinished(min(self.slider_interval.value() * 0.8 * 0.25, 1000)):
                stderr = bytes(process.readAllStandardError()).decode("utf-8")
                stdout = bytearray(process.readAllStandardOutput())
                if len(stderr) > 0:
                    print(f"failed to read shared memory {shm_name}: {stderr}")
                    shm_data[reg] = None
                else:
                    shm_data[reg] = stdout
            else:
                process.kill()
                shm_data[reg] = None
                print(f"failed to read shared memory {shm_name}: dump-shm timed out")

        def reg_swap(data: bytearray) -> bytearray:
            result = data[::-1]
            for j in range(0, len(data), 2):
                result[j], result[j + 1] = result[j + 1], result[j]
            return result

        for i in range(self.data_table.rowCount()):
            row_data_item = self.data_table.item(i, int(self.TableCols.NAME))
            row_data = row_data_item.inspect_data
            match type(row_data):
                case InspectSHMAddInt.InspectSHMInt:
                    match row_data.register:
                        case InspectSHMAddInt.Register.AO:
                            shm_bytes = shm_data["AO"]
                        case InspectSHMAddInt.Register.AI:
                            shm_bytes = shm_data["AI"]
                        case _:
                            raise RuntimeError(f"Internal error: unexpected register type {row_data.register}")
                    if shm_bytes:
                        int_bytes = shm_bytes[row_data.address:row_data.address + row_data.size]
                        if row_data.reversed_registers:
                            int_bytes = reg_swap(int_bytes)
                        int_value = int.from_bytes(int_bytes, "little" if row_data.little_endian else "big",
                                                   signed=row_data.display_type == InspectSHMAddInt.DisplayType.SIGNED)
                        match row_data.display_type:
                            case InspectSHMAddInt.DisplayType.UNSIGNED:
                                text = f"{int_value:0{dec_size(row_data.size)}d}"
                            case InspectSHMAddInt.DisplayType.SIGNED:
                                text = f"{int_value:0{dec_size(row_data.size) + (1 if int_value < 0 else 0)}d}"
                            case InspectSHMAddInt.DisplayType.HEX:
                                text = f"{int_value:0{row_data.size * 2}x}"
                            case InspectSHMAddInt.DisplayType.OCT:
                                text = f"{int_value:0{oct_size(row_data.size)}o}"
                            case InspectSHMAddInt.DisplayType.BIN:
                                text = f"{int_value:0{row_data.size * 8}b}"
                            case _:
                                raise RuntimeError(f"Internal error: unexpected display type {row_data.display_type}")
                        self.data_table.item(i, int(self.TableCols.VALUE)).setText(text)
                    else:
                        self.data_table.item(i, int(self.TableCols.VALUE)).setText("#####")

                case InspectSHMAddFloat.InspectSHMFloat:
                    match row_data.register:
                        case InspectSHMAddFloat.Register.AO:
                            shm_bytes = shm_data["AO"]
                        case InspectSHMAddFloat.Register.AI:
                            shm_bytes = shm_data["AI"]
                        case _:
                            raise RuntimeError(f"Internal error: unexpected register type {row_data.register}")
                    if shm_bytes:
                        float_bytes = shm_bytes[row_data.address:row_data.address + row_data.size]
                        if row_data.reversed_registers:
                            float_bytes = reg_swap(float_bytes)
                        endian_char = '<' if row_data.little_endian else '>'
                        match len(float_bytes):
                            case 4:
                                float_value = struct.unpack(f'{endian_char}f', float_bytes)[0]
                            case 8:
                                float_value = struct.unpack(f'{endian_char}d', float_bytes)[0]
                            case _:
                                raise RuntimeError(f"Internal error: unexpected lenght: {len(float_bytes)}")
                        match row_data.display_type:
                            case InspectSHMAddFloat.DisplayType.FIXED:
                                text = f"{float_value:.8f}"
                            case InspectSHMAddFloat.DisplayType.SCIENTIFIC:
                                text = f"{float_value:e}"
                            case _:
                                raise RuntimeError(f"Internal error: unexpected display type {row_data.display_type}")
                        self.data_table.item(i, int(self.TableCols.VALUE)).setText(text)
                    else:
                        self.data_table.item(i, int(self.TableCols.VALUE)).setText("#####")

                case InspectSHMAddBool.InspectSHMBool:
                    # TODO
                    pass
                case InspectSHMAddCharArray.InspectSHMCharArray:
                    # TODO
                    pass
                case _:
                    raise RuntimeError(f"Internal error: unexpected data type {type(row_data)}")
        self.exec_mutex.unlock()

    def closeEvent(self, event):
        super(InspectSHM, self).closeEvent(event)
        if self.command_window:
            self.command_window.close()
        self.timer.stop()
        self.closed.emit()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = InspectSHM("modbus_", 2 ** 16, 2 ** 16, 2 ** 16, 2 ** 16, "modbus")
    window.closed.connect(lambda: print("window closed"))
    window.show()

    app.exec()
