#!/usr/bin/python

import sys
from PySide6 import QtWidgets
import argparse

from MainWindow import MainWindow
import constants


def main() -> None:
    parser = argparse.ArgumentParser(constants.APP_NAME,
                                     "Graphical interfaces for shared memory modbus tools to simulate a modbus client")
    parser.add_argument("--version", help="print version and exit", action="store_true")
    args = parser.parse_args()

    if args.version:
        print(f"{constants.APP_NAME} {constants.VERSION}")
        exit(0)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
