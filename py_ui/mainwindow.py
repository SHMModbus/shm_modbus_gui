# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGridLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QToolButton,
    QWidget)

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
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionsave_modbus_tcp_client_config = QAction(MainWindow)
        self.actionsave_modbus_tcp_client_config.setObjectName(u"actionsave_modbus_tcp_client_config")
        self.actionsave_modbus_rtu_client_config = QAction(MainWindow)
        self.actionsave_modbus_rtu_client_config.setObjectName(u"actionsave_modbus_rtu_client_config")
        self.actionopen_modbus_tcp_client_config = QAction(MainWindow)
        self.actionopen_modbus_tcp_client_config.setObjectName(u"actionopen_modbus_tcp_client_config")
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
        self.tabWidget_modbus_clients = QTabWidget(self.tab_modbus_clients)
        self.tabWidget_modbus_clients.setObjectName(u"tabWidget_modbus_clients")
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
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
        self.mbtcp_settings_content.setGeometry(QRect(0, 0, 727, 1013))
        self.gridLayout_4 = QGridLayout(self.mbtcp_settings_content)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_5 = QWidget(self.mbtcp_settings_content)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_9 = QGridLayout(self.widget_5)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.mbtcp_sem_force = QCheckBox(self.widget_5)
        self.mbtcp_sem_force.setObjectName(u"mbtcp_sem_force")
        sizePolicy1.setHeightForWidth(self.mbtcp_sem_force.sizePolicy().hasHeightForWidth())
        self.mbtcp_sem_force.setSizePolicy(sizePolicy1)

        self.gridLayout_9.addWidget(self.mbtcp_sem_force, 0, 3, 1, 1)

        self.mbtcp_sem_enable = QCheckBox(self.widget_5)
        self.mbtcp_sem_enable.setObjectName(u"mbtcp_sem_enable")
        self.mbtcp_sem_enable.setChecked(True)

        self.gridLayout_9.addWidget(self.mbtcp_sem_enable, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.mbtcp_sem_defaults = QPushButton(self.widget_5)
        self.mbtcp_sem_defaults.setObjectName(u"mbtcp_sem_defaults")

        self.gridLayout_9.addWidget(self.mbtcp_sem_defaults, 0, 4, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_5, 16, 0, 1, 1)

        self.label_9 = QLabel(self.mbtcp_settings_content)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)

        self.gridLayout_4.addWidget(self.label_9, 6, 0, 1, 1)

        self.widget = QWidget(self.mbtcp_settings_content)
        self.widget.setObjectName(u"widget")
        self.gridLayout_5 = QGridLayout(self.widget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mbtcp_port = QSpinBox(self.widget)
        self.mbtcp_port.setObjectName(u"mbtcp_port")
        self.mbtcp_port.setMaximum(65535)
        self.mbtcp_port.setValue(502)

        self.gridLayout_5.addWidget(self.mbtcp_port, 2, 1, 1, 1)

        self.mbtcp_host_default = QPushButton(self.widget)
        self.mbtcp_host_default.setObjectName(u"mbtcp_host_default")

        self.gridLayout_5.addWidget(self.mbtcp_host_default, 1, 2, 1, 1)

        self.label_38 = QLabel(self.widget)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_38, 5, 0, 1, 1)

        self.mbtcp_port_default = QPushButton(self.widget)
        self.mbtcp_port_default.setObjectName(u"mbtcp_port_default")

        self.gridLayout_5.addWidget(self.mbtcp_port_default, 2, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)

        self.mbtcp_sytstem_tcp_timeout = QCheckBox(self.widget)
        self.mbtcp_sytstem_tcp_timeout.setObjectName(u"mbtcp_sytstem_tcp_timeout")

        self.gridLayout_5.addWidget(self.mbtcp_sytstem_tcp_timeout, 4, 1, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_11, 3, 0, 1, 1)

        self.mbtcp_tcp_timeout = QSpinBox(self.widget)
        self.mbtcp_tcp_timeout.setObjectName(u"mbtcp_tcp_timeout")
        self.mbtcp_tcp_timeout.setMinimum(1)
        self.mbtcp_tcp_timeout.setMaximum(86400)
        self.mbtcp_tcp_timeout.setValue(5)

        self.gridLayout_5.addWidget(self.mbtcp_tcp_timeout, 3, 1, 1, 1)

        self.mbtcp_connections_default = QPushButton(self.widget)
        self.mbtcp_connections_default.setObjectName(u"mbtcp_connections_default")

        self.gridLayout_5.addWidget(self.mbtcp_connections_default, 5, 2, 1, 1)

        self.mbtcp_host = QLineEdit(self.widget)
        self.mbtcp_host.setObjectName(u"mbtcp_host")
        self.mbtcp_host.setCursor(QCursor(Qt.IBeamCursor))

        self.gridLayout_5.addWidget(self.mbtcp_host, 1, 1, 1, 1)

        self.mbtcp_tcp_timeout_default = QPushButton(self.widget)
        self.mbtcp_tcp_timeout_default.setObjectName(u"mbtcp_tcp_timeout_default")

        self.gridLayout_5.addWidget(self.mbtcp_tcp_timeout_default, 3, 2, 1, 1)

        self.mbtcp_connections = QSpinBox(self.widget)
        self.mbtcp_connections.setObjectName(u"mbtcp_connections")
        self.mbtcp_connections.setMinimum(1)
        self.mbtcp_connections.setMaximum(1024)

        self.gridLayout_5.addWidget(self.mbtcp_connections, 5, 1, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.mbtcp_reconnect = QCheckBox(self.widget)
        self.mbtcp_reconnect.setObjectName(u"mbtcp_reconnect")
        self.mbtcp_reconnect.setChecked(True)

        self.gridLayout_5.addWidget(self.mbtcp_reconnect, 6, 1, 1, 1)

        self.mbtcp_nw_flags_default = QPushButton(self.widget)
        self.mbtcp_nw_flags_default.setObjectName(u"mbtcp_nw_flags_default")

        self.gridLayout_5.addWidget(self.mbtcp_nw_flags_default, 6, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 1, 0, 1, 1)

        self.widget_9 = QWidget(self.mbtcp_settings_content)
        self.widget_9.setObjectName(u"widget_9")
        self.gridLayout_13 = QGridLayout(self.widget_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.mbtcp_byte_timeout = QDoubleSpinBox(self.widget_9)
        self.mbtcp_byte_timeout.setObjectName(u"mbtcp_byte_timeout")
        self.mbtcp_byte_timeout.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.mbtcp_byte_timeout.sizePolicy().hasHeightForWidth())
        self.mbtcp_byte_timeout.setSizePolicy(sizePolicy1)
        self.mbtcp_byte_timeout.setMaximum(86400.000000000000000)

        self.gridLayout_13.addWidget(self.mbtcp_byte_timeout, 0, 1, 1, 1)

        self.label_17 = QLabel(self.widget_9)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_17, 1, 0, 1, 1)

        self.mbtcp_response_timeout = QDoubleSpinBox(self.widget_9)
        self.mbtcp_response_timeout.setObjectName(u"mbtcp_response_timeout")
        self.mbtcp_response_timeout.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.mbtcp_response_timeout.sizePolicy().hasHeightForWidth())
        self.mbtcp_response_timeout.setSizePolicy(sizePolicy1)
        self.mbtcp_response_timeout.setMinimum(0.000000000000000)
        self.mbtcp_response_timeout.setMaximum(86400.000000000000000)
        self.mbtcp_response_timeout.setValue(0.000000000000000)

        self.gridLayout_13.addWidget(self.mbtcp_response_timeout, 1, 1, 1, 1)

        self.label_16 = QLabel(self.widget_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(80, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_15, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_9, 13, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 18, 0, 1, 1)

        self.widget_8 = QWidget(self.mbtcp_settings_content)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.gridLayout_12 = QGridLayout(self.widget_8)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.mbtcp_monitor = QCheckBox(self.widget_8)
        self.mbtcp_monitor.setObjectName(u"mbtcp_monitor")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mbtcp_monitor.sizePolicy().hasHeightForWidth())
        self.mbtcp_monitor.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(9)
        self.mbtcp_monitor.setFont(font1)

        self.gridLayout_12.addWidget(self.mbtcp_monitor, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.mbtcp_enable_byte_timeout = QCheckBox(self.widget_8)
        self.mbtcp_enable_byte_timeout.setObjectName(u"mbtcp_enable_byte_timeout")

        self.gridLayout_12.addWidget(self.mbtcp_enable_byte_timeout, 0, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_8, 0, 4, 1, 1)

        self.mbtcp_enable_response_timeout = QCheckBox(self.widget_8)
        self.mbtcp_enable_response_timeout.setObjectName(u"mbtcp_enable_response_timeout")
        sizePolicy1.setHeightForWidth(self.mbtcp_enable_response_timeout.sizePolicy().hasHeightForWidth())
        self.mbtcp_enable_response_timeout.setSizePolicy(sizePolicy1)

        self.gridLayout_12.addWidget(self.mbtcp_enable_response_timeout, 0, 5, 1, 1)

        self.mbtcp_mb_flags_default = QPushButton(self.widget_8)
        self.mbtcp_mb_flags_default.setObjectName(u"mbtcp_mb_flags_default")

        self.gridLayout_12.addWidget(self.mbtcp_mb_flags_default, 0, 6, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget_8, 12, 0, 1, 1)

        self.widget_6 = QWidget(self.mbtcp_settings_content)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_10 = QGridLayout(self.widget_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_14 = QLabel(self.widget_6)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 1)

        self.mbtcp_sem_name = QLineEdit(self.widget_6)
        self.mbtcp_sem_name.setObjectName(u"mbtcp_sem_name")

        self.gridLayout_10.addWidget(self.mbtcp_sem_name, 0, 1, 1, 1)

        self.mbtcp_sem_name_default = QPushButton(self.widget_6)
        self.mbtcp_sem_name_default.setObjectName(u"mbtcp_sem_name_default")

        self.gridLayout_10.addWidget(self.mbtcp_sem_name_default, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_6, 17, 0, 1, 1)

        self.widget_3 = QWidget(self.mbtcp_settings_content)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_7 = QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 3, 1, 1)

        self.mbtcp_force = QCheckBox(self.widget_3)
        self.mbtcp_force.setObjectName(u"mbtcp_force")
        sizePolicy2.setHeightForWidth(self.mbtcp_force.sizePolicy().hasHeightForWidth())
        self.mbtcp_force.setSizePolicy(sizePolicy2)

        self.gridLayout_7.addWidget(self.mbtcp_force, 0, 2, 1, 1)

        self.mbtcp_separate = QCheckBox(self.widget_3)
        self.mbtcp_separate.setObjectName(u"mbtcp_separate")

        self.gridLayout_7.addWidget(self.mbtcp_separate, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 5, 1, 1)

        self.mbtcp_separate_all = QCheckBox(self.widget_3)
        self.mbtcp_separate_all.setObjectName(u"mbtcp_separate_all")
        self.mbtcp_separate_all.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.mbtcp_separate_all.sizePolicy().hasHeightForWidth())
        self.mbtcp_separate_all.setSizePolicy(sizePolicy1)

        self.gridLayout_7.addWidget(self.mbtcp_separate_all, 0, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.mbtcp_shm_defaults = QPushButton(self.widget_3)
        self.mbtcp_shm_defaults.setObjectName(u"mbtcp_shm_defaults")

        self.gridLayout_7.addWidget(self.mbtcp_shm_defaults, 0, 7, 1, 1)


        self.gridLayout_4.addWidget(self.widget_3, 7, 0, 1, 1)

        self.line_3 = QFrame(self.mbtcp_settings_content)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_3, 10, 0, 1, 1)

        self.line = QFrame(self.mbtcp_settings_content)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line, 2, 0, 1, 1)

        self.line_4 = QFrame(self.mbtcp_settings_content)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_4, 14, 0, 1, 1)

        self.widget_4 = QWidget(self.mbtcp_settings_content)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_8 = QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)

        self.mbtcp_name_prefix = QLineEdit(self.widget_4)
        self.mbtcp_name_prefix.setObjectName(u"mbtcp_name_prefix")

        self.gridLayout_8.addWidget(self.mbtcp_name_prefix, 0, 1, 1, 1)

        self.mbtcp_name_default = QPushButton(self.widget_4)
        self.mbtcp_name_default.setObjectName(u"mbtcp_name_default")

        self.gridLayout_8.addWidget(self.mbtcp_name_default, 0, 2, 1, 1)

        self.label_12 = QLabel(self.widget_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1)

        self.mbtcp_separate_list = QLineEdit(self.widget_4)
        self.mbtcp_separate_list.setObjectName(u"mbtcp_separate_list")
        self.mbtcp_separate_list.setEnabled(False)

        self.gridLayout_8.addWidget(self.mbtcp_separate_list, 1, 1, 1, 1)

        self.mbtcp_separate_list_clear = QPushButton(self.widget_4)
        self.mbtcp_separate_list_clear.setObjectName(u"mbtcp_separate_list_clear")

        self.gridLayout_8.addWidget(self.mbtcp_separate_list_clear, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_4, 9, 0, 1, 1)

        self.label_4 = QLabel(self.mbtcp_settings_content)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_15 = QLabel(self.mbtcp_settings_content)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.gridLayout_4.addWidget(self.label_15, 11, 0, 1, 1)

        self.line_2 = QFrame(self.mbtcp_settings_content)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 5, 0, 1, 1)

        self.widget_2 = QWidget(self.mbtcp_settings_content)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_6 = QGridLayout(self.widget_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_6 = QLabel(self.widget_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.mbtcp_ao = QSpinBox(self.widget_2)
        self.mbtcp_ao.setObjectName(u"mbtcp_ao")
        sizePolicy1.setHeightForWidth(self.mbtcp_ao.sizePolicy().hasHeightForWidth())
        self.mbtcp_ao.setSizePolicy(sizePolicy1)
        self.mbtcp_ao.setMinimum(1)
        self.mbtcp_ao.setMaximum(65536)
        self.mbtcp_ao.setValue(65536)

        self.gridLayout_6.addWidget(self.mbtcp_ao, 2, 1, 1, 1)

        self.mbtcp_ai = QSpinBox(self.widget_2)
        self.mbtcp_ai.setObjectName(u"mbtcp_ai")
        sizePolicy1.setHeightForWidth(self.mbtcp_ai.sizePolicy().hasHeightForWidth())
        self.mbtcp_ai.setSizePolicy(sizePolicy1)
        self.mbtcp_ai.setMinimum(1)
        self.mbtcp_ai.setMaximum(65536)
        self.mbtcp_ai.setValue(65536)

        self.gridLayout_6.addWidget(self.mbtcp_ai, 3, 1, 1, 1)

        self.mbtcp_do = QSpinBox(self.widget_2)
        self.mbtcp_do.setObjectName(u"mbtcp_do")
        sizePolicy1.setHeightForWidth(self.mbtcp_do.sizePolicy().hasHeightForWidth())
        self.mbtcp_do.setSizePolicy(sizePolicy1)
        self.mbtcp_do.setMinimum(1)
        self.mbtcp_do.setMaximum(65536)
        self.mbtcp_do.setValue(65536)

        self.gridLayout_6.addWidget(self.mbtcp_do, 0, 1, 1, 1)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.mbtcp_di = QSpinBox(self.widget_2)
        self.mbtcp_di.setObjectName(u"mbtcp_di")
        sizePolicy1.setHeightForWidth(self.mbtcp_di.sizePolicy().hasHeightForWidth())
        self.mbtcp_di.setSizePolicy(sizePolicy1)
        self.mbtcp_di.setMinimum(1)
        self.mbtcp_di.setMaximum(65536)
        self.mbtcp_di.setValue(65536)

        self.gridLayout_6.addWidget(self.mbtcp_di, 1, 1, 1, 1)

        self.mbtcp_do_default = QPushButton(self.widget_2)
        self.mbtcp_do_default.setObjectName(u"mbtcp_do_default")
        sizePolicy2.setHeightForWidth(self.mbtcp_do_default.sizePolicy().hasHeightForWidth())
        self.mbtcp_do_default.setSizePolicy(sizePolicy2)
        self.mbtcp_do_default.setMinimumSize(QSize(0, 0))
        self.mbtcp_do_default.setMaximumSize(QSize(16777215, 16777215))
        self.mbtcp_do_default.setIconSize(QSize(16, 16))

        self.gridLayout_6.addWidget(self.mbtcp_do_default, 0, 2, 1, 1)

        self.mbtcp_di_default = QPushButton(self.widget_2)
        self.mbtcp_di_default.setObjectName(u"mbtcp_di_default")
        self.mbtcp_di_default.setMinimumSize(QSize(0, 0))
        self.mbtcp_di_default.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.mbtcp_di_default, 1, 2, 1, 1)

        self.mbtcp_ao_default = QPushButton(self.widget_2)
        self.mbtcp_ao_default.setObjectName(u"mbtcp_ao_default")
        self.mbtcp_ao_default.setMinimumSize(QSize(0, 0))
        self.mbtcp_ao_default.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.mbtcp_ao_default, 2, 2, 1, 1)

        self.mbtcp_ai_default = QPushButton(self.widget_2)
        self.mbtcp_ai_default.setObjectName(u"mbtcp_ai_default")
        self.mbtcp_ai_default.setMinimumSize(QSize(0, 0))
        self.mbtcp_ai_default.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_6.addWidget(self.mbtcp_ai_default, 3, 2, 1, 1)


        self.gridLayout_4.addWidget(self.widget_2, 4, 0, 1, 1)

        self.label_13 = QLabel(self.mbtcp_settings_content)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.gridLayout_4.addWidget(self.label_13, 15, 0, 1, 1)

        self.label = QLabel(self.mbtcp_settings_content)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setUnderline(False)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.mbtcp_settings.setWidget(self.mbtcp_settings_content)

        self.gridLayout_3.addWidget(self.mbtcp_settings, 12, 3, 1, 1)

        self.tabWidget_modbus_clients.addTab(self.tab_mbtcp, "")
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
        self.mbrtu_settings.setGeometry(QRect(0, 0, 519, 1025))
        self.gridLayout_15 = QGridLayout(self.mbrtu_settings)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.line_5 = QFrame(self.mbrtu_settings)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_15.addWidget(self.line_5, 2, 0, 1, 1)

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

        self.label_18 = QLabel(self.mbrtu_settings)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_15.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_25 = QLabel(self.mbrtu_settings)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_15.addWidget(self.label_25, 3, 0, 1, 1)

        self.label_32 = QLabel(self.mbrtu_settings)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_15.addWidget(self.label_32, 11, 0, 1, 1)

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

        self.mbrtu_byte_timeout = QDoubleSpinBox(self.widget_15)
        self.mbrtu_byte_timeout.setObjectName(u"mbrtu_byte_timeout")
        self.mbrtu_byte_timeout.setMaximum(86400.000000000000000)

        self.gridLayout_21.addWidget(self.mbrtu_byte_timeout, 1, 1, 1, 1)

        self.mbrtu_response_timeout = QDoubleSpinBox(self.widget_15)
        self.mbrtu_response_timeout.setObjectName(u"mbrtu_response_timeout")
        self.mbrtu_response_timeout.setMaximum(86400.000000000000000)

        self.gridLayout_21.addWidget(self.mbrtu_response_timeout, 2, 1, 1, 1)

        self.label_36 = QLabel(self.widget_15)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_36, 1, 0, 1, 1)

        self.label_37 = QLabel(self.widget_15)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_37, 2, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_15, 14, 0, 1, 1)

        self.widget_12 = QWidget(self.mbrtu_settings)
        self.widget_12.setObjectName(u"widget_12")
        self.gridLayout_18 = QGridLayout(self.widget_12)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.mbrtu_force = QCheckBox(self.widget_12)
        self.mbrtu_force.setObjectName(u"mbrtu_force")
        sizePolicy1.setHeightForWidth(self.mbrtu_force.sizePolicy().hasHeightForWidth())
        self.mbrtu_force.setSizePolicy(sizePolicy1)

        self.gridLayout_18.addWidget(self.mbrtu_force, 0, 1, 1, 1)

        self.mbrtu_shm_flags_default = QPushButton(self.widget_12)
        self.mbrtu_shm_flags_default.setObjectName(u"mbrtu_shm_flags_default")

        self.gridLayout_18.addWidget(self.mbrtu_shm_flags_default, 0, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_12, 8, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_2, 5, 0, 1, 1)

        self.line_8 = QFrame(self.mbrtu_settings)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_15.addWidget(self.line_8, 15, 0, 1, 1)

        self.widget_11 = QWidget(self.mbrtu_settings)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_17 = QGridLayout(self.widget_11)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.mbrtu_ao = QSpinBox(self.widget_11)
        self.mbrtu_ao.setObjectName(u"mbrtu_ao")
        sizePolicy1.setHeightForWidth(self.mbrtu_ao.sizePolicy().hasHeightForWidth())
        self.mbrtu_ao.setSizePolicy(sizePolicy1)
        self.mbrtu_ao.setMinimum(1)
        self.mbrtu_ao.setMaximum(65536)
        self.mbrtu_ao.setValue(65536)

        self.gridLayout_17.addWidget(self.mbrtu_ao, 2, 1, 1, 1)

        self.label_28 = QLabel(self.widget_11)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_28, 2, 0, 1, 1)

        self.mbrtu_ai = QSpinBox(self.widget_11)
        self.mbrtu_ai.setObjectName(u"mbrtu_ai")
        sizePolicy1.setHeightForWidth(self.mbrtu_ai.sizePolicy().hasHeightForWidth())
        self.mbrtu_ai.setSizePolicy(sizePolicy1)
        self.mbrtu_ai.setMinimum(1)
        self.mbrtu_ai.setMaximum(65536)
        self.mbrtu_ai.setValue(65536)

        self.gridLayout_17.addWidget(self.mbrtu_ai, 3, 1, 1, 1)

        self.label_29 = QLabel(self.widget_11)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_29, 3, 0, 1, 1)

        self.mbrtu_di = QSpinBox(self.widget_11)
        self.mbrtu_di.setObjectName(u"mbrtu_di")
        sizePolicy1.setHeightForWidth(self.mbrtu_di.sizePolicy().hasHeightForWidth())
        self.mbrtu_di.setSizePolicy(sizePolicy1)
        self.mbrtu_di.setMinimum(1)
        self.mbrtu_di.setMaximum(65536)
        self.mbrtu_di.setValue(65536)

        self.gridLayout_17.addWidget(self.mbrtu_di, 1, 1, 1, 1)

        self.label_27 = QLabel(self.widget_11)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_27, 1, 0, 1, 1)

        self.label_26 = QLabel(self.widget_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_26, 0, 0, 1, 1)

        self.mbrtu_do = QSpinBox(self.widget_11)
        self.mbrtu_do.setObjectName(u"mbrtu_do")
        sizePolicy1.setHeightForWidth(self.mbrtu_do.sizePolicy().hasHeightForWidth())
        self.mbrtu_do.setSizePolicy(sizePolicy1)
        self.mbrtu_do.setMinimum(1)
        self.mbrtu_do.setMaximum(65536)
        self.mbrtu_do.setValue(65536)

        self.gridLayout_17.addWidget(self.mbrtu_do, 0, 1, 1, 1)

        self.mbtru_do_default = QPushButton(self.widget_11)
        self.mbtru_do_default.setObjectName(u"mbtru_do_default")

        self.gridLayout_17.addWidget(self.mbtru_do_default, 0, 2, 1, 1)

        self.mbrtu_di_default = QPushButton(self.widget_11)
        self.mbrtu_di_default.setObjectName(u"mbrtu_di_default")

        self.gridLayout_17.addWidget(self.mbrtu_di_default, 1, 2, 1, 1)

        self.mbrtu_ao_default = QPushButton(self.widget_11)
        self.mbrtu_ao_default.setObjectName(u"mbrtu_ao_default")

        self.gridLayout_17.addWidget(self.mbrtu_ao_default, 2, 2, 1, 1)

        self.mbrtu_ai_default = QPushButton(self.widget_11)
        self.mbrtu_ai_default.setObjectName(u"mbrtu_ai_default")

        self.gridLayout_17.addWidget(self.mbrtu_ai_default, 3, 2, 1, 1)


        self.gridLayout_15.addWidget(self.widget_11, 4, 0, 1, 1)

        self.label_34 = QLabel(self.mbrtu_settings)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font)

        self.gridLayout_15.addWidget(self.label_34, 16, 0, 1, 1)

        self.widget_13 = QWidget(self.mbrtu_settings)
        self.widget_13.setObjectName(u"widget_13")
        self.gridLayout_19 = QGridLayout(self.widget_13)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.mbrtu_shm_name_default = QPushButton(self.widget_13)
        self.mbrtu_shm_name_default.setObjectName(u"mbrtu_shm_name_default")

        self.gridLayout_19.addWidget(self.mbrtu_shm_name_default, 0, 2, 1, 1)

        self.mbrtu_shm_name = QLineEdit(self.widget_13)
        self.mbrtu_shm_name.setObjectName(u"mbrtu_shm_name")

        self.gridLayout_19.addWidget(self.mbrtu_shm_name, 0, 1, 1, 1)

        self.label_31 = QLabel(self.widget_13)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_19.addWidget(self.label_31, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.widget_13, 9, 0, 1, 1)

        self.widget_14 = QWidget(self.mbrtu_settings)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_20 = QGridLayout(self.widget_14)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.mbrtu_enable_byte_timeout = QCheckBox(self.widget_14)
        self.mbrtu_enable_byte_timeout.setObjectName(u"mbrtu_enable_byte_timeout")

        self.gridLayout_20.addWidget(self.mbrtu_enable_byte_timeout, 0, 3, 1, 1)

        self.mbrtu_modbus_flags_default = QPushButton(self.widget_14)
        self.mbrtu_modbus_flags_default.setObjectName(u"mbrtu_modbus_flags_default")

        self.gridLayout_20.addWidget(self.mbrtu_modbus_flags_default, 0, 6, 1, 1)

        self.mbrtu_monitor = QCheckBox(self.widget_14)
        self.mbrtu_monitor.setObjectName(u"mbrtu_monitor")
        sizePolicy2.setHeightForWidth(self.mbrtu_monitor.sizePolicy().hasHeightForWidth())
        self.mbrtu_monitor.setSizePolicy(sizePolicy2)

        self.gridLayout_20.addWidget(self.mbrtu_monitor, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)

        self.mbrtu_enable_response_timeout = QCheckBox(self.widget_14)
        self.mbrtu_enable_response_timeout.setObjectName(u"mbrtu_enable_response_timeout")
        sizePolicy1.setHeightForWidth(self.mbrtu_enable_response_timeout.sizePolicy().hasHeightForWidth())
        self.mbrtu_enable_response_timeout.setSizePolicy(sizePolicy1)

        self.gridLayout_20.addWidget(self.mbrtu_enable_response_timeout, 0, 5, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_14, 0, 4, 1, 1)


        self.gridLayout_15.addWidget(self.widget_14, 13, 0, 1, 1)

        self.line_6 = QFrame(self.mbrtu_settings)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_15.addWidget(self.line_6, 6, 0, 1, 1)

        self.line_7 = QFrame(self.mbrtu_settings)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_15.addWidget(self.line_7, 10, 0, 1, 1)

        self.widget_16 = QWidget(self.mbrtu_settings)
        self.widget_16.setObjectName(u"widget_16")
        self.gridLayout_22 = QGridLayout(self.widget_16)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.mbrtu_sem_force = QCheckBox(self.widget_16)
        self.mbrtu_sem_force.setObjectName(u"mbrtu_sem_force")
        sizePolicy1.setHeightForWidth(self.mbrtu_sem_force.sizePolicy().hasHeightForWidth())
        self.mbrtu_sem_force.setSizePolicy(sizePolicy1)

        self.gridLayout_22.addWidget(self.mbrtu_sem_force, 0, 3, 1, 1)

        self.mbrtu_sem_enable = QCheckBox(self.widget_16)
        self.mbrtu_sem_enable.setObjectName(u"mbrtu_sem_enable")

        self.gridLayout_22.addWidget(self.mbrtu_sem_enable, 0, 1, 1, 1)

        self.mbtru_sem_flags_default = QPushButton(self.widget_16)
        self.mbtru_sem_flags_default.setObjectName(u"mbtru_sem_flags_default")

        self.gridLayout_22.addWidget(self.mbtru_sem_flags_default, 0, 4, 1, 1)


        self.gridLayout_15.addWidget(self.widget_16, 17, 0, 1, 1)

        self.label_30 = QLabel(self.mbrtu_settings)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font)
        self.label_30.setToolTipDuration(-1)
        self.label_30.setFrameShadow(QFrame.Plain)
        self.label_30.setLineWidth(1)

        self.gridLayout_15.addWidget(self.label_30, 7, 0, 1, 1)

        self.widget_18 = QWidget(self.mbrtu_settings)
        self.widget_18.setObjectName(u"widget_18")
        self.gridLayout_24 = QGridLayout(self.widget_18)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.label_35 = QLabel(self.widget_18)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_24.addWidget(self.label_35, 0, 0, 1, 1)

        self.mbrtu_sem_name = QLineEdit(self.widget_18)
        self.mbrtu_sem_name.setObjectName(u"mbrtu_sem_name")

        self.gridLayout_24.addWidget(self.mbrtu_sem_name, 0, 1, 1, 1)

        self.mbrtu_sem_name_default = QPushButton(self.widget_18)
        self.mbrtu_sem_name_default.setObjectName(u"mbrtu_sem_name_default")

        self.gridLayout_24.addWidget(self.mbrtu_sem_name_default, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.widget_18, 18, 0, 1, 1)

        self.scrollArea_2.setWidget(self.mbrtu_settings)

        self.gridLayout_14.addWidget(self.scrollArea_2, 1, 0, 1, 1)

        self.tabWidget_modbus_clients.addTab(self.tab_mbrtu, "")

        self.gridLayout_2.addWidget(self.tabWidget_modbus_clients, 0, 0, 1, 1)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 238, 447))
        self.gridLayout_26 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.line_9 = QFrame(self.scrollAreaWidgetContents)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setEnabled(True)
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_26.addWidget(self.line_9, 1, 0, 1, 1)

        self.widget_19 = QWidget(self.scrollAreaWidgetContents)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setEnabled(True)
        self.gridLayout_27 = QGridLayout(self.widget_19)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.tool_set_values = QPushButton(self.widget_19)
        self.tool_set_values.setObjectName(u"tool_set_values")
        self.tool_set_values.setEnabled(True)

        self.gridLayout_27.addWidget(self.tool_set_values, 0, 0, 1, 1)


        self.gridLayout_26.addWidget(self.widget_19, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_3, 7, 0, 1, 1)

        self.line_10 = QFrame(self.scrollAreaWidgetContents)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setEnabled(True)
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.gridLayout_26.addWidget(self.line_10, 3, 0, 1, 1)

        self.line_11 = QFrame(self.scrollAreaWidgetContents)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.gridLayout_26.addWidget(self.line_11, 5, 0, 1, 1)

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


        self.gridLayout_26.addWidget(self.widget_21, 4, 0, 1, 1)

        self.widget_20 = QWidget(self.scrollAreaWidgetContents)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setEnabled(True)
        self.gridLayout_28 = QGridLayout(self.widget_20)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.tool_dump_ao = QPushButton(self.widget_20)
        self.tool_dump_ao.setObjectName(u"tool_dump_ao")
        self.tool_dump_ao.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_ao, 2, 0, 1, 1)

        self.tool_dump_ai = QPushButton(self.widget_20)
        self.tool_dump_ai.setObjectName(u"tool_dump_ai")
        self.tool_dump_ai.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_ai, 3, 0, 1, 1)

        self.tool_dump_do = QPushButton(self.widget_20)
        self.tool_dump_do.setObjectName(u"tool_dump_do")
        self.tool_dump_do.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_do, 0, 0, 1, 1)

        self.tool_dump_ao_file = QLineEdit(self.widget_20)
        self.tool_dump_ao_file.setObjectName(u"tool_dump_ao_file")

        self.gridLayout_28.addWidget(self.tool_dump_ao_file, 2, 1, 1, 1)

        self.tool_dump_do_file = QLineEdit(self.widget_20)
        self.tool_dump_do_file.setObjectName(u"tool_dump_do_file")

        self.gridLayout_28.addWidget(self.tool_dump_do_file, 0, 1, 1, 1)

        self.tool_dump_di = QPushButton(self.widget_20)
        self.tool_dump_di.setObjectName(u"tool_dump_di")
        self.tool_dump_di.setEnabled(True)

        self.gridLayout_28.addWidget(self.tool_dump_di, 1, 0, 1, 1)

        self.tool_dump_ai_file = QLineEdit(self.widget_20)
        self.tool_dump_ai_file.setObjectName(u"tool_dump_ai_file")

        self.gridLayout_28.addWidget(self.tool_dump_ai_file, 3, 1, 1, 1)

        self.tool_dump_di_file = QLineEdit(self.widget_20)
        self.tool_dump_di_file.setObjectName(u"tool_dump_di_file")

        self.gridLayout_28.addWidget(self.tool_dump_di_file, 1, 1, 1, 1)

        self.tool_dump_ai_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_ai_file_dialog.setObjectName(u"tool_dump_ai_file_dialog")
        icon = QIcon()
        iconThemeName = u"document-open"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.tool_dump_ai_file_dialog.setIcon(icon)

        self.gridLayout_28.addWidget(self.tool_dump_ai_file_dialog, 3, 2, 1, 1)

        self.tool_dump_ao_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_ao_file_dialog.setObjectName(u"tool_dump_ao_file_dialog")
        self.tool_dump_ao_file_dialog.setIcon(icon)

        self.gridLayout_28.addWidget(self.tool_dump_ao_file_dialog, 2, 2, 1, 1)

        self.tool_dump_di_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_di_file_dialog.setObjectName(u"tool_dump_di_file_dialog")
        self.tool_dump_di_file_dialog.setIcon(icon)

        self.gridLayout_28.addWidget(self.tool_dump_di_file_dialog, 1, 2, 1, 1)

        self.tool_dump_do_file_dialog = QToolButton(self.widget_20)
        self.tool_dump_do_file_dialog.setObjectName(u"tool_dump_do_file_dialog")
        self.tool_dump_do_file_dialog.setIcon(icon)

        self.gridLayout_28.addWidget(self.tool_dump_do_file_dialog, 0, 2, 1, 1)


        self.gridLayout_26.addWidget(self.widget_20, 2, 0, 1, 1)

        self.random_ai = QWidget(self.scrollAreaWidgetContents)
        self.random_ai.setObjectName(u"random_ai")
        self.gridLayout_30 = QGridLayout(self.random_ai)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.tool_random_ao = QPushButton(self.random_ai)
        self.tool_random_ao.setObjectName(u"tool_random_ao")

        self.gridLayout_30.addWidget(self.tool_random_ao, 0, 1, 1, 1)

        self.tool_random_do = QPushButton(self.random_ai)
        self.tool_random_do.setObjectName(u"tool_random_do")

        self.gridLayout_30.addWidget(self.tool_random_do, 0, 0, 1, 1)

        self.tool_random_di = QPushButton(self.random_ai)
        self.tool_random_di.setObjectName(u"tool_random_di")

        self.gridLayout_30.addWidget(self.tool_random_di, 1, 0, 1, 1)

        self.tool_random_ai = QPushButton(self.random_ai)
        self.tool_random_ai.setObjectName(u"tool_random_ai")

        self.gridLayout_30.addWidget(self.tool_random_ai, 1, 1, 1, 1)


        self.gridLayout_26.addWidget(self.random_ai, 6, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_25.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.tabWidget_tools.addTab(self.tab_shm_tools, "")

        self.gridLayout.addWidget(self.tabWidget_tools, 0, 0, 1, 1)

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
        self.menuFile.addAction(self.actionopen_modbus_tcp_client_config)
        self.menuFile.addAction(self.actionopen_modbus_rtu_client_config)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionsave_modbus_tcp_client_config)
        self.menuFile.addAction(self.actionsave_modbus_rtu_client_config)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabWidget_tools.setCurrentIndex(0)
        self.tabWidget_modbus_clients.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SHM Modbus", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionsave_modbus_tcp_client_config.setText(QCoreApplication.translate("MainWindow", u"save modbus tcp client config", None))
        self.actionsave_modbus_rtu_client_config.setText(QCoreApplication.translate("MainWindow", u"save modbus rtu client config", None))
        self.actionopen_modbus_tcp_client_config.setText(QCoreApplication.translate("MainWindow", u"open modbus tcp client config", None))
        self.actionopen_modbus_rtu_client_config.setText(QCoreApplication.translate("MainWindow", u"open modbus rtu client config", None))
        self.mbtcp_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.mbtcp_defaults.setText(QCoreApplication.translate("MainWindow", u"Defaults", None))
        self.mbtcp_sem_force.setText(QCoreApplication.translate("MainWindow", u"force", None))
        self.mbtcp_sem_enable.setText(QCoreApplication.translate("MainWindow", u"enable", None))
        self.mbtcp_sem_defaults.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Shared Memory", None))
        self.mbtcp_host_default.setText(QCoreApplication.translate("MainWindow", u"any", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"connections:", None))
        self.mbtcp_port_default.setText(QCoreApplication.translate("MainWindow", u"502", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"port", None))
        self.mbtcp_sytstem_tcp_timeout.setText(QCoreApplication.translate("MainWindow", u"use system TCP timeout", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TCP timeout:", None))
        self.mbtcp_connections_default.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.mbtcp_host.setText(QCoreApplication.translate("MainWindow", u"any", None))
        self.mbtcp_tcp_timeout_default.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"host:", None))
        self.mbtcp_reconnect.setText(QCoreApplication.translate("MainWindow", u"reconnect", None))
        self.mbtcp_nw_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"response timeout:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"byte timeout:", None))
        self.mbtcp_monitor.setText(QCoreApplication.translate("MainWindow", u"monitor", None))
        self.mbtcp_enable_byte_timeout.setText(QCoreApplication.translate("MainWindow", u"edit byte timeout", None))
        self.mbtcp_enable_response_timeout.setText(QCoreApplication.translate("MainWindow", u"edit response timeout", None))
        self.mbtcp_mb_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"name:", None))
        self.mbtcp_sem_name.setText(QCoreApplication.translate("MainWindow", u"modbus", None))
        self.mbtcp_sem_name_default.setText(QCoreApplication.translate("MainWindow", u"modbus", None))
        self.mbtcp_force.setText(QCoreApplication.translate("MainWindow", u"force", None))
        self.mbtcp_separate.setText(QCoreApplication.translate("MainWindow", u"separate", None))
        self.mbtcp_separate_all.setText(QCoreApplication.translate("MainWindow", u"separate-all", None))
        self.mbtcp_shm_defaults.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"name prefix:", None))
        self.mbtcp_name_prefix.setText(QCoreApplication.translate("MainWindow", u"modbus_", None))
        self.mbtcp_name_default.setText(QCoreApplication.translate("MainWindow", u"modbus_", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"separate:", None))
        self.mbtcp_separate_list_clear.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Registers", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Modbus", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"AO:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"AI:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DI:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DO:", None))
        self.mbtcp_do_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.mbtcp_di_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.mbtcp_ao_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.mbtcp_ai_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Semaphore", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.tabWidget_modbus_clients.setTabText(self.tabWidget_modbus_clients.indexOf(self.tab_mbtcp), QCoreApplication.translate("MainWindow", u"TCP", None))
        self.mbrtu_start.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.mbrtu_defaults.setText(QCoreApplication.translate("MainWindow", u"Defaults", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"baud rate:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"device:", None))
        self.mbrtu_stopbits_default.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"stop bits:", None))
        self.mbrtu_databits_default.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.mbrtu_baudrate.setText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"parity:", None))
        self.mbrtu_parity_default.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.mbrtu_baudrate_default.setText(QCoreApplication.translate("MainWindow", u"115200", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"data bits:", None))
        self.mbrtu_parity.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.mbrtu_parity.setItemText(1, QCoreApplication.translate("MainWindow", u"Even", None))
        self.mbrtu_parity.setItemText(2, QCoreApplication.translate("MainWindow", u"Odd", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"type:", None))
        self.mbrtu_serialtype.setItemText(0, QCoreApplication.translate("MainWindow", u"rs232", None))
        self.mbrtu_serialtype.setItemText(1, QCoreApplication.translate("MainWindow", u"rs485", None))

        self.mbrtu_serialtype_default.setText(QCoreApplication.translate("MainWindow", u"rs232", None))
        self.mbrtu_device_default.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Serial", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Registers", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Modbus", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"client id:", None))
        self.mbrtu_clientid_default.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"byte timeout:", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"response timeout:", None))
        self.mbrtu_force.setText(QCoreApplication.translate("MainWindow", u"force", None))
        self.mbrtu_shm_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"AO:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"AI:", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"DI:", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"DO:", None))
        self.mbtru_do_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.mbrtu_di_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.mbrtu_ao_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.mbrtu_ai_default.setText(QCoreApplication.translate("MainWindow", u"65536", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Semaphore (not yet supported)", None))
        self.mbrtu_shm_name_default.setText(QCoreApplication.translate("MainWindow", u"modbus_", None))
        self.mbrtu_shm_name.setText(QCoreApplication.translate("MainWindow", u"modbus_", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"name prefix:", None))
        self.mbrtu_enable_byte_timeout.setText(QCoreApplication.translate("MainWindow", u"edit byte timeout", None))
        self.mbrtu_modbus_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.mbrtu_monitor.setText(QCoreApplication.translate("MainWindow", u"monitor", None))
        self.mbrtu_enable_response_timeout.setText(QCoreApplication.translate("MainWindow", u"edit response timeout", None))
        self.mbrtu_sem_force.setText(QCoreApplication.translate("MainWindow", u"force", None))
        self.mbrtu_sem_enable.setText(QCoreApplication.translate("MainWindow", u"enable", None))
        self.mbtru_sem_flags_default.setText(QCoreApplication.translate("MainWindow", u"defaults", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Shared Memory", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"name:", None))
        self.mbrtu_sem_name.setText(QCoreApplication.translate("MainWindow", u"modbus", None))
        self.mbrtu_sem_name_default.setText(QCoreApplication.translate("MainWindow", u"modbus", None))
        self.tabWidget_modbus_clients.setTabText(self.tabWidget_modbus_clients.indexOf(self.tab_mbrtu), QCoreApplication.translate("MainWindow", u"RTU", None))
        self.tabWidget_tools.setTabText(self.tabWidget_tools.indexOf(self.tab_modbus_clients), QCoreApplication.translate("MainWindow", u"Modbus Clients", None))
        self.tool_set_values.setText(QCoreApplication.translate("MainWindow", u"set values", None))
        self.tool_hexdump_ai.setText(QCoreApplication.translate("MainWindow", u"hexdump AI", None))
        self.tool_hexdump_di.setText(QCoreApplication.translate("MainWindow", u"hexdump DI", None))
        self.tool_hexdump_do.setText(QCoreApplication.translate("MainWindow", u"hexdump DO", None))
        self.tool_hexdump_ao.setText(QCoreApplication.translate("MainWindow", u"hexdump AO", None))
        self.tool_dump_ao.setText(QCoreApplication.translate("MainWindow", u"dump AO to file", None))
        self.tool_dump_ai.setText(QCoreApplication.translate("MainWindow", u"dump AI to file", None))
        self.tool_dump_do.setText(QCoreApplication.translate("MainWindow", u"dump DO to file", None))
        self.tool_dump_ao_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_AO", None))
        self.tool_dump_do_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_DO", None))
        self.tool_dump_di.setText(QCoreApplication.translate("MainWindow", u"dump DI to file", None))
        self.tool_dump_ai_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_AI", None))
        self.tool_dump_di_file.setText(QCoreApplication.translate("MainWindow", u"/tmp/modbus_DI", None))
        self.tool_dump_ai_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tool_dump_ao_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tool_dump_di_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tool_dump_do_file_dialog.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.tool_random_ao.setText(QCoreApplication.translate("MainWindow", u"randomize AO", None))
        self.tool_random_do.setText(QCoreApplication.translate("MainWindow", u"randomize DO", None))
        self.tool_random_di.setText(QCoreApplication.translate("MainWindow", u"randomize DI", None))
        self.tool_random_ai.setText(QCoreApplication.translate("MainWindow", u"randomize AI", None))
        self.tabWidget_tools.setTabText(self.tabWidget_tools.indexOf(self.tab_shm_tools), QCoreApplication.translate("MainWindow", u"Shared Memory Tools", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

