# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inspect_shm.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QFrame,
    QGridLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_InspectSHM(object):
    def setupUi(self, InspectSHM):
        if not InspectSHM.objectName():
            InspectSHM.setObjectName(u"InspectSHM")
        InspectSHM.resize(950, 600)
        self.actionSave_config = QAction(InspectSHM)
        self.actionSave_config.setObjectName(u"actionSave_config")
        self.actionLoad_config = QAction(InspectSHM)
        self.actionLoad_config.setObjectName(u"actionLoad_config")
        self.actionExport_values = QAction(InspectSHM)
        self.actionExport_values.setObjectName(u"actionExport_values")
        self.centralwidget = QWidget(InspectSHM)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_add_char_array = QPushButton(self.widget)
        self.button_add_char_array.setObjectName(u"button_add_char_array")

        self.gridLayout_2.addWidget(self.button_add_char_array, 1, 3, 1, 1)

        self.button_add_int = QPushButton(self.widget)
        self.button_add_int.setObjectName(u"button_add_int")

        self.gridLayout_2.addWidget(self.button_add_int, 1, 1, 1, 1)

        self.button_add_float = QPushButton(self.widget)
        self.button_add_float.setObjectName(u"button_add_float")

        self.gridLayout_2.addWidget(self.button_add_float, 1, 2, 1, 1)

        self.button_add_bool = QPushButton(self.widget)
        self.button_add_bool.setObjectName(u"button_add_bool")

        self.gridLayout_2.addWidget(self.button_add_bool, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 934, 409))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.data_table = QTableWidget(self.scrollAreaWidgetContents)
        if (self.data_table.columnCount() < 9):
            self.data_table.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.data_table.setObjectName(u"data_table")
        self.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.data_table.setAlternatingRowColors(True)
        self.data_table.setSortingEnabled(True)

        self.gridLayout_3.addWidget(self.data_table, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.auto_refresh = QCheckBox(self.widget_2)
        self.auto_refresh.setObjectName(u"auto_refresh")

        self.gridLayout_4.addWidget(self.auto_refresh, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 0, 1, 1, 1)

        self.slider_interval = QSlider(self.widget_2)
        self.slider_interval.setObjectName(u"slider_interval")
        self.slider_interval.setMinimum(100)
        self.slider_interval.setMaximum(10000)
        self.slider_interval.setSingleStep(100)
        self.slider_interval.setPageStep(1000)
        self.slider_interval.setValue(2000)
        self.slider_interval.setOrientation(Qt.Horizontal)

        self.gridLayout_4.addWidget(self.slider_interval, 0, 3, 1, 1)

        self.spinbox_interval = QSpinBox(self.widget_2)
        self.spinbox_interval.setObjectName(u"spinbox_interval")
        self.spinbox_interval.setMinimum(100)
        self.spinbox_interval.setMaximum(10000)
        self.spinbox_interval.setSingleStep(100)
        self.spinbox_interval.setValue(2000)

        self.gridLayout_4.addWidget(self.spinbox_interval, 0, 4, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 2, 1, 1)

        self.button_refresh = QPushButton(self.widget_2)
        self.button_refresh.setObjectName(u"button_refresh")

        self.gridLayout_4.addWidget(self.button_refresh, 0, 7, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 0, 6, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 5, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 5, 0, 1, 1)

        InspectSHM.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(InspectSHM)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 950, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        InspectSHM.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(InspectSHM)
        self.statusbar.setObjectName(u"statusbar")
        InspectSHM.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave_config)
        self.menuFile.addAction(self.actionLoad_config)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExport_values)

        self.retranslateUi(InspectSHM)

        QMetaObject.connectSlotsByName(InspectSHM)
    # setupUi

    def retranslateUi(self, InspectSHM):
        InspectSHM.setWindowTitle(QCoreApplication.translate("InspectSHM", u"Inspect Values", None))
        self.actionSave_config.setText(QCoreApplication.translate("InspectSHM", u"Save config", None))
        self.actionLoad_config.setText(QCoreApplication.translate("InspectSHM", u"Load config", None))
        self.actionExport_values.setText(QCoreApplication.translate("InspectSHM", u"Export values", None))
        self.button_add_char_array.setText(QCoreApplication.translate("InspectSHM", u"add string", None))
        self.button_add_int.setText(QCoreApplication.translate("InspectSHM", u"add int", None))
        self.button_add_float.setText(QCoreApplication.translate("InspectSHM", u"add float", None))
        self.button_add_bool.setText(QCoreApplication.translate("InspectSHM", u"add bool", None))
        ___qtablewidgetitem = self.data_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InspectSHM", u"Name", None));
        ___qtablewidgetitem1 = self.data_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InspectSHM", u"Register", None));
        ___qtablewidgetitem2 = self.data_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InspectSHM", u"Address", None));
        ___qtablewidgetitem3 = self.data_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InspectSHM", u"Data Type", None));
        ___qtablewidgetitem4 = self.data_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InspectSHM", u"Size", None));
        ___qtablewidgetitem5 = self.data_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("InspectSHM", u"Endianness", None));
        ___qtablewidgetitem6 = self.data_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("InspectSHM", u"Value", None));
        ___qtablewidgetitem7 = self.data_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("InspectSHM", u"Time", None));
        self.auto_refresh.setText(QCoreApplication.translate("InspectSHM", u"Auto refresh", None))
        self.label_5.setText(QCoreApplication.translate("InspectSHM", u"auto refresh interval:", None))
        self.button_refresh.setText(QCoreApplication.translate("InspectSHM", u"refresh", None))
        self.label_6.setText(QCoreApplication.translate("InspectSHM", u"ms", None))
        self.menuFile.setTitle(QCoreApplication.translate("InspectSHM", u"File", None))
    # retranslateUi

