from PySide6 import QtWidgets
import sys

from src import InspectSHM

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = InspectSHM.InspectSHM("modbus_", 4, 8, 16, 32, "modbus")
    window.show()
    app.exec()
