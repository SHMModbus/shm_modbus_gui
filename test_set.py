from PySide6 import QtWidgets
import sys

from src import SetValues

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SetValues.SetValues("modbus_", 32, 32, 16, 32, "modbus")
    window.show()
    app.exec()
