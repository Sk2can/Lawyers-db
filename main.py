import ctypes
import json
from datetime import date
import sys
from pathlib import Path
from PyQt6.QtWidgets import QTableWidgetItem

from py_files.MainWindow import *
from py_files.addRecordWindow import *
from py_files.addDocWindow import *
from py_files.EditDocInfo import *
from py_files.deleteDocWindow import *
from py_files.deleteRecordWindow import *
from py_files.addPatientWindow import *

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
        for patient in Data["Doctors"][spec][doctorid]["Records"]:
            row = int(Data["Times_rev"][patient["Time"]])
            column = int(str(patient["Date"]).split('.')[0]) - int(date.today().day)
            mainwindowUI.shedule.setItem(row,column,QTableWidgetItem(""))
            mainwindowUI.shedule.item(row,column).setText(patient["Surname"] + ' ' + patient["Name"][0] + "." + patient["Patronymic"][0] +".")

class UiAddRecordWindow(Ui_AddingRecord):
    pass

class UiAddPatientWindow(Ui_AddPatientWindow):
    def reg_patient(self):
        path = Path('Data.json')
        data = json.loads(path.read_text(encoding='utf-8'))
        print(data["Patients"])
        data["Patients"].append({"Name": "Владислав",
            "Surname": "Хмелёв",
            "Patronymic": "Анатольевич",
            "SNILS": "000-000-000 00",
            "OMS": "0000 0000 0000 0000",
            "Passport": "00 00 000000"})

        path.write_text(json.dumps(data, indent=4, ensure_ascii=False), encoding='utf-8')

class Patient:
    def __init__(self, name, surname, patronymic, snils_number, polis_number, pasport_number):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
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
    with open("Data.json", "r", encoding="utf-8") as json_file:
        path = Path("Data.json")
        Data = json.load(json_file)
        for spec in Data["Specs"]:
            doc_index = -1
            for doctor in Data["Doctors"][spec]:
                doc_index +=1
                patient_index = -1
                for patient in doctor["Records"]:
                    patient_index +=1
                    if date.today().today().month > int(str(patient["Date"]).split('.')[1]):
                        print(Data["Doctors"][spec][doc_index]["Records"][patient_index])
                        del Data["Doctors"][spec][doc_index]["Records"][patient_index]
                        path.write_text(json.dumps(Data, indent=4, ensure_ascii=False), encoding='utf-8')
                    elif date.today().day > int(str(patient["Date"]).split('.')[0]):
                        print(Data["Doctors"][spec][doc_index]["Records"][patient_index])
                        del Data["Doctors"][spec][doc_index]["Records"][patient_index]
                        path.write_text(json.dumps(Data, indent=4, ensure_ascii=False), encoding='utf-8')

    # Создание экземпляров окон
    mainwindowUI, mainwindow = initWindow(UiMainWindow(),QtWidgets.QMainWindow())
    addrecordwindowUI, addrecordwindow = initWindow(Ui_AddingRecord(),QtWidgets.QDialog())
    deletedocwindowUI, deletedocwindow = initWindow(Ui_DeleteDocWindow(),QtWidgets.QDialog())
    editdocwindowUI, editdocwindow = initWindow(Ui_EditWindow(),QtWidgets.QDialog())
    adddocwindowUI, adddocwindow = initWindow(Ui_AddingDoc(),QtWidgets.QDialog())
    deleterecordwindowUI, deleterecordwindow = initWindow(Ui_deleteRecordWindow(), QtWidgets.QDialog())
    addpatientUI, addpatientwindow = initWindow(UiAddPatientWindow(), QtWidgets.QDialog())


    mainwindow.showMaximized()
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
    mainwindowUI.register_patient.triggered.connect(lambda: addpatientwindow.show())
    addpatientUI.reg_button.clicked.connect(lambda: addpatientUI.reg_patient())
    # addpatientUI.OMS_lineEdit.connect(addpatientUI.setCursor)
    # addpatientUI.SNILS_lineEdit.cursorPositionChanged.connect(addpatientUI.setCursor)
    # addpatientUI.Pasport_lineEdit.cursorPositionChanged.connect(addpatientUI.setCursor)


    sys.exit(app.exec())