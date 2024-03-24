import json
import re

import MBConfig
import constants

JSON_KEYS = (("serial.device", str),
             ("serial.parity", int),
             ("serial.databits", int),
             ("serial.stopbits", int),
             ("serial.baud", str),
             ("serial.type", int),
             ("modbus.clientid", int))


class MBRTUConfig(MBConfig.MBConfig):
    def __init__(self, main_window: any) -> None:
        super().__init__(main_window)

        # serial
        self.device = main_window.mbrtu_device.text()
        self.parity = main_window.mbrtu_parity.currentIndex()
        self.databits = main_window.mbrtu_databits.value()
        self.stopbits = main_window.mbrtu_stopbits.value()
        self.baud = main_window.mbrtu_baudrate.text()
        self.serialtype = main_window.mbrtu_serialtype.currentIndex()

        # modbus
        self.client_id = main_window.mbrtu_clientid.value()

    def save(self, filename: str) -> None:
        data = self.as_dict()
        data["serial"] = {
            "device": self.device,
            "parity": self.parity,
            "databits": self.databits,
            "stopbits": self.stopbits,
            "baud": self.baud,
            "type": self.serialtype,
        }
        data["modbus"]["clientid"] = self.client_id

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)

    def load(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)

        # check data
        MBConfig.MBConfig.check_loaded_data(data, JSON_KEYS)

        # more checks:
        # - serial device
        if not re.match(constants.DEVICE_REGEX, data["serial"]["device"]):
            raise RuntimeError("serial.device is invalid")

        # - parity
        parity = data["serial"]["parity"]
        if parity < 0 or parity > 2:
            raise RuntimeError("serial.parity is invalid")

        # - data bits
        databits = data["serial"]["databits"]
        if databits < 5 or databits > 8:
            raise RuntimeError("serial.databits is invalid")

        # - stop bits
        stopbits = data["serial"]["stopbits"]
        if stopbits < 1 or stopbits > 2:
            raise RuntimeError("serial.stopbits is invalid")

        # - baud
        if not re.match(constants.BAUD_REGEX, data["serial"]["baud"]):
            raise RuntimeError("serial.baud is invalid")

        # - serial type
        serialtype = data["serial"]["type"]
        if serialtype < 0 or serialtype > 1:
            raise RuntimeError("serial.type is invalid")

        # - client id
        client_id = data["modbus"]["clientid"]
        if client_id < 0 or client_id > 255:
            raise RuntimeError("serial.clientid is invalid")

        # load data
        self.load_from_dict(data)
        self.device = data["serial"]["device"]
        self.parity = data["serial"]["parity"]
        self.databits = data["serial"]["databits"]
        self.stopbits = data["serial"]["stopbits"]
        self.baud = data["serial"]["baud"]
        self.serialtype = data["serial"]["type"]
        self.client_id = data["modbus"]["clientid"]

    def apply(self, main_window: any) -> None:
        # serial
        main_window.mbrtu_device.setText(self.device)
        main_window.mbrtu_parity.setCurrentIndex(self.parity)
        main_window.mbrtu_databits.setValue(self.databits)
        main_window.mbrtu_stopbits.setValue(self.stopbits)
        main_window.mbrtu_baudrate.setText(self.baud)
        main_window.mbrtu_serialtype.setCurrentIndex(self.serialtype)

        # registers
        main_window.mbrtu_di.setValue(self.di)
        main_window.mbrtu_do.setValue(self.do)
        main_window.mbrtu_ao.setValue(self.ao)
        main_window.mbrtu_ai.setValue(self.ai)

        # shm
        main_window.mbrtu_force.setChecked(self.force)
        main_window.mbrtu_shm_name.setText(self.name_prefix)

        # modbus
        main_window.mbrtu_monitor.setChecked(self.monitor)
        main_window.mbrtu_enable_byte_timeout.setChecked(self.edit_byte_timeout)
        main_window.mbrtu_enable_response_timeout.setChecked(self.edit_response_timeout)
        main_window.mbrtu_byte_timeout.setValue(self.byte_timeout)
        main_window.mbrtu_response_timeout.setValue(self.response_timeout)
        main_window.mbrtu_clientid.setValue(self.client_id)

        # semaphore
        main_window.mbtcp_sem_enable.setChecked(self.sem_enable)
        main_window.mbtcp_sem_force.setChecked(self.sem_force)
        main_window.mbtcp_sem_name.setText(self.sem_name)

    def get_command(self) -> list:
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
