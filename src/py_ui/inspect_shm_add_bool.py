# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inspect_shm_add_bool.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_InspectSHMAddBool(object):
    def setupUi(self, InspectSHMAddBool):
        if not InspectSHMAddBool.objectName():
            InspectSHMAddBool.setObjectName(u"InspectSHMAddBool")
        InspectSHMAddBool.resize(320, 530)
        InspectSHMAddBool.setMinimumSize(QSize(320, 150))
        self.verticalLayout = QVBoxLayout(InspectSHMAddBool)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(InspectSHMAddBool)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 474))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.endian_little = QRadioButton(self.widget_2)
        self.endian_little.setObjectName(u"endian_little")
        self.endian_little.setEnabled(False)
        self.endian_little.setChecked(True)

        self.verticalLayout_3.addWidget(self.endian_little)

        self.endian_big = QRadioButton(self.widget_2)
        self.endian_big.setObjectName(u"endian_big")
        self.endian_big.setEnabled(False)

        self.verticalLayout_3.addWidget(self.endian_big)


        self.gridLayout.addWidget(self.widget_2, 12, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 3, 0, 1, 3)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)

        self.bit = QSpinBox(self.scrollAreaWidgetContents)
        self.bit.setObjectName(u"bit")
        self.bit.setEnabled(False)
        self.bit.setMinimum(0)
        self.bit.setMaximum(15)
        self.bit.setValue(0)

        self.gridLayout.addWidget(self.bit, 6, 2, 1, 1)

        self.name = QLineEdit(self.scrollAreaWidgetContents)
        self.name.setObjectName(u"name")

        self.gridLayout.addWidget(self.name, 0, 2, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.address_dec = QSpinBox(self.scrollAreaWidgetContents)
        self.address_dec.setObjectName(u"address_dec")

        self.gridLayout.addWidget(self.address_dec, 5, 2, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 7, 0, 1, 3)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)

        self.address = QSpinBox(self.scrollAreaWidgetContents)
        self.address.setObjectName(u"address")
        self.address.setDisplayIntegerBase(16)

        self.gridLayout.addWidget(self.address, 4, 2, 1, 1)

        self.true_text = QLineEdit(self.scrollAreaWidgetContents)
        self.true_text.setObjectName(u"true_text")

        self.gridLayout.addWidget(self.true_text, 9, 2, 1, 1)

        self.false_text = QLineEdit(self.scrollAreaWidgetContents)
        self.false_text.setObjectName(u"false_text")

        self.gridLayout.addWidget(self.false_text, 10, 2, 1, 1)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.reg_DO = QRadioButton(self.widget)
        self.reg_DO.setObjectName(u"reg_DO")
        self.reg_DO.setChecked(True)

        self.verticalLayout_2.addWidget(self.reg_DO)

        self.reg_DI = QRadioButton(self.widget)
        self.reg_DI.setObjectName(u"reg_DI")

        self.verticalLayout_2.addWidget(self.reg_DI)

        self.reg_AO = QRadioButton(self.widget)
        self.reg_AO.setObjectName(u"reg_AO")

        self.verticalLayout_2.addWidget(self.reg_AO)

        self.reg_AI = QRadioButton(self.widget)
        self.reg_AI.setObjectName(u"reg_AI")

        self.verticalLayout_2.addWidget(self.reg_AI)


        self.gridLayout.addWidget(self.widget, 2, 2, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 13, 0, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_4, 11, 0, 1, 3)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_5, 0, 1, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_6, 2, 1, 1, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_7, 4, 1, 3, 1)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_8, 9, 1, 2, 1)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_9, 12, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.button_add = QPushButton(InspectSHMAddBool)
        self.button_add.setObjectName(u"button_add")

        self.verticalLayout.addWidget(self.button_add)


        self.retranslateUi(InspectSHMAddBool)

        QMetaObject.connectSlotsByName(InspectSHMAddBool)
    # setupUi

    def retranslateUi(self, InspectSHMAddBool):
        InspectSHMAddBool.setWindowTitle(QCoreApplication.translate("InspectSHMAddBool", u"Add Bool", None))
        self.endian_little.setText(QCoreApplication.translate("InspectSHMAddBool", u"little", None))
        self.endian_big.setText(QCoreApplication.translate("InspectSHMAddBool", u"big", None))
        self.label_7.setText(QCoreApplication.translate("InspectSHMAddBool", u"True text:", None))
        self.label.setText(QCoreApplication.translate("InspectSHMAddBool", u"Address (hex):", None))
        self.label_2.setText(QCoreApplication.translate("InspectSHMAddBool", u"Address (dec):", None))
        self.label_5.setText(QCoreApplication.translate("InspectSHMAddBool", u"Bit:", None))
        self.name.setText(QCoreApplication.translate("InspectSHMAddBool", u"Bool", None))
        self.label_3.setText(QCoreApplication.translate("InspectSHMAddBool", u"Register:", None))
        self.label_6.setText(QCoreApplication.translate("InspectSHMAddBool", u"False text:", None))
        self.address.setPrefix(QCoreApplication.translate("InspectSHMAddBool", u"0x", None))
        self.true_text.setText(QCoreApplication.translate("InspectSHMAddBool", u"true", None))
        self.false_text.setText(QCoreApplication.translate("InspectSHMAddBool", u"false", None))
        self.reg_DO.setText(QCoreApplication.translate("InspectSHMAddBool", u"DO", None))
        self.reg_DI.setText(QCoreApplication.translate("InspectSHMAddBool", u"DI", None))
        self.reg_AO.setText(QCoreApplication.translate("InspectSHMAddBool", u"AO", None))
        self.reg_AI.setText(QCoreApplication.translate("InspectSHMAddBool", u"AI", None))
        self.label_8.setText(QCoreApplication.translate("InspectSHMAddBool", u"Endianness:", None))
        self.label_4.setText(QCoreApplication.translate("InspectSHMAddBool", u"Name:", None))
        self.button_add.setText(QCoreApplication.translate("InspectSHMAddBool", u"Add", None))
    # retranslateUi

