import os

from PySide6 import QtWidgets
from PySide6.QtCore import QRegularExpression
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QFileDialog, QMessageBox

import MBConfig
import SHMTools
from py_ui import Ui_MainWindow
from mbtcp_config import MBTCPConfig
from mbrtu_config import MBRTUConfig
from MBxxOutput import MBxxOutput
import constants


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # disable tools
        self.tab_shm_tools.setEnabled(False)

        # Modbus TCP
        self.__init_mbtcp()

        # Modbus RTU
        self.__init_mbrtu()

        # Command Window
        self.command_window: MBxxOutput | None = None
        self.process_active: bool = False
        self.window_open: bool = False

        # internal variables
        self.modbus_cfg: MBConfig.MBConfig | None = None

        # SHM Tools
        self.shm_tools = SHMTools.SHMTools(self)
        self.__shm_tools_init_gui()

        # Version popup
        self.actionVersion.triggered.connect(
            lambda: QMessageBox.information(self, "SHM Modbus Version", f"{constants.APP_NAME} {constants.VERSION}"))

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

        # Registers
        self.mbtcp_do_default.click()
        self.mbtcp_di_default.click()
        self.mbtcp_ao_default.click()
        self.mbtcp_ai_default.click()

        # Shared memory
        self.mbtcp_shm_defaults.click()
        self.mbtcp_name_default.click()
        self.mbtcp_separate_list_clear.click()

        # Modbus
        self.mbtcp_mb_flags_default.click()

        # Semaphore
        self.mbtcp_sem_defaults.click()
        self.mbtcp_sem_name_default.click()

    def __mbtcp_button_actions(self) -> None:
        """
        @brief connect button signals
        """
        # Network
        self.mbtcp_host_default.clicked.connect(lambda: self.mbtcp_host.setText("any"))
        self.mbtcp_port_default.clicked.connect(lambda: self.mbtcp_port.setValue(502))

        def tcp_timeout_default() -> None:
            self.mbtcp_tcp_timeout.setValue(5),
            self.mbtcp_sytstem_tcp_timeout.setChecked(False)

        self.mbtcp_tcp_timeout_default.clicked.connect(tcp_timeout_default)
        self.mbtcp_connections_default.clicked.connect(lambda: self.mbtcp_connections.setValue(1))
        self.mbtcp_nw_flags_default.clicked.connect(lambda: self.mbtcp_reconnect.setChecked(True))

        # Registers
        self.mbtcp_do_default.clicked.connect(lambda: self.mbtcp_do.setValue(65536))
        self.mbtcp_di_default.clicked.connect(lambda: self.mbtcp_di.setValue(65536))
        self.mbtcp_ao_default.clicked.connect(lambda: self.mbtcp_ao.setValue(65536))
        self.mbtcp_ai_default.clicked.connect(lambda: self.mbtcp_ai.setValue(65536))

        # Shared Memory
        def shm_default_flags() -> None:
            self.mbtcp_force.setChecked(False)
            self.mbtcp_separate.setChecked(False)
            self.mbtcp_separate_all.setChecked(False)
            self.mbtcp_separate_all.setEnabled(False)

        self.mbtcp_shm_defaults.clicked.connect(shm_default_flags)
        self.mbtcp_name_default.clicked.connect(lambda: self.mbtcp_name_prefix.setText("modbus_"))
        self.mbtcp_separate_list_clear.clicked.connect(lambda: self.mbtcp_separate_list.clear())

        # Modbus
        def modbus_defaults() -> None:
            self.mbtcp_monitor.setChecked(False)
            self.mbtcp_enable_byte_timeout.setChecked(False)
            self.mbtcp_enable_response_timeout.setChecked(False)
            self.mbtcp_byte_timeout.setEnabled(False)
            self.mbtcp_byte_timeout.setValue(0)
            self.mbtcp_response_timeout.setEnabled(False)
            self.mbtcp_response_timeout.setValue(0)

        self.mbtcp_mb_flags_default.clicked.connect(modbus_defaults)

        # Semaphore
        def semaphore_defaults() -> None:
            self.mbtcp_sem_enable.setChecked(True)
            self.mbtcp_sem_force.setChecked(False)

        self.mbtcp_sem_defaults.clicked.connect(semaphore_defaults)
        self.mbtcp_sem_name_default.clicked.connect(lambda: self.mbtcp_sem_name.setText("modbus"))

        # reset all
        self.mbtcp_defaults.clicked.connect(self.__mbtcp_default_values)

        # start button
        self.mbtcp_start.clicked.connect(self.__mbtcp_start_button_clicked)

        # save / load
        self.actionsave_modbus_tcp_client_config.triggered.connect(self.__mbtcp_config_save)
        self.actionopen_modbus_tcp_client_config.triggered.connect(self.__mbtcp_config_load)

    def __mbtcp_validators(self) -> None:
        """
        @brief set validators for text input
        """
        name_re = QRegularExpression(constants.NAME_REGEX)
        separate_list_re = QRegularExpression(constants.BYTE_REGEX)

        name_validator = QRegularExpressionValidator(name_re)
        separate_list_validator = QRegularExpressionValidator(separate_list_re)

        self.mbtcp_host.setValidator(name_validator)
        self.mbtcp_name_prefix.setValidator(name_validator)
        self.mbtcp_sem_name.setValidator(name_validator)
        self.mbtcp_separate_list.setValidator(separate_list_validator)

    def __mbtcp_ui_actions(self) -> None:
        """
        @brief connect signals/slots for ui
        """

        # shared memory separate
        def shm_separate_changed(value: int) -> None:
            enabled = value != 0
            self.mbtcp_separate_all.setEnabled(enabled)
            self.mbtcp_separate_list.setEnabled(enabled and not self.mbtcp_separate_all.isChecked())

        self.mbtcp_separate.stateChanged.connect(shm_separate_changed)

        # shared memory separate all
        self.mbtcp_separate_all.stateChanged.connect(
            lambda value: self.mbtcp_separate_list.setEnabled(value == 0 and self.mbtcp_separate.isChecked())
        )

        # modbus byte timeout
        self.mbtcp_enable_byte_timeout.stateChanged.connect(
            lambda value: self.mbtcp_byte_timeout.setEnabled(value != 0)
        )

        # modbus response timeout
        self.mbtcp_enable_response_timeout.stateChanged.connect(
            lambda value: self.mbtcp_response_timeout.setEnabled(value != 0)
        )

        # semaphore enable
        def semaphore_enable_changes(value: int) -> None:
            enabled = value != 0
            self.mbtcp_sem_force.setEnabled(enabled)
            self.mbtcp_sem_name.setEnabled(enabled)

        self.mbtcp_sem_enable.stateChanged.connect(semaphore_enable_changes)

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
            self.mbrtu_start.setEnabled(False)
            self.mbtcp_settings.setEnabled(False)
            self.mbtcp_defaults.setEnabled(False)
            self.mbtcp_start.setText("Stop")
            self.tab_shm_tools.setEnabled(True)

            # execute command
            self.modbus_cfg = MBTCPConfig(self)
            self.__exec_process("Shared Memory Modbus TCP Client")

    def __mbtcp_config_save(self) -> None:
        """
        @brief save mbtcp config to file
        """

        file_name, _ = QFileDialog.getSaveFileName(self, caption="Save Modbus TCP config", filter="*.json")

        if len(file_name):
            try:
                MBTCPConfig(self).save(file_name)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save configuration: {e}")

    def __mbtcp_config_load(self) -> None:
        """
        @brief load mbtcp config from file
        """
        file_name, _ = QFileDialog.getOpenFileName(self, caption="Load Modbus TCP config", filter="*.json")

        if len(file_name):
            try:
                config = MBTCPConfig(self)
                config.load(file_name)
                config.apply(self)
            except RuntimeError as e:
                QMessageBox.critical(self, "Error", f"Failed to load configuration: {e}")

    def __init_mbrtu(self) -> None:
        """
        @brief initialize modbus rtu ui
        """
        self.__mbrtu_button_actions()
        self.__mbrtu_default_values()
        self.__mbrtu_ui_actions()
        self.__mbrtu_validators()

    def __mbrtu_default_values(self) -> None:
        # Registers
        self.mbrtu_do_default.click()
        self.mbrtu_di_default.click()
        self.mbrtu_ao_default.click()
        self.mbrtu_ai_default.click()

        # Shared memory
        self.mbrtu_shm_flags_default.click()
        self.mbrtu_shm_name_default.click()

        # Modbus
        self.mbrtu_modbus_flags_default.click()
        self.mbrtu_clientid_default.click()

        # Semaphore
        self.mbrtu_sem_flags_default.click()
        self.mbrtu_sem_name_default.click()

    def __mbrtu_button_actions(self) -> None:
        """
        @brief connect button signals
        """
        # Serial
        self.mbrtu_device_default.clicked.connect(lambda: self.mbrtu_device.clear())
        self.mbrtu_parity_default.clicked.connect(lambda: self.mbrtu_parity.setCurrentIndex(0))
        self.mbrtu_databits_default.clicked.connect(lambda: self.mbrtu_databits.setValue(8))
        self.mbrtu_stopbits_default.clicked.connect(lambda: self.mbrtu_stopbits.setValue(1))
        self.mbrtu_baudrate_default.clicked.connect(lambda: self.mbrtu_baudrate.text("115200"))
        self.mbrtu_serialtype_default.clicked.connect(lambda: self.mbrtu_serialtype.setCurrentIndex(0))

        # Registers
        self.mbrtu_do_default.clicked.connect(lambda: self.mbrtu_do.setValue(65536))
        self.mbrtu_di_default.clicked.connect(lambda: self.mbrtu_di.setValue(65536))
        self.mbrtu_ao_default.clicked.connect(lambda: self.mbrtu_ao.setValue(65536))
        self.mbrtu_ai_default.clicked.connect(lambda: self.mbrtu_ai.setValue(65536))

        # Shared Memory
        self.mbrtu_shm_flags_default.clicked.connect(lambda: self.mbrtu_force.setChecked(False))
        self.mbrtu_shm_name_default.clicked.connect(lambda: self.mbrtu_shm_name.setText("modbus_"))

        # Modbus
        def modbus_defaults() -> None:
            self.mbrtu_monitor.setChecked(False)
            self.mbrtu_enable_byte_timeout.setChecked(False)
            self.mbrtu_enable_response_timeout.setChecked(False)
            self.mbrtu_byte_timeout.setEnabled(False)
            self.mbrtu_byte_timeout.setValue(0)
            self.mbrtu_response_timeout.setEnabled(False)
            self.mbrtu_response_timeout.setValue(0)

        self.mbrtu_modbus_flags_default.clicked.connect(modbus_defaults)
        self.mbrtu_clientid_default.clicked.connect(lambda: self.mbrtu_clientid.setValue(0))

        # Semaphore
        def semaphore_defaults() -> None:
            self.mbrtu_sem_enable.setChecked(True)
            self.mbrtu_sem_force.setChecked(False)

        self.mbrtu_sem_flags_default.clicked.connect(semaphore_defaults)
        self.mbrtu_sem_name_default.clicked.connect(lambda: self.mbrtu_sem_name.setText("modbus"))

    def __mbrtu_validators(self) -> None:
        """
        @brief set validators for text input
        """
        device_re = QRegularExpression(constants.DEVICE_REGEX)
        name_re = QRegularExpression(constants.NAME_REGEX)
        baud_re = QRegularExpression(constants.BAUD_REGEX)

        device_validator = QRegularExpressionValidator(device_re)
        name_validator = QRegularExpressionValidator(name_re)
        baud_validator = QRegularExpressionValidator(baud_re)

        self.mbrtu_device.setValidator(device_validator)
        self.mbrtu_shm_name.setValidator(name_validator)
        self.mbrtu_sem_name.setValidator(name_validator)
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
            self.mbtcp_start.setEnabled(False)
            self.mbrtu_settings.setEnabled(False)
            self.mbrtu_defaults.setEnabled(False)
            self.mbrtu_start.setText("Stop")
            self.tab_shm_tools.setEnabled(True)

            # execute command
            self.modbus_cfg = MBRTUConfig(self)
            self.__exec_process("Shared Memory Modbus RTU Client")

    def __mbrtu_ui_actions(self) -> None:
        """
        @brief connect signals/slots for ui
        """
        # modbus byte timeout
        self.mbrtu_enable_byte_timeout.stateChanged.connect(
            lambda value: self.mbrtu_byte_timeout.setEnabled(value != 0)
        )

        # modbus response timeout
        self.mbrtu_enable_response_timeout.stateChanged.connect(
            lambda value: self.mbrtu_response_timeout.setEnabled(value != 0)
        )

        # semaphore enable
        def semaphore_enable_changes(value: int) -> None:
            enabled = value != 0
            self.mbrtu_sem_force.setEnabled(enabled)
            self.mbrtu_sem_name.setEnabled(enabled)

        self.mbrtu_sem_enable.stateChanged.connect(semaphore_enable_changes)

        # reset all
        self.mbrtu_defaults.clicked.connect(self.__mbrtu_default_values)

        # start button
        self.mbrtu_start.clicked.connect(self.__mbrtu_start_button_clicked)

        # save / load
        self.actionsave_modbus_rtu_client_config.triggered.connect(self.__mbrtu_config_save)
        self.actionopen_modbus_rtu_client_config.triggered.connect(self.__mbrtu_config_load)

    def __mbrtu_config_save(self) -> None:
        """
        @brief save mbrtu config to file
        """
        file_name, _ = QFileDialog.getSaveFileName(self, caption="Save Modbus RTU config", filter="*.json")

        if len(file_name):
            try:
                MBRTUConfig(self).save(file_name)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save configuration: {e}")
                raise

    def __mbrtu_config_load(self) -> None:
        """
        @brief load mbrtu config from file
        """
        file_name, _ = QFileDialog.getOpenFileName(self, caption="Load Modbus RTU config", filter="*.json")

        if len(file_name):
            try:
                config = MBRTUConfig(self)
                config.load(file_name)
                config.apply(self)
            except RuntimeError as e:
                QMessageBox.critical(self, "Error", f"Failed to load configuration: {e}")

    def __exec_process(self, title: str):
        cmd = self.modbus_cfg.get_command()
        self.process_active = True
        self.window_open = True
        self.command_window = MBxxOutput(cmd, title)
        self.command_window.finished.connect(self.__process_finished)
        self.command_window.closed.connect(self.__command_window_closed)
        self.command_window.show()

    def __process_finished(self) -> None:
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

    def __shm_tools_init_gui(self) -> None:
        """
        @brief initialize tool gui
        """
        self.__shm_tools_init_hexdump_gui()
        self.__shm_tools_init_random_gui()
        self.__shm_tools_init_dump_gui()
        self.__shm_tools_init_load_gui()

    def __shm_tools_init_hexdump_gui(self) -> None:
        def on_button_hexdump_do_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}DO", self.modbus_cfg.do, 1,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_do.setEnabled(False)
            hexdump.closed.connect(lambda: self.tool_hexdump_do.setEnabled(True))

        self.tool_hexdump_do.clicked.connect(on_button_hexdump_do_clicked)

        def on_button_hexdump_di_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}DI", self.modbus_cfg.di, 1,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_di.setEnabled(False)
            hexdump.closed.connect(lambda: self.tool_hexdump_di.setEnabled(True))

        self.tool_hexdump_di.clicked.connect(on_button_hexdump_di_clicked)

        def on_button_hexdump_ao_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}AO", self.modbus_cfg.ao, 2,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_ao.setEnabled(False)
            hexdump.closed.connect(lambda: self.tool_hexdump_ao.setEnabled(True))

        self.tool_hexdump_ao.clicked.connect(on_button_hexdump_ao_clicked)

        def on_button_hexdump_ai_clicked() -> None:
            hexdump = self.shm_tools.start_hexdump(f"{self.modbus_cfg.name_prefix}AI", self.modbus_cfg.ai, 2,
                                                   self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_hexdump_ai.setEnabled(False)
            hexdump.closed.connect(lambda: self.tool_hexdump_ai.setEnabled(True))

        self.tool_hexdump_ai.clicked.connect(on_button_hexdump_ai_clicked)

    def __shm_tools_init_random_gui(self) -> None:
        def on_button_random_do_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}DO", self.modbus_cfg.do, 1,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None, 0x1)
            self.tool_random_do.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_do.setEnabled(True))

        self.tool_random_do.clicked.connect(on_button_random_do_clicked)

        def on_button_random_di_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}DI", self.modbus_cfg.do, 1,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None, 0x1)
            self.tool_random_di.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_di.setEnabled(True))

        self.tool_random_di.clicked.connect(on_button_random_di_clicked)

        def on_button_random_ao_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}AO", self.modbus_cfg.do, 2,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_random_ao.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_ao.setEnabled(True))

        self.tool_random_ao.clicked.connect(on_button_random_ao_clicked)

        def on_button_random_ai_clicked() -> None:
            random = self.shm_tools.start_random(f"{self.modbus_cfg.name_prefix}AI", self.modbus_cfg.do, 2,
                                                 self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            self.tool_random_ai.setEnabled(False)
            random.closed.connect(lambda: self.tool_random_ai.setEnabled(True))

        self.tool_random_ai.clicked.connect(on_button_random_ai_clicked)

    def __shm_tools_init_dump_gui(self) -> None:
        # file dialogs
        def on_dump_do_file_dialog() -> None:
            text = self.tool_dump_do_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DO"

            file_name, _ = QFileDialog.getSaveFileName(self, caption="select DO register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_do_file.setText(file_name)

        self.tool_dump_do_file_dialog.clicked.connect(on_dump_do_file_dialog)

        def on_dump_di_file_dialog() -> None:
            text = self.tool_dump_di_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DI"

            file_name, _ = QFileDialog.getSaveFileName(self, caption="select DI register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_di_file.setText(file_name)

        self.tool_dump_di_file_dialog.clicked.connect(on_dump_di_file_dialog)

        def on_dump_ao_file_dialog() -> None:
            text = self.tool_dump_ao_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}ao"

            file_name, _ = QFileDialog.getSaveFileName(self, caption="select AO register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_ao_file.setText(file_name)

        self.tool_dump_ao_file_dialog.clicked.connect(on_dump_ao_file_dialog)

        def on_dump_ai_file_dialog() -> None:
            text = self.tool_dump_ai_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}ai"

            file_name, _ = QFileDialog.getSaveFileName(self, caption="select AI register dump file", dir=filename)
            if len(file_name):
                self.tool_dump_ai_file.setText(file_name)

        self.tool_dump_ai_file_dialog.clicked.connect(on_dump_ai_file_dialog)

        # dump buttons
        def on_dump_do() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}DO", self.tool_dump_do_file.text(),
                                                self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_do.clicked.connect(on_dump_do)

        def on_dump_di() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}DI", self.tool_dump_di_file.text(),
                                                self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_di.clicked.connect(on_dump_di)

        def on_dump_ao() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}AO", self.tool_dump_ao_file.text(),
                                                self.modbus_cfg.sem_name if self.modbus_cfg.sem_enable else None)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_ao.clicked.connect(on_dump_ao)

        def on_dump_ai() -> None:
            try:
                self.shm_tools.dump_shm_to_file(f"{self.modbus_cfg.name_prefix}AI", self.tool_dump_ai_file.text())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to dump shared memory: {e}")

        self.tool_dump_ai.clicked.connect(on_dump_ai)

    def __shm_tools_init_load_gui(self):
        def on_load_do_file_dialog() -> None:
            text = self.tool_load_do_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DO"

            file_name, _ = QFileDialog.getOpenFileName(self, caption="select DO register load file", dir=filename)
            if len(file_name):
                self.tool_load_do_file.setText(file_name)

        self.tool_load_do_file_dialog.clicked.connect(on_load_do_file_dialog)

        def on_load_di_file_dialog() -> None:
            text = self.tool_load_di_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}DI"

            file_name, _ = QFileDialog.getOpenFileName(self, caption="select DI register load file", dir=filename)
            if len(file_name):
                self.tool_load_di_file.setText(file_name)

        self.tool_load_di_file_dialog.clicked.connect(on_load_di_file_dialog)

        def on_load_ao_file_dialog() -> None:
            text = self.tool_load_ao_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}AO"

            file_name, _ = QFileDialog.getOpenFileName(self, caption="select AO register load file", dir=filename)
            if len(file_name):
                self.tool_load_ao_file.setText(file_name)

        self.tool_load_ao_file_dialog.clicked.connect(on_load_ao_file_dialog)

        def on_load_ai_file_dialog() -> None:
            text = self.tool_load_ai_file.text()
            filename = text if len(text) else f"{os.getcwd()}/{self.modbus_cfg.name_prefix}AI"

            file_name, _ = QFileDialog.getOpenFileName(self, caption="select AI register load file", dir=filename)
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
                QMessageBox.critical(self, "Error", f"Failed to load shared memory: {e}")

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
                QMessageBox.critical(self, "Error", f"Failed to load shared memory: {e}")

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
                QMessageBox.critical(self, "Error", f"Failed to load shared memory: {e}")

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
                QMessageBox.critical(self, "Error", f"Failed to load shared memory: {e}")

        self.tool_load_ai.clicked.connect(on_load_ai)

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
