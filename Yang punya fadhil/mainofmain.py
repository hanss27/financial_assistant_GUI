from posixpath import expanduser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt, QDate
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QMessageBox
import os, sys, csv
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
        login.clear()
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def signupbtn(self):
        print("Sign up Button") 
        signup.clear()
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
        self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")
        
        #SET PASSWORD
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setStyleSheet('lineedit-password-character: 9679')

    def clear(self):
        print("test clear")
        self.username.clear()
        self.password.clear()
        self.cond.clear()

    def visible(self):
        self.co +=1
        if (self.co%2 == 0): #Cek Ganjil Genap
            print("Visible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.visiblebutton.setStyleSheet("background-image : url(img/visible.png);")

        else:
            print("Invisible")
            self.password.setEchoMode(QtWidgets.QLineEdit.Password)
            self.password.setStyleSheet('lineedit-password-character: 9679')      
            self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")

    def login(self):
        print("Login Button")
        counter = 0
        user = self.username.text()
        password = self.password.text()
        self.cond.setStyleSheet("color: red;")
        count = 0
        for i in rows :
            count += 1
            if i[0] == user:
                print("Username is correct")
                counter += 1
                if i[1] == password:
                    print("Access Granted")
                    self.cond.setStyleSheet("color: green;")
                    self.cond.setText("Login Succesfull!")
                    main  = Main(count-1)
                    widget.addWidget(main)
                    finstat = Finstat()
                    widget.addWidget(finstat)
                    break
                    
                else:
                    self.cond.setText("Password is incorrect")
                    break         
        if counter == 0:
            self.cond.setText("Username or Password is incorrect")
        
        if self.cond.text() == "Login Succesfull!":
                
                widget.setFixedHeight(686)
                widget.setFixedWidth(660)
                widget.setCurrentIndex(widget.currentIndex()+2)
        
        
    def signup(self):
        print("Sign up Button") 
        signup.clear()
        widget.setFixedHeight(542)
        widget.setFixedWidth(476)
        widget.setCurrentIndex(widget.currentIndex()+1)

class Signup(QtWidgets.QMainWindow): #QtWidgets.QDialog
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("signup.ui", self)
        self.mainbutton.clicked.connect(self.main)
        self.signupbutton.clicked.connect(self.Signup)
        self.visiblebutton.clicked.connect(self.visible)
        self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")
        self.visiblebutton_2.clicked.connect(self.visible_cpw)
        self.visiblebutton_2.setStyleSheet("background-image : url(img/invisible.png);")
        self.co = 1

        #SET PASSWORD
        self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwsignup.setStyleSheet('lineedit-password-character: 9679')
        self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpwsignup.setStyleSheet('lineedit-password-character: 9679')

    def clear(self):
        print("test clear")
        self.unsignup.clear()
        self.pwsignup.clear()
        self.cpwsignup.clear()
        self.cond.clear()

    def visible(self):
            self.co +=1
            if (self.co%2 == 0):
                print("Invisible")
                self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.visiblebutton.setStyleSheet("background-image : url(img/visible.png);")

            else:
                print("Visible")
                self.pwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
                self.pwsignup.setStyleSheet('lineedit-password-character: 9679')         
                self.visiblebutton.setStyleSheet("background-image : url(img/invisible.png);")

    def visible_cpw(self):
            self.co +=1
            if (self.co%2 == 0):
                print("Visible")
                self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Normal)
                self.visiblebutton_2.setStyleSheet("background-image : url(img/visible.png);")

            else:
                print("Invisible")
                self.cpwsignup.setEchoMode(QtWidgets.QLineEdit.Password)
                self.cpwsignup.setStyleSheet('lineedit-password-character: 9679')      
                self.visiblebutton_2.setStyleSheet("background-image : url(img/invisible.png);")

    def Signup(self):
        print("Signup Button")
        user = self.unsignup.text()
        password = self.pwsignup.text()
        password2 =self.cpwsignup.text()
        self.cond.setStyleSheet("color: red;")

        with open('database.csv',mode='a', newline='') as file:
            Writer = csv.writer(file,delimiter=",")
            self.signcounter = 0
            for line in rows : 
                if line[0] != user:
                    print("Username allowed")
                    self.signcounter += 1
                else:
                    print("Username existed!")
                    self.cond.setStyleSheet("color: red;")
                    self.cond.setText("Username already existed!")
                    break

            if (self.signcounter == len(rows)):
                if password == password2:
                    self.cond.setStyleSheet("color : green")
                    self.cond.setText("Account Created!")
                    Writer.writerow([user,password])
                    rows.append([user,password])
                else:
                    self.cond.setStyleSheet("color: red;")
                    self.cond.setText("Confirm Error!")
        file.close()
    def main(self):
        print("Back to main")        
        widget.setFixedHeight(201)
        widget.setFixedWidth(421)
        widget.setCurrentIndex(widget.currentIndex()-2)

class Main(QtWidgets.QMainWindow):
    
    def __init__(self,logincounter):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("main.ui", self)
       
        self.finstatbtn.clicked.connect(self.finstatwin)
        self.finstatbtn2.clicked.connect(self.finstatwin)
        self.logincounter = logincounter
        print(len(transrows))
        if len(transrows) > logincounter:       
            for i in transrows[self.logincounter]:
                y = i.split(";") 
                y[2] = int(y[2])
                trans.append(y) 

    def finstatwin(self):
            print("Finstat Button")
            widget.setCurrentIndex(widget.currentIndex()+1)
            
    def loaddata(self):
        # Load Database
        print(self.logincounter)
        
class Finstat(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("finstat.ui", self)
        count = 0
        
        tempdate = []
        tempinc = []
        tempexp = []
        tempsuminc = 0
        tempsumexp = 0
        if len(trans) != 0:
            for i in trans:
                count += 1
                moncounter = i[0][0:7]
                mon = monthlist[int(moncounter[5:7])-1] + " "
                mon += moncounter[0:4]
                datelbl = i[0][8:10] + " " + mon
                print(datelbl)
                print(mon)
                if count == 1:
                    month.append(mon)
                    self.monthselector.addItem(mon)
                    self.monthlabel.setText(mon)       
                if month[len(month)-1] == mon:
                    tempdate.append(datelbl)  
                    if i[2] > 0:
                        tempinc.append(i[2])
                        tempexp.append(0)
                        tempsuminc += i[2]
                    elif i[2] < 0:
                        expe = i[2] * -1
                        tempinc.append(0)
                        tempexp.append(expe)
                        tempsumexp += expe
                else:
                    self.monthselector.addItem(mon)
                    month.append(mon)
                    inc.append(tempinc[:])
                    exp.append(tempexp[:])
                    suminc.append(tempsuminc)
                    sumexp.append(tempsumexp)

                    date.append(tempdate[:])

                    tempdate.clear()
                    tempinc.clear()
                    tempexp.clear()
                    tempsuminc = 0
                    tempsumexp = 0

                    tempdate.append(i[0])
                    if i[2] > 0:
                        tempinc.append(i[2])
                        tempexp.append(0)
                        tempsuminc += i[2]
                    elif i[2] < 0:
                        expe = i[2] * -1
                        tempinc.append(0)
                        tempexp.append(expe)
                        tempsumexp += expe
            date.append(tempdate[:])

            inc.append(tempinc)
            exp.append(tempexp)
            suminc.append(tempsuminc)
            sumexp.append(tempsumexp)
      
        else:
            self.monthlabel.setText("-")
            self.monthincome.setText("-")
            self.monthexpen.setText("-")
        
        #First initialize on UI
        self.disp(0)
        balance = sum(suminc) - sum(sumexp)
        balancelbl = "Rp.%d" % balance
        self.balancemoney.setText(balancelbl)
        self.monthselector.currentIndexChanged.connect(self.disp)


    def disp(self,co):
        for i in range(len(date[co])):
            a = i+1
            datelbl = "top%dlabel" % a
            if inc[co][i] != 0:
                inclbl = "Rp.%d" % inc[co][i]
            else:
                inclbl = "-"
            if exp[co][i] != 0:
                explbl = "Rp.%d" % exp[co][i]
            else:
                explbl = "-"
            incomelbl = "top%dlabelinc" % a
            expenlbl = "top%dlabelexp" % a
            transdate = "self.%s.setText(date[co][i])" % datelbl
            transinc = "self.%s.setText(inclbl)" % incomelbl
            transexp = "self.%s.setText(explbl)" % expenlbl 
            exec(transdate)
            exec(transinc)
            exec(transexp)
        suminclbl= "Rp.%d" % suminc[co]
        sumexplbl = "Rp.%d" % sumexp[co]
        self.monthlabel.setText(month[co])
        self.monthincome.setText(suminclbl)
        self.monthexpen.setText(sumexplbl)
class Exin(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("transaction.ui", self)
        self.open_file()
        print(self.transaction)
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.transactData = []
        self.dateselected = QDate.currentDate().toPyDate()
        self.date.setDisplayFormat("d MMM yyyy")
        self.date.setDateTime(QtCore.QDateTime.currentDateTime())
        self.savebutton.setEnabled(False)
        self.savebutton.setStyleSheet("background-color:rgb(226,226,226);border-width: 2px;border-radius: 20px;padding: 4px;")
        self.balancemoney.setText(str(self.balance))
        self.savebutton.clicked.connect(self.Save)
        self.confirmbutton1.clicked.connect(self.conf1)
        self.confirmbutton2.clicked.connect(self.conf2)
        self.date.dateChanged.connect(self.set_date)
        self.tabWidget.currentChanged.connect(self.tabChanged)

    def open_file(self):
        with open('income.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            self.balance = 0
            self.transaction = []
            self.header = []
            self.header = next(csv_reader)
            for row in csv_reader:
                self.balance = self.balance + int(row[1])
                self.transaction.append(row)

    def tabChanged(self):
        if self.tabWidget.currentIndex() == 0:
            self.expline.clear()
            self.note.clear()
            self.date.setDateTime(QtCore.QDateTime.currentDateTime())
            print(self.tabWidget.currentIndex())
        elif self.tabWidget.currentIndex() == 1:
            self.incline.clear()
            self.note.clear()
            self.date.setDateTime(QtCore.QDateTime.currentDateTime())
            print(self.tabWidget.currentIndex())

    def conf1(self):
        income = self.incline.text()
        try:
            income = int(income)
            self.trans = int(income)
            self.savebutton.setEnabled(True)
            self.savebutton.setStyleSheet("background-color: rgb(85, 255, 0);border-width: 2px;border-radius: 20px;padding: 4px;")
        except:
            warn = QMessageBox()
            warn.setWindowFlag(Qt.FramelessWindowHint)
            #warn.setStyleSheet("background-color:white;")
            warn.setText("Invalid Input!")
            warn.setIcon(QMessageBox.Warning)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setDefaultButton(QMessageBox.Ok)
            x = warn.exec_()
            pass
        
    def conf2(self): 
        expenditure = self.expline.text()
        try:
            expenditure = int(expenditure)
            self.trans = int(expenditure)*-1
            self.savebutton.setEnabled(True)
            self.savebutton.setStyleSheet("background-color: rgb(85, 255, 0);border-width: 2px;border-radius: 20px;padding: 4px;")
        except:
            warn = QMessageBox()
            warn.setWindowFlag(Qt.FramelessWindowHint)
            #warn.setStyleSheet("background-color:white;")
            warn.setText("Invalid Input!")
            warn.setIcon(QMessageBox.Warning)
            warn.setStandardButtons(QMessageBox.Ok)
            warn.setDefaultButton(QMessageBox.Ok)
            x = warn.exec_()
            pass
    
    def set_date(self):
        self.dateselected = self.date.date().toPyDate()

    def Save(self):
        note = self.note.text()
        if note == '':
            note = '-'  
        self.balance += self.trans 
        self.datepicked = str(self.dateselected)
        self.balancemoney.setText(str(self.balance))
        '''
        if self.trans < 0:
            trans =  "'" + str(self.trans)
        else:
            trans = str(self.trans)
            
        self.transactData.append(self.datepicked)
        self.transactData.append(trans)
        self.transactData.append(note)
        #transactData = self.datepicked+';'+trans+';'+note
        print(self.transactData)
        '''
        if self.transaction[0] == []:
            self.transaction[0] = [str(self.dateselected), str(self.trans), note]
        else:
            self.transaction.append([str(self.dateselected), str(self.trans), note])
        
        print(self.transaction)
        self.transaction.sort()
        self.transaction.reverse() 
        print(self.transaction)
        self.datepicked = None
        self.trans = 0
        self.incline.clear()
        self.expline.clear()
        self.note.clear()
        self.savebutton.setEnabled(False)
        self.savebutton.setStyleSheet("background-color:rgb(226,226,226);border-width: 2px;border-radius: 20px;padding: 4px;")
        self.popup()

    def record(self):
        with open('income.csv',mode='w', newline = '') as file:
            writer = csv.writer(file,delimiter=",")
            writer.writerow(self.header)
            for row in self.transaction:
                writer.writerow(row)
    def popup(self):
        msg = QMessageBox()
        msg.setWindowFlag(Qt.FramelessWindowHint)
        msg.setText("Transaksi Anda Telah Disimpan!")
        #msg.setStyleSheet("background-color:white;")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setDefaultButton(QMessageBox.Ok)
        x = msg.exec_()
        
#Load Database
file = open('database.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
monthlist = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Des"]
for row in csvreader:
    rows.append(row)
file.close()

month = []
date = []
inc = []
exp =[]
suminc = []
sumexp = []
balance = 0
file2 = open('income.csv')
csvreader = csv.reader(file2)
headerinc = []
headerinc = next(csvreader)
transrows = []
trans = []
for row in csvreader:
    transrows.append(row)
file.close()

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