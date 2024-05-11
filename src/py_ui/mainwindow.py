# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 300))
        self.actionVersion = QAction(MainWindow)
        self.actionVersion.setObjectName(u"actionVersion")
        self.actionsave_modbus_client_config = QAction(MainWindow)
        self.actionsave_modbus_client_config.setObjectName(u"actionsave_modbus_client_config")
        self.actionsave_modbus_rtu_client_config = QAction(MainWindow)
        self.actionsave_modbus_rtu_client_config.setObjectName(u"actionsave_modbus_rtu_client_config")
        self.actionopen_modbus_client_config = QAction(MainWindow)
        self.actionopen_modbus_client_config.setObjectName(u"actionopen_modbus_client_config")
        self.actionopen_modbus_rtu_client_config = QAction(MainWindow)
        self.actionopen_modbus_rtu_client_config.setObjectName(u"actionopen_modbus_rtu_client_config")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget_tools = QTabWidget(self.centralwidget)
        self.tabWidget_tools.setObjectName(u"tabWidget_tools")
        self.tabWidget_tools.setEnabled(True)
        self.tab_modbus_clients = QWidget()
        self.tab_modbus_clients.setObjectName(u"tab_modbus_clients")
        self.gridLayout_2 = QGridLayout(self.tab_modbus_clients)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget_modbus_cl = QTabWidget(self.tab_modbus_clients)
        self.tabWidget_modbus_cl.setObjectName(u"tabWidget_modbus_cl")
        self.tab_modbus_setings = QWidget()
        self.tab_modbus_setings.setObjectName(u"tab_modbus_setings")
        self.gridLayout_33 = QGridLayout(self.tab_modbus_setings)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.scrollArea_3 = QScrollArea(self.tab_modbus_setings)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 727, 573))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.widget_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.mb_do = QSpinBox(self.widget_2)
        self.mb_do.setObjectName(u"mb_do")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mb_do.sizePolicy().hasHeightForWidth())
        self.mb_do.setSizePolicy(sizePolicy1)
        self.mb_do.setMinimum(1)
        self.mb_do.setMaximum(65536)
        self.mb_do.setValue(65536)

        self.gridLayout_6.addWidget(self.mb_do, 0, 1, 1, 1)

        self.mb_do_default = QPushButton(self.widget_2)
        self.mb_do_default.setObjectName(u"mb_do_default")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mb_do_default.sizePolicy().hasHeightForWidth())
        self.mb_do_default.setSizePolicy(sizePolicy2)
        self.mb_do_default.setMinimumSize(QSize(0, 0))
        self.mb_do_default.setMaximumSize(QSize(16777215, 16777215))
        self.mb_do_default.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.mb_do_default, 0, 2, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.mb_di = QSpinBox(self.widget_2)
        self.mb_di.setObjectName(u"mb_di")
        sizePolicy1.setHeightForWidth(self.mb_di.sizePolicy().hasHeightForWidth())
        self.mb_di.setSizePolicy(sizePolicy1)
        self.mb_di.setMinimum(1)
        self.mb_di.setMaximum(65536)
        self.mb_di.setValue(65536)

        self.gridLayout_6.addWidget(self.mb_di, 1, 1, 1, 1)

        self.mb_ai = QSpinBox(self.widget_2)
        self.mb_ai.setObjectName(u"mb_ai")
        sizePolicy1.setHeightForWidth(self.mb_ai.sizePolicy().hasHeightForWidth())
        self.mb_ai.setSizePolicy(sizePolicy1)
        self.mb_ai.setMinimum(1)
        self.mb_ai.setMaximum(65536)
        self.mb_ai.setValue(65536)

        self.gridLayout_6.addWidget(self.mb_ai, 1, 5, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.mb_ao = QSpinBox(self.widget_2)
        self.mb_ao.setObjectName(u"mb_ao")
        sizePolicy1.setHeightForWidth(self.mb_ao.sizePolicy().hasHeightForWidth())
        self.mb_ao.setSizePolicy(sizePolicy1)
        self.mb_ao.setMinimum(1)
        self.mb_ao.setMaximum(65536)
        self.mb_ao.setValue(65536)

        self.gridLayout_6.addWidget(self.mb_ao, 0, 5, 1, 1)

        self.mb_ai_default = QPushButton(self.widget_2)
        self.mb_ai_default.setObjectName(u"mb_ai_default")
        self.mb_ai_default.setMinimumSize(QSize(0, 0))
        self.mb_ai_default.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.mb_ai_default, 1, 6, 1, 1)

        self.mb_ao_default = QPushButton(self.widget_2)
        self.mb_ao_default.setObjectName(u"mb_ao_default")
        self.mb_ao_default.setMinimumSize(QSize(0, 0))
        self.mb_ao_default.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.mb_ao_default, 0, 6, 1, 1)

        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_7, 0, 4, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_8, 1, 4, 1, 1)

        self.mb_di_default = QPushButton(self.widget_2)
        self.mb_di_default.setObjectName(u"mb_di_default")
        self.mb_di_default.setMinimumSize(QSize(0, 0))
        self.mb_di_default.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.mb_di_default, 1, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_16, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)

        self.line_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.label_30 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setToolTipDuration(-1)
        self.label_30.setFrameShadow(QFrame.Plain)
        self.label_30.setLineWidth(1)

        self.verticalLayout.addWidget(self.label_30)

        self.widget_12 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_18 = QGridLayout(self.widget_12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.mb_shm_flags_default = QPushButton(self.widget_12)
        self.mb_shm_flags_default.setObjectName(u"mb_shm_flags_default")

        self.gridLayout_18.addWidget(self.mb_shm_flags_default, 0, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.mb_force = QCheckBox(self.widget_12)
        self.mb_force.setObjectName(u"mb_force")
        sizePolicy1.setHeightForWidth(self.mb_force.sizePolicy().hasHeightForWidth())
        self.mb_force.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.mb_force, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_19 = QGridLayout(self.widget_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.mb_shm_name = QLineEdit(self.widget_13)
        self.mb_shm_name.setObjectName(u"mb_shm_name")

        self.gridLayout_19.addWidget(self.mb_shm_name, 0, 1, 1, 1)

        self.mb_shm_name_default = QPushButton(self.widget_13)
        self.mb_shm_name_default.setObjectName(u"mb_shm_name_default")

        self.gridLayout_19.addWidget(self.mb_shm_name_default, 0, 2, 1, 1)

        self.label_31 = QLabel(self.widget_13)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_19.addWidget(self.label_31, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_13)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.label_15 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.verticalLayout.addWidget(self.label_15)

        self.widget_8 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.gridLayout_12 = QGridLayout(self.widget_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.mb_monitor = QCheckBox(self.widget_8)
        self.mb_monitor.setObjectName(u"mb_monitor")
        sizePolicy2.setHeightForWidth(self.mb_monitor.sizePolicy().hasHeightForWidth())
        self.mb_monitor.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(9)
        self.mb_monitor.setFont(font1)

        self.gridLayout_12.addWidget(self.mb_monitor, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.mb_enable_byte_timeout = QCheckBox(self.widget_8)
        self.mb_enable_byte_timeout.setObjectName(u"mb_enable_byte_timeout")

        self.gridLayout_12.addWidget(self.mb_enable_byte_timeout, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.mb_enable_response_timeout = QCheckBox(self.widget_8)
        self.mb_enable_response_timeout.setObjectName(u"mb_enable_response_timeout")
        sizePolicy1.setHeightForWidth(self.mb_enable_response_timeout.sizePolicy().hasHeightForWidth())
        self.mb_enable_response_timeout.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.mb_enable_response_timeout, 0, 5, 1, 1)

        self.mb_mb_flags_default = QPushButton(self.widget_8)
        self.mb_mb_flags_default.setObjectName(u"mb_mb_flags_default")

        self.gridLayout_12.addWidget(self.mb_mb_flags_default, 0, 6, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_13 = QGridLayout(self.widget_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.mb_byte_timeout = QDoubleSpinBox(self.widget_9)
        self.mb_byte_timeout.setObjectName(u"mb_byte_timeout")
        self.mb_byte_timeout.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.mb_byte_timeout.sizePolicy().hasHeightForWidth())
        self.mb_byte_timeout.setSizePolicy(sizePolicy1)
        self.mb_byte_timeout.setMaximum(86400.000000000000000)

        self.gridLayout_13.addWidget(self.mb_byte_timeout, 0, 1, 1, 1)

        self.label_17 = QLabel(self.widget_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_17, 0, 3, 1, 1)

        self.mb_response_timeout = QDoubleSpinBox(self.widget_9)
        self.mb_response_timeout.setObjectName(u"mb_response_timeout")
        self.mb_response_timeout.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.mb_response_timeout.sizePolicy().hasHeightForWidth())
        self.mb_response_timeout.setSizePolicy(sizePolicy1)
        self.mb_response_timeout.setMinimum(0.000000000000000)
        self.mb_response_timeout.setMaximum(86400.000000000000000)
        self.mb_response_timeout.setValue(0.000000000000000)

        self.gridLayout_13.addWidget(self.mb_response_timeout, 0, 4, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_15, 0, 5, 1, 1)

        self.label_16 = QLabel(self.widget_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget_9)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.label_13 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.verticalLayout.addWidget(self.label_13)

        self.widget_5 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_9 = QGridLayout(self.widget_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.mb_sem_force = QCheckBox(self.widget_5)
        self.mb_sem_force.setObjectName(u"mb_sem_force")
        sizePolicy1.setHeightForWidth(self.mb_sem_force.sizePolicy().hasHeightForWidth())
        self.mb_sem_force.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.mb_sem_force, 0, 3, 1, 1)

        self.mb_sem_enable = QCheckBox(self.widget_5)
        self.mb_sem_enable.setObjectName(u"mb_sem_enable")
        self.mb_sem_enable.setChecked(True)

        self.gridLayout_9.addWidget(self.mb_sem_enable, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.mb_sem_defaults = QPushButton(self.widget_5)
        self.mb_sem_defaults.setObjectName(u"mb_sem_defaults")

        self.gridLayout_9.addWidget(self.mb_sem_defaults, 0, 4, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_10 = QGridLayout(self.widget_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 1)

        self.mb_sem_name = QLineEdit(self.widget_6)
        self.mb_sem_name.setObjectName(u"mb_sem_name")

        self.gridLayout_10.addWidget(self.mb_sem_name, 0, 1, 1, 1)

        self.mb_sem_name_default = QPushButton(self.widget_6)
        self.mb_sem_name_default.setObjectName(u"mb_sem_name_default")

        self.gridLayout_10.addWidget(self.mb_sem_name_default, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.widget_6)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_33.addWidget(self.scrollArea_3, 0, 0, 1, 1)

        self.widget_11 = QWidget(self.tab_modbus_setings)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_17 = QGridLayout(self.widget_11)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.mb_defaults = QPushButton(self.widget_11)
        self.mb_defaults.setObjectName(u"mb_defaults")

        self.gridLayout_17.addWidget(self.mb_defaults, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_33.addWidget(self.widget_11, 1, 0, 1, 1)

        self.tabWidget_modbus_cl.addTab(self.tab_modbus_setings, "")
        self.tab_mbtcp = QWidget()
        self.tab_mbtcp.setObjectName(u"tab_mbtcp")
        self.gridLayout_3 = QGridLayout(self.tab_mbtcp)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.widget_7 = QWidget(self.tab_mbtcp)
        self.widget_7.setObjectName(u"widget_7")
        self.gridLayout_11 = QGridLayout(self.widget_7)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.mbtcp_start = QPushButton(self.widget_7)
        self.mbtcp_start.setObjectName(u"mbtcp_start")
        sizePolicy1.setHeightForWidth(self.mbtcp_start.sizePolicy().hasHeightForWidth())
        self.mbtcp_start.setSizePolicy(sizePolicy1)

        self.gridLayout_11.addWidget(self.mbtcp_start, 0, 1, 1, 1)

        self.mbtcp_defaults = QPushButton(self.widget_7)
        self.mbtcp_defaults.setObjectName(u"mbtcp_defaults")

        self.gridLayout_11.addWidget(self.mbtcp_defaults, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.widget_7, 13, 3, 1, 1)

        self.mbtcp_settings = QScrollArea(self.tab_mbtcp)
        self.mbtcp_settings.setObjectName(u"mbtcp_settings")
        self.mbtcp_settings.setWidgetResizable(True)
        self.mbtcp_settings_content = QWidget()
        self.mbtcp_settings_content.setObjectName(u"mbtcp_settings_content")
        self.mbtcp_settings_content.setGeometry(QRect(0, 0, 373, 437))
        self.gridLayout_4 = QGridLayout(self.mbtcp_settings_content)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.mbtcp_settings_content)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_4.addWidget(self.label_9, 3, 0, 1, 1)

        self.widget = QWidget(self.mbtcp_settings_content)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mbtcp_port = QSpinBox(self.widget)
        self.mbtcp_port.setObjectName(u"mbtcp_port")
        self.mbtcp_port.setMaximum(65535)
        self.mbtcp_port.setValue(502)

        self.gridLayout_5.addWidget(self.mbtcp_port, 2, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.mbtcp_host_default = QPushButton(self.widget)
        self.mbtcp_host_default.setObjectName(u"mbtcp_host_default")

        self.gridLayout_5.addWidget(self.mbtcp_host_default, 1, 2, 1, 1)

        self.mbtcp_nw_flags_default = QPushButton(self.widget)
        self.mbtcp_nw_flags_default.setObjectName(u"mbtcp_nw_flags_default")

        self.gridLayout_5.addWidget(self.mbtcp_nw_flags_default, 6, 2, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_38 = QLabel(self.widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_38, 5, 0, 1, 1)

        self.mbtcp_tcp_timeout_default = QPushButton(self.widget)
        self.mbtcp_tcp_timeout_default.setObjectName(u"mbtcp_tcp_timeout_default")

        self.gridLayout_5.addWidget(self.mbtcp_tcp_timeout_default, 3, 2, 1, 1)

        self.mbtcp_tcp_timeout = QSpinBox(self.widget)
        self.mbtcp_tcp_timeout.setObjectName(u"mbtcp_tcp_timeout")
        self.mbtcp_tcp_timeout.setMinimum(1)
        self.mbtcp_tcp_timeout.setMaximum(86400)
        self.mbtcp_tcp_timeout.setValue(5)

        self.gridLayout_5.addWidget(self.mbtcp_tcp_timeout, 3, 1, 1, 1)

        self.mbtcp_host = QLineEdit(self.widget)
        self.mbtcp_host.setObjectName(u"mbtcp_host")
        self.mbtcp_host.setCursor(QCursor(Qt.IBeamCursor))

        self.gridLayout_5.addWidget(self.mbtcp_host, 1, 1, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)

        self.mbtcp_port_default = QPushButton(self.widget)
        self.mbtcp_port_default.setObjectName(u"mbtcp_port_default")

        self.gridLayout_5.addWidget(self.mbtcp_port_default, 2, 2, 1, 1)

        self.mbtcp_connections_default = QPushButton(self.widget)
        self.mbtcp_connections_default.setObjectName(u"mbtcp_connections_default")

        self.gridLayout_5.addWidget(self.mbtcp_connections_default, 5, 2, 1, 1)

        self.mbtcp_connections = QSpinBox(self.widget)
        self.mbtcp_connections.setObjectName(u"mbtcp_connections")
        self.mbtcp_connections.setMinimum(1)
        self.mbtcp_connections.setMaximum(65536)

        self.gridLayout_5.addWidget(self.mbtcp_connections, 5, 1, 1, 1)

        self.mbtcp_reconnect = QCheckBox(self.widget)
        self.mbtcp_reconnect.setObjectName(u"mbtcp_reconnect")
        self.mbtcp_reconnect.setChecked(True)

        self.gridLayout_5.addWidget(self.mbtcp_reconnect, 6, 1, 1, 1)

        self.mbtcp_sytstem_tcp_timeout = QCheckBox(self.widget)
        self.mbtcp_sytstem_tcp_timeout.setObjectName(u"mbtcp_sytstem_tcp_timeout")

        self.gridLayout_5.addWidget(self.mbtcp_sytstem_tcp_timeout, 4, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.widget_4 = QWidget(self.mbtcp_settings_content)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_8 = QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.mbtcp_separate_list = QLineEdit(self.widget_4)
        self.mbtcp_separate_list.setObjectName(u"mbtcp_separate_list")
        self.mbtcp_separate_list.setEnabled(False)

        self.gridLayout_8.addWidget(self.mbtcp_separate_list, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_12, 0, 0, 1, 1)

        self.mbtcp_separate_list_clear = QPushButton(self.widget_4)
        self.mbtcp_separate_list_clear.setObjectName(u"mbtcp_separate_list_clear")

        self.gridLayout_8.addWidget(self.mbtcp_separate_list_clear, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 6, 0, 1, 1)

        self.label = QLabel(self.mbtcp_settings_content)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setUnderline(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.line = QFrame(self.mbtcp_settings_content)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 1)

        self.widget_3 = QWidget(self.mbtcp_settings_content)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.mbtcp_separate = QCheckBox(self.widget_3)
        self.mbtcp_separate.setObjectName(u"mbtcp_separate")

        self.gridLayout_7.addWidget(self.mbtcp_separate, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.mbtcp_shm_defaults = QPushButton(self.widget_3)
        self.mbtcp_shm_defaults.setObjectName(u"mbtcp_shm_defaults")

        self.gridLayout_7.addWidget(self.mbtcp_shm_defaults, 0, 5, 1, 1)

        self.mbtcp_separate_all = QCheckBox(self.widget_3)
        self.mbtcp_separate_all.setObjectName(u"mbtcp_separate_all")
        self.mbtcp_separate_all.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.mbtcp_separate_all.sizePolicy().hasHeightForWidth())
        self.mbtcp_separate_all.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.mbtcp_separate_all, 0, 4, 1, 1)


        self.gridLayout_4.addWidget(self.widget_3, 4, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 7, 0, 1, 1)

        self.mbtcp_settings.setWidget(self.mbtcp_settings_content)

        self.gridLayout_3.addWidget(self.mbtcp_settings, 12, 3, 1, 1)

        self.tabWidget_modbus_cl.addTab(self.tab_mbtcp, "")
        self.tab_mbrtu = QWidget()
        self.tab_mbrtu.setObjectName(u"tab_mbrtu")
        self.gridLayout_14 = QGridLayout(self.tab_mbrtu)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_17 = QWidget(self.tab_mbrtu)
        self.widget_17.setObjectName(u"widget_17")
        self.gridLayout_23 = QGridLayout(self.widget_17)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.mbrtu_start = QPushButton(self.widget_17)
        self.mbrtu_start.setObjectName(u"mbrtu_start")
        sizePolicy1.setHeightForWidth(self.mbrtu_start.sizePolicy().hasHeightForWidth())
        self.mbrtu_start.setSizePolicy(sizePolicy1)

        self.gridLayout_23.addWidget(self.mbrtu_start, 0, 1, 1, 1)

        self.mbrtu_defaults = QPushButton(self.widget_17)
        self.mbrtu_defaults.setObjectName(u"mbrtu_defaults")

        self.gridLayout_23.addWidget(self.mbrtu_defaults, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.widget_17, 2, 0, 1, 1)

        self.scrollArea_2 = QScrollArea(self.tab_mbrtu)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.mbrtu_settings = QWidget()
        self.mbrtu_settings.setObjectName(u"mbrtu_settings")
        self.mbrtu_settings.setGeometry(QRect(0, 0, 253, 391))
        self.gridLayout_15 = QGridLayout(self.mbrtu_settings)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_32 = QLabel(self.mbrtu_settings)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_15.addWidget(self.label_32, 3, 0, 1, 1)

        self.widget_15 = QWidget(self.mbrtu_settings)
        self.widget_15.setObjectName(u"widget_15")
        self.gridLayout_21 = QGridLayout(self.widget_15)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_33 = QLabel(self.widget_15)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_33, 0, 0, 1, 1)

        self.mbrtu_clientid_default = QPushButton(self.widget_15)
        self.mbrtu_clientid_default.setObjectName(u"mbrtu_clientid_default")

        self.gridLayout_21.addWidget(self.mbrtu_clientid_default, 0, 2, 1, 1)

        self.mbrtu_clientid = QSpinBox(self.widget_15)
        self.mbrtu_clientid.setObjectName(u"mbrtu_clientid")
        sizePolicy1.setHeightForWidth(self.mbrtu_clientid.sizePolicy().hasHeightForWidth())
        self.mbrtu_clientid.setSizePolicy(sizePolicy1)
        self.mbrtu_clientid.setMaximum(255)

        self.gridLayout_21.addWidget(self.mbrtu_clientid, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.widget_15, 5, 0, 1, 1)

        self.widget_10 = QWidget(self.mbrtu_settings)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_16 = QGridLayout(self.widget_10)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_23 = QLabel(self.widget_10)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_23, 4, 0, 1, 1)

        self.label_19 = QLabel(self.widget_10)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)

        self.mbrtu_device = QLineEdit(self.widget_10)
        self.mbrtu_device.setObjectName(u"mbrtu_device")

        self.gridLayout_16.addWidget(self.mbrtu_device, 0, 1, 1, 1)

        self.mbrtu_stopbits_default = QPushButton(self.widget_10)
        self.mbrtu_stopbits_default.setObjectName(u"mbrtu_stopbits_default")

        self.gridLayout_16.addWidget(self.mbrtu_stopbits_default, 3, 2, 1, 1)

        self.label_22 = QLabel(self.widget_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_22, 3, 0, 1, 1)

        self.mbrtu_databits_default = QPushButton(self.widget_10)
        self.mbrtu_databits_default.setObjectName(u"mbrtu_databits_default")

        self.gridLayout_16.addWidget(self.mbrtu_databits_default, 2, 2, 1, 1)

        self.mbrtu_baudrate = QLineEdit(self.widget_10)
        self.mbrtu_baudrate.setObjectName(u"mbrtu_baudrate")

        self.gridLayout_16.addWidget(self.mbrtu_baudrate, 4, 1, 1, 1)

        self.label_20 = QLabel(self.widget_10)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_20, 1, 0, 1, 1)

        self.mbrtu_databits = QSpinBox(self.widget_10)
        self.mbrtu_databits.setObjectName(u"mbrtu_databits")
        self.mbrtu_databits.setMinimum(5)
        self.mbrtu_databits.setMaximum(8)
        self.mbrtu_databits.setValue(8)

        self.gridLayout_16.addWidget(self.mbrtu_databits, 2, 1, 1, 1)

        self.mbrtu_parity_default = QPushButton(self.widget_10)
        self.mbrtu_parity_default.setObjectName(u"mbrtu_parity_default")

        self.gridLayout_16.addWidget(self.mbrtu_parity_default, 1, 2, 1, 1)

        self.mbrtu_baudrate_default = QPushButton(self.widget_10)
        self.mbrtu_baudrate_default.setObjectName(u"mbrtu_baudrate_default")

        self.gridLayout_16.addWidget(self.mbrtu_baudrate_default, 4, 2, 1, 1)

        self.label_21 = QLabel(self.widget_10)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_21, 2, 0, 1, 1)

        self.mbrtu_stopbits = QSpinBox(self.widget_10)
        self.mbrtu_stopbits.setObjectName(u"mbrtu_stopbits")
        self.mbrtu_stopbits.setMinimum(1)
        self.mbrtu_stopbits.setMaximum(2)

        self.gridLayout_16.addWidget(self.mbrtu_stopbits, 3, 1, 1, 1)

        self.mbrtu_parity = QComboBox(self.widget_10)
        self.mbrtu_parity.addItem("")
        self.mbrtu_parity.addItem("")
        self.mbrtu_parity.addItem("")
        self.mbrtu_parity.setObjectName(u"mbrtu_parity")

        self.gridLayout_16.addWidget(self.mbrtu_parity, 1, 1, 1, 1)

        self.label_24 = QLabel(self.widget_10)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_16.addWidget(self.label_24, 5, 0, 1, 1)

        self.mbrtu_serialtype = QComboBox(self.widget_10)
        self.mbrtu_serialtype.addItem("")
        self.mbrtu_serialtype.addItem("")
        self.mbrtu_serialtype.setObjectName(u"mbrtu_serialtype")

        self.gridLayout_16.addWidget(self.mbrtu_serialtype, 5, 1, 1, 1)

        self.mbrtu_serialtype_default = QPushButton(self.widget_10)
        self.mbrtu_serialtype_default.setObjectName(u"mbrtu_serialtype_default")

        self.gridLayout_16.addWidget(self.mbrtu_serialtype_default, 5, 2, 1, 1)

        self.mbrtu_device_default = QPushButton(self.widget_10)
        self.mbrtu_device_default.setObjectName(u"mbrtu_device_default")

        self.gridLayout_16.addWidget(self.mbrtu_device_default, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.widget_10, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_6, 6, 0, 1, 1)

        self.line_5 = QFrame(self.mbrtu_settings)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.HLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_15.addWidget(self.line_5, 2, 0, 1, 1)

        self.label_18 = QLabel(self.mbrtu_settings)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_15.addWidget(self.label_18, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.mbrtu_settings)

        self.gridLayout_14.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.tabWidget_modbus_cl.addTab(self.tab_mbrtu, "")

        self.gridLayout_2.addWidget(self.tabWidget_modbus_cl, 0, 0, 1, 1)

        self.tabWidget_tools.addTab(self.tab_modbus_clients, "")
        self.tab_shm_tools = QWidget()
        self.tab_shm_tools.setObjectName(u"tab_shm_tools")
        self.tab_shm_tools.setEnabled(True)
        self.gridLayout_25 = QGridLayout(self.tab_shm_tools)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.scrollArea = QScrollArea(self.tab_shm_tools)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setEnabled(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -162, 745, 646))
        self.gridLayout_26 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.Shape.HLine)
        self.line_11.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_26.addWidget(self.line_11, 6, 0, 1, 1)

        self.widget_22 = QWidget(self.scrollAreaWidgetContents)
        self.widget_22.setObjectName(u"widget_22")
        self.gridLayout_31 = QGridLayout(self.widget_22)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.tool_load_ao_file_dialog = QToolButton(self.widget_22)
        self.tool_load_ao_file_dialog.setObjectName(u"tool_load_ao_file_dialog")
        icon = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u"../../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.tool_load_ao_file_dialog.setIcon(icon)

        self.gridLayout_31.addWidget(self.tool_load_ao_file_dialog, 2, 4, 1, 1)

        self.tool_load_ai = QPushButton(self.widget_22)
        self.tool_load_ai.setObjectName(u"tool_load_ai")

        self.gridLayout_31.addWidget(self.tool_load_ai, 3, 0, 1, 1)

        self.tool_load_do_repeat = QCheckBox(self.widget_22)
        self.tool_load_do_repeat.setObjectName(u"tool_load_do_repeat")
        self.tool_load_do_repeat.setChecked(True)

        self.gridLayout_31.addWidget(self.tool_load_do_repeat, 0, 2, 1, 1)

        self.tool_load_di_file = QLineEdit(self.widget_22)
        self.tool_load_di_file.setObjectName(u"tool_load_di_file")

        self.gridLayout_31.addWidget(self.tool_load_di_file, 1, 3, 1, 1)

        self.tool_load_do = QPushButton(self.widget_22)
        self.tool_load_do.setObjectName(u"tool_load_do")

        self.gridLayout_31.addWidget(self.tool_load_do, 0, 0, 1, 1)

        self.tool_load_ai_file = QLineEdit(self.widget_22)
        self.tool_load_ai_file.setObjectName(u"tool_load_ai_file")

        self.gridLayout_31.addWidget(self.tool_load_ai_file, 3, 3, 1, 1)

        self.tool_load_ao_file = QLineEdit(self.widget_22)
        self.tool_load_ao_file.setObjectName(u"tool_load_ao_file")

        self.gridLayout_31.addWidget(self.tool_load_ao_file, 2, 3, 1, 1)

        self.tool_load_ao_invert = QCheckBox(self.widget_22)
        self.tool_load_ao_invert.setObjectName(u"tool_load_ao_invert")

        self.gridLayout_31.addWidget(self.tool_load_ao_invert, 2, 1, 1, 1)

        self.tool_load_di = QPushButton(self.widget_22)
        self.tool_load_di.setObjectName(u"tool_load_di")

        self.gridLayout_31.addWidget(self.tool_load_di, 1, 0, 1, 1)

        self.tool_load_do_file = QLineEdit(self.widget_22)
        self.tool_load_do_file.setObjectName(u"tool_load_do_file")

        self.gridLayout_31.addWidget(self.tool_load_do_file, 0, 3, 1, 1)

        self.tool_load_di_repeat = QCheckBox(self.widget_22)
        self.tool_load_di_repeat.setObjectName(u"tool_load_di_repeat")
        self.tool_load_di_repeat.setChecked(True)

        self.gridLayout_31.addWidget(self.tool_load_di_repeat, 1, 2, 1, 1)

        self.tool_load_do_invert = QCheckBox(self.widget_22)
        self.tool_load_do_invert.setObjectName(u"tool_load_do_invert")

        self.gridLayout_31.addWidget(self.tool_load_do_invert, 0, 1, 1, 1)

        self.tool_load_do_file_dialog = QToolButton(self.widget_22)
        self.tool_load_do_file_dialog.setObjectName(u"tool_load_do_file_dialog")
        self.tool_load_do_file_dialog.setIcon(icon)

        self.gridLayout_31.addWidget(self.tool_load_do_file_dialog, 0, 4, 1, 1)

        self.tool_load_ai_invert = QCheckBox(self.widget_22)
        self.tool_load_ai_invert.setObjectName(u"tool_load_ai_invert")

        self.gridLayout_31.addWidget(self.tool_load_ai_invert, 3, 1, 1, 1)

        self.tool_load_ao = QPushButton(self.widget_22)
        self.tool_load_ao.setObjectName(u"tool_load_ao")

        self.gridLayout_31.addWidget(self.tool_load_ao, 2, 0, 1, 1)

        self.tool_load_ai_repeat = QCheckBox(self.widget_22)
        self.tool_load_ai_repeat.setObjectName(u"tool_load_ai_repeat")
        self.tool_load_ai_repeat.setChecked(True)

        self.gridLayout_31.addWidget(self.tool_load_ai_repeat, 3, 2, 1, 1)

        self.tool_load_ao_repeat = QCheckBox(self.widget_22)
        self.tool_load_ao_repeat.setObjectName(u"tool_load_ao_repeat")
        self.tool_load_ao_repeat.setChecked(True)

        self.gridLayout_31.addWidget(self.tool_load_ao_repeat, 2, 2, 1, 1)

        self.tool_load_di_file_dialog = QToolButton(self.widget_22)
        self.tool_load_di_file_dialog.setObjectName(u"tool_load_di_file_dialog")
        self.tool_load_di_file_dialog.setIcon(icon)

        self.gridLayout_31.addWidget(self.tool_load_di_file_dialog, 1, 4, 1, 1)

        self.tool_load_di_invert = QCheckBox(self.widget_22)
        self.tool_load_di_invert.setObjectName(u"tool_load_di_invert")

        self.gridLayout_31.addWidget(self.tool_load_di_invert, 1, 1, 1, 1)

        self.tool_load_ai_file_dialog = QToolButton(self.widget_22)
        self.tool_load_ai_file_dialog.setObjectName(u"tool_load_ai_file_dialog")
        self.tool_load_ai_file_dialog.setIcon(icon)

        self.gridLayout_31.addWidget(self.tool_load_ai_file_dialog, 3, 4, 1, 1)


        self.gridLayout_26.addWidget(self.widget_22, 3, 0, 1, 1)

        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setEnabled(True)
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_26.addWidget(self.line_10, 4, 0, 1, 1)

        self.widget_20 = QWidget(self.scrollAreaWidgetContents)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setEnabled(True)
        self.gridLayout_28 = QGridLayout(self.widget_20)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.tool_dump_ai = QPushButton(self.widget_20)
        self.tool_dump_ai.setObjectName(u"tool_dump_ai")
        self.tool_dump_ai.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_ai, 3, 1, 1, 1)

        self.tool_dump_di_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_di_file_dialog.setObjectName(u"tool_dump_di_file_dialog")
        icon1 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u"../../../../../.designer/backup", QSize(), QIcon.Normal, QIcon.Off)

        self.tool_dump_di_file_dialog.setIcon(icon1)

        self.gridLayout_28.addWidget(self.tool_dump_di_file_dialog, 1, 3, 1, 1)

        self.tool_dump_do_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_do_file_dialog.setObjectName(u"tool_dump_do_file_dialog")
        self.tool_dump_do_file_dialog.setIcon(icon1)

        self.gridLayout_28.addWidget(self.tool_dump_do_file_dialog, 0, 3, 1, 1)

        self.tool_dump_ao = QPushButton(self.widget_20)
        self.tool_dump_ao.setObjectName(u"tool_dump_ao")
        self.tool_dump_ao.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_ao, 2, 1, 1, 1)

        self.tool_dump_do_file = QLineEdit(self.widget_20)
        self.tool_dump_do_file.setObjectName(u"tool_dump_do_file")

        self.gridLayout_28.addWidget(self.tool_dump_do_file, 0, 2, 1, 1)

        self.tool_dump_di_file = QLineEdit(self.widget_20)
        self.tool_dump_di_file.setObjectName(u"tool_dump_di_file")

        self.gridLayout_28.addWidget(self.tool_dump_di_file, 1, 2, 1, 1)

        self.tool_dump_ao_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_ao_file_dialog.setObjectName(u"tool_dump_ao_file_dialog")
        self.tool_dump_ao_file_dialog.setIcon(icon1)

        self.gridLayout_28.addWidget(self.tool_dump_ao_file_dialog, 2, 3, 1, 1)

        self.tool_dump_do = QPushButton(self.widget_20)
        self.tool_dump_do.setObjectName(u"tool_dump_do")
        self.tool_dump_do.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_do, 0, 1, 1, 1)

        self.tool_dump_ao_file = QLineEdit(self.widget_20)
        self.tool_dump_ao_file.setObjectName(u"tool_dump_ao_file")

        self.gridLayout_28.addWidget(self.tool_dump_ao_file, 2, 2, 1, 1)

        self.tool_dump_di = QPushButton(self.widget_20)
        self.tool_dump_di.setObjectName(u"tool_dump_di")
        self.tool_dump_di.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_di, 1, 1, 1, 1)

        self.tool_dump_ai_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_ai_file_dialog.setObjectName(u"tool_dump_ai_file_dialog")
        self.tool_dump_ai_file_dialog.setIcon(icon1)

        self.gridLayout_28.addWidget(self.tool_dump_ai_file_dialog, 3, 3, 1, 1)

        self.tool_dump_ai_file = QLineEdit(self.widget_20)
        self.tool_dump_ai_file.setObjectName(u"tool_dump_ai_file")

        self.gridLayout_28.addWidget(self.tool_dump_ai_file, 3, 2, 1, 1)


        self.gridLayout_26.addWidget(self.widget_20, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.random_ai = QWidget(self.scrollAreaWidgetContents)
        self.random_ai.setObjectName(u"random_ai")
        self.gridLayout_30 = QGridLayout(self.random_ai)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.tool_random_do = QPushButton(self.random_ai)
        self.tool_random_do.setObjectName(u"tool_random_do")

        self.gridLayout_30.addWidget(self.tool_random_do, 0, 0, 1, 1)

        self.tool_random_di = QPushButton(self.random_ai)
        self.tool_random_di.setObjectName(u"tool_random_di")

        self.gridLayout_30.addWidget(self.tool_random_di, 0, 1, 1, 1)

        self.tool_random_ao = QPushButton(self.random_ai)
        self.tool_random_ao.setObjectName(u"tool_random_ao")

        self.gridLayout_30.addWidget(self.tool_random_ao, 1, 0, 1, 1)

        self.tool_random_ai = QPushButton(self.random_ai)
        self.tool_random_ai.setObjectName(u"tool_random_ai")

        self.gridLayout_30.addWidget(self.tool_random_ai, 1, 1, 1, 1)


        self.gridLayout_26.addWidget(self.random_ai, 7, 0, 1, 1)

        self.widget_19 = QWidget(self.scrollAreaWidgetContents)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setEnabled(True)
        self.gridLayout_27 = QGridLayout(self.widget_19)
        self.gridLayout_27.setObjectName(u"gridLayout_27")

        self.gridLayout_26.addWidget(self.widget_19, 0, 0, 1, 1)

        self.line_12 = QFrame(self.scrollAreaWidgetContents)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.Shape.HLine)
        self.line_12.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_26.addWidget(self.line_12, 2, 0, 1, 1)

        self.widget_21 = QWidget(self.scrollAreaWidgetContents)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setEnabled(True)
        self.gridLayout_29 = QGridLayout(self.widget_21)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.tool_hexdump_ai = QPushButton(self.widget_21)
        self.tool_hexdump_ai.setObjectName(u"tool_hexdump_ai")
        self.tool_hexdump_ai.setEnabled(True)

        self.gridLayout_29.addWidget(self.tool_hexdump_ai, 1, 1, 1, 1)

        self.tool_hexdump_di = QPushButton(self.widget_21)
        self.tool_hexdump_di.setObjectName(u"tool_hexdump_di")
        self.tool_hexdump_di.setEnabled(True)

        self.gridLayout_29.addWidget(self.tool_hexdump_di, 0, 1, 1, 1)

        self.tool_hexdump_do = QPushButton(self.widget_21)
        self.tool_hexdump_do.setObjectName(u"tool_hexdump_do")
        self.tool_hexdump_do.setEnabled(True)

        self.gridLayout_29.addWidget(self.tool_hexdump_do, 0, 0, 1, 1)

        self.tool_hexdump_ao = QPushButton(self.widget_21)
        self.tool_hexdump_ao.setObjectName(u"tool_hexdump_ao")
        self.tool_hexdump_ao.setEnabled(True)

        self.gridLayout_29.addWidget(self.tool_hexdump_ao, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.widget_21, 5, 0, 1, 1)

        self.line_6 = QFrame(self.scrollAreaWidgetContents)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_26.addWidget(self.line_6, 8, 0, 1, 1)

        self.widget_14 = QWidget(self.scrollAreaWidgetContents)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_20 = QGridLayout(self.widget_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.tool_inspec_values = QPushButton(self.widget_14)
        self.tool_inspec_values.setObjectName(u"tool_inspec_values")

        self.gridLayout_20.addWidget(self.tool_inspec_values, 0, 0, 1, 1)

        self.tool_set_values = QPushButton(self.widget_14)
        self.tool_set_values.setObjectName(u"tool_set_values")
        self.tool_set_values.setEnabled(True)

        self.gridLayout_20.addWidget(self.tool_set_values, 0, 1, 1, 1)


        self.gridLayout_26.addWidget(self.widget_14, 10, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_25.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.tabWidget_tools.addTab(self.tab_shm_tools, "")

        self.gridLayout.addWidget(self.tabWidget_tools, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionopen_modbus_client_config)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionsave_modbus_client_config)
        self.menuHelp.addAction(self.actionVersion)

        self.retranslateUi(MainWindow)

        self.tabWidget_tools.setCurrentIndex(0)
        self.tabWidget_modbus_cl.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SHM Modbus", None))
        self.actionVersion.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.actionsave_modbus_client_config.setText(QCoreApplication.translate("MainWindow", u"save modbus client config", None))
        self.actionsave_modbus_rtu_client_config.setText(QCoreApplication.translate("MainWindow", u"save modbus rtu client config", None))
        self.actionopen_modbus_client_config.setText(QCoreApplication.translate("MainWindow", u"open modbus client config", None))
        self.actionopen_modbus_rtu_client_config.setText(QCoreApplication.translate("MainWindow", u"open modbus rtu client config", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Registers", None))
#if QT_CONFIG(tooltip)
        self.mb_do.setToolTip(QCoreApplication.translate("MainWindow", u"number of DO registers (Coils, discrete output)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_do.setStatusTip(QCoreApplication.translate("MainWindow", u"number of DO registers (Coils, discrete output)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mb_do_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default number of DO registers (Coils, discrete output) (65536)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_do_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default number of DO registers (Coils, discrete output) (65536)", None))
#endif // QT_CONFIG(statustip)
        self.mb_do_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DI:", None))
#if QT_CONFIG(tooltip)
        self.mb_di.setToolTip(QCoreApplication.translate("MainWindow", u"number of DI registers (discrete input)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_di.setStatusTip(QCoreApplication.translate("MainWindow", u"number of DI registers (discrete input)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mb_ai.setToolTip(QCoreApplication.translate("MainWindow", u"number of AI registers (input registers)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_ai.setStatusTip(QCoreApplication.translate("MainWindow", u"number of AI registers (input registers)", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DO:", None))
#if QT_CONFIG(tooltip)
        self.mb_ao.setToolTip(QCoreApplication.translate("MainWindow", u"number of AO registers (holding registers)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_ao.setStatusTip(QCoreApplication.translate("MainWindow", u"number of AO registers (holding registers)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mb_ai_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default number of AI registers (input registers) (65536)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_ai_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default number of AI registers (input registers) (65536)", None))
#endif // QT_CONFIG(statustip)
        self.mb_ai_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
#if QT_CONFIG(tooltip)
        self.mb_ao_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default number of AO registers (holding registers) (65536)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_ao_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default number of AO registers (holding registers) (65536)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.mb_ao_default.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.mb_ao_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
#if QT_CONFIG(tooltip)
        self.label_7.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AO:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"AI:", None))
#if QT_CONFIG(tooltip)
        self.mb_di_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default number of DI registers (discrete input) (65536)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_di_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default number of DI registers (discrete input) (65536)", None))
#endif // QT_CONFIG(statustip)
        self.mb_di_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Shared Memory", None))
#if QT_CONFIG(tooltip)
        self.mb_shm_flags_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default shared memory flags (force: false)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_shm_flags_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default shared memory flags (force: false)", None))
#endif // QT_CONFIG(statustip)
        self.mb_shm_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
#if QT_CONFIG(tooltip)
        self.mb_force.setToolTip(QCoreApplication.translate("MainWindow", u"orce the use of the shared memory even if it already exists. Do not use this option per default! It should only be used if the shared memory of an improperly terminated instance continues to exist as an orphan and is no longer used.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_force.setStatusTip(QCoreApplication.translate("MainWindow", u"force the use of the shared memory even if it already exists. ", None))
#endif // QT_CONFIG(statustip)
        self.mb_force.setText(QCoreApplication.translate("MainWindow", u"force", None))
        self.mb_shm_name.setText(QCoreApplication.translate("MainWindow", u"modbus_", None))
#if QT_CONFIG(tooltip)
        self.mb_shm_name_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default shared memory name prefix (modbus_)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_shm_name_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default shared memory name prefix (modbus_)", None))
#endif // QT_CONFIG(statustip)
        self.mb_shm_name_default.setText(QCoreApplication.translate("MainWindow", u"modbus_", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"name prefix:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Modbus", None))
#if QT_CONFIG(tooltip)
        self.mb_monitor.setToolTip(QCoreApplication.translate("MainWindow", u"monitor all modbus PDUs", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_monitor.setStatusTip(QCoreApplication.translate("MainWindow", u"monitor all modbus PDUs (strong impact on performance)", None))
#endif // QT_CONFIG(statustip)
        self.mb_monitor.setText(QCoreApplication.translate("MainWindow", u"monitor", None))
#if QT_CONFIG(tooltip)
        self.mb_enable_byte_timeout.setToolTip(QCoreApplication.translate("MainWindow", u"manually set the libmodbus byte timeout", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_enable_byte_timeout.setStatusTip(QCoreApplication.translate("MainWindow", u"manually set the libmodbus byte timeout", None))
#endif // QT_CONFIG(statustip)
        self.mb_enable_byte_timeout.setText(QCoreApplication.translate("MainWindow", u"edit byte timeout", None))
#if QT_CONFIG(tooltip)
        self.mb_enable_response_timeout.setToolTip(QCoreApplication.translate("MainWindow", u"manually set the libmodbus response timeout", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_enable_response_timeout.setStatusTip(QCoreApplication.translate("MainWindow", u"manually set the libmodbus response timeout", None))
#endif // QT_CONFIG(statustip)
        self.mb_enable_response_timeout.setText(QCoreApplication.translate("MainWindow", u"edit response timeout", None))
#if QT_CONFIG(tooltip)
        self.mb_mb_flags_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default modbus flags (all false)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_mb_flags_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default modbus flags (all false)", None))
#endif // QT_CONFIG(statustip)
        self.mb_mb_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
#if QT_CONFIG(tooltip)
        self.mb_byte_timeout.setToolTip(QCoreApplication.translate("MainWindow", u"libmodbus byte timeout", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_byte_timeout.setStatusTip(QCoreApplication.translate("MainWindow", u"libmodbus byte timeout", None))
#endif // QT_CONFIG(statustip)
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"response timeout:", None))
#if QT_CONFIG(tooltip)
        self.mb_response_timeout.setToolTip(QCoreApplication.translate("MainWindow", u"libmodbus response timeout", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_response_timeout.setStatusTip(QCoreApplication.translate("MainWindow", u"libmodbus response timeout", None))
#endif // QT_CONFIG(statustip)
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"byte timeout:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Semaphore", None))
#if QT_CONFIG(tooltip)
        self.mb_sem_force.setToolTip(QCoreApplication.translate("MainWindow", u"Force the use of the semaphore even if it already exists. Do not use this option per default! It should only be used if the semaphore of an improperly terminated instance continues to exist as an orphan and is no longer used.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_sem_force.setStatusTip(QCoreApplication.translate("MainWindow", u"Force the use of the semaphore even if it already exists.", None))
#endif // QT_CONFIG(statustip)
        self.mb_sem_force.setText(QCoreApplication.translate("MainWindow", u"force", None))
#if QT_CONFIG(tooltip)
        self.mb_sem_enable.setToolTip(QCoreApplication.translate("MainWindow", u"enable semaphore mechanism", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_sem_enable.setStatusTip(QCoreApplication.translate("MainWindow", u"enable semaphore mechanism to protect the shared memory from simultaneous access.", None))
#endif // QT_CONFIG(statustip)
        self.mb_sem_enable.setText(QCoreApplication.translate("MainWindow", u"enable", None))
#if QT_CONFIG(tooltip)
        self.mb_sem_defaults.setToolTip(QCoreApplication.translate("MainWindow", u"set default semaphore flags (enabled: true, force: false)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_sem_defaults.setStatusTip(QCoreApplication.translate("MainWindow", u"set default semaphore flags (enabled: true, force: false)", None))
#endif // QT_CONFIG(statustip)
        self.mb_sem_defaults.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"name:", None))
#if QT_CONFIG(tooltip)
        self.mb_sem_name.setToolTip(QCoreApplication.translate("MainWindow", u"semaphore name", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_sem_name.setStatusTip(QCoreApplication.translate("MainWindow", u"semaphore name", None))
#endif // QT_CONFIG(statustip)
        self.mb_sem_name.setText(QCoreApplication.translate("MainWindow", u"modbus", None))
#if QT_CONFIG(tooltip)
        self.mb_sem_name_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default semaphore name (modbus)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mb_sem_name_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default semaphore name (modbus)", None))
#endif // QT_CONFIG(statustip)
        self.mb_sem_name_default.setText(QCoreApplication.translate("MainWindow", u"modbus", None))
        self.mb_defaults.setText(QCoreApplication.translate("MainWindow", u"Defaults", None))
        self.tabWidget_modbus_cl.setTabText(self.tabWidget_modbus_cl.indexOf(self.tab_modbus_setings), QCoreApplication.translate("MainWindow", u"Modbus Settings", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_start.setToolTip(QCoreApplication.translate("MainWindow", u"start/stop Modbus TCP client", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_start.setStatusTip(QCoreApplication.translate("MainWindow", u"start/stop Modbus TCP client", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_defaults.setToolTip(QCoreApplication.translate("MainWindow", u"set default values", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_defaults.setStatusTip(QCoreApplication.translate("MainWindow", u"set default values", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_defaults.setText(QCoreApplication.translate("MainWindow", u"Defaults", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Shared Memory", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_port.setToolTip(QCoreApplication.translate("MainWindow", u"TCP port to listen for connections", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_port.setStatusTip(QCoreApplication.translate("MainWindow", u"TCP port to listen for connections", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"host:", None))
#if QT_CONFIG(statustip)
        self.mbtcp_host_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default host (any): no restrictions", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_host_default.setText(QCoreApplication.translate("MainWindow", u"any", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_nw_flags_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default modbus client flags (reconnect: true)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_nw_flags_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default modbus client flags (reconnect: true)", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_nw_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TCP timeout:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"connections:", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_tcp_timeout_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default TCP timeout (5s)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_tcp_timeout_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default TCP timeout (5s)", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_tcp_timeout_default.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_tcp_timeout.setToolTip(QCoreApplication.translate("MainWindow", u"TCP timeout", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_tcp_timeout.setStatusTip(QCoreApplication.translate("MainWindow", u"TCP timeout (aplies to established connections)", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mbtcp_host.setToolTip(QCoreApplication.translate("MainWindow", u"host that is allowed to connect", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_host.setStatusTip(QCoreApplication.translate("MainWindow", u"host that is allowed to connect", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_host.setText(QCoreApplication.translate("MainWindow", u"any", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"port", None))
#if QT_CONFIG(statustip)
        self.mbtcp_port_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default modbus port (502)", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_port_default.setText(QCoreApplication.translate("MainWindow", u"502", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_connections_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default number of allowed simultaneous connections (1)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_connections_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default number of allowed simultaneous connections (1)", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_connections_default.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_connections.setToolTip(QCoreApplication.translate("MainWindow", u"number of allowed simultaneous connections", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_connections.setStatusTip(QCoreApplication.translate("MainWindow", u"number of allowed simultaneous connections", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mbtcp_reconnect.setToolTip(QCoreApplication.translate("MainWindow", u"If unchecked, the modbus client is terminated once all connections are terminated.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_reconnect.setStatusTip(QCoreApplication.translate("MainWindow", u"If unchecked, the modbus client is terminated once all connections are terminated.", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_reconnect.setText(QCoreApplication.translate("MainWindow", u"reconnect", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_sytstem_tcp_timeout.setToolTip(QCoreApplication.translate("MainWindow", u"Use TCP system timeout (TCP timeout is not explicitly set)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_sytstem_tcp_timeout.setStatusTip(QCoreApplication.translate("MainWindow", u"Use TCP system timeout (TCP timeout is not explicitly set)", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_sytstem_tcp_timeout.setText(QCoreApplication.translate("MainWindow", u"use system TCP timeout", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_separate_list.setToolTip(QCoreApplication.translate("MainWindow", u"comma separated list of client ids for wich a separate shared memory is used.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_separate_list.setStatusTip(QCoreApplication.translate("MainWindow", u"comma separated list of client ids for wich a separate shared memory is used.", None))
#endif // QT_CONFIG(statustip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"separate:", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_separate_list_clear.setToolTip(QCoreApplication.translate("MainWindow", u"clear list", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_separate_list_clear.setStatusTip(QCoreApplication.translate("MainWindow", u"clear list", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_separate_list_clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Network", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_separate.setToolTip(QCoreApplication.translate("MainWindow", u"Use a separate shared memory for requests with specific client ids.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_separate.setStatusTip(QCoreApplication.translate("MainWindow", u"Use a separate shared memory for requests with specific client ids.", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_separate.setText(QCoreApplication.translate("MainWindow", u"separate", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_shm_defaults.setToolTip(QCoreApplication.translate("MainWindow", u"set default shared memory flags (force: false, separate: false)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_shm_defaults.setStatusTip(QCoreApplication.translate("MainWindow", u"set default shared memory flags (force: false, separate: false)", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_shm_defaults.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
#if QT_CONFIG(tooltip)
        self.mbtcp_separate_all.setToolTip(QCoreApplication.translate("MainWindow", u"Use a separate shared memory for each client id .", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbtcp_separate_all.setStatusTip(QCoreApplication.translate("MainWindow", u"Use a separate shared memory for each client id .", None))
#endif // QT_CONFIG(statustip)
        self.mbtcp_separate_all.setText(QCoreApplication.translate("MainWindow", u"separate-all", None))
        self.tabWidget_modbus_cl.setTabText(self.tabWidget_modbus_cl.indexOf(self.tab_mbtcp), QCoreApplication.translate("MainWindow", u"Modbus Client TCP", None))
        self.mbrtu_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.mbrtu_defaults.setText(QCoreApplication.translate("MainWindow", u"Defaults", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Modbus", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"client id:", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_clientid_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default modbus client id (0)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_clientid_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default modbus client id (0)", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_clientid_default.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_clientid.setToolTip(QCoreApplication.translate("MainWindow", u"modbus client id", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_clientid.setStatusTip(QCoreApplication.translate("MainWindow", u"modbus client id", None))
#endif // QT_CONFIG(statustip)
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"baud rate:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"device:", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_device.setToolTip(QCoreApplication.translate("MainWindow", u"serial device", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_device.setStatusTip(QCoreApplication.translate("MainWindow", u"serial device", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mbrtu_stopbits_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default number of stop bits (1)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_stopbits_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default number of stop bits (1)", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_stopbits_default.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"stop bits:", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_databits_default.setToolTip(QCoreApplication.translate("MainWindow", u"default number of data bits (8)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_databits_default.setStatusTip(QCoreApplication.translate("MainWindow", u"default number of data bits (8)", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_databits_default.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_baudrate.setToolTip(QCoreApplication.translate("MainWindow", u"serial baud rate", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_baudrate.setStatusTip(QCoreApplication.translate("MainWindow", u"serial baud rate", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_baudrate.setText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"parity:", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_databits.setToolTip(QCoreApplication.translate("MainWindow", u"number of data bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_databits.setStatusTip(QCoreApplication.translate("MainWindow", u"number of data bits", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mbrtu_parity_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default serial parity (None)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_parity_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default serial parity (None)", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_parity_default.setText(QCoreApplication.translate("MainWindow", u"None", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_baudrate_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default serial baud rate", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_baudrate_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default serial baud rate", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_baudrate_default.setText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"data bits:", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_stopbits.setToolTip(QCoreApplication.translate("MainWindow", u"number of stop bits", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_stopbits.setStatusTip(QCoreApplication.translate("MainWindow", u"number of stop bits", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_parity.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.mbrtu_parity.setItemText(1, QCoreApplication.translate("MainWindow", u"Even", None))
        self.mbrtu_parity.setItemText(2, QCoreApplication.translate("MainWindow", u"Odd", None))

#if QT_CONFIG(tooltip)
        self.mbrtu_parity.setToolTip(QCoreApplication.translate("MainWindow", u"serial parity", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_parity.setStatusTip(QCoreApplication.translate("MainWindow", u"serial parity", None))
#endif // QT_CONFIG(statustip)
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"type:", None))
        self.mbrtu_serialtype.setItemText(0, QCoreApplication.translate("MainWindow", u"rs232", None))
        self.mbrtu_serialtype.setItemText(1, QCoreApplication.translate("MainWindow", u"rs485", None))

#if QT_CONFIG(tooltip)
        self.mbrtu_serialtype.setToolTip(QCoreApplication.translate("MainWindow", u"serial type", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_serialtype.setStatusTip(QCoreApplication.translate("MainWindow", u"serial type", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(tooltip)
        self.mbrtu_serialtype_default.setToolTip(QCoreApplication.translate("MainWindow", u"set default serial type (rs232)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_serialtype_default.setStatusTip(QCoreApplication.translate("MainWindow", u"set default serial type (rs232)", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_serialtype_default.setText(QCoreApplication.translate("MainWindow", u"rs232", None))
#if QT_CONFIG(tooltip)
        self.mbrtu_device_default.setToolTip(QCoreApplication.translate("MainWindow", u"clear serial device", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.mbrtu_device_default.setStatusTip(QCoreApplication.translate("MainWindow", u"clear serial device", None))
#endif // QT_CONFIG(statustip)
        self.mbrtu_device_default.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.tabWidget_modbus_cl.setTabText(self.tabWidget_modbus_cl.indexOf(self.tab_mbrtu), QCoreApplication.translate("MainWindow", u"Modbus Client RTU", None))
        self.tabWidget_tools.setTabText(self.tabWidget_tools.indexOf(self.tab_modbus_clients), QCoreApplication.translate("MainWindow", u"Modbus Clients", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ao_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to load AO registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ao_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to load AO registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ao_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ai.setToolTip(QCoreApplication.translate("MainWindow", u"load AI from file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ai.setStatusTip(QCoreApplication.translate("MainWindow", u"load AI from file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ai.setText(QCoreApplication.translate("MainWindow", u"load AI from file", None))
#if QT_CONFIG(tooltip)
        self.tool_load_do_repeat.setToolTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_do_repeat.setStatusTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_do_repeat.setText(QCoreApplication.translate("MainWindow", u"repeat", None))
#if QT_CONFIG(tooltip)
        self.tool_load_di_file.setToolTip(QCoreApplication.translate("MainWindow", u"DI dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_di_file.setStatusTip(QCoreApplication.translate("MainWindow", u"DI dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_di_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_DI", None))
#if QT_CONFIG(tooltip)
        self.tool_load_do.setToolTip(QCoreApplication.translate("MainWindow", u"load DO from file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_do.setStatusTip(QCoreApplication.translate("MainWindow", u"load DO from file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_do.setText(QCoreApplication.translate("MainWindow", u"load DO from file", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ai_file.setToolTip(QCoreApplication.translate("MainWindow", u"AI dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ai_file.setStatusTip(QCoreApplication.translate("MainWindow", u"AI dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ai_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_AI", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ao_file.setToolTip(QCoreApplication.translate("MainWindow", u"AO dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ao_file.setStatusTip(QCoreApplication.translate("MainWindow", u"AO dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ao_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_AO", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ao_invert.setToolTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ao_invert.setStatusTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ao_invert.setText(QCoreApplication.translate("MainWindow", u"invert", None))
#if QT_CONFIG(tooltip)
        self.tool_load_di.setToolTip(QCoreApplication.translate("MainWindow", u"load DI from file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_di.setStatusTip(QCoreApplication.translate("MainWindow", u"load DI from file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_di.setText(QCoreApplication.translate("MainWindow", u"load DI from file", None))
#if QT_CONFIG(tooltip)
        self.tool_load_do_file.setToolTip(QCoreApplication.translate("MainWindow", u"DO dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_do_file.setStatusTip(QCoreApplication.translate("MainWindow", u"DO dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_do_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_DO", None))
#if QT_CONFIG(tooltip)
        self.tool_load_di_repeat.setToolTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_di_repeat.setStatusTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_di_repeat.setText(QCoreApplication.translate("MainWindow", u"repeat", None))
#if QT_CONFIG(tooltip)
        self.tool_load_do_invert.setToolTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_do_invert.setStatusTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_do_invert.setText(QCoreApplication.translate("MainWindow", u"invert", None))
#if QT_CONFIG(tooltip)
        self.tool_load_do_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to load DO registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_do_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to load DO registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_do_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ai_invert.setToolTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ai_invert.setStatusTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ai_invert.setText(QCoreApplication.translate("MainWindow", u"invert", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ao.setToolTip(QCoreApplication.translate("MainWindow", u"load AO from file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ao.setStatusTip(QCoreApplication.translate("MainWindow", u"load AO from file", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ao.setText(QCoreApplication.translate("MainWindow", u"load AO from file", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ai_repeat.setToolTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ai_repeat.setStatusTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ai_repeat.setText(QCoreApplication.translate("MainWindow", u"repeat", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ao_repeat.setToolTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ao_repeat.setStatusTip(QCoreApplication.translate("MainWindow", u"repeat loading the data untill the complete shared memory is filled", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ao_repeat.setText(QCoreApplication.translate("MainWindow", u"repeat", None))
#if QT_CONFIG(tooltip)
        self.tool_load_di_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to load DI registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_di_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to load DI registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_di_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_load_di_invert.setToolTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_di_invert.setStatusTip(QCoreApplication.translate("MainWindow", u"invert loaded data", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_di_invert.setText(QCoreApplication.translate("MainWindow", u"invert", None))
#if QT_CONFIG(tooltip)
        self.tool_load_ai_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to load AI registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_load_ai_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to load AI registers. The file is not loaded. Use load button (left) to load registers from dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_load_ai_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_ai.setToolTip(QCoreApplication.translate("MainWindow", u"dump AI to file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_ai.setStatusTip(QCoreApplication.translate("MainWindow", u"dump AI to file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_ai.setText(QCoreApplication.translate("MainWindow", u"dump AI to file", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_di_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to dump DI registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_di_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to dump DI registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_di_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_do_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to dump DO registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_do_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to dump DO registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_do_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_ao.setToolTip(QCoreApplication.translate("MainWindow", u"dump AO to file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_ao.setStatusTip(QCoreApplication.translate("MainWindow", u"dump AO to file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_ao.setText(QCoreApplication.translate("MainWindow", u"dump AO to file", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_do_file.setToolTip(QCoreApplication.translate("MainWindow", u"DO dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_do_file.setStatusTip(QCoreApplication.translate("MainWindow", u"DO dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_do_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_DO", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_di_file.setToolTip(QCoreApplication.translate("MainWindow", u"DI dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_di_file.setStatusTip(QCoreApplication.translate("MainWindow", u"DI dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_di_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_DI", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_ao_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to dump AO registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_ao_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to dump AO registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_ao_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_do.setToolTip(QCoreApplication.translate("MainWindow", u"dump DO to file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_do.setStatusTip(QCoreApplication.translate("MainWindow", u"dump DO to file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_do.setText(QCoreApplication.translate("MainWindow", u"dump DO to file", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_ao_file.setToolTip(QCoreApplication.translate("MainWindow", u"AO dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_ao_file.setStatusTip(QCoreApplication.translate("MainWindow", u"AO dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_ao_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_AO", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_di.setToolTip(QCoreApplication.translate("MainWindow", u"dump DI to file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_di.setStatusTip(QCoreApplication.translate("MainWindow", u"dump DI to file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_di.setText(QCoreApplication.translate("MainWindow", u"dump DI to file", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_ai_file_dialog.setToolTip(QCoreApplication.translate("MainWindow", u"Select file to dump AI registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_ai_file_dialog.setStatusTip(QCoreApplication.translate("MainWindow", u"Select file to dump AI registers. The file is not written. Use dump (left) to execute dump.", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_ai_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.tool_dump_ai_file.setToolTip(QCoreApplication.translate("MainWindow", u"AI dump file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_dump_ai_file.setStatusTip(QCoreApplication.translate("MainWindow", u"AI dump file", None))
#endif // QT_CONFIG(statustip)
        self.tool_dump_ai_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_AI", None))
#if QT_CONFIG(tooltip)
        self.tool_random_do.setToolTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_random_do.setStatusTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_random_do.setText(QCoreApplication.translate("MainWindow", u"randomize DO", None))
#if QT_CONFIG(tooltip)
        self.tool_random_di.setToolTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_random_di.setStatusTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_random_di.setText(QCoreApplication.translate("MainWindow", u"randomize DI", None))
#if QT_CONFIG(tooltip)
        self.tool_random_ao.setToolTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_random_ao.setStatusTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_random_ao.setText(QCoreApplication.translate("MainWindow", u"randomize AO", None))
#if QT_CONFIG(tooltip)
        self.tool_random_ai.setToolTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_random_ai.setStatusTip(QCoreApplication.translate("MainWindow", u"start randomize tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_random_ai.setText(QCoreApplication.translate("MainWindow", u"randomize AI", None))
#if QT_CONFIG(tooltip)
        self.tool_hexdump_ai.setToolTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_hexdump_ai.setStatusTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_hexdump_ai.setText(QCoreApplication.translate("MainWindow", u"hexdump AI", None))
#if QT_CONFIG(tooltip)
        self.tool_hexdump_di.setToolTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_hexdump_di.setStatusTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_hexdump_di.setText(QCoreApplication.translate("MainWindow", u"hexdump DI", None))
#if QT_CONFIG(tooltip)
        self.tool_hexdump_do.setToolTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_hexdump_do.setStatusTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_hexdump_do.setText(QCoreApplication.translate("MainWindow", u"hexdump DO", None))
#if QT_CONFIG(tooltip)
        self.tool_hexdump_ao.setToolTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.tool_hexdump_ao.setStatusTip(QCoreApplication.translate("MainWindow", u"start hexdump tool", None))
#endif // QT_CONFIG(statustip)
        self.tool_hexdump_ao.setText(QCoreApplication.translate("MainWindow", u"hexdump AO", None))
        self.tool_inspec_values.setText(QCoreApplication.translate("MainWindow", u"inspect values", None))
        self.tool_set_values.setText(QCoreApplication.translate("MainWindow", u"set values", None))
        self.tabWidget_tools.setTabText(self.tabWidget_tools.indexOf(self.tab_shm_tools), QCoreApplication.translate("MainWindow", u"Shared Memory Tools", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

