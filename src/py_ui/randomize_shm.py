# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randomize_shm.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QWidget)

class Ui_RandomizeShm(object):
    def setupUi(self, RandomizeShm):
        if not RandomizeShm.objectName():
            RandomizeShm.setObjectName(u"RandomizeShm")
        RandomizeShm.resize(450, 164)
        RandomizeShm.setMinimumSize(QSize(450, 164))
        RandomizeShm.setMaximumSize(QSize(450, 164))
        self.gridLayout = QGridLayout(RandomizeShm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(RandomizeShm)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.registers = QSpinBox(self.widget)
        self.registers.setObjectName(u"registers")
        self.registers.setMinimum(1)
        self.registers.setMaximum(65536)
        self.registers.setValue(65536)

        self.gridLayout_2.addWidget(self.registers, 0, 5, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 4, 1, 1)

        self.offset = QSpinBox(self.widget)
        self.offset.setObjectName(u"offset")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offset.sizePolicy().hasHeightForWidth())
        self.offset.setSizePolicy(sizePolicy)
        self.offset.setMaximum(65535)

        self.gridLayout_2.addWidget(self.offset, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 6, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)

        self.widget_3 = QWidget(RandomizeShm)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.slider_interval = QSlider(self.widget_3)
        self.slider_interval.setObjectName(u"slider_interval")
        self.slider_interval.setMinimum(100)
        self.slider_interval.setMaximum(60000)
        self.slider_interval.setSingleStep(100)
        self.slider_interval.setPageStep(10000)
        self.slider_interval.setValue(1000)
        self.slider_interval.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.slider_interval, 0, 1, 1, 1)

        self.label_interval = QLabel(self.widget_3)
        self.label_interval.setObjectName(u"label_interval")

        self.gridLayout_4.addWidget(self.label_interval, 0, 3, 1, 1)

        self.spinbox_interval = QSpinBox(self.widget_3)
        self.spinbox_interval.setObjectName(u"spinbox_interval")
        self.spinbox_interval.setMinimum(1000)
        self.spinbox_interval.setMaximum(60000)
        self.spinbox_interval.setSingleStep(100)

        self.gridLayout_4.addWidget(self.spinbox_interval, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 2, 1, 1, 1)

        self.widget_2 = QWidget(RandomizeShm)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.button_start = QPushButton(self.widget_2)
        self.button_start.setObjectName(u"button_start")

        self.gridLayout_3.addWidget(self.button_start, 0, 1, 1, 1)

        self.button_once = QPushButton(self.widget_2)
        self.button_once.setObjectName(u"button_once")

        self.gridLayout_3.addWidget(self.button_once, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)


        self.retranslateUi(RandomizeShm)

        QMetaObject.connectSlotsByName(RandomizeShm)
    # setupUi

    def retranslateUi(self, RandomizeShm):
        RandomizeShm.setWindowTitle(QCoreApplication.translate("RandomizeShm", u"Form", None))
        self.label.setText(QCoreApplication.translate("RandomizeShm", u"offset:", None))
#if QT_CONFIG(tooltip)
        self.registers.setToolTip(QCoreApplication.translate("RandomizeShm", u"number of registers", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.registers.setStatusTip(QCoreApplication.translate("RandomizeShm", u"number of registers to randomize", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("RandomizeShm", u"registers:", None))
#if QT_CONFIG(tooltip)
        self.offset.setToolTip(QCoreApplication.translate("RandomizeShm", u"register offset", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.offset.setStatusTip(QCoreApplication.translate("RandomizeShm", u"register offset (ignore first n registers)", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("RandomizeShm", u"interval:", None))
#if QT_CONFIG(tooltip)
        self.slider_interval.setToolTip(QCoreApplication.translate("RandomizeShm", u"randomization time intervall", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.slider_interval.setStatusTip(QCoreApplication.translate("RandomizeShm", u"intervall", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.slider_interval.setWhatsThis(QCoreApplication.translate("RandomizeShm", u"randomization time intervall", None))
#endif // QT_CONFIG(whatsthis)
        self.label_interval.setText(QCoreApplication.translate("RandomizeShm", u"ms", None))
#if QT_CONFIG(tooltip)
        self.spinbox_interval.setToolTip(QCoreApplication.translate("RandomizeShm", u"randomization time intervall", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.spinbox_interval.setStatusTip(QCoreApplication.translate("RandomizeShm", u"randomization time intervall", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.button_start.setToolTip(QCoreApplication.translate("RandomizeShm", u"start/stop randomization", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_start.setStatusTip(QCoreApplication.translate("RandomizeShm", u"start/stop randomization", None))
#endif // QT_CONFIG(statustip)
        self.button_start.setText(QCoreApplication.translate("RandomizeShm", u"Start", None))
#if QT_CONFIG(tooltip)
        self.button_once.setToolTip(QCoreApplication.translate("RandomizeShm", u"randomize once", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_once.setStatusTip(QCoreApplication.translate("RandomizeShm", u"randomize once", None))
#endif // QT_CONFIG(statustip)
        self.button_once.setText(QCoreApplication.translate("RandomizeShm", u"Once", None))
    # retranslateUi

