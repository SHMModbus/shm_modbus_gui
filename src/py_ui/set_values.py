# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set_values.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_SetValues(object):
    def setupUi(self, SetValues):
        if not SetValues.objectName():
            SetValues.setObjectName(u"SetValues")
        SetValues.resize(800, 600)
        self.actionload_config = QAction(SetValues)
        self.actionload_config.setObjectName(u"actionload_config")
        self.actionsave_config = QAction(SetValues)
        self.actionsave_config.setObjectName(u"actionsave_config")
        self.centralwidget = QWidget(SetValues)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.data_table = QTableWidget(self.centralwidget)
        if (self.data_table.columnCount() < 11):
            self.data_table.setColumnCount(11)
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
        __qtablewidgetitem9 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.data_table.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.data_table.setObjectName(u"data_table")

        self.gridLayout.addWidget(self.data_table, 2, 0, 1, 1)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_add_float = QPushButton(self.widget)
        self.button_add_float.setObjectName(u"button_add_float")

        self.gridLayout_2.addWidget(self.button_add_float, 0, 2, 1, 1)

        self.button_add_bool = QPushButton(self.widget)
        self.button_add_bool.setObjectName(u"button_add_bool")

        self.gridLayout_2.addWidget(self.button_add_bool, 0, 0, 1, 1)

        self.button_add_int = QPushButton(self.widget)
        self.button_add_int.setObjectName(u"button_add_int")

        self.gridLayout_2.addWidget(self.button_add_int, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.button_apply_all = QPushButton(self.widget_2)
        self.button_apply_all.setObjectName(u"button_apply_all")

        self.gridLayout_3.addWidget(self.button_apply_all, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_2, 4, 0, 1, 1)

        SetValues.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SetValues)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        SetValues.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SetValues)
        self.statusbar.setObjectName(u"statusbar")
        SetValues.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionload_config)
        self.menuFile.addAction(self.actionsave_config)

        self.retranslateUi(SetValues)

        QMetaObject.connectSlotsByName(SetValues)
    # setupUi

    def retranslateUi(self, SetValues):
        SetValues.setWindowTitle(QCoreApplication.translate("SetValues", u"Set Values", None))
        self.actionload_config.setText(QCoreApplication.translate("SetValues", u"load config", None))
        self.actionsave_config.setText(QCoreApplication.translate("SetValues", u"save config", None))
        ___qtablewidgetitem = self.data_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SetValues", u"Name", None));
        ___qtablewidgetitem1 = self.data_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SetValues", u"Register", None));
        ___qtablewidgetitem2 = self.data_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SetValues", u"Address", None));
        ___qtablewidgetitem3 = self.data_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SetValues", u"Data Type", None));
        ___qtablewidgetitem4 = self.data_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("SetValues", u"Size", None));
        ___qtablewidgetitem5 = self.data_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("SetValues", u"Endianness", None));
        ___qtablewidgetitem6 = self.data_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("SetValues", u"Value", None));
        ___qtablewidgetitem7 = self.data_table.horizontalHeaderItem(8)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("SetValues", u"Time", None));
        ___qtablewidgetitem8 = self.data_table.horizontalHeaderItem(9)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("SetValues", u"New Column", None));
        self.button_add_float.setText(QCoreApplication.translate("SetValues", u"add float", None))
        self.button_add_bool.setText(QCoreApplication.translate("SetValues", u"add bool", None))
        self.button_add_int.setText(QCoreApplication.translate("SetValues", u"add int", None))
        self.button_apply_all.setText(QCoreApplication.translate("SetValues", u"apply all", None))
        self.menuFile.setTitle(QCoreApplication.translate("SetValues", u"File", None))
    # retranslateUi

