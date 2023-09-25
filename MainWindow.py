# Form implementation generated from reading ui file 'C:\Users\khmel\Desktop\Projects\patients_record\UI\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QtCore.QSize(16, 9))
        MainWindow.setBaseSize(QtCore.QSize(16, 9))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shedule = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.shedule.setGeometry(QtCore.QRect(630, 30, 1021, 731))
        self.shedule.setObjectName("shedule")
        self.shedule.setColumnCount(7)
        self.shedule.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setHorizontalHeaderItem(6, item)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(90, 630, 312, 190))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.NoSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.doctors_table = QtWidgets.QListWidget(parent=self.centralwidget)
        self.doctors_table.setGeometry(QtCore.QRect(40, 60, 121, 471))
        self.doctors_table.setStyleSheet("")
        self.doctors_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.doctors_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.doctors_table.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.doctors_table.setObjectName("doctors_table")
        self.surnames_table = QtWidgets.QListWidget(parent=self.centralwidget)
        self.surnames_table.setGeometry(QtCore.QRect(200, 60, 281, 471))
        self.surnames_table.setObjectName("surnames_table")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(parent=self.menuBar)
        self.menu.setSeparatorsCollapsible(False)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.add_doctor_menu = QtGui.QAction(parent=MainWindow)
        self.add_doctor_menu.setObjectName("add_doctor_menu")
        self.add_patient_menu = QtGui.QAction(parent=MainWindow)
        self.add_patient_menu.setObjectName("add_patient_menu")
        self.remove_doctor_menu = QtGui.QAction(parent=MainWindow)
        self.remove_doctor_menu.setObjectName("remove_doctor_menu")
        self.remove_patient_menu = QtGui.QAction(parent=MainWindow)
        self.remove_patient_menu.setObjectName("remove_patient_menu")
        self.edit_doc_menu = QtGui.QAction(parent=MainWindow)
        self.edit_doc_menu.setObjectName("edit_doc_menu")
        self.menu.addAction(self.add_doctor_menu)
        self.menu.addAction(self.add_patient_menu)
        self.menu.addAction(self.remove_doctor_menu)
        self.menu.addAction(self.remove_patient_menu)
        self.menu.addAction(self.edit_doc_menu)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Doctor\'s shedule"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.add_doctor_menu.setText(_translate("MainWindow", "Добавить врача"))
        self.add_patient_menu.setText(_translate("MainWindow", "Добавить запись"))
        self.remove_doctor_menu.setText(_translate("MainWindow", "Удалить врача"))
        self.remove_patient_menu.setText(_translate("MainWindow", "Удалить запись"))
        self.edit_doc_menu.setText(_translate("MainWindow", "Редактировать врача"))