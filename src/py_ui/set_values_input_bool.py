# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_values_input_bool.ui'
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
    QGridLayout, QRadioButton, QSizePolicy, QWidget)

class Ui_InputValue(object):
    def setupUi(self, InputValue):
        if not InputValue.objectName():
            InputValue.setObjectName(u"InputValue")
        InputValue.resize(186, 102)
        self.gridLayout = QGridLayout(InputValue)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(InputValue)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.radioButton = QRadioButton(InputValue)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)

        self.radioButton_2 = QRadioButton(InputValue)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)


        self.retranslateUi(InputValue)

        QMetaObject.connectSlotsByName(InputValue)
    # setupUi

    def retranslateUi(self, InputValue):
        InputValue.setWindowTitle(QCoreApplication.translate("InputValue", u"Input Value", None))
        self.radioButton.setText(QCoreApplication.translate("InputValue", u"false (0)", None))
        self.radioButton_2.setText(QCoreApplication.translate("InputValue", u"true (1)", None))
    # retranslateUi

