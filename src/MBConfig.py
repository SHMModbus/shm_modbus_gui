import re
from abc import ABC, abstractmethod

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
             ("shm.name_prefix", str))


class MBConfig(ABC):
    def __init__(self, main_window: any):
        # registers
        self.do = main_window.mbtcp_do.value()
        self.di = main_window.mbtcp_di.value()
        self.ao = main_window.mbtcp_ao.value()
        self.ai = main_window.mbtcp_ai.value()

        # shm
        self.force = main_window.mbtcp_force.isChecked()
        self.name_prefix = main_window.mbtcp_name_prefix.text()

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

    @abstractmethod
    def get_command(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def apply(self, main_window: any) -> None:
        raise NotImplementedError

    @abstractmethod
    def save(self, filename: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def load(self, filename: str) -> None:
        raise NotImplementedError
