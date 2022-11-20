# Form implementation generated from reading ui file 'v2.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from grocery_tracker import Groceries
    # def __init__(self):
        
    #     pass

    # def display_main(self):
    #     pass

    # def display_current_groceries(self):
    #     pass

    # def display_notification(self, food, count):
    #     pass

    # def food_adder(self):
    #     pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.groceries = Groceries()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAcceptDrops(False)
        MainWindow.setDocumentMode(False)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.add_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.add_it())
        self.add_button.setGeometry(QtCore.QRect(50, 50, 131, 32))
        self.add_button.setObjectName("add_button")
        
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 20, 200, 16))
        self.title.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget, placeholderText = "Product Name")
        self.lineEdit.setGeometry(QtCore.QRect(180, 50, 181, 32))
        self.lineEdit.returnPressed.connect(self.add_it)
        self.lineEdit.setObjectName("lineEdit")
        
        self.col_1 = QtWidgets.QListWidget(self.centralwidget)
        self.col_1.setGeometry(QtCore.QRect(60, 120, 220, 411))
        self.col_1.setObjectName("col_1")
        
        self.col_2 = QtWidgets.QListWidget(self.centralwidget)
        self.col_2.setGeometry(QtCore.QRect(300, 120, 220, 411))
        self.col_2.setObjectName("col_2")
        
        self.col_3 = QtWidgets.QListWidget(self.centralwidget)
        self.col_3.setGeometry(QtCore.QRect(540, 120, 220, 411))
        self.col_3.setObjectName("col_3")
        
        self.col_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.col_label_1.setGeometry(QtCore.QRect(120, 90, 101, 16))
        self.col_label_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.col_label_1.setObjectName("col_label_1")
        
        self.col_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.col_label_2.setGeometry(QtCore.QRect(360, 90, 101, 16))
        self.col_label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.col_label_2.setObjectName("col_label_2")
        
        self.col_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.col_label_3.setGeometry(QtCore.QRect(600, 90, 101, 16))
        self.col_label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.col_label_3.setObjectName("col_label_3")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 42))
        self.menubar.setObjectName("menubar")
        self.menuLanding_Page = QtWidgets.QMenu(self.menubar)
        self.menuLanding_Page.setObjectName("menuLanding_Page")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuLanding_Page.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.groceries.sort_foods_list()
        for item in self.groceries.food_good:
                self.col_1.addItem(item[0])

    # Add Item to List
    def add_it(self):
        # Grab the item from the list box
        if(self.lineEdit.text() != ""):
            item = self.lineEdit.text()

            # Add item to list
            self.col_1.addItem(item)
            self.groceries.add_food(item) # find a way to add an expiration date for the second parameter

            # Clear the item box
            self.lineEdit.setText("")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_button.setText(_translate("MainWindow", "Add purchases"))
        self.title.setText(_translate("MainWindow", "LANDING PAGE"))
        self.col_label_1.setText(_translate("MainWindow", "Groceries"))
        self.col_label_2.setText(_translate("MainWindow", "Expiring Soon"))
        self.col_label_3.setText(_translate("MainWindow", "Expired"))
        self.menuLanding_Page.setTitle(_translate("MainWindow", "Landing Page"))

def run_ui():

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
