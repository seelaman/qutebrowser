import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget)
from qutebrowser.widgets.statusbar import StatusBar
from qutebrowser.widgets.tabbar import TabWidget

class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName(self.__class__.__name__)

        self.cwidget = QWidget(self)
        self.cwidget.setObjectName("cwidget")
        self.setCentralWidget(self.cwidget)

        self.vbox = QVBoxLayout(self.cwidget)
        self.vbox.setObjectName("vbox")
        self.vbox.setContentsMargins(0, 0, 0, 0)
        self.vbox.setSpacing(0)

        self.tabs = TabWidget(self.cwidget)
        self.tabs.setObjectName("tabs")
        self.tab = QWidget()
        self.tab2 = QWidget()
        self.tab.setObjectName("tab")
        self.tab2.setObjectName("tab2")
        self.tabs.addTab(self.tab, "test")
        self.tabs.addTab(self.tab2, "test2")
        self.vbox.addWidget(self.tabs)

        self.status = StatusBar(self.cwidget)
        self.status.lbl.setText("Hello World")
        self.vbox.addWidget(self.status)

        #self.retranslateUi(MainWindow)
        #self.tabWidget.setCurrentIndex(0)
        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.show()

def main():
    app = QApplication(sys.argv)
    tw = TestWindow()
    sys.exit(app.exec_())
