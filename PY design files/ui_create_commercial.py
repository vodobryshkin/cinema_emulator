# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_create_commercial.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateCommercialWindow(object):
    def setupUi(self, CreateCommercialWindow):
        CreateCommercialWindow.setObjectName("CreateCommercialWindow")
        CreateCommercialWindow.resize(223, 128)
        CreateCommercialWindow.setMinimumSize(QtCore.QSize(223, 128))
        CreateCommercialWindow.setMaximumSize(QtCore.QSize(223, 128))
        self.combo_box = QtWidgets.QComboBox(CreateCommercialWindow)
        self.combo_box.setGeometry(QtCore.QRect(20, 30, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combo_box.setFont(font)
        self.combo_box.setObjectName("combo_box")
        self.create_button = QtWidgets.QPushButton(CreateCommercialWindow)
        self.create_button.setGeometry(QtCore.QRect(20, 90, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.create_button.setFont(font)
        self.create_button.setObjectName("create_button")

        self.retranslateUi(CreateCommercialWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateCommercialWindow)

    def retranslateUi(self, CreateCommercialWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateCommercialWindow.setWindowTitle(_translate("CreateCommercialWindow", "Form"))
        self.create_button.setText(_translate("CreateCommercialWindow", "Создать"))