# Form implementation generated from reading ui file 'C:\Users\khmel\Desktop\Projects\patients_record\UI\deleteDocWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DeleteDocWindow(object):
    def setupUi(self, DeleteDocWindow):
        DeleteDocWindow.setObjectName("DeleteDocWindow")
        DeleteDocWindow.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(parent=DeleteDocWindow)
        self.pushButton.setGeometry(QtCore.QRect(200, 260, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(parent=DeleteDocWindow)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 258, 216))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.doctors_list = QtWidgets.QListView(parent=self.layoutWidget)
        self.doctors_list.setObjectName("doctors_list")
        self.verticalLayout.addWidget(self.doctors_list)

        self.retranslateUi(DeleteDocWindow)
        QtCore.QMetaObject.connectSlotsByName(DeleteDocWindow)

    def retranslateUi(self, DeleteDocWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteDocWindow.setWindowTitle(_translate("DeleteDocWindow", "Удаление врача"))
        self.pushButton.setText(_translate("DeleteDocWindow", "Удалить"))
        self.label.setText(_translate("DeleteDocWindow", "Список Врачей"))
