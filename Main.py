from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys, math, csv
from PyQt5.uic import loadUi


class Greet(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("Greet.ui", self)

        #If the button is pushed
        self.button1.clicked.connect(self.loginbtn)
        self.button2.clicked.connect(self.signupbtn)
    
    def loginbtn(self):
        print("Login Button")
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupbtn(self):
        print("Sign up Button") 
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+2)

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.co = 1
    
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.login)
        self.createaccbutton.clicked.connect(self.signup) 
        self.visiblebutton.clicked.connect(self.visible)
        self.visiblebutton.setStyleSheet("background-image : url(invisible.png);")

        
        #SET PASSWORD
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet('lineedit-password-character: 9679')

    def visible(self):
        self.co +=1
        if (self.co%2 == 0):
            print("Invisible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.visiblebutton.setStyleSheet("background-image : url(visible.png);")

        else:
            print("Visible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password.setStyleSheet('lineedit-password-character: 9679')      
            self.visiblebutton.setStyleSheet("background-image : url(invisible.png);")

    def login(self):
        print("Login Button")
        counter = 0
        user = self.username.text()
        password = self.password.text()
        self.cond.setStyleSheet("color: red;")

        for i in rows :
            if i[0] == user:
                print("Username is correct")
                counter += 1
                if i[1] == password:
                    print("Access Granted")
                    self.cond.setStyleSheet("color: green;")
                    self.cond.setText("Login Succesfull!")
                    counter += 1
                    break
                else:
                    self.cond.setText("Password is incorrect")
                    break         
        if counter == 0:
            self.cond.setText("Username or Password is incorrect")

    def signup(self):
        print("Sign up Button") 
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Signup(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("signup.ui", self)
        self.mainbutton.clicked.connect(self.main)

    def main(self):
        print("Back to main")        
        widget.setFixedHeight(201)
        widget.setFixedWidth(421)
        widget.setCurrentIndex(widget.currentIndex()-2)



#Load Database
file = open('database.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

#Call Qt
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
greet= Greet()
login = Login()
signup = Signup()
widget.addWidget(greet)
widget.addWidget(login)
widget.addWidget(signup)
widget.setFixedHeight(201)
widget.setFixedWidth(421)
widget.show()

try :
    sys.exit(app.exec_())
except:
    print("Exiting")