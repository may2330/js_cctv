# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seulgi_3.ui',
# licensing of 'seulgi_3.ui' applies.
#
# Created: Tue Aug 27 14:12:21 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QMediaPlayer, QMediaPlaylist
from PySide2.QtMultimediaWidgets import QVideoWidget

import sys

class Ui_Logon(object):
    def setupUi(self, Logon):
        Logon.setObjectName("Logon")
        Logon.resize(714, 533)

        self.horizontalLayoutWidget = QtWidgets.QWidget(Logon)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 711, 531))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.h_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.h_layout.setContentsMargins(0, 0, 0, 0)
        self.h_layout.setObjectName("h_layout")

        self.menu_v_layout = QtWidgets.QVBoxLayout()
        self.menu_v_layout.setObjectName("verticalLayout_2")

        self.menuButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.menuButton.setObjectName("menuButton")
        self.menuButton.setCheckable(True)
        self.menuButton.toggle()
        self.menuButton.clicked.connect(self.onButtonClicked)
        self.menu_v_layout.addWidget(self.menuButton)

        self.list_v_layout = QtWidgets.QVBoxLayout()
        self.list_v_layout.setObjectName("list_v_layout")

        self.videoButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.videoButton.setObjectName("videoButton")
        self.videoButton.clicked.connect(self.stack1UI)
        self.list_v_layout.addWidget(self.videoButton)

        self.mapButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mapButton.setObjectName("mapButton")
        self.mapButton.clicked.connect(self.stack2UI)
        self.list_v_layout.addWidget(self.mapButton)

        self.widget1 = QtWidgets.QWidget()
        self.menu_v_layout.addWidget(self.widget1)
        self.widget1.setLayout(self.list_v_layout)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.list_v_layout.addItem(spacerItem)
        self.menu_v_layout.addLayout(self.list_v_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_v_layout.addItem(spacerItem1)
        self.h_layout.addLayout(self.menu_v_layout)

        self.Stack = QtWidgets.QStackedWidget(self.horizontalLayoutWidget)
        self.Stack.setObjectName("Stack")
        # self.page_3 = QtWidgets.QWidget()
        # self.page_3.setObjectName("page_3")
        # self.Stack.addWidget(self.page_3)
        # self.page_4 = QtWidgets.QWidget()
        # self.page_4.setObjectName("page_4")
        # self.Stack.addWidget(self.page_4)

        self.stack1 = QWidget()
        self.stack2 = QWidget()

        self.stack1UI()
        self.stack2UI()

        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.h_layout.addWidget(self.Stack)

        self.retranslateUi(Logon)
        QtCore.QMetaObject.connectSlotsByName(Logon)

    def retranslateUi(self, Logon):
        Logon.setWindowTitle(QtWidgets.QApplication.translate("Logon", "Logon", None, -1))
        self.menuButton.setText(QtWidgets.QApplication.translate("Logon", "Menu", None, -1))
        self.videoButton.setText(QtWidgets.QApplication.translate("Logon", "Video", None, -1))
        self.mapButton.setText(QtWidgets.QApplication.translate("Logon", "HeatMap", None, -1))

    def onButtonClicked(self):
        if self.menuButton.isChecked():
            self.widget1.setVisible(True)
        else:
            self.widget1.setVisible(False)

    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("Name", QLineEdit())
        layout.addRow("Address", QLineEdit())
        # self.setTabText(0,"Contact Details")
        self.stack1.setLayout(layout)
        # self.stack1.setVisible(True)
        # self.stack2.setVisible(False)
        self.display(0)

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("Male"))
        sex.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Sex"), sex)
        layout.addRow("Date of Birth", QLineEdit())

        self.stack2.setLayout(layout)
        # self.stack2.setVisible(True)
        # self.stack1.setVisible(False)
        self.display(1)


    def display(self, i):
        self.Stack.setCurrentIndex(i)

def main():
    app = QApplication(sys.argv)
    Dialog = QDialog()
    form = Ui_Logon()
    form.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
