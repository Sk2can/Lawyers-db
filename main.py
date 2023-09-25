import ctypes
import json
import datetime
import sys

from MainWindow import *
from addRecordWindow import *
from addDocWindow import *
from EditDocInfo import *
from deleteWindow import *


class Patient:
    def __init__(self, name, surname, patronymic, snils_number, polis_number, pasport_number):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.snils_number = snils_number
        self.polis_number = polis_number
        self.pasport_number = pasport_number

    appointments = []  # список словарей - запись(кабинет, время, дата, врач)

class Doctor:
    def __init__(self, name, surname, patronymic, cabinet_number, experience, post):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.cabinet_number = cabinet_number
        self.experience = experience
        self.post = post

    work_schedule = []

class MainWindow(QtWidgets.QMainWindow):
    def show(self):
        self.showMaximized()

    def draw_schedule(self):
        for day in range(0, 7):
            self.ui.shedule.horizontalHeaderItem(day).setText(str(int(datetime.date.today().day) + day))

    def draw_doctorsList(self):
        for spec in Data["Specs"]:
            self.ui.doctors_table.addItem(spec)

    def draw_surnamesList(self):
        self.ui.surnames_table.clear()
        for doctor in Data["Doctors"][self.ui.doctors_table.currentItem().text()]:
            self.ui.surnames_table.addItem(doctor["Surname"] + ' ' + doctor["Name"] + ' ' + doctor["Patronymic"])

class DeleteDocWindow(QtWidgets.QDialog):
    pass

class AddDocWindow(QtWidgets.QDialog):
        def add_doctor(self):
            spec = self.post.text()
            name = self.name.text().title()
            surname = self.surname.text().title()
            patronymic = self.patronymic.text().title()
            cab = self.cabinet.text()
            exp = self.expirience.text()
            info = {
                "Name": name,
                "Surname": surname,
                "Patronymic": patronymic,
                "Cabinet": cab,
                "Experience": exp
            }
            Data["Doctors"][spec].append(info)
            with open("Data.json", "w", encoding="utf8") as file:
                json.dump(Data, file, indent=4)

class EditWindow(QtWidgets.QDialog):
        def draw_specs(self):
            self.spec_comboBox.clear()
            for spec in Data["Specs"]:
                self.spec_comboBox.addItem(spec)

        def draw_surnames(self):
            self.doctors_table.clear()
            spec = self.spec_comboBox.currentText()
            for info in Data["Doctors"][spec]:
                self.doctors_table.addItem(info["Surname"] + ' ' + info["Name"] + ' ' + info["Patronymic"])

        def show_info(self):
            spec = self.spec_comboBox.currentText()
            index = self.doctors_table.currentRow()
            info = Data["Doctors"][spec][index]
            self.name_2.setText(info["Name"])
            self.surname_2.setText(info["Surname"])
            self.patronymic_2.setText(info["Patronymic"])
            self.expirience_2.setText(info["Experience"])
            self.cabinet_2.setText(info["Cabinet"])
            self.post_2.setText(spec)

        def accept_edit(self):
            spec = self.spec_comboBox.currentText()
            index = self.doctors_table.currentRow()
            info = {
                "Name": self.name_2.text(),
                "Surname": self.surname_2.text(),
                "Patronymic": self.patronymic_2.text(),
                "Cabinet": self.cabinet_2.text(),
                "Experience": self.expirience_2.text()
            }
            new_spec = self.post_2.text()
            if spec != new_spec:
                del Data["Doctors"][spec][index]
                Data["Doctors"][new_spec].append(info)
            else:
                Data["Doctors"][spec][index] = info
            with open("Data.json", "w", encoding="utf8") as file:
                json.dump(Data, file, indent=4)

class AddRecordWindow(QtWidgets.QDialog):
    pass

def initWindow(ui, windowClass):
    window = windowClass()
    ui.setupUi(window)
    return ui, window

if __name__ == '__main__':
    # Инициализация оконнокого приложения
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('mycompany.myproduct.subproduct.version')
    app = QtWidgets.QApplication(sys.argv)

    # Открываем файл на чтение
    with open("Data.json", "r", encoding="utf8") as json_file:
        Data = json.load(json_file)

    # Инициализация окон
    MainWindow_ui, MainWindow = initWindow(Ui_MainWindow(), MainWindow)
    addDocWindowUI, addDocWindow = initWindow(Ui_AddingDoc(), AddDocWindow)
    editDocWindowUI, editDocWindow = initWindow(Ui_EditWindow(), EditWindow)
    deleteDocWindowUI, deleteDocWindow = initWindow(Ui_DeleteWindow(), DeleteDocWindow)
    AddingRecordUI, addRecordWindow = initWindow(Ui_AddingRecord(), AddRecordWindow)
    MainWindow.show()

    # События
    MainWindow_ui.edit_doc_menu.triggered.connect(editDocWindow.show)
    MainWindow_ui.add_doctor_menu.triggered.connect(addDocWindow.show)
    MainWindow_ui.add_patient_menu.triggered.connect(addRecordWindow.show)
    MainWindow_ui.remove_doctor_menu.triggered.connect(deleteDocWindow.show)

    # Создание объектов
    patient = Patient("Олег", "Комаров", "Викторович", "123456780000", "2142145323", "323421313")
    doctor = Doctor("Владислав", "Хмелёв", "Анатольевич", 312, 5, "Кардиолог")

    sys.exit(app.exec())