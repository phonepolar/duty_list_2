# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'person_list_v2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pB_add_new_person = QtWidgets.QPushButton(self.centralwidget)
        self.pB_add_new_person.setGeometry(QtCore.QRect(20, 60, 141, 27))
        self.pB_add_new_person.setObjectName("pB_add_new_person")
        self.label_person_info = QtWidgets.QLabel(self.centralwidget)
        self.label_person_info.setGeometry(QtCore.QRect(20, 130, 181, 19))
        self.label_person_info.setObjectName("label_person_info")
        self.pB_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pB_edit.setGeometry(QtCore.QRect(360, 130, 88, 27))
        self.pB_edit.setObjectName("pB_edit")
        self.pB_del = QtWidgets.QPushButton(self.centralwidget)
        self.pB_del.setGeometry(QtCore.QRect(460, 130, 88, 27))
        self.pB_del.setObjectName("pB_del")
        self.label_person_list = QtWidgets.QLabel(self.centralwidget)
        self.label_person_list.setGeometry(QtCore.QRect(20, 100, 181, 19))
        self.label_person_list.setObjectName("label_person_list")
        self.pB_show = QtWidgets.QPushButton(self.centralwidget)
        self.pB_show.setGeometry(QtCore.QRect(270, 130, 88, 27))
        self.pB_show.setObjectName("pB_show")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 190, 731, 81))
        self.listWidget.setObjectName("listWidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(30, 280, 731, 91))
        self.tableView.setObjectName("tableView")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(30, 380, 731, 91))
        self.columnView.setObjectName("columnView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pB_add_new_person.setText(_translate("MainWindow", "add new person"))
        self.label_person_info.setText(_translate("MainWindow", "person info"))
        self.pB_edit.setText(_translate("MainWindow", "edit"))
        self.pB_del.setText(_translate("MainWindow", "delete"))
        self.label_person_list.setText(_translate("MainWindow", "person list"))
        self.pB_show.setText(_translate("MainWindow", "show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
