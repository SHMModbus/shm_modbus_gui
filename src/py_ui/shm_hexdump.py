# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shm_hexdump.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QTextBrowser, QWidget)

class Ui_ShmHexdump(object):
    def setupUi(self, ShmHexdump):
        if not ShmHexdump.objectName():
            ShmHexdump.setObjectName(u"ShmHexdump")
        ShmHexdump.resize(800, 600)
        ShmHexdump.setMinimumSize(QSize(600, 300))
        self.actionSave = QAction(ShmHexdump)
        self.actionSave.setObjectName(u"actionSave")
        self.centralwidget = QWidget(ShmHexdump)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hexdump_text = QTextBrowser(self.centralwidget)
        self.hexdump_text.setObjectName(u"hexdump_text")
        font = QFont()
        font.setFamilies([u"Noto Sans Mono Medium"])
        self.hexdump_text.setFont(font)

        self.gridLayout.addWidget(self.hexdump_text, 2, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.registers = QSpinBox(self.widget)
        self.registers.setObjectName(u"registers")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registers.sizePolicy().hasHeightForWidth())
        self.registers.setSizePolicy(sizePolicy)
        self.registers.setMinimumSize(QSize(80, 0))
        self.registers.setMinimum(1)

        self.gridLayout_2.addWidget(self.registers, 1, 6, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.checkbox_autorefresh = QCheckBox(self.widget)
        self.checkbox_autorefresh.setObjectName(u"checkbox_autorefresh")

        self.gridLayout_2.addWidget(self.checkbox_autorefresh, 1, 0, 1, 1)

        self.button_refresh = QPushButton(self.widget)
        self.button_refresh.setObjectName(u"button_refresh")

        self.gridLayout_2.addWidget(self.button_refresh, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 6, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 2, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.slider_interval = QSlider(self.widget_2)
        self.slider_interval.setObjectName(u"slider_interval")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.slider_interval.sizePolicy().hasHeightForWidth())
        self.slider_interval.setSizePolicy(sizePolicy2)
        self.slider_interval.setMinimum(100)
        self.slider_interval.setMaximum(10000)
        self.slider_interval.setSingleStep(100)
        self.slider_interval.setPageStep(1000)
        self.slider_interval.setValue(2000)
        self.slider_interval.setOrientation(Qt.Horizontal)

        self.gridLayout_3.addWidget(self.slider_interval, 0, 0, 1, 1)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 2, 1, 1)

        self.spinbox_interval = QSpinBox(self.widget_2)
        self.spinbox_interval.setObjectName(u"spinbox_interval")

        self.gridLayout_3.addWidget(self.spinbox_interval, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 7, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 4, 1, 1)

        self.offset = QSpinBox(self.widget)
        self.offset.setObjectName(u"offset")
        sizePolicy.setHeightForWidth(self.offset.sizePolicy().hasHeightForWidth())
        self.offset.setSizePolicy(sizePolicy)
        self.offset.setMinimumSize(QSize(80, 0))

        self.gridLayout_2.addWidget(self.offset, 1, 4, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 0, 3, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        ShmHexdump.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ShmHexdump)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        ShmHexdump.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ShmHexdump)
        self.statusbar.setObjectName(u"statusbar")
        ShmHexdump.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave)

        self.retranslateUi(ShmHexdump)

        QMetaObject.connectSlotsByName(ShmHexdump)
    # setupUi

    def retranslateUi(self, ShmHexdump):
        ShmHexdump.setWindowTitle(QCoreApplication.translate("ShmHexdump", u"MainWindow", None))
        self.actionSave.setText(QCoreApplication.translate("ShmHexdump", u"Save", None))
#if QT_CONFIG(tooltip)
        self.registers.setToolTip(QCoreApplication.translate("ShmHexdump", u"number of registers to hexdump", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.registers.setStatusTip(QCoreApplication.translate("ShmHexdump", u"number of registers to hexdump", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.checkbox_autorefresh.setToolTip(QCoreApplication.translate("ShmHexdump", u"auto refresh", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.checkbox_autorefresh.setStatusTip(QCoreApplication.translate("ShmHexdump", u"auto refresh", None))
#endif // QT_CONFIG(statustip)
        self.checkbox_autorefresh.setText(QCoreApplication.translate("ShmHexdump", u"auto refresh", None))
#if QT_CONFIG(tooltip)
        self.button_refresh.setToolTip(QCoreApplication.translate("ShmHexdump", u"refresh hexdump", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.button_refresh.setStatusTip(QCoreApplication.translate("ShmHexdump", u"refresh hexdump", None))
#endif // QT_CONFIG(statustip)
        self.button_refresh.setText(QCoreApplication.translate("ShmHexdump", u"refresh", None))
        self.label_2.setText(QCoreApplication.translate("ShmHexdump", u"registers", None))
        self.label.setText(QCoreApplication.translate("ShmHexdump", u"auto refresh interval", None))
#if QT_CONFIG(tooltip)
        self.slider_interval.setToolTip(QCoreApplication.translate("ShmHexdump", u"auto refresh interval", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.slider_interval.setStatusTip(QCoreApplication.translate("ShmHexdump", u"auto refresh interval", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("ShmHexdump", u"ms", None))
#if QT_CONFIG(tooltip)
        self.spinbox_interval.setToolTip(QCoreApplication.translate("ShmHexdump", u"auto refresh interval", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.spinbox_interval.setStatusTip(QCoreApplication.translate("ShmHexdump", u"auto refresh interval", None))
#endif // QT_CONFIG(statustip)
        self.label_3.setText(QCoreApplication.translate("ShmHexdump", u"offset", None))
#if QT_CONFIG(tooltip)
        self.offset.setToolTip(QCoreApplication.translate("ShmHexdump", u"register offset (ignore first n registers)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.offset.setStatusTip(QCoreApplication.translate("ShmHexdump", u"register offset (ignore first n registers)", None))
#endif // QT_CONFIG(statustip)
        self.menuFile.setTitle(QCoreApplication.translate("ShmHexdump", u"File", None))
    # retranslateUi

