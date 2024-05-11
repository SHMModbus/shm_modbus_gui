# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_values_add_float.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_InspectSHMAddFloat(object):
    def setupUi(self, InspectSHMAddFloat):
        if not InspectSHMAddFloat.objectName():
            InspectSHMAddFloat.setObjectName(u"InspectSHMAddFloat")
        InspectSHMAddFloat.resize(320, 454)
        InspectSHMAddFloat.setMinimumSize(QSize(300, 150))
        InspectSHMAddFloat.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(InspectSHMAddFloat)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea = QScrollArea(InspectSHMAddFloat)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 304, 398))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 7, 0, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 9, 0, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 8, 0, 1, 3)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_3, 6, 0, 1, 3)

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


        self.gridLayout_3.addWidget(self.widget_3, 9, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 10, 0, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 0, 1, 1, 1)

        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.VLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_11, 9, 1, 1, 1)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 3)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 4, 1, 2, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 2, 1, 1, 1)

        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_9, 7, 1, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_2, 4, 0, 1, 1)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_3.addWidget(self.line_2, 3, 0, 1, 3)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.size_4 = QRadioButton(self.widget)
        self.size_4.setObjectName(u"size_4")
        self.size_4.setChecked(True)

        self.verticalLayout.addWidget(self.size_4)

        self.size_8 = QRadioButton(self.widget)
        self.size_8.setObjectName(u"size_8")
        self.size_8.setChecked(False)

        self.verticalLayout.addWidget(self.size_8)


        self.gridLayout_3.addWidget(self.widget, 7, 2, 1, 1)

        self.address = QSpinBox(self.scrollAreaWidgetContents)
        self.address.setObjectName(u"address")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.address.sizePolicy().hasHeightForWidth())
        self.address.setSizePolicy(sizePolicy3)
        self.address.setDisplayIntegerBase(16)

        self.gridLayout_3.addWidget(self.address, 4, 2, 1, 1)

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

        self.name = QLineEdit(self.scrollAreaWidgetContents)
        self.name.setObjectName(u"name")

        self.gridLayout_3.addWidget(self.name, 0, 2, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 3)

        self.button_add = QPushButton(InspectSHMAddFloat)
        self.button_add.setObjectName(u"button_add")

        self.gridLayout.addWidget(self.button_add, 4, 0, 1, 3)


        self.retranslateUi(InspectSHMAddFloat)

        QMetaObject.connectSlotsByName(InspectSHMAddFloat)
    # setupUi

    def retranslateUi(self, InspectSHMAddFloat):
        InspectSHMAddFloat.setWindowTitle(QCoreApplication.translate("InspectSHMAddFloat", u"Add Float", None))
        self.label_6.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Address (dec):", None))
        self.label.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Size:", None))
        self.label_3.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Name:", None))
        self.label_5.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Endianness:", None))
        self.endian_little.setText(QCoreApplication.translate("InspectSHMAddFloat", u"little", None))
        self.endian_big.setText(QCoreApplication.translate("InspectSHMAddFloat", u"big", None))
        self.endian_reversed.setText(QCoreApplication.translate("InspectSHMAddFloat", u"reversed registers", None))
        self.label_2.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Address (hex):", None))
        self.size_4.setText(QCoreApplication.translate("InspectSHMAddFloat", u"4 Byte", None))
        self.size_8.setText(QCoreApplication.translate("InspectSHMAddFloat", u"8 Byte", None))
        self.address.setPrefix(QCoreApplication.translate("InspectSHMAddFloat", u"0x", None))
        self.reg_AO.setText(QCoreApplication.translate("InspectSHMAddFloat", u"AO", None))
        self.reg_AI.setText(QCoreApplication.translate("InspectSHMAddFloat", u"AI", None))
        self.name.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Float", None))
        self.label_7.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Register:", None))
        self.button_add.setText(QCoreApplication.translate("InspectSHMAddFloat", u"Add", None))
    # retranslateUi

