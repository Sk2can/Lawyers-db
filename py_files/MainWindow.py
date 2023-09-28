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
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.doctors_table = QtWidgets.QListWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.doctors_table.setFont(font)
        self.doctors_table.setStyleSheet("")
        self.doctors_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.doctors_table.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.doctors_table.setViewMode(QtWidgets.QListView.ViewMode.ListMode)
        self.doctors_table.setObjectName("doctors_table")
        self.verticalLayout_2.addWidget(self.doctors_table)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.surnames_table = QtWidgets.QListWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.surnames_table.setFont(font)
        self.surnames_table.setObjectName("surnames_table")
        self.verticalLayout.addWidget(self.surnames_table)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 10)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.NoSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)
        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.shedule = QtWidgets.QTableWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.shedule.setFont(font)
        self.shedule.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.shedule.setObjectName("shedule")
        self.shedule.setColumnCount(7)
        self.shedule.setRowCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.shedule.setVerticalHeaderItem(20, item)
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
        self.shedule.horizontalHeader().setCascadingSectionResizes(True)
        self.shedule.horizontalHeader().setDefaultSectionSize(140)
        self.shedule.verticalHeader().setVisible(True)
        self.shedule.verticalHeader().setCascadingSectionResizes(True)
        self.shedule.verticalHeader().setDefaultSectionSize(33)
        self.shedule.verticalHeader().setMinimumSectionSize(24)
        self.shedule.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_2.addWidget(self.shedule)
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
        self.register_patient = QtGui.QAction(parent=MainWindow)
        self.register_patient.setObjectName("register_patient")
        self.menu.addAction(self.register_patient)
        self.menu.addAction(self.add_patient_menu)
        self.menu.addAction(self.remove_patient_menu)
        self.menu.addAction(self.add_doctor_menu)
        self.menu.addAction(self.edit_doc_menu)
        self.menu.addAction(self.remove_doctor_menu)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Doctor\'s shedule"))
        self.label.setText(_translate("MainWindow", "Специальность"))
        self.label_2.setText(_translate("MainWindow", "Доктор"))
        item = self.shedule.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "8:00"))
        item = self.shedule.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "8:20"))
        item = self.shedule.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "8:40"))
        item = self.shedule.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "9:00"))
        item = self.shedule.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "9:20"))
        item = self.shedule.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "9:40"))
        item = self.shedule.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "10:00"))
        item = self.shedule.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "10:20"))
        item = self.shedule.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "10:40"))
        item = self.shedule.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "11:00"))
        item = self.shedule.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "11:20"))
        item = self.shedule.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "11:40"))
        item = self.shedule.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "12:00"))
        item = self.shedule.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "12:20"))
        item = self.shedule.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "12:40"))
        item = self.shedule.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "13:00"))
        item = self.shedule.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "13:20"))
        item = self.shedule.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "13:40"))
        item = self.shedule.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "14:00"))
        item = self.shedule.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "14:20"))
        item = self.shedule.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "14:40"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.add_doctor_menu.setText(_translate("MainWindow", "Добавить врача"))
        self.add_patient_menu.setText(_translate("MainWindow", "Добавить запись"))
        self.remove_doctor_menu.setText(_translate("MainWindow", "Удалить врача"))
        self.remove_patient_menu.setText(_translate("MainWindow", "Удалить запись"))
        self.edit_doc_menu.setText(_translate("MainWindow", "Редактировать врача"))
        self.register_patient.setText(_translate("MainWindow", "Зарегистрировать пациента"))
