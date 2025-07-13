from PySide6.QtCore import QProcess

from .SHMHexdump import SHMHexdump
from .SHMRandom import SHMRandom
from .InspectSHM import InspectSHM
from .SetValues import SetValues


class SHMTools:
    def __init__(self, main_window: any) -> None:
        self.main_window = main_window

        self.hexdump: dict[str, SHMHexdump] = {}
        self.random: dict[str, SHMRandom] = {}
        self.inspect_values: dict[str, InspectSHM] = {}
        self.set_values: dict[str, SetValues] = {}

    def close_all(self) -> None:
        # close all hexdump windows
        hexdump_shm_names = [x for x in self.hexdump.keys()]
        for shm_name in hexdump_shm_names:
            self.hexdump[shm_name].close()

        # close all random windows
        random_shm_name = [x for x in self.random.keys()]
        for shm_name in random_shm_name:
            self.random[shm_name].close()

        # close inspect_values
        inspec_shm_name = [x for x in self.inspect_values.keys()]
        for shm_name in inspec_shm_name:
            self.inspect_values[shm_name].close()

        # close set_values
        set_shm_name = [x for x in self.set_values.keys()]
        for shm_name in set_shm_name:
            self.set_values[shm_name].close()

    def start_hexdump(self, shm_name: str, registers: int, register_size: int,
                      semaphore: str | None = None) -> SHMHexdump:
        if shm_name in self.hexdump:
            raise RuntimeError(f"Internal Error: A SHMHexdump object already exists for {shm_name}")

        hexdump = SHMHexdump(shm_name, registers, register_size, semaphore)
        self.hexdump[shm_name] = hexdump
        hexdump.closed.connect(lambda: self.hexdump.pop(shm_name))
        hexdump.show()
        return hexdump

    def start_random(self, shm_name: str, registers, register_size, semaphore: str | None = None,
                     bitmask: int or None = None, mb_client_pid: int | None = None) -> SHMRandom:
        if shm_name in self.random:
            raise RuntimeError(f"Internal Error: A SHMRandom object already exists for {shm_name}")

        random = SHMRandom(shm_name, registers, register_size, bitmask=bitmask, semaphore=semaphore,
                           mb_client_pid=mb_client_pid)
        self.random[shm_name] = random
        random.closed.connect(lambda: self.random.pop(shm_name))
        random.show()
        return random

    def start_inspect_values(self, shm_prefix: str, num_DO: int, num_DI: int, num_AO: int, num_AI: int, semaphore: str | None = None):
        if shm_prefix in self.inspect_values:
            raise RuntimeError(f"Internal Error: A inspect_values object for shm prefix {shm_prefix} already exists")

        self.inspect_values[shm_prefix] = InspectSHM(shm_prefix, num_DO, num_DI, num_AO, num_AI, semaphore)
        self.inspect_values[shm_prefix].closed.connect(lambda: self.inspect_values.pop(shm_prefix))
        self.inspect_values[shm_prefix].show()
        return self.inspect_values[shm_prefix]

    def start_set_values(self, shm_prefix: str, num_DO: int, num_DI: int, num_AO: int, num_AI: int, semaphore: str | None = None):
        if shm_prefix in self.set_values:
            raise RuntimeError(f"Internal Error: A set_values object shm prefix {shm_prefix} already exists")

        self.set_values[shm_prefix] = SetValues(shm_prefix, num_DO, num_DI, num_AO, num_AI, semaphore)
        self.set_values[shm_prefix].closed.connect(lambda: self.set_values.pop(shm_prefix))
        self.set_values[shm_prefix].show()
        return self.set_values[shm_prefix]

    @staticmethod
    def dump_shm_to_file(shm_name: str, filename: str, semaphore: str | None) -> None:
        print(f"{shm_name} > {filename}")
        sem_cmd = f" -s \"{semaphore}\"" if semaphore else ""
        process = QProcess()
        process.start("bash", ["-c", f"dump-shm \"{shm_name}\"{sem_cmd} > \"{filename}\""])
        if process.waitForFinished(1000):
            if process.exitCode() != 0:
                stderr = bytes(process.readAllStandardError()).decode("utf-8")
                err_msg = stderr.split(':', maxsplit=2)
                if len(err_msg) == 3:
                    err_msg = err_msg[-1].strip()
                else:
                    err_msg = stderr
                raise RuntimeError(f"{err_msg}\n\nexit code: {process.exitCode()}")
        else:
            process.kill()
            raise RuntimeError(f"command dump-shm timed out")
        pass

    @staticmethod
    def load_shm_from_file(shm_name: str, filename: str, invert: bool, repeat: bool, semaphore: str | None) -> None:
        print(f"{shm_name} < {filename}")
        sem_cmd = f" -s \"{semaphore}\"" if semaphore else ""
        cmd = f"write-shm -n \"{shm_name}\""
        if invert:
            cmd += " -i"
        if repeat:
            cmd += " -r"
        cmd += f"{sem_cmd} < \"{filename}\""

        process = QProcess()
        process.start("bash", ["-c", cmd])
        if process.waitForFinished(1000):
            if process.exitCode() != 0:
                stderr = bytes(process.readAllStandardError()).decode("utf-8")
                err_msg = stderr.split(':', maxsplit=2)
                if len(err_msg) == 3:
                    err_msg = err_msg[-1].strip()
                else:
                    err_msg = stderr
                raise RuntimeError(f"{err_msg}\n\nexit code: {process.exitCode()}")
        else:
            process.kill()
            raise RuntimeError(f"command write-shm timed out")
