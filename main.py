import ctypes
import json
from datetime import date
import sys

from PyQt6.QtWidgets import QTableWidgetItem

from py_files.MainWindow import *
from py_files.addRecordWindow import *
from py_files.addDocWindow import *
from py_files.EditDocInfo import *
from py_files.deleteDocWindow import *
from py_files.deleteRecordWindow import *

class UiMainWindow(Ui_MainWindow):
    def draw_shedule(self):
        for day in range(0,7):
            self.shedule.setHorizontalHeaderItem(day, QTableWidgetItem(""))
            self.shedule.horizontalHeaderItem(day).setText(str(date.today().day + day))
        for time in range(0, 21):
            self.shedule.setVerticalHeaderItem(time, QTableWidgetItem(""))
            self.shedule.verticalHeaderItem(time).setText(Data["Times"][str(time)])
    def draw_specs(self):
        for spec in Data["Specs"]:
            self.doctors_table.addItem(spec)
    def draw_surnames(self, spec):
        self.shedule.clear()
        self.draw_shedule()
        self.surnames_table.clear()
        for doctor in Data["Doctors"][spec]:
            self.surnames_table.addItem(doctor["Surname"] + " " + doctor["Name"] + " " + doctor["Patronymic"])
    def draw_records(self,spec,doctorid):
        self.shedule.clear()
        self.draw_shedule()
        for patient in Data["Doctors"][spec][doctorid]["Patients"]:
            row = int(Data["Times_rev"][patient["Time"]])
            column = int(patient["Date"]) - int(date.today().day)
            mainwindowUI.shedule.setItem(row,column,QTableWidgetItem(""))
            mainwindowUI.shedule.item(row,column).setText(patient["Surname"] + ' ' + patient["Name"][0] + "." + patient["Patronymic"] +".")

class UiAddRecordWindow(Ui_AddingRecord):
    pass

class Patient:
    def __init__(self, name, surname, patronymic, snils_number, polis_number, pasport_number, date, time):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.date = date
        self.time = time
        self.snils_number = snils_number
        self.polis_number = polis_number
        self.pasport_number = pasport_number

class Doctor:
    def __init__(self, name, surname, patronymic, cabinet_number, experience, post):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.cabinet_number = cabinet_number
        self.experience = experience
        self.post = post

def initWindow(ui, window_class):
    window = window_class
    ui.setupUi(window)
    return ui, window

if __name__ == '__main__':
    # Инициализация оконнокого приложения
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
    app = QtWidgets.QApplication(sys.argv)

    # Открываем файл на чтение
    with open("Data.json", "r", encoding="utf8") as json_file:
        Data = json.load(json_file)

    # Создание экземпляров окон
    mainwindowUI, mainwindow = initWindow(UiMainWindow(),QtWidgets.QMainWindow())
    addrecordwindowUI, addrecordwindow = initWindow(Ui_AddingRecord(),QtWidgets.QDialog())
    deletedocwindowUI, deletedocwindow = initWindow(Ui_DeleteDocWindow(),QtWidgets.QDialog())
    editdocwindowUI, editdocwindow = initWindow(Ui_EditWindow(),QtWidgets.QDialog())
    adddocwindowUI, adddocwindow = initWindow(Ui_AddingDoc(),QtWidgets.QDialog())
    deleterecordwindowUI, deleterecordwindow = initWindow(Ui_deleteRecordWindow(), QtWidgets.QDialog())

    mainwindow.show()
    mainwindowUI.draw_shedule()
    mainwindowUI.draw_specs()

    #События
    mainwindowUI.doctors_table.itemSelectionChanged.connect(lambda : mainwindowUI.draw_surnames(mainwindowUI.doctors_table.currentItem().text()))
    mainwindowUI.surnames_table.itemClicked.connect(lambda : mainwindowUI.draw_records(mainwindowUI.doctors_table.currentItem().text(), mainwindowUI.surnames_table.currentIndex().row()))
    mainwindowUI.add_patient_menu.triggered.connect(lambda : addrecordwindow.show())
    mainwindowUI.remove_doctor_menu.triggered.connect(lambda: deletedocwindow.show())
    mainwindowUI.edit_doc_menu.triggered.connect(lambda: editdocwindow.show())
    mainwindowUI.add_doctor_menu.triggered.connect(lambda: adddocwindow.show())
    mainwindowUI.remove_patient_menu.triggered.connect(lambda: deleterecordwindow.show())

    sys.exit(app.exec())