import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
#from person_list import Ui_MainWindow
from person_list_v2 import Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.listWidget.addItem("name1")


class Person():

    per_count = 0

    def __init__(self, name1, name2, name3, number, bday):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.number = number
        self.bday = bday
        Person.per_count += 1


    def return_person_info(self):
        return(self.name1, self.name2, self.name3, self.number, self.bday)

first_person = Person("Иванов", "Иван", "Иванович", "11223344", "01.01")
second_person = Person("Петров", "Петр", "Петрович", "22334455", "02.02")
print(first_person.return_person_info())
print(second_person.return_person_info())
print(Person.per_count)



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
