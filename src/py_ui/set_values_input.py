# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_values_input.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_InputValue(object):
    def setupUi(self, InputValue):
        if not InputValue.objectName():
            InputValue.setObjectName(u"InputValue")
        InputValue.resize(229, 107)
        self.gridLayout = QGridLayout(InputValue)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(InputValue)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 1, 1, 1)

        self.value_input = QLineEdit(InputValue)
        self.value_input.setObjectName(u"value_input")

        self.gridLayout.addWidget(self.value_input, 0, 1, 1, 1)

        self.label = QLabel(InputValue)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.retranslateUi(InputValue)

        QMetaObject.connectSlotsByName(InputValue)
    # setupUi

    def retranslateUi(self, InputValue):
        InputValue.setWindowTitle(QCoreApplication.translate("InputValue", u"Input Value", None))
        self.label.setText(QCoreApplication.translate("InputValue", u"Value:", None))
    # retranslateUi

