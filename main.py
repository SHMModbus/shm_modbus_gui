#!/usr/bin/python

import sys
from MainWindow import MainWindow
from PySide6 import QtWidgets


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
