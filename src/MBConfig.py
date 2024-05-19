import re
import json

from . import constants

JSON_KEYS = (("modbus.byte_timeout", float),
             ("modbus.edit_byte_timeout", bool),
             ("modbus.edit_response_timeout", bool),
             ("modbus.monitor", bool),
             ("modbus.response_timeout", float),
             ("registers.ai", int),
             ("registers.ao", int),
             ("registers.di", int),
             ("registers.do", int),
             ("semaphore.enable", bool),
             ("semaphore.force", bool),
             ("semaphore.name", str),
             ("shm.force", bool),
             ("shm.name_prefix", str),
             ("tcp.network.connections", int),
             ("tcp.network.host", str),
             ("tcp.network.port", int),
             ("tcp.network.system_tcp_timeout", bool),
             ("tcp.network.tcp_timeout", int),
             ("tcp.shm.separate", bool),
             ("tcp.shm.separate_all", bool),
             ("tcp.shm.separate_list", list),
             ("rtu.serial.device", str),
             ("rtu.serial.parity", int),
             ("rtu.serial.databits", int),
             ("rtu.serial.stopbits", int),
             ("rtu.serial.baud", str),
             ("rtu.serial.type", int),
             ("rtu.modbus.client_id", int))


class MBConfig:
    def __init__(self, main_window: any):
        # registers
        self.do = main_window.mb_do.value()
        self.di = main_window.mb_di.value()
        self.ao = main_window.mb_ao.value()
        self.ai = main_window.mb_ai.value()

        # shm
        self.force = main_window.mb_force.isChecked()
        self.name_prefix = main_window.mb_shm_name.text()

        # modbus
        self.monitor = main_window.mb_monitor.isChecked()
        self.edit_byte_timeout = main_window.mb_enable_byte_timeout.isChecked()
        self.edit_response_timeout = main_window.mb_enable_response_timeout.isChecked()
        self.byte_timeout = main_window.mb_byte_timeout.value()
        self.response_timeout = main_window.mb_response_timeout.value()

        # semaphore
        self.sem_enable = main_window.mb_sem_enable.isChecked()
        self.sem_force = main_window.mb_sem_force.isChecked()
        self.sem_name = main_window.mb_sem_name.text()

        self.__init_tcp(main_window)
        self.__init_rtu(main_window)

        self.modbus_type = None

    def __init_tcp(self, main_window: any) -> None:
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
            self.separate_list = set(
                [int(x) for x in main_window.mbtcp_separate_list.text().strip().rstrip(',').split(',')])
        else:
            self.separate_list = set()

    def __init_rtu(self, main_window: any) -> None:
        # serial
        self.device = main_window.mbrtu_device.text()
        self.parity = main_window.mbrtu_parity.currentIndex()
        self.databits = main_window.mbrtu_databits.value()
        self.stopbits = main_window.mbrtu_stopbits.value()
        self.baud = main_window.mbrtu_baudrate.text()
        self.serialtype = main_window.mbrtu_serialtype.currentIndex()

        # modbus
        self.client_id = main_window.mbrtu_clientid.value()

    def apply(self, main_window: any) -> None:
        # registers
        main_window.mb_di.setValue(self.di)
        main_window.mb_do.setValue(self.do)
        main_window.mb_ao.setValue(self.ao)
        main_window.mb_ai.setValue(self.ai)

        # shm
        main_window.mb_force.setChecked(self.force)
        main_window.mb_shm_name.setText(self.name_prefix)

        # modbus
        main_window.mb_monitor.setChecked(self.monitor)
        main_window.mb_enable_byte_timeout.setChecked(self.edit_byte_timeout)
        main_window.mb_enable_response_timeout.setChecked(self.edit_response_timeout)
        main_window.mb_byte_timeout.setValue(self.byte_timeout)
        main_window.mb_response_timeout.setValue(self.response_timeout)

        # semaphore
        main_window.mb_sem_enable.setChecked(self.sem_enable)
        main_window.mb_sem_force.setChecked(self.sem_force)
        main_window.mb_sem_name.setText(self.sem_name)

        self.apply_tcp(main_window)
        self.apply_rtu(main_window)

    def apply_tcp(self, main_window: any) -> None:
        # network
        main_window.mbtcp_host.setText(self.host)
        main_window.mbtcp_port.setValue(self.port)
        main_window.mbtcp_tcp_timeout.setValue(self.tcp_timeout)
        main_window.mbtcp_sytstem_tcp_timeout.setChecked(self.system_tcp_timeout)
        main_window.mbtcp_connections.setValue(self.connections)
        main_window.mbtcp_reconnect.setChecked(self.reconnect)

        # shm
        main_window.mbtcp_separate.setChecked(self.separate)
        main_window.mbtcp_separate_all.setChecked(self.separate_all)
        main_window.mbtcp_separate_list.setText(','.join([f"{x}" for x in sorted(self.separate_list)]))

    def apply_rtu(self, main_window: any) -> None:
        # serial
        main_window.mbrtu_device.setText(self.device)
        main_window.mbrtu_parity.setCurrentIndex(self.parity)
        main_window.mbrtu_databits.setValue(self.databits)
        main_window.mbrtu_stopbits.setValue(self.stopbits)
        main_window.mbrtu_baudrate.setText(self.baud)
        main_window.mbrtu_serialtype.setCurrentIndex(self.serialtype)

        # modbus
        main_window.mbrtu_clientid.setValue(self.client_id)

    def as_dict(self) -> dict:
        data = {
            "registers": {
                "do": self.do,
                "di": self.di,
                "ao": self.ao,
                "ai": self.ai,
            },
            "shm": {
                "force": self.force,
                "name_prefix": self.name_prefix,
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
            },
            "tcp": {
                "network": {
                    "host": self.host,
                    "port": self.port,
                    "tcp_timeout": self.tcp_timeout,
                    "system_tcp_timeout": self.system_tcp_timeout,
                    "connections": self.connections,
                    "reconnect": self.reconnect,
                },
                "shm": {
                    "separate": self.separate,
                    "separate_all": self.separate_all,
                    "separate_list": list(self.separate_list)
                }
            },
            "rtu": {
                "serial": {
                    "device": self.device,
                    "parity": self.parity,
                    "databits": self.databits,
                    "stopbits": self.stopbits,
                    "baud": self.baud,
                    "type": self.serialtype,
                },
                "modbus": {
                    "client_id": self.client_id
                }
            }
        }
        return data

    def load_from_dict(self, data: dict) -> None:
        self.byte_timeout = data["modbus"]["byte_timeout"]
        self.edit_byte_timeout = data["modbus"]["edit_byte_timeout"]
        self.edit_response_timeout = data["modbus"]["edit_response_timeout"]
        self.monitor = data["modbus"]["monitor"]
        self.response_timeout = data["modbus"]["response_timeout"]
        self.ai = data["registers"]["ai"]
        self.ao = data["registers"]["ao"]
        self.di = data["registers"]["di"]
        self.do = data["registers"]["do"]
        self.sem_name = data["semaphore"]["name"]
        self.sem_force = data["semaphore"]["force"]
        self.sem_enable = data["semaphore"]["enable"]
        self.force = data["shm"]["force"]
        self.name_prefix = data["shm"]["name_prefix"]

        # rtu
        self.device = data["rtu"]["serial"]["device"]
        self.parity = data["rtu"]["serial"]["parity"]
        self.databits = data["rtu"]["serial"]["databits"]
        self.stopbits = data["rtu"]["serial"]["stopbits"]
        self.baud = data["rtu"]["serial"]["baud"]
        self.serialtype = data["rtu"]["serial"]["type"]
        self.client_id = data["rtu"]["modbus"]["client_id"]

        # tcp
        self.connections = data["tcp"]["network"]["connections"]
        self.host = data["tcp"]["network"]["host"]
        self.port = data["tcp"]["network"]["port"]
        self.system_tcp_timeout = data["tcp"]["network"]["system_tcp_timeout"]
        self.tcp_timeout = data["tcp"]["network"]["tcp_timeout"]
        self.separate = data["tcp"]["shm"]["separate"]
        self.separate_all = data["tcp"]["shm"]["separate_all"]
        self.separate_list = set(data["tcp"]["shm"]["separate_list"])

    @staticmethod
    def check_loaded_data(data, additional_json_keys):
        # check data
        for json_key, data_type in JSON_KEYS + additional_json_keys:
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
        if not re.match(constants.NAME_REGEX, data["semaphore"]["name"]):
            raise RuntimeError("semaphore.name is invalid")

        # - byte timeout
        if data["modbus"]["byte_timeout"] < 0.0:
            raise RuntimeError("modbus.byte_timeout must be greater than 0")

        # - response timeout
        if data["modbus"]["response_timeout"] < 0.0:
            raise RuntimeError("modbus.response_timeout must be greater than 0")

        # - shm name
        if not re.match(constants.NAME_REGEX, data["shm"]["name_prefix"]):
            raise RuntimeError("shm.name_prefix is invalid")

        MBConfig.check_loaded_data_tcp(data)
        MBConfig.check_loaded_data_rtu(data)

    @staticmethod
    def check_loaded_data_tcp(data):
        # - network connections
        if data["tcp"]["network"]["connections"] < 0:
            raise RuntimeError("network.connections is negative")

        # - host
        host = data["tcp"]["network"]["host"]
        if len(host) < 1:
            raise RuntimeError("network.host is empty")
        if not re.match(constants.NAME_REGEX, host):
            raise RuntimeError("network.host is invalid")

        # - port
        if data["tcp"]["network"]["port"] <= 0 or data["tcp"]["network"]["port"] >= 2 ** 16:
            raise RuntimeError("network.port is not a valid TCP port")

        # - tcp timeout
        if data["tcp"]["network"]["tcp_timeout"] <= 0:
            raise RuntimeError("network.tcp_timeout must be greater than 0")

        # - separate list
        for i, value in enumerate(data["tcp"]["shm"]["separate_list"]):
            if not isinstance(value, int):
                raise RuntimeError(f"shm.separate_list[{i}]: invalid data type {type(value).__name__}")
            if value > 255:
                raise RuntimeError(f"shm.separate_list[{i}]: value to large")

    @staticmethod
    def check_loaded_data_rtu(data):
        # - serial device
        if not re.match(constants.DEVICE_REGEX, data["rtu"]["serial"]["device"]):
            raise RuntimeError("serial.device is invalid")

        # - parity
        parity = data["rtu"]["serial"]["parity"]
        if parity < 0 or parity > 2:
            raise RuntimeError("serial.parity is invalid")

        # - data bits
        databits = data["rtu"]["serial"]["databits"]
        if databits < 5 or databits > 8:
            raise RuntimeError("serial.databits is invalid")

        # - stop bits
        stopbits = data["rtu"]["serial"]["stopbits"]
        if stopbits < 1 or stopbits > 2:
            raise RuntimeError("serial.stopbits is invalid")

        # - baud
        if not re.match(constants.BAUD_REGEX, data["rtu"]["serial"]["baud"]):
            raise RuntimeError("serial.baud is invalid")

        # - serial type
        serialtype = data["rtu"]["serial"]["type"]
        if serialtype < 0 or serialtype > 1:
            raise RuntimeError("serial.type is invalid")

        # - client id
        client_id = data["rtu"]["modbus"]["client_id"]
        if client_id < 0 or client_id > 255:
            raise RuntimeError("serial.clientid is invalid")

    def get_command_tcp(self) -> list:
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

    def get_command_rtu(self) -> list:
        command = [
            "modbus-rtu-client-shm",
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
            "-d",
            self.device,
            "-i",
            f"{self.client_id}",
            "--data-bits",
            f"{self.databits}",
            "--stop-bits",
            f"{self.stopbits}",
            "-b",
            self.baud,
            "-p"
        ]

        match self.parity:
            case 0:
                command.append("N")
            case 1:
                command.append("E")
            case 2:
                command.append("O")
            case _:
                raise RuntimeError("Internal error: invalid parity")

        command.append("--rs232" if self.serialtype == 0 else "--rs485")

        if self.monitor:
            command.append("-m")

        if self.edit_byte_timeout:
            command.append("--byte-timeout")
            command.append(f"{self.byte_timeout}")

        if self.edit_response_timeout:
            command.append("--response-timeout")
            command.append(f"{self.response_timeout}")

        if self.force:
            command.append("--force")

        if self.sem_enable:
            command.append("--semaphore")
            command.append(self.sem_name)

            if self.sem_force:
                command.append("--semaphore-force")

        return command

    def save(self, filename: str) -> None:
        data = self.as_dict()

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

    def load(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)

        MBConfig.check_loaded_data(data, JSON_KEYS)

        self.load_from_dict(data)
