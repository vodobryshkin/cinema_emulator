# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_create_product.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateProductWindow(object):
    def setupUi(self, CreateProductWindow):
        CreateProductWindow.setObjectName("CreateProductWindow")
        CreateProductWindow.resize(319, 382)
        CreateProductWindow.setMinimumSize(QtCore.QSize(319, 382))
        CreateProductWindow.setMaximumSize(QtCore.QSize(319, 382))
        font = QtGui.QFont()
        font.setPointSize(12)
        CreateProductWindow.setFont(font)
        self.formLayoutWidget = QtWidgets.QWidget(CreateProductWindow)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(44)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_input.setObjectName("name_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name_input)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.price_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.price_input.setObjectName("price_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.price_input)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.anum_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.anum_input.setObjectName("anum_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.anum_input)
        self.create_product_button = QtWidgets.QPushButton(CreateProductWindow)
        self.create_product_button.setGeometry(QtCore.QRect(60, 240, 201, 41))
        self.create_product_button.setObjectName("create_product_button")
        self.error_widget = QtWidgets.QLabel(CreateProductWindow)
        self.error_widget.setGeometry(QtCore.QRect(10, 320, 301, 51))
        self.error_widget.setObjectName("error_widget")

        self.retranslateUi(CreateProductWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateProductWindow)

    def retranslateUi(self, CreateProductWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateProductWindow.setWindowTitle(_translate("CreateProductWindow", "Form"))
        self.label.setText(_translate("CreateProductWindow", "Название"))
        self.label_2.setText(_translate("CreateProductWindow", "Цена"))
        self.label_3.setText(_translate("CreateProductWindow", "Количество"))
        self.create_product_button.setText(_translate("CreateProductWindow", "Создать товар"))
        self.error_widget.setText(_translate("CreateProductWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
