import os
import re

from PyQt6.QtWidgets import QMessageBox
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QDialogButtonBox

from .py_ui import Ui_SelectTTY

class SelectTTY(QtWidgets.QWidget, Ui_SelectTTY):
    closed = QtCore.Signal()
    set_tty = QtCore.Signal(str)

    def __init__(self):
        super(SelectTTY, self).__init__()
        self.setupUi(self)
        self.setDisabled(True)

        self.button_retry = self.buttons.button(QDialogButtonBox.StandardButton.Retry)
        self.button_ok = self.buttons.button(QDialogButtonBox.StandardButton.Ok)

        self.button_ok.clicked.connect(self.__ok)
        self.button_retry.clicked.connect(self.__retry)
        self.tty_list.itemClicked.connect(self.__item_selected)
        self.tty_list.itemActivated.connect(self.__item_activated)

    def __retry(self):
        num_ttys = self.search_tty()
        if num_ttys:
            QMessageBox.information(None, "Success", f"{num_ttys} serial devices found")
        else:
            QMessageBox.warning(None, "No Serial Devices", "Could not find any serial devices")


    def search_tty(self) -> int:
        self.setDisabled(True)
        ttys = set()

        # /dev/serial
        for tty_dir in ["/dev/serial/by-id", "/dev/serial/by-path"]:
            if os.path.isdir(tty_dir):
                tty_by_id = os.listdir(tty_dir)
                tty_path = [os.path.realpath(f"{tty_dir}/{x}") for x in tty_by_id]
                ttys.update(tty_path)
                break

        # /dev/tty*
        warnings = []
        re_usb_acm = re.compile(r"^USB|ACM\d+$")
        re_s = re.compile(r"^S\d+$")
        for device in [x[3:] for x in os.listdir("/dev") if x.startswith("tty")]:
            # /dev/ttyUSB* and /dev/ttyACM*
            if re_usb_acm.match(device):
                ttys.add(f"/dev/tty{device}")
                continue

            # /dev/ttyS*
            if re_s.match(device):
                type_file = f"/sys/class/tty/tty{device}/type"
                try:
                    with open(type_file, 'r', encoding='ascii') as f:
                        tty_type = int(f.read().strip())
                except OSError as err:
                    warnings.append(f"Failed to read file '{type_file}': {err}")
                    continue
                except TypeError as err:
                    warnings.append(f"Unexpected value in file '{type_file}': {err}")
                    continue

                if tty_type != 0:
                    ttys.add(f"/dev/tty{device}")

        if len(warnings) > 0:
            msg = "\n  > ".join(warnings)
            QMessageBox.warning(None, "Warnings", f"Problems occurred while searching for serial devices:\n  > {msg}")

        self.tty_list.clear()
        for tty in sorted(ttys):
            self.tty_list.addItem(tty)

        self.button_ok.setDisabled(True)
        self.setEnabled(True)
        return len(ttys)

    def __item_selected(self, item):
        self.button_ok.setEnabled(item is not None)

    def __item_activated(self, item):
        self.__set_tty(item.text())

    def __ok(self):
        selected = self.tty_list.selectedItems()
        assert len(selected) == 1
        self.__set_tty(selected[0].text())

    def accept(self):
        pass

    def reject(self):
        self.close()

    def closeEvent(self, event):
        super(SelectTTY, self).closeEvent(event)
        self.closed.emit()

    def __set_tty(self, tty: str):
        self.set_tty.emit(tty)
        self.close()
