# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inspect_shm_add_int.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_InspectSHMAddInt(object):
    def setupUi(self, InspectSHMAddInt):
        if not InspectSHMAddInt.objectName():
            InspectSHMAddInt.setObjectName(u"InspectSHMAddInt")
        InspectSHMAddInt.resize(320, 670)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InspectSHMAddInt.sizePolicy().hasHeightForWidth())
        InspectSHMAddInt.setSizePolicy(sizePolicy)
        InspectSHMAddInt.setMinimumSize(QSize(320, 150))
        InspectSHMAddInt.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(InspectSHMAddInt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_add = QPushButton(InspectSHMAddInt)
        self.button_add.setObjectName(u"button_add")

        self.gridLayout.addWidget(self.button_add, 6, 0, 1, 2)

        self.scrollArea = QScrollArea(InspectSHMAddInt)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 614))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_2 = QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.endian_little = QRadioButton(self.widget_3)
        self.endian_little.setObjectName(u"endian_little")
        self.endian_little.setChecked(True)

        self.verticalLayout_2.addWidget(self.endian_little)

        self.endian_big = QRadioButton(self.widget_3)
        self.endian_big.setObjectName(u"endian_big")

        self.verticalLayout_2.addWidget(self.endian_big)

        self.endian_reversed = QCheckBox(self.widget_3)
        self.endian_reversed.setObjectName(u"endian_reversed")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.endian_reversed.sizePolicy().hasHeightForWidth())
        self.endian_reversed.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.endian_reversed)


        self.gridLayout_3.addWidget(self.widget_3, 12, 2, 1, 1)

        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_10, 10, 1, 1, 1)

        self.name = QLineEdit(self.scrollAreaWidgetContents)
        self.name.setObjectName(u"name")

        self.gridLayout_3.addWidget(self.name, 0, 2, 1, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 4, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 13, 0, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 10, 0, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 2, 1, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 3, 0, 1, 3)

        self.address = QSpinBox(self.scrollAreaWidgetContents)
        self.address.setObjectName(u"address")
        self.address.setDisplayIntegerBase(16)

        self.gridLayout_3.addWidget(self.address, 4, 2, 1, 1)

        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_11, 12, 1, 1, 1)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.size_1 = QRadioButton(self.widget)
        self.size_1.setObjectName(u"size_1")

        self.verticalLayout.addWidget(self.size_1)

        self.size_2 = QRadioButton(self.widget)
        self.size_2.setObjectName(u"size_2")
        self.size_2.setChecked(True)

        self.verticalLayout.addWidget(self.size_2)

        self.size_4 = QRadioButton(self.widget)
        self.size_4.setObjectName(u"size_4")

        self.verticalLayout.addWidget(self.size_4)

        self.size_8 = QRadioButton(self.widget)
        self.size_8.setObjectName(u"size_8")
        self.size_8.setChecked(False)

        self.verticalLayout.addWidget(self.size_8)


        self.gridLayout_3.addWidget(self.widget, 8, 2, 1, 1)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.type_oct = QRadioButton(self.widget_2)
        self.type_oct.setObjectName(u"type_oct")

        self.gridLayout_2.addWidget(self.type_oct, 3, 0, 1, 1)

        self.type_bin = QRadioButton(self.widget_2)
        self.type_bin.setObjectName(u"type_bin")

        self.gridLayout_2.addWidget(self.type_bin, 4, 0, 1, 1)

        self.type_signed = QRadioButton(self.widget_2)
        self.type_signed.setObjectName(u"type_signed")
        self.type_signed.setChecked(True)

        self.gridLayout_2.addWidget(self.type_signed, 0, 0, 1, 1)

        self.type_unsigned = QRadioButton(self.widget_2)
        self.type_unsigned.setObjectName(u"type_unsigned")

        self.gridLayout_2.addWidget(self.type_unsigned, 1, 0, 1, 1)

        self.type_hex = QRadioButton(self.widget_2)
        self.type_hex.setObjectName(u"type_hex")

        self.gridLayout_2.addWidget(self.type_hex, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_2, 10, 2, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 12, 0, 1, 1)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_9, 8, 1, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 8, 0, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 7, 0, 1, 3)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 11, 0, 1, 3)

        self.address_dec = QSpinBox(self.scrollAreaWidgetContents)
        self.address_dec.setObjectName(u"address_dec")
        self.address_dec.setMinimumSize(QSize(80, 0))

        self.gridLayout_3.addWidget(self.address_dec, 5, 2, 1, 1)

        self.widget_4 = QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.reg_AO = QRadioButton(self.widget_4)
        self.reg_AO.setObjectName(u"reg_AO")
        self.reg_AO.setChecked(True)

        self.gridLayout_4.addWidget(self.reg_AO, 0, 0, 1, 1)

        self.reg_AI = QRadioButton(self.widget_4)
        self.reg_AI.setObjectName(u"reg_AI")

        self.gridLayout_4.addWidget(self.reg_AI, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_4, 2, 2, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_4, 9, 0, 1, 3)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 0, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 2)


        self.retranslateUi(InspectSHMAddInt)

        QMetaObject.connectSlotsByName(InspectSHMAddInt)
    # setupUi

    def retranslateUi(self, InspectSHMAddInt):
        InspectSHMAddInt.setWindowTitle(QCoreApplication.translate("InspectSHMAddInt", u"Add Integer", None))
        self.button_add.setText(QCoreApplication.translate("InspectSHMAddInt", u"Add", None))
        self.endian_little.setText(QCoreApplication.translate("InspectSHMAddInt", u"little", None))
        self.endian_big.setText(QCoreApplication.translate("InspectSHMAddInt", u"big", None))
        self.endian_reversed.setText(QCoreApplication.translate("InspectSHMAddInt", u"reversed registers", None))
        self.name.setText(QCoreApplication.translate("InspectSHMAddInt", u"Integer", None))
        self.label_4.setText(QCoreApplication.translate("InspectSHMAddInt", u"Display type:", None))
        self.label_6.setText(QCoreApplication.translate("InspectSHMAddInt", u"Address (dec):", None))
        self.label_2.setText(QCoreApplication.translate("InspectSHMAddInt", u"Address (hex):", None))
        self.address.setPrefix(QCoreApplication.translate("InspectSHMAddInt", u"0x", None))
        self.size_1.setText(QCoreApplication.translate("InspectSHMAddInt", u"1 Byte", None))
        self.size_2.setText(QCoreApplication.translate("InspectSHMAddInt", u"2 Byte", None))
        self.size_4.setText(QCoreApplication.translate("InspectSHMAddInt", u"4 Byte", None))
        self.size_8.setText(QCoreApplication.translate("InspectSHMAddInt", u"8 Byte", None))
        self.type_oct.setText(QCoreApplication.translate("InspectSHMAddInt", u"oct", None))
        self.type_bin.setText(QCoreApplication.translate("InspectSHMAddInt", u"bin", None))
        self.type_signed.setText(QCoreApplication.translate("InspectSHMAddInt", u"signed (dec)", None))
        self.type_unsigned.setText(QCoreApplication.translate("InspectSHMAddInt", u"unsigend (dec)", None))
        self.type_hex.setText(QCoreApplication.translate("InspectSHMAddInt", u"hex", None))
        self.label_5.setText(QCoreApplication.translate("InspectSHMAddInt", u"Endianness:", None))
        self.label_7.setText(QCoreApplication.translate("InspectSHMAddInt", u"Name:", None))
        self.label_3.setText(QCoreApplication.translate("InspectSHMAddInt", u"Register:", None))
        self.label.setText(QCoreApplication.translate("InspectSHMAddInt", u"Size:", None))
        self.reg_AO.setText(QCoreApplication.translate("InspectSHMAddInt", u"AO", None))
        self.reg_AI.setText(QCoreApplication.translate("InspectSHMAddInt", u"AI", None))
    # retranslateUi

