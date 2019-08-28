# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seulgi_4.ui',
# licensing of 'seulgi_4.ui' applies.
#
# Created: Wed Aug 28 11:29:48 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(917, 663)

        self.menu_widget = QtWidgets.QWidget(Form)
        self.menu_widget.setGeometry(QtCore.QRect(10, 10, 131, 641))
        self.menu_widget.setObjectName("menu_widget")

        self.menu1_widget = QtWidgets.QWidget(self.menu_widget)
        self.menu1_widget.setGeometry(QtCore.QRect(4, 10, 121, 41))
        self.menu1_widget.setObjectName("menu1_widget")

        self.menu_btn = QtWidgets.QPushButton(self.menu1_widget)
        self.menu_btn.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.menu_btn.setObjectName("menu_btn")
        self.menu_btn.setCheckable(True)
        self.menu_btn.toggle()
        self.menu_btn.clicked.connect(self.menu_btn_clicked)

        self.menu2_widget = QtWidgets.QWidget(self.menu_widget)
        self.menu2_widget.setGeometry(QtCore.QRect(3, 70, 121, 111))
        self.menu2_widget.setObjectName("menu2_widget")

        self.vid_btn = QtWidgets.QPushButton(self.menu2_widget)
        self.vid_btn.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.vid_btn.setObjectName("vid_btn")

        self.vid_btn.setCheckable(True)
        self.vid_btn.toggle()
        self.vid_btn.clicked.connect(self.vid_btn_clicked)

        self.heat_btn = QtWidgets.QPushButton(self.menu2_widget)
        self.heat_btn.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.heat_btn.setObjectName("heat_btn")

        self.heat_btn.setCheckable(True)
        self.heat_btn.toggle()
        self.heat_btn.clicked.connect(self.heat_btn_clicked)

        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 10, 761, 641))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.main_lay = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.main_lay.setContentsMargins(0, 0, 0, 0)
        self.main_lay.setObjectName("main_lay")

        self.vid_lay = QtWidgets.QGridLayout()
        self.vid_lay.setObjectName("vid_lay")

        self.vid_widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.vid_widget.setObjectName("vid_widget")

        self.video_widget = QtWidgets.QWidget(self.vid_widget)
        self.video_widget.setGeometry(QtCore.QRect(20, 110, 331, 331))
        self.video_widget.setObjectName("video_widget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.vid_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 371, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.videoMenu_VLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.videoMenu_VLayout.setContentsMargins(0, 0, 0, 0)
        self.videoMenu_VLayout.setObjectName("videoMenu_VLayout")

        self.dateMenu_HLayout = QtWidgets.QHBoxLayout()
        self.dateMenu_HLayout.setObjectName("horizontalLayout")

        self.dateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dateLabel.setObjectName("dateLabel")
        self.dateMenu_HLayout.addWidget(self.dateLabel)

        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateMenu_HLayout.addWidget(self.dateEdit)

        self.videoMenu_VLayout.addLayout(self.dateMenu_HLayout)

        self.timeLabel_HLayout = QtWidgets.QHBoxLayout()
        self.timeLabel_HLayout.setObjectName("horizontalLayout_2")

        self.timeLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.timeLabel.setObjectName("label_2")
        self.timeLabel_HLayout.addWidget(self.timeLabel)

        self.timeEdit_1 = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.timeEdit_1.setObjectName("timeEdit")
        self.timeLabel_HLayout.addWidget(self.timeEdit_1)

        self.timeEdit_2 = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.timeLabel_HLayout.addWidget(self.timeEdit_2)

        self.videoMenu_VLayout.addLayout(self.timeLabel_HLayout)

        self.total_videoBtn_HLayout = QtWidgets.QWidget(self.vid_widget)
        self.total_videoBtn_HLayout.setGeometry(QtCore.QRect(70, 460, 231, 80))
        self.total_videoBtn_HLayout.setObjectName("videoBtn_HLayout")

        self.videoBtn_HLayout = QtWidgets.QHBoxLayout(self.total_videoBtn_HLayout)
        self.videoBtn_HLayout.setContentsMargins(0, 0, 0, 0)
        self.videoBtn_HLayout.setObjectName("horizontalLayout_3")

        self.playBtn = QtWidgets.QPushButton(self.total_videoBtn_HLayout)
        self.playBtn.setObjectName("playBtn")
        self.playBtn.clicked.connect(self.play_btn_clicked)
        self.videoBtn_HLayout.addWidget(self.playBtn)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.videoBtn_HLayout.addItem(spacerItem)

        self.stopBtn = QtWidgets.QPushButton(self.total_videoBtn_HLayout)
        self.stopBtn.setObjectName("pushButton_2")
        self.stopBtn.clicked.connect(self.stop_btn_clicked)
        self.videoBtn_HLayout.addWidget(self.stopBtn)

        self.vid_lay.addWidget(self.vid_widget, 0, 1, 1, 1)
        self.main_lay.addLayout(self.vid_lay, 0, 0, 1, 1)

        self.heat_lay = QtWidgets.QGridLayout()
        self.heat_lay.setObjectName("heat_lay")

        self.heat_widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.heat_widget.setObjectName("heat_widget")

        self.heat_label = QtWidgets.QLabel(self.heat_widget)
        self.heat_label.setGeometry(QtCore.QRect(10, 10, 56, 12))
        self.heat_label.setObjectName("heat_label")

        self.time_check = QtWidgets.QCheckBox(self.heat_widget)
        self.time_check.setGeometry(QtCore.QRect(10, 33, 81, 16))
        self.time_check.setObjectName("time_check")

        self.start_time = QtWidgets.QTimeEdit(self.heat_widget)
        self.start_time.setGeometry(QtCore.QRect(100, 30, 118, 22))
        self.start_time.setObjectName("start_time")

        self.end_time = QtWidgets.QTimeEdit(self.heat_widget)
        self.end_time.setGeometry(QtCore.QRect(230, 30, 118, 22))
        self.end_time.setObjectName("end_time")

        self.img_label = QtWidgets.QLabel(self.heat_widget)
        self.img_label.setGeometry(QtCore.QRect(10, 70, 56, 12))
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")

        self.heat_lay.addWidget(self.heat_widget, 0, 0, 1, 1)
        self.main_lay.addLayout(self.heat_lay, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.menu_mainPage()

        # video player widget
        self.vWidget = QtMultimediaWidgets.QVideoWidget(self.video_widget)
        self.vWidget.resize(self.video_widget.size())

        # media area
        self.player = QtMultimedia.QMediaPlayer(self.video_widget)
        self.player.setMedia(QUrl.fromLocalFile("C:\\Users\\bit\\Downloads\\cctv_store.mp4"))
        self.player.setVideoOutput(self.vWidget)


    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.menu_btn.setText(QtWidgets.QApplication.translate("Form", "메뉴", None, -1))
        self.vid_btn.setText(QtWidgets.QApplication.translate("Form", "영상", None, -1))
        self.heat_btn.setText(QtWidgets.QApplication.translate("Form", "히트맵", None, -1))
        self.dateLabel.setText(QtWidgets.QApplication.translate("Form", "Date", None, -1))
        self.timeLabel.setText(QtWidgets.QApplication.translate("Form", "Time", None, -1))
        self.playBtn.setText(QtWidgets.QApplication.translate("Form", "재생", None, -1))
        self.stopBtn.setText(QtWidgets.QApplication.translate("Form", "정지", None, -1))
        self.heat_label.setText(QtWidgets.QApplication.translate("Form", "히트맵", None, -1))
        self.time_check.setText(QtWidgets.QApplication.translate("Form", "적용시간", None, -1))

    def menu_btn_clicked(self):
        if self.menu_btn.isChecked():
            self.menu2_widget.setVisible(True)
        else:
            self.menu2_widget.setVisible(False)

    def vid_btn_clicked(self):
        self.vid_widget.setVisible(True)
        self.heat_widget.setVisible(False)

    def heat_btn_clicked(self):
        self.heat_widget.setVisible(True)
        self.vid_widget.setVisible(False)

    def menu_mainPage(self):
        self.mainPage = QtWidgets.QWidget(self.gridLayoutWidget)
        self.mainPage.setObjectName("mainPage")

        self.mainPage_lay = QtWidgets.QGridLayout()
        self.mainPage_lay.setObjectName("mainPage_lay")

        self.mainPage_lay.addWidget(self.mainPage, 0, 0, 1, 1)
        self.main_lay.addLayout(self.mainPage_lay, 0, 1, 1, 1)

        self.mainPage.setVisible(True)
        self.vid_widget.setVisible(False)
        self.heat_widget.setVisible(False)

    def play_btn_clicked(self):
        self.player.play()

    def stop_btn_clicked(self):
        self.player.stop()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())