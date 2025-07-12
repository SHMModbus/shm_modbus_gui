import os
import shlex
from PySide6 import QtWidgets
from PySide6.QtCore import QRegularExpression, QProcess
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFileDialog, QMessageBox

from . import MBConfig
from . import SHMTools
from .SelectTTY import SelectTTY
from .py_ui import Ui_MainWindow
from .MBxxOutput import MBxxOutput
from . import constants
from .MBConfig import MBConfig


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # disable tools
        self.tab_shm_tools.setEnabled(False)

        # Modbus common settings
        self.__init_mb()

        # Modbus TCP
        self.__init_mbtcp()

        # Modbus RTU
        self.__init_mbrtu()

        # Command Window
        self.command_window: MBxxOutput | None = None
        self.command_pid: int | None = None
        self.process_active: bool = False
        self.window_open: bool = False

        # search tty window
        self.search_tty_window: SelectTTY | None = None

        # internal variables
        self.modbus_cfg: MBConfig.MBConfig | None = None

        # SHM Tools
        self.shm_tools = SHMTools.SHMTools(self)
        self.__shm_tools_init_gui()

        # Version popup
        self.actionVersion.triggered.connect(lambda: self.version_popup())

    def __init_mb(self) -> None:
        self.__mb_button_actions()
        self.__mb_default_values()
        self.__mb_ui_actions()
        self.__mb_validators()

    def __mb_button_actions(self):
        # Registers
        self.mb_do_default.clicked.connect(lambda: self.mb_do.setValue(65536))
        self.mb_di_default.clicked.connect(lambda: self.mb_di.setValue(65536))
        self.mb_ao_default.clicked.connect(lambda: self.mb_ao.setValue(65536))
        self.mb_ai_default.clicked.connect(lambda: self.mb_ai.setValue(65536))

        # Shared Memory
        self.mb_shm_flags_default.clicked.connect(
            lambda: self.mb_force.setChecked(False))
        self.mb_shm_name_default.clicked.connect(
            lambda: self.mb_shm_name.setText("modbus_"))

        # Modbus
        def modbus_defaults() -> None:
            self.mb_monitor.setChecked(False)
            self.mb_enable_byte_timeout.setChecked(False)
            self.mb_enable_response_timeout.setChecked(False)
            self.mb_byte_timeout.setEnabled(False)
            self.mb_byte_timeout.setValue(0)
            self.mb_response_timeout.setEnabled(False)
            self.mb_response_timeout.setValue(0)

        self.mb_mb_flags_default.clicked.connect(modbus_defaults)

        # Semaphore
        def semaphore_defaults() -> None:
            self.mb_sem_enable.setChecked(True)
            self.mb_sem_force.setChecked(False)

        self.mb_sem_defaults.clicked.connect(semaphore_defaults)
        self.mb_sem_name_default.clicked.connect(
            lambda: self.mb_sem_name.setText("modbus"))

        # reset all
        self.mb_defaults.clicked.connect(lambda: self.__mb_default_values())

        # save / load
        self.actionsave_modbus_client_config.triggered.connect(
            self.__config_save)
        self.actionopen_modbus_client_config.triggered.connect(
            self.__config_load)

    def __mb_default_values(self) -> None:
        # Registers
        self.mb_do_default.click()
        self.mb_di_default.click()
        self.mb_ao_default.click()
        self.mb_ai_default.click()

        # Shared memory
        self.mb_shm_flags_default.click()
        self.mb_shm_name_default.click()

        # Modbus
        self.mb_mb_flags_default.click()

        # Semaphore
        self.mb_sem_defaults.click()
        self.mb_sem_name_default.click()

    def __mb_ui_actions(self) -> None:
        # modbus byte timeout
        self.mb_enable_byte_timeout.stateChanged.connect(
            lambda value: self.mb_byte_timeout.setEnabled(value != 0)
        )

        # modbus response timeout
        self.mb_enable_response_timeout.stateChanged.connect(
            lambda value: self.mb_response_timeout.setEnabled(value != 0)
        )

        # semaphore enable
        def semaphore_enable_changes(value: int) -> None:
            enabled = value != 0
            self.mb_sem_force.setEnabled(enabled)
            self.mb_sem_name.setEnabled(enabled)

        self.mb_sem_enable.stateChanged.connect(semaphore_enable_changes)

    def __mb_validators(self) -> None:
        name_re = QRegularExpression(constants.NAME_REGEX)
        name_validator = QRegularExpressionValidator(name_re)
        self.mb_shm_name.setValidator(name_validator)
        self.mb_sem_name.setValidator(name_validator)

    def __config_save(self) -> None:
        """
        @brief save config to file
        """

        file_name, _ = QFileDialog.getSaveFileName(
            self, caption="Save config", filter="*.json")

        if len(file_name):
            try:
                MBConfig(self).save(file_name)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to save configuration: {e}")

    def __config_load(self) -> None:
        """
        @brief load config from file
        """
        file_name, _ = QFileDialog.getOpenFileName(
            self, caption="Load config", filter="*.json")

        if len(file_name):
            try:
                config = MBConfig(self)
                config.load(file_name)
                config.apply(self)
            except RuntimeError as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load configuration: {e}")

    def __init_mbtcp(self) -> None:
        """
        @brief initialize modbus tcp ui
        """
        self.__mbtcp_button_actions()
        self.__mbtcp_default_values()
        self.__mbtcp_ui_actions()
        self.__mbtcp_validators()

    def __mbtcp_default_values(self) -> None:
        """
        @brief set default ui values for mbtcp
        """
        # Network
        self.mbtcp_host_default.click()
        self.mbtcp_port_default.click()
        self.mbtcp_tcp_timeout_default.click()
        self.mbtcp_connections_default.click()
        self.mbtcp_nw_flags_default.click()

        # Shared memory
        self.mbtcp_shm_defaults.click()
        self.mbtcp_separate_list_clear.click()

    def __mbtcp_button_actions(self) -> None:
        """
        @brief connect button signals
        """
        # Network
        self.mbtcp_host_default.clicked.connect(
            lambda: self.mbtcp_host.setText("any"))
        self.mbtcp_port_default.clicked.connect(
            lambda: self.mbtcp_port.setValue(502))

        def tcp_timeout_default() -> None:
            self.mbtcp_tcp_timeout.setValue(5),
            self.mbtcp_sytstem_tcp_timeout.setChecked(False)

        self.mbtcp_tcp_timeout_default.clicked.connect(tcp_timeout_default)
        self.mbtcp_connections_default.clicked.connect(
            lambda: self.mbtcp_connections.setValue(1))
        self.mbtcp_nw_flags_default.clicked.connect(
            lambda: self.mbtcp_reconnect.setChecked(True))

        # Shared Memory
        def shm_default_flags() -> None:
            self.mbtcp_separate.setChecked(False)
            self.mbtcp_separate_all.setChecked(False)
            self.mbtcp_separate_all.setEnabled(False)

        self.mbtcp_shm_defaults.clicked.connect(shm_default_flags)

        self.mbtcp_separate_list_clear.clicked.connect(
            lambda: self.mbtcp_separate_list.clear())

        # reset all
        self.mbtcp_defaults.clicked.connect(self.__mbtcp_default_values)

        # start button
        self.mbtcp_start.clicked.connect(self.__mbtcp_start_button_clicked)

    def __mbtcp_validators(self) -> None:
        """
        @brief set validators for text input
        """
        name_re = QRegularExpression(constants.NAME_REGEX)
        separate_list_re = QRegularExpression(constants.BYTE_REGEX)

        name_validator = QRegularExpressionValidator(name_re)
        separate_list_validator = QRegularExpressionValidator(separate_list_re)

        self.mbtcp_host.setValidator(name_validator)
        self.mbtcp_separate_list.setValidator(separate_list_validator)

    def __mbtcp_ui_actions(self) -> None:
        """
        @brief connect signals/slots for ui
        """
        # tcp system timeout
        self.mbtcp_sytstem_tcp_timeout.stateChanged.connect(
            lambda state: self.mbtcp_tcp_timeout.setEnabled(state == 0))

        # shared memory separate
        def shm_separate_changed(value: int) -> None:
            enabled = value != 0
            self.mbtcp_separate_all.setEnabled(enabled)
            self.mbtcp_separate_list.setEnabled(
                enabled and not self.mbtcp_separate_all.isChecked())

        self.mbtcp_separate.stateChanged.connect(shm_separate_changed)

        # shared memory separate all
        self.mbtcp_separate_all.stateChanged.connect(
            lambda value: self.mbtcp_separate_list.setEnabled(
                value == 0 and self.mbtcp_separate.isChecked())
        )

    def __mbtcp_start_button_clicked(self) -> None:
        """
        @brief mbtcp start button clicked
        """
        if self.process_active:
            # already running --> stop mbtcp client
            self.command_window.terminate()
            self.mbtcp_start.setEnabled(False)
        else:
            # start mbtcp client
            if self.command_window:
                raise RuntimeError("Internal error: command window still open")

            # lock ui elements
            self.tab_mbrtu.setEnabled(False)
            self.tab_modbus_setings.setEnabled(False)
            self.mbrtu_start.setEnabled(False)
            self.mbtcp_settings.setEnabled(False)
            self.mbtcp_defaults.setEnabled(False)
            self.mbtcp_start.setText("Stop")
            self.tab_shm_tools.setEnabled(True)

            # execute command
            self.modbus_cfg = MBConfig(self)
            self.modbus_cfg.modbus_type = "tcp"
            self.__exec_process("Shared Memory Modbus TCP Client")

    def __init_mbrtu(self) -> None:
        """
        @brief initialize modbus rtu ui
        """
        self.__mbrtu_button_actions()
        self.__mbrtu_default_values()
        self.__mbrtu_ui_actions()
        self.__mbrtu_validators()

    def __mbrtu_default_values(self) -> None:
        # Modbus
        self.mbrtu_clientid_default.click()

    def __mbrtu_button_actions(self) -> None:
        """
        @brief connect button signals
        """
        # Serial
        self.mbrtu_device_default.clicked.connect(
            lambda: self.mbrtu_device.clear())
        self.mbrtu_parity_default.clicked.connect(
            lambda: self.mbrtu_parity.setCurrentIndex(0))
        self.mbrtu_databits_default.clicked.connect(
            lambda: self.mbrtu_databits.setValue(8))
        self.mbrtu_stopbits_default.clicked.connect(
            lambda: self.mbrtu_stopbits.setValue(1))
        self.mbrtu_baudrate_default.clicked.connect(
            lambda: self.mbrtu_baudrate.text("115200"))
        self.mbrtu_serialtype_default.clicked.connect(
            lambda: self.mbrtu_serialtype.setCurrentIndex(0))
        self.mbrtu_search_tty.clicked.connect(self.__mbrtu_search_tty)

        # Modbus
        self.mbrtu_clientid_default.clicked.connect(
            lambda: self.mbrtu_clientid.setValue(0))

    def __mbrtu_validators(self) -> None:
        """
        @brief set validators for text input
        """
        device_re = QRegularExpression(constants.DEVICE_REGEX)
        baud_re = QRegularExpression(constants.BAUD_REGEX)

        device_validator = QRegularExpressionValidator(device_re)
        baud_validator = QRegularExpressionValidator(baud_re)

        self.mbrtu_device.setValidator(device_validator)
        self.mbrtu_baudrate.setValidator(baud_validator)

    def __mbrtu_start_button_clicked(self) -> None:
        """
        @brief mbrtu start button clicked
        """

        if self.process_active:
            # already running --> stop mbtcp client
            self.command_window.terminate()
            self.mbrtu_start.setEnabled(False)
        else:
            # start mbrtu client
            if self.command_window:
                raise RuntimeError("Internal error: command window still open")

            # check inputs
            if len(self.mbrtu_device.text()) == 0:
                QMessageBox.critical(self, "Error", f"No device specified.")
                return
            if len(self.mbrtu_baudrate.text()) == 0:
                QMessageBox.critical(self, "Error", f"No baud rate specified.")
                return

            # lock ui elements
            self.tab_mbtcp.setEnabled(False)
            self.tab_modbus_setings.setEnabled(False)
            self.mbtcp_start.setEnabled(False)
            self.mbrtu_settings.setEnabled(False)
            self.mbrtu_defaults.setEnabled(False)
            self.mbrtu_start.setText("Stop")
            self.tab_shm_tools.setEnabled(True)

            # execute command
            self.modbus_cfg = MBConfig(self)
            self.modbus_cfg.modbus_type = "rtu"
            self.__exec_process("Shared Memory Modbus RTU Client")

    def __mbrtu_search_tty(self) -> None:
        def search_done():
            self.setEnabled(True)
            self.search_tty_window = None

        self.setEnabled(False)
        if self.search_tty_window:
            raise RuntimeError("Internal Error: search_tty_window exists")
        self.search_tty_window = SelectTTY()
        self.search_tty_window.closed.connect(search_done)
        self.search_tty_window.set_tty.connect(self.mbrtu_device.setText)
        self.search_tty_window.show()
        self.search_tty_window.search_tty()

    def __mbrtu_ui_actions(self) -> None:
        """
        @brief connect signals/slots for ui
        """
        # reset all
        self.mbrtu_defaults.clicked.connect(self.__mbrtu_default_values)

        # start button
        self.mbrtu_start.clicked.connect(self.__mbrtu_start_button_clicked)

    def __exec_process(self, title: str):
        if self.modbus_cfg.modbus_type == "tcp":
            cmd = self.modbus_cfg.get_command_tcp()
        elif self.modbus_cfg.modbus_type == "rtu":
            cmd = self.modbus_cfg.get_command_rtu()
        else:
            raise RuntimeError(
                f"Invalid application state: self.modbus_cfg.modbus_type = {self.modbus_cfg.modbus_type}")
        self.process_active = True
        self.window_open = True
        self.command_window = MBxxOutput(cmd, title)
        self.command_window.finished.connect(self.__process_finished)
        self.command_window.closed.connect(self.__command_window_closed)
        self.command_window.show()
        self.command_pid = self.command_window.pid

    def __process_finished(self, exit_code: int) -> None:
        """
        @brief actions when modbus process is finished
        """
        self.process_active = False

        # disable tools and tool tab
        self.tab_shm_tools.setEnabled(False)
        self.__close_tool_windows()

        if not self.window_open:
            # window not open --> destroy window, enable start buttons
            self.command_window = None
            self.mbtcp_start.setEnabled(True)
            self.mbrtu_start.setEnabled(True)
        else:
            # window still open --> disable start buttons
            self.mbtcp_start.setEnabled(False)
            self.mbrtu_start.setEnabled(False)

        # enable ui elements
        self.tab_mbrtu.setEnabled(True)
        self.mbtcp_settings.setEnabled(True)
        self.mbtcp_defaults.setEnabled(True)
        self.mbtcp_start.setText("Start")
        self.tab_mbtcp.setEnabled(True)
        self.mbrtu_settings.setEnabled(True)
        self.mbrtu_defaults.setEnabled(True)
        self.mbrtu_start.setText("Start")
        self.tab_modbus_setings.setEnabled(True)

        if exit_code != 0:
            QMessageBox.information(
                self, "Client terminated", f"Modbus client terminated with exit code {exit_code}")

    def __command_window_closed(self) -> None:
        """
        @brief actions when command window is closed
        """
        self.window_open = False
        if not self.process_active:
            # process already inactive --> destroy window, enable start buttons
            self.command_window = None
            self.mbtcp_start.setEnabled(True)
            self.mbrtu_start.setEnabled(True)
        else:
            # process still active --> disable start buttons
            self.mbtcp_start.setEnabled(False)
            self.mbrtu_start.setEnabled(False)

        self.__close_tool_windows()

        self.command_pid = None

    def __shm_tools_init_gui(self) -> None:
        """
        @brief initialize tool gui
        """
        self.__shm_tools_init_hexdump_gui()
        self.__shm_tools_init_random_gui()
        self.__shm_tools_init_dump_gui()
        self.__shm_tools_init_load_gui()
        self.__shm_tools_init_inspect_gui()
        self.__shm_tools_init_set_gui()

    def __shm_tools_init_hexdump_gui(self) -> None:
        def on_button_hexdump_do_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}DO", self.modbus_cfg.do, 1,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_do.setEnabled(False)
            hexdump.closed.connect(
                lambda: self.tool_hexdump_do.setEnabled(True))

        self.tool_hexdump_do.clicked.connect(on_button_hexdump_do_clicked)

        def on_button_hexdump_di_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}DI", self.modbus_cfg.di, 1,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_di.setEnabled(False)
            hexdump.closed.connect(
                lambda: self.tool_hexdump_di.setEnabled(True))

        self.tool_hexdump_di.clicked.connect(on_button_hexdump_di_clicked)

        def on_button_hexdump_ao_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}AO", self.modbus_cfg.ao, 2,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_ao.setEnabled(False)
            hexdump.closed.connect(
                lambda: self.tool_hexdump_ao.setEnabled(True))

        self.tool_hexdump_ao.clicked.connect(on_button_hexdump_ao_clicked)

        def on_button_hexdump_ai_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}AI", self.modbus_cfg.ai, 2,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_ai.setEnabled(False)
            hexdump.closed.connect(
                lambda: self.tool_hexdump_ai.setEnabled(True))

        self.tool_hexdump_ai.clicked.connect(on_button_hexdump_ai_clicked)

    def __shm_tools_init_random_gui(self) -> None:
        def on_button_random_do_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}DO", self.modbus_cfg.do, 1,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None, 0x1,
                                                 mb_client_pid=self.command_pid)
            self.tool_random_do.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_do.setEnabled(True))

        self.tool_random_do.clicked.connect(on_button_random_do_clicked)

        def on_button_random_di_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}DI", self.modbus_cfg.di, 1,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None, 0x1,
                                                 mb_client_pid=self.command_pid)
            self.tool_random_di.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_di.setEnabled(True))

        self.tool_random_di.clicked.connect(on_button_random_di_clicked)

        def on_button_random_ao_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}AO", self.modbus_cfg.ao, 2,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None,
                                                 mb_client_pid=self.command_pid)
            self.tool_random_ao.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_ao.setEnabled(True))

        self.tool_random_ao.clicked.connect(on_button_random_ao_clicked)

        def on_button_random_ai_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}AI", self.modbus_cfg.ai, 2,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None,
                                                 mb_client_pid=self.command_pid)
            self.tool_random_ai.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_ai.setEnabled(True))

        self.tool_random_ai.clicked.connect(on_button_random_ai_clicked)

    def __shm_tools_init_dump_gui(self) -> None:
        # file dialogs
        def on_dump_do_file_dialog() -> None:
            text = self.tool_dump_do_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DO"

            file_name, _ = QFileDialog.getSaveFileName(
                self, caption="select DO register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_do_file.setText(file_name)

        self.tool_dump_do_file_dialog.clicked.connect(on_dump_do_file_dialog)

        def on_dump_di_file_dialog() -> None:
            text = self.tool_dump_di_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DI"

            file_name, _ = QFileDialog.getSaveFileName(
                self, caption="select DI register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_di_file.setText(file_name)

        self.tool_dump_di_file_dialog.clicked.connect(on_dump_di_file_dialog)

        def on_dump_ao_file_dialog() -> None:
            text = self.tool_dump_ao_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}ao"

            file_name, _ = QFileDialog.getSaveFileName(
                self, caption="select AO register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_ao_file.setText(file_name)

        self.tool_dump_ao_file_dialog.clicked.connect(on_dump_ao_file_dialog)

        def on_dump_ai_file_dialog() -> None:
            text = self.tool_dump_ai_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}ai"

            file_name, _ = QFileDialog.getSaveFileName(
                self, caption="select AI register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_ai_file.setText(file_name)

        self.tool_dump_ai_file_dialog.clicked.connect(on_dump_ai_file_dialog)

        # dump buttons
        def on_dump_do() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}DO", self.tool_dump_do_file.text(),
                                                self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_do.clicked.connect(on_dump_do)

        def on_dump_di() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}DI", self.tool_dump_di_file.text(),
                                                self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_di.clicked.connect(on_dump_di)

        def on_dump_ao() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}AO", self.tool_dump_ao_file.text(),
                                                self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_ao.clicked.connect(on_dump_ao)

        def on_dump_ai() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}AI", self.tool_dump_ai_file.text(),
                                                self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_ai.clicked.connect(on_dump_ai)

    def __shm_tools_init_load_gui(self):
        def on_load_do_file_dialog() -> None:
            text = self.tool_load_do_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DO"

            file_name, _ = QFileDialog.getOpenFileName(
                self, caption="select DO register load file", dir=filename)
            if len(file_name):
                self.tool_load_do_file.setText(file_name)

        self.tool_load_do_file_dialog.clicked.connect(on_load_do_file_dialog)

        def on_load_di_file_dialog() -> None:
            text = self.tool_load_di_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DI"

            file_name, _ = QFileDialog.getOpenFileName(
                self, caption="select DI register load file", dir=filename)
            if len(file_name):
                self.tool_load_di_file.setText(file_name)

        self.tool_load_di_file_dialog.clicked.connect(on_load_di_file_dialog)

        def on_load_ao_file_dialog() -> None:
            text = self.tool_load_ao_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}AO"

            file_name, _ = QFileDialog.getOpenFileName(
                self, caption="select AO register load file", dir=filename)
            if len(file_name):
                self.tool_load_ao_file.setText(file_name)

        self.tool_load_ao_file_dialog.clicked.connect(on_load_ao_file_dialog)

        def on_load_ai_file_dialog() -> None:
            text = self.tool_load_ai_file.text()
            filename = text if len(
                text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}AI"

            file_name, _ = QFileDialog.getOpenFileName(
                self, caption="select AI register load file", dir=filename)
            if len(file_name):
                self.tool_load_ai_file.setText(file_name)

        self.tool_load_ai_file_dialog.clicked.connect(on_load_ai_file_dialog)

        # button load
        def on_load_do() -> None:
            try:
                self.shm_tools.load_shm_from_file(
                    f"{self.modbus_cfg.name_prefix}DO",
                    self.tool_load_do_file.text(),
                    self.tool_load_do_invert.isChecked(),
                    self.tool_load_do_repeat.isChecked(),
                    self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load shared memory: {e}")

        self.tool_load_do.clicked.connect(on_load_do)

        def on_load_di() -> None:
            try:
                self.shm_tools.load_shm_from_file(
                    f"{self.modbus_cfg.name_prefix}DI",
                    self.tool_load_di_file.text(),
                    self.tool_load_di_invert.isChecked(),
                    self.tool_load_di_repeat.isChecked(),
                    self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load shared memory: {e}")

        self.tool_load_di.clicked.connect(on_load_di)

        def on_load_ao() -> None:
            try:
                self.shm_tools.load_shm_from_file(
                    f"{self.modbus_cfg.name_prefix}AO",
                    self.tool_load_ao_file.text(),
                    self.tool_load_ao_invert.isChecked(),
                    self.tool_load_ao_repeat.isChecked(),
                    self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load shared memory: {e}")

        self.tool_load_ao.clicked.connect(on_load_ao)

        def on_load_ai() -> None:
            try:
                self.shm_tools.load_shm_from_file(
                    f"{self.modbus_cfg.name_prefix}AI",
                    self.tool_load_ai_file.text(),
                    self.tool_load_ai_invert.isChecked(),
                    self.tool_load_ai_repeat.isChecked(),
                    self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load shared memory: {e}")

        self.tool_load_ai.clicked.connect(on_load_ai)

    def __shm_tools_init_inspect_gui(self):
        def on_button_tool_inspect() -> None:
            inspect_values = self.shm_tools.start_inspect_values(self.modbus_cfg.name_prefix, self.modbus_cfg.do,
                                                                 self.modbus_cfg.di, self.modbus_cfg.ao,
                                                                 self.modbus_cfg.ai,
                                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_inspec_values.setEnabled(False)
            inspect_values.closed.connect(
                lambda: self.tool_inspec_values.setEnabled(True))

        self.tool_inspec_values.clicked.connect(on_button_tool_inspect)

    def __shm_tools_init_set_gui(self):
        def on_button_tool_set() -> None:
            set_values = self.shm_tools.start_set_values(self.modbus_cfg.name_prefix, self.modbus_cfg.do,
                                                         self.modbus_cfg.di, self.modbus_cfg.ao,
                                                         self.modbus_cfg.ai,
                                                         self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_set_values.setEnabled(False)
            set_values.closed.connect(
                lambda: self.tool_set_values.setEnabled(True))

        self.tool_set_values.clicked.connect(on_button_tool_set)

    def __close_tool_windows(self):
        """
        @brief close all tool windows
        """
        self.shm_tools.close_all()

    def closeEvent(self, event):
        super().closeEvent(event)
        self.__close_tool_windows()
        if self.window_open:
            self.command_window.closeEvent(event)
        if self.search_tty_window:
            self.search_tty_window.closeEvent(event)

    def version_popup(self):
        version_cmd = ["shm-modbus", "--version-all"]
        cmd = shlex.join(version_cmd)
        process = QProcess()
        process.start(version_cmd[0], version_cmd[1:])
        finished = process.waitForFinished(2000)

        if not finished:
            if process.exitStatus() == QProcess.NormalExit:
                version_str = f"command '{cmd}' crashed!"
            else:
                version_str = f"command '{cmd}' timed out!"
        else:
            if process.exitCode() != 0:
                data = process.readAllStandardError()
                exit_code = process.exitCode()
                msg = bytes(data).decode("utf-8")
                version_str = f"command '{cmd}' failed!\n\nexit code: {exit_code}\nstderr: {msg}"
            else:
                data = process.readAllStandardOutput()
                lines = bytes(data).decode("utf-8").split('\n')
                version_str = "\n".join(x.split(' (')[0] for x in lines)

        QMessageBox.information(
            self, "SHM Modbus Version", version_str)
