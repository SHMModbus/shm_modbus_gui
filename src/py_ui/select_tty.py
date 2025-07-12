# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_tty.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QListWidget, QListWidgetItem, QScrollArea,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SelectTTY(object):
    def setupUi(self, SelectTTY):
        if not SelectTTY.objectName():
            SelectTTY.setObjectName(u"SelectTTY")
        SelectTTY.resize(400, 300)
        self.verticalLayout = QVBoxLayout(SelectTTY)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(SelectTTY)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 384, 244))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tty_list = QListWidget(self.scrollAreaWidgetContents)
        self.tty_list.setObjectName(u"tty_list")
        self.tty_list.setSelectionRectVisible(True)
        self.tty_list.setSortingEnabled(False)

        self.gridLayout.addWidget(self.tty_list, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.buttons = QDialogButtonBox(SelectTTY)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setOrientation(Qt.Orientation.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Retry)

        self.verticalLayout.addWidget(self.buttons)


        self.retranslateUi(SelectTTY)
        self.buttons.accepted.connect(SelectTTY.accept)
        self.buttons.rejected.connect(SelectTTY.reject)

        QMetaObject.connectSlotsByName(SelectTTY)
    # setupUi

    def retranslateUi(self, SelectTTY):
        SelectTTY.setWindowTitle(QCoreApplication.translate("SelectTTY", u"Select TTY", None))
    # retranslateUi

