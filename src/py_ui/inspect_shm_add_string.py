# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inspect_shm_add_string.ui'
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
    QSizePolicy, QSpinBox, QWidget)

class Ui_InspectSHMAddString(object):
    def setupUi(self, InspectSHMAddString):
        if not InspectSHMAddString.objectName():
            InspectSHMAddString.setObjectName(u"InspectSHMAddString")
        InspectSHMAddString.resize(320, 340)
        InspectSHMAddString.setMinimumSize(QSize(320, 150))
        InspectSHMAddString.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(InspectSHMAddString)
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_add = QPushButton(InspectSHMAddString)
        self.button_add.setObjectName(u"button_add")

        self.gridLayout.addWidget(self.button_add, 3, 0, 1, 2)

        self.line = QFrame(InspectSHMAddString)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)

        self.scrollArea = QScrollArea(InspectSHMAddString)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 298, 275))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.address = QSpinBox(self.scrollAreaWidgetContents)
        self.address.setObjectName(u"address")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.address.sizePolicy().hasHeightForWidth())
        self.address.setSizePolicy(sizePolicy)
        self.address.setDisplayIntegerBase(16)

        self.gridLayout_2.addWidget(self.address, 4, 3, 1, 1)

        self.name = QLineEdit(self.scrollAreaWidgetContents)
        self.name.setObjectName(u"name")

        self.gridLayout_2.addWidget(self.name, 0, 3, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.widget = QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.reg_AO = QRadioButton(self.widget)
        self.reg_AO.setObjectName(u"reg_AO")
        self.reg_AO.setChecked(True)

        self.gridLayout_3.addWidget(self.reg_AO, 0, 0, 1, 1)

        self.reg_AI = QRadioButton(self.widget)
        self.reg_AI.setObjectName(u"reg_AI")

        self.gridLayout_3.addWidget(self.reg_AI, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget, 2, 3, 1, 1)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_2, 4, 0, 1, 1)

        self.length = QSpinBox(self.scrollAreaWidgetContents)
        self.length.setObjectName(u"length")
        self.length.setMinimum(1)

        self.gridLayout_2.addWidget(self.length, 9, 3, 1, 1)

        self.line_7 = QFrame(self.scrollAreaWidgetContents)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_7, 9, 2, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_6, 8, 0, 1, 4)

        self.line_3 = QFrame(self.scrollAreaWidgetContents)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 4)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 4)

        self.label_4 = QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_6 = QLabel(self.scrollAreaWidgetContents)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)

        self.line_8 = QFrame(self.scrollAreaWidgetContents)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_8, 4, 2, 2, 1)

        self.address_dec = QSpinBox(self.scrollAreaWidgetContents)
        self.address_dec.setObjectName(u"address_dec")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.address_dec.sizePolicy().hasHeightForWidth())
        self.address_dec.setSizePolicy(sizePolicy2)
        self.address_dec.setMinimumSize(QSize(80, 0))

        self.gridLayout_2.addWidget(self.address_dec, 5, 3, 1, 1)

        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 9, 0, 1, 1)

        self.line_4 = QFrame(self.scrollAreaWidgetContents)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 2, 2, 1, 1)

        self.line_5 = QFrame(self.scrollAreaWidgetContents)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 0, 2, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 1, 1, 1)


        self.retranslateUi(InspectSHMAddString)

        QMetaObject.connectSlotsByName(InspectSHMAddString)
    # setupUi

    def retranslateUi(self, InspectSHMAddString):
        InspectSHMAddString.setWindowTitle(QCoreApplication.translate("InspectSHMAddString", u"Add String", None))
        self.button_add.setText(QCoreApplication.translate("InspectSHMAddString", u"Add", None))
        self.address.setPrefix(QCoreApplication.translate("InspectSHMAddString", u"0x", None))
        self.name.setText(QCoreApplication.translate("InspectSHMAddString", u"String", None))
        self.label_3.setText(QCoreApplication.translate("InspectSHMAddString", u"Register:", None))
        self.reg_AO.setText(QCoreApplication.translate("InspectSHMAddString", u"AO", None))
        self.reg_AI.setText(QCoreApplication.translate("InspectSHMAddString", u"AI", None))
        self.label_2.setText(QCoreApplication.translate("InspectSHMAddString", u"Address (hex):", None))
        self.label_4.setText(QCoreApplication.translate("InspectSHMAddString", u"Name:", None))
        self.label_6.setText(QCoreApplication.translate("InspectSHMAddString", u"Address (dec):", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("InspectSHMAddString", u"Maximum string length.", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("InspectSHMAddString", u"Max. length:", None))
    # retranslateUi

