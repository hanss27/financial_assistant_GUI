# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(421, 542)
        SignUp.setStyleSheet("background-color: rgb(248, 237, 215);")
        self.centralwidget = QtWidgets.QWidget(SignUp)
        self.centralwidget.setObjectName("centralwidget")
        self.labelsignup = QtWidgets.QLabel(self.centralwidget)
        self.labelsignup.setGeometry(QtCore.QRect(140, -40, 211, 151))
        font = QtGui.QFont()
        font.setFamily("Gagalin")
        font.setPointSize(24)
        self.labelsignup.setFont(font)
        self.labelsignup.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelsignup.setObjectName("labelsignup")
        self.labelun = QtWidgets.QLabel(self.centralwidget)
        self.labelun.setGeometry(QtCore.QRect(30, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Champagne & Limousines")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelun.setFont(font)
        self.labelun.setObjectName("labelun")
        self.unsignup = QtWidgets.QLineEdit(self.centralwidget)
        self.unsignup.setGeometry(QtCore.QRect(160, 170, 221, 31))
        self.unsignup.setObjectName("unsignup")
        self.labelpw = QtWidgets.QLabel(self.centralwidget)
        self.labelpw.setGeometry(QtCore.QRect(30, 240, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Champagne & Limousines")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelpw.setFont(font)
        self.labelpw.setObjectName("labelpw")
        self.pwsignup = QtWidgets.QLineEdit(self.centralwidget)
        self.pwsignup.setGeometry(QtCore.QRect(160, 250, 221, 31))
        self.pwsignup.setObjectName("pwsignup")
        self.signupbutton = QtWidgets.QPushButton(self.centralwidget)
        self.signupbutton.setGeometry(QtCore.QRect(290, 390, 93, 28))
        self.signupbutton.setStyleSheet("background-color: rgb(226, 131, 180);\n"
"")
        self.signupbutton.setObjectName("signupbutton")
        self.labelcpw = QtWidgets.QLabel(self.centralwidget)
        self.labelcpw.setGeometry(QtCore.QRect(30, 330, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Champagne & Limousines")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelcpw.setFont(font)
        self.labelcpw.setObjectName("labelcpw")
        self.cpwsignup = QtWidgets.QLineEdit(self.centralwidget)
        self.cpwsignup.setGeometry(QtCore.QRect(160, 330, 221, 31))
        self.cpwsignup.setObjectName("cpwsignup")
        SignUp.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SignUp)
        self.statusbar.setObjectName("statusbar")
        SignUp.setStatusBar(self.statusbar)

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Sign Up"))
        self.labelsignup.setText(_translate("SignUp", "Sign Up"))
        self.labelun.setText(_translate("SignUp", "Username"))
        self.labelpw.setText(_translate("SignUp", "Password"))
        self.signupbutton.setText(_translate("SignUp", "Sign Up"))
        self.labelcpw.setText(_translate("SignUp", "Confirm Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUp = QtWidgets.QMainWindow()
    ui = Ui_SignUp()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())
