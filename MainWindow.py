from PySide6 import QtWidgets
from PySide6.QtWidgets import QFileDialog, QMessageBox

from py_ui import Ui_MainWindow
from mbtcp_config import MBTCPConfig


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # disable tools
        self.tab_shm_tools.setEnabled(False)

        self.__inti_mbtcp()

        # TODO RTU
        self.tab_mbrtu.setEnabled(False)

    def __inti_mbtcp(self) -> None:
        """
        @brief initialize modbus tcp ui
        """
        self.__mbtcp_button_actions()
        self.__mbtcp_default_values()
        self.__mbtcp_ui_actions()

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

        def mbtcp_tcp_timeout_default() -> None:
            self.mbtcp_tcp_timeout.setValue(5),
            self.mbtcp_sytstem_tcp_timeout.setChecked(False)

        self.mbtcp_tcp_timeout_default.clicked.connect(mbtcp_tcp_timeout_default)
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
        # TODO start mbtcp client
        pass

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
