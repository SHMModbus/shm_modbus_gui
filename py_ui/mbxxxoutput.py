# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mbxxxoutput.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QSplitter, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MBxxxOutput(object):
    def setupUi(self, MBxxxOutput):
        if not MBxxxOutput.objectName():
            MBxxxOutput.setObjectName(u"MBxxxOutput")
        MBxxxOutput.resize(800, 600)
        self.actionSave_STDOUT = QAction(MBxxxOutput)
        self.actionSave_STDOUT.setObjectName(u"actionSave_STDOUT")
        self.actionSave_STDERR = QAction(MBxxxOutput)
        self.actionSave_STDERR.setObjectName(u"actionSave_STDERR")
        self.centralwidget = QWidget(MBxxxOutput)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.stdout = QTextBrowser(self.splitter)
        self.stdout.setObjectName(u"stdout")
        self.stdout.setFocusPolicy(Qt.StrongFocus)
        self.stdout.setToolTipDuration(10)
        self.splitter.addWidget(self.stdout)
        self.stderr = QTextBrowser(self.splitter)
        self.stderr.setObjectName(u"stderr")
        self.splitter.addWidget(self.stderr)

        self.verticalLayout.addWidget(self.splitter)

        MBxxxOutput.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MBxxxOutput)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 30))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MBxxxOutput.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MBxxxOutput)
        self.statusbar.setObjectName(u"statusbar")
        MBxxxOutput.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionSave_STDOUT)
        self.menuFile.addAction(self.actionSave_STDERR)

        self.retranslateUi(MBxxxOutput)

        QMetaObject.connectSlotsByName(MBxxxOutput)
    # setupUi

    def retranslateUi(self, MBxxxOutput):
        MBxxxOutput.setWindowTitle(QCoreApplication.translate("MBxxxOutput", u"MainWindow", None))
        self.actionSave_STDOUT.setText(QCoreApplication.translate("MBxxxOutput", u"Save stdout", None))
        self.actionSave_STDERR.setText(QCoreApplication.translate("MBxxxOutput", u"Save stderr", None))
#if QT_CONFIG(tooltip)
        self.stdout.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.menuFile.setTitle(QCoreApplication.translate("MBxxxOutput", u"File", None))
    # retranslateUi

