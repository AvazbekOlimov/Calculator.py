
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Desktop/Python/Nazariy/3.12.2023/img/calculator.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("background-color: rgb(249, 247, 247);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 270, 93, 28))
        self.pushButton.setStyleSheet("background-color: #3F72AF;color: #DBE2EF;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 100, 291, 22))
        self.lineEdit.setStyleSheet("background-color: rgb(219, 226, 239);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 170, 291, 22))
        self.lineEdit_2.setStyleSheet("background-color: rgb(219, 226, 239);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(150, 230, 95, 20))
        self.radioButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton.setStyleSheet("color: #3F72AF;")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(230, 230, 95, 20))
        self.radioButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton_2.setStyleSheet("color: #3F72AF;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(320, 230, 95, 20))
        self.radioButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.radioButton_3.setStyleSheet("color: #3F72AF;")
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 275, 95, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(parent=self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuAbout = QtWidgets.QMenu(parent=self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_us = QtGui.QAction(parent=MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.actionAbout_programming = QtGui.QAction(parent=MainWindow)
        self.actionAbout_programming.setObjectName("actionAbout_programming")
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionExit)
        self.menuAbout.addAction(self.actionAbout_us)
        self.menuAbout.addAction(self.actionAbout_programming)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.pushButton.clicked.connect(self.calc_slot)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "Bu Asosiy Oyna"))
        self.pushButton.setText(_translate("MainWindow", "Result"))
        self.radioButton.setText(_translate("MainWindow", "Qo\'shish"))
        self.radioButton_2.setText(_translate("MainWindow", "Ayirish"))
        self.radioButton_3.setText(_translate("MainWindow", "Ko\'paytirish"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label.setStyleSheet("""
            QLabel{
                font-weight: 700;
                font-size: 20px;
                color: #3F72AF;
            }
        """)
        self.lineEdit.setStyleSheet("""
            QLineEdit{
                border: none;
                background-color: #DBE2EF;
            }    
        """)
        self.lineEdit_2.setStyleSheet("""
            QLineEdit{
                border: none;
                background-color: #DBE2EF;
            }    
        """)
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAbout_us.setText(_translate("MainWindow", "About us"))
        self.actionAbout_programming.setText(_translate("MainWindow", "About programming"))
    def calc_slot(self):
        nat = 0
        if self.radioButton.isChecked():
            nat = int(self.lineEdit.text())+int(self.lineEdit_2.text())
        elif self.radioButton_2.isChecked():
            nat = int(self.lineEdit.text())-int(self.lineEdit_2.text())
        elif self.radioButton_3.isChecked():
            nat = int(self.lineEdit.text())*int(self.lineEdit_2.text()) 
        else:
            nat = 'Iltimos amalni tanlang !'
        self.label.setText(str(nat))
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)           
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
