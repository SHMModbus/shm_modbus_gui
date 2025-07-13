from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QProcess
from PySide6.QtGui import QFontDatabase, QTextCursor
from PySide6.QtWidgets import QFileDialog, QMessageBox

from .py_ui import Ui_MBxxxOutput


class MBxxOutput(QtWidgets.QMainWindow, Ui_MBxxxOutput):
    finished = QtCore.Signal(int)
    closed = QtCore.Signal()

    def __init__(self, command: list, title: str) -> None:
        super(MBxxOutput, self).__init__()
        self.setupUi(self)

        self.setWindowTitle(title)

        fixed_font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.stdout.setFont(fixed_font)
        self.stderr.setFont(fixed_font)

        self.actionSave_STDOUT.triggered.connect(self.__save_stdout)
        self.actionSave_STDERR.triggered.connect(self.__save_stderr)

        self.process_terminated_by_event: bool = False
        self.process = QProcess()
        self.process.readyReadStandardOutput.connect(self.__handle_stdout)
        self.process.readyReadStandardError.connect(self.__handle_stderr)
        self.process.finished.connect(self.__process_finished)
        self.process.start(command[0], command[1:])
        self.process.waitForStarted()
        self.pid = self.process.processId()

    def __handle_stdout(self):
        data = self.process.readAllStandardOutput()
        text = bytes(data).decode("utf-8")
        self.stdout.moveCursor(QTextCursor.End)
        self.stdout.insertPlainText(text)
        pass

    def __handle_stderr(self):
        data = self.process.readAllStandardError()
        text = bytes(data).decode("utf-8")
        self.stderr.moveCursor(QTextCursor.End)
        self.stderr.insertPlainText(text)

    def __process_finished(self, exit_code: int, exit_status: QProcess.ExitStatus):
        if exit_code != 0:
            msg = [
                f"Modbus client terminated with exit code {exit_code}.",
                "See stderr output for details."
            ]
            QMessageBox.critical(
                self, "Client terminated", "\n".join(msg))
        elif not self.process_terminated_by_event:
            QMessageBox.information(self, "Client terminated",
                                    "Modbus client terminated successfully.")
        self.finished.emit(exit_code)

    def closeEvent(self, event):
        super(MBxxOutput, self).closeEvent(event)
        self.process_terminated_by_event = True
        self.process.terminate()
        self.closed.emit()

    def terminate(self):
        self.process.terminate()

    def __save_data_to_file(self, data, caption: str):
        file_name, _ = QFileDialog.getSaveFileName(self, caption=caption, filter="*.txt")
        try:
            with open(file_name, 'w') as f:
                f.write(data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save: {e}")

    def __save_stdout(self):
        data = self.stdout.toPlainText()
        self.__save_data_to_file(data, "Save STDOUT")

    def __save_stderr(self):
        data = self.stderr.toPlainText()
        self.__save_data_to_file(data, "Save STDERR")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MBxxOutput(["uname", "-a"], "Test MBxxOutput")
    window.finished.connect(lambda: print("process finished"))
    window.closed.connect(lambda: print("window closed"))
    window.show()

    app.exec()
