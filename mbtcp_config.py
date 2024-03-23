import json
import re
import constants

import MBConfig

JSON_KEYS = (("network.connections", int),
             ("network.host", str),
             ("network.port", int),
             ("network.system_tcp_timeout", bool),
             ("network.tcp_timeout", int),
             ("shm.separate", bool),
             ("shm.separate_all", bool),
             ("shm.separate_list", list))


class MBTCPConfig(MBConfig.MBConfig):

    def __init__(self, main_window: any) -> None:
        super().__init__(main_window)
        # network
        self.host = main_window.mbtcp_host.text()
        self.port = main_window.mbtcp_port.value()
        self.tcp_timeout = main_window.mbtcp_tcp_timeout.value()
        self.system_tcp_timeout = main_window.mbtcp_sytstem_tcp_timeout.isChecked()
        self.connections = main_window.mbtcp_connections.value()
        self.reconnect = main_window.mbtcp_reconnect.isChecked()

        # shm
        self.separate = main_window.mbtcp_separate.isChecked()
        self.separate_all = main_window.mbtcp_separate_all.isChecked()
        if len(main_window.mbtcp_separate_list.text().strip()):
            self.separate_list = set([int(x) for x in main_window.mbtcp_separate_list.text().strip().split(',')])
        else:
            self.separate_list = set()

    def save(self, filename: str) -> None:
        data = self.as_dict()
        data["network"] ={
                "host": self.host,
                "port": self.port,
                "tcp_timeout": self.tcp_timeout,
                "system_tcp_timeout": self.system_tcp_timeout,
                "connections": self.connections,
                "reconnect": self.reconnect,
            }
        data["shm"]["separate"] = self.separate
        data["shm"]["separate_all"] = self.separate_all
        data["shm"]["separate_list"] = list(self.separate_list)

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

    def load(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)

        # check data
        MBConfig.MBConfig.check_loaded_data(data, JSON_KEYS)

        # more checks:
        # - network connections
        if data["network"]["connections"] < 0:
            raise RuntimeError("network.connections is negative")

        # - host
        host = data["network"]["host"]
        if len(host) < 1:
            raise RuntimeError("network.host is empty")
        if not re.match(constants.NAME_REGEX, host):
            raise RuntimeError("network.host is invalid")

        # - port
        if data["network"]["port"] <= 0 or data["network"]["port"] >= 2**16:
            raise RuntimeError("network.port is not a valid TCP port")

        # - tcp timeout
        if data["network"]["tcp_timeout"] <= 0:
            raise RuntimeError("network.tcp_timeout must be greater than 0")

        # - separate list
        for i, value in enumerate(data["shm"]["separate_list"]):
            if not isinstance(value, int):
                raise RuntimeError(f"shm.separate_list[{i}]: invalid data type {type(value).__name__}")
            if value > 255:
                raise RuntimeError(f"shm.separate_list[{i}]: value to large")

        # load data
        self.load_from_dict(data)
        self.connections = data["network"]["connections"]
        self.host = data["network"]["host"]
        self.port = data["network"]["port"]
        self.system_tcp_timeout = data["network"]["system_tcp_timeout"]
        self.tcp_timeout = data["network"]["tcp_timeout"]
        self.separate = data["shm"]["separate"]
        self.separate_all = data["shm"]["separate_all"]
        self.separate_list = set(data["shm"]["separate_list"])

    def apply(self, main_window: any) -> None:
        # network
        main_window.mbtcp_host.setText(self.host)
        main_window.mbtcp_port.setValue(self.port)
        main_window.mbtcp_tcp_timeout.setValue(self.tcp_timeout)
        main_window.mbtcp_sytstem_tcp_timeout.setChecked(self.system_tcp_timeout)
        main_window.mbtcp_connections.setValue(self.connections)
        main_window.mbtcp_reconnect.setChecked(self.reconnect)

        # registers
        main_window.mbtcp_di.setValue(self.di)
        main_window.mbtcp_do.setValue(self.do)
        main_window.mbtcp_ao.setValue(self.ao)
        main_window.mbtcp_ai.setValue(self.ai)

        # shm
        main_window.mbtcp_force.setChecked(self.force)
        main_window.mbtcp_separate.setChecked(self.separate)
        main_window.mbtcp_separate_all.setChecked(self.separate_all)
        main_window.mbtcp_name_prefix.setText(self.name_prefix)
        main_window.mbtcp_separate_list.setText(','.join([f"{x}"for x in sorted(self.separate_list)]))

        # modbus
        main_window.mbtcp_monitor.setChecked(self.monitor)
        main_window.mbtcp_enable_byte_timeout.setChecked(self.edit_byte_timeout)
        main_window.mbtcp_enable_response_timeout.setChecked(self.edit_response_timeout)
        main_window.mbtcp_byte_timeout.setValue(self.byte_timeout)
        main_window.mbtcp_response_timeout.setValue(self.response_timeout)

        # semaphore
        main_window.mbtcp_sem_enable.setChecked(self.sem_enable)
        main_window.mbtcp_sem_force.setChecked(self.sem_force)
        main_window.mbtcp_sem_name.setText(self.sem_name)

    def get_command(self) -> list:
        command = [
            "modbus-tcp-client-shm",
            "-i",
            self.host,
            "-p",
            f"{self.port}",
            "-c",
            f"{self.connections}",
            "-n",
            self.name_prefix,
            "--do-registers",
            f"{self.do}",
            "--di-registers",
            f"{self.di}",
            "--ao-registers",
            f"{self.ao}",
            "--ai-registers",
            f"{self.ai}",
            "-t",
            "0" if self.system_tcp_timeout else f"{self.tcp_timeout}",
        ]

        if self.edit_byte_timeout:
            command.append("--byte-timeout")
            command.append(f"{self.byte_timeout}")

        if self.edit_response_timeout:
            command.append("--response-timeout")
            command.append(f"{self.response_timeout}")

        if self.monitor:
            command.append("-m")

        if self.reconnect:
            command.append('-r')

        if self.force:
            command.append("--force")

        if self.sem_enable:
            command.append("--semaphore")
            command.append(self.sem_name)

            if self.sem_force:
                command.append("--semaphore-force")

        if self.separate:
            if self.separate_all:
                command.append("--separate-all")
            else:
                command.append("-s")
                command.append(",".join([f"{x}" for x in self.separate_list]))

        return command
