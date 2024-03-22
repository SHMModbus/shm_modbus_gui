import json

JSON_KEYS = (("modbus.byte_timeout", float),
             ("modbus.edit_byte_timeout", bool),
             ("modbus.edit_response_timeout", bool),
             ("modbus.monitor", bool),
             ("modbus.response_timeout", float),
             ("network.connections", int),
             ("network.host", str),
             ("network.port", int),
             ("network.system_tcp_timeout", bool),
             ("network.tcp_timeout", int),
             ("registers.ai", int),
             ("registers.ao", int),
             ("registers.di", int),
             ("registers.do", int),
             ("semaphore.enable", bool),
             ("semaphore.force", bool),
             ("semaphore.name", str),
             ("shm.force", bool),
             ("shm.name_prefix", str),
             ("shm.separate", bool),
             ("shm.separate_all", bool),
             ("shm.separate_list", list),
             )


class MBTCPConfig:

    def __init__(self, main_window: any) -> None:
        # network
        self.host = main_window.mbtcp_host.text()
        self.port = main_window.mbtcp_port.value()
        self.tcp_timeout = main_window.mbtcp_tcp_timeout.value()
        self.system_tcp_timeout = main_window.mbtcp_sytstem_tcp_timeout.isChecked()
        self.connections = main_window.mbtcp_connections.value()
        self.reconnect = main_window.mbtcp_reconnect.isChecked()

        # registers
        self.do = main_window.mbtcp_do.value()
        self.di = main_window.mbtcp_di.value()
        self.ao = main_window.mbtcp_ao.value()
        self.ai = main_window.mbtcp_ai.value()

        # shm
        self.force = main_window.mbtcp_force.isChecked()
        self.separate = main_window.mbtcp_separate.isChecked()
        self.separate_all = main_window.mbtcp_separate_all.isChecked()
        self.name_prefix = main_window.mbtcp_name_prefix.text()
        if len(main_window.mbtcp_separate_list.text().strip()):
            self.separate_list = set([int(x) for x in main_window.mbtcp_separate_list.text().strip().split(',')])
        else:
            self.separate_list = set()

        # modbus
        self.monitor = main_window.mbtcp_monitor.isChecked()
        self.edit_byte_timeout = main_window.mbtcp_enable_byte_timeout.isChecked()
        self.edit_response_timeout = main_window.mbtcp_enable_response_timeout.isChecked()
        self.byte_timeout = main_window.mbtcp_byte_timeout.value()
        self.response_timeout = main_window.mbtcp_response_timeout.value()

        # semaphore
        self.sem_enable = main_window.mbtcp_sem_enable.isChecked()
        self.sem_force = main_window.mbtcp_sem_force.isChecked()
        self.sem_name = main_window.mbtcp_sem_name.text()

    def save(self, filename: str) -> None:
        data = {
            "network": {
                "host": self.host,
                "port": self.port,
                "tcp_timeout": self.tcp_timeout,
                "system_tcp_timeout": self.system_tcp_timeout,
                "connections": self.connections,
                "reconnect": self.reconnect,
            },
            "registers": {
                "do": self.do,
                "di": self.di,
                "ao": self.ao,
                "ai": self.ai,
            },
            "shm": {
                "force": self.force,
                "separate": self.separate,
                "separate_all": self.separate_all,
                "name_prefix": self.name_prefix,
                "separate_list": list(self.separate_list)
            },
            "modbus": {
                "monitor": self.monitor,
                "edit_byte_timeout": self.edit_byte_timeout,
                "edit_response_timeout": self.edit_response_timeout,
                "byte_timeout": self.byte_timeout,
                "response_timeout": self.response_timeout,
            },
            "semaphore": {
                "enable": self.sem_enable,
                "force": self.sem_force,
                "name": self.sem_name,
            }
        }

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

    def load(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)

        # check data
        for json_key, data_type in JSON_KEYS:
            key_list = json_key.split('.')
            cur = data
            for k in key_list:
                if not isinstance(cur, dict) or k not in cur:
                    raise RuntimeError(f"Missing json key '{json_key}'")
                cur = cur[k]

            if not isinstance(cur, data_type):
                raise RuntimeError(
                    f"'{json_key}' has invalid data type {type(cur).__name__} (expected {data_type.__name__})")

        # more checks:
        # - register sizes
        for reg in ("ai", "ao", "di", "do"):
            if data["registers"][reg] > 65536:
                raise RuntimeError(f"Invalid data: registers.{reg} must be less than 65536")
            if data["registers"][reg] < 0:
                raise RuntimeError(f"Invalid data: registers.{reg} must be at least 1")

        # - semaphore name
        if len(data["semaphore"]["name"]) < 1:
            raise RuntimeError("semaphore.name is empty")

        # - byte timeout
        if data["modbus"]["byte_timeout"] <= 0.0:
            raise RuntimeError("modbus.byte_timeout must be greater than 0")

        # - response timeout
        if data["modbus"]["response_timeout"] <= 0.0:
            raise RuntimeError("modbus.response_timeout must be greater than 0")

        # - network connections
        if data["network"]["connections"] < 0:
            raise RuntimeError("network.connections is negative")

        # - host
        if len(data["network"]["host"]) < 1:
            raise RuntimeError("network.host is empty")

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
        self.byte_timeout = data["modbus"]["byte_timeout"]
        self.edit_byte_timeout = data["modbus"]["edit_byte_timeout"]
        self.edit_response_timeout = data["modbus"]["edit_response_timeout"]
        self.monitor = data["modbus"]["monitor"]
        self.response_timeout = data["modbus"]["response_timeout"]
        self.connections = data["network"]["connections"]
        self.host = data["network"]["host"]
        self.port = data["network"]["port"]
        self.system_tcp_timeout = data["network"]["system_tcp_timeout"]
        self.tcp_timeout = data["network"]["tcp_timeout"]
        self.ai = data["registers"]["ai"]
        self.ao = data["registers"]["ao"]
        self.di = data["registers"]["di"]
        self.do = data["registers"]["do"]
        self.sem_name = data["semaphore"]["name"]
        self.sem_force = data["semaphore"]["force"]
        self.sem_enable = data["semaphore"]["enable"]
        self.force = data["shm"]["force"]
        self.name_prefix = data["shm"]["name_prefix"]
        self.separate = data["shm"]["separate"]
        self.separate_all = data["shm"]["separate_all"]
        self.separate_list = set(data["shm"]["separate_list"])

    def apply(self, main_window: any):
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
