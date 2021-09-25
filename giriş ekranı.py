import sys
from PyQt5 import QtWidgets
import sqlite3
from girişdb import *

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.Database = database()
    def init_ui(self):

        self.setGeometry(1400,200,300,300)
        self.setWindowTitle("LOGIN")

        self.text =QtWidgets.QLabel()
        self.text.setText("Please Login or Sign in")


        #Username alanı
        self.username = QtWidgets.QLabel()
        self.username.setText("Username")


        self.usernameI=QtWidgets.QLineEdit()


        #Password alanı
        self.password=QtWidgets.QLabel()
        self.password.setText("Password")


        self.passwordI = QtWidgets.QLineEdit()



        #Login butonu
        self.login=QtWidgets.QPushButton()
        self.login.setText("Login")


        #Signin butonu
        self.signin = QtWidgets.QPushButton()
        self.signin.setText("Sign in")


        #hbox
        #username
        h1_box=QtWidgets.QHBoxLayout()
        h1_box.addStretch()
        h1_box.addWidget(self.username)
        h1_box.addWidget(self.usernameI)
        h1_box.addStretch()
        #password
        h2_box=QtWidgets.QHBoxLayout()
        h2_box.addStretch()
        h2_box.addWidget(self.password)
        h2_box.addWidget(self.passwordI)
        h2_box.addStretch()
        #butonlar
        h3_box = QtWidgets.QHBoxLayout()
        h3_box.addStretch()
        h3_box.addWidget(self.login)
        h3_box.addWidget(self.signin)
        h3_box.addStretch()
        #text
        h4_box=QtWidgets.QHBoxLayout()
        h3_box.addStretch()
        h4_box.addWidget(self.text)
        h3_box.addStretch()
        #vbox
        v_box=QtWidgets.QVBoxLayout()
        v_box.addStretch()
        v_box.addLayout(h4_box)
        v_box.addLayout(h1_box)
        v_box.addLayout(h2_box)
        v_box.addLayout(h3_box)
        v_box.addStretch()
        self.setLayout(v_box)


        self.login.clicked.connect(self.loginclick)
        self.signin.clicked.connect(self.signinclick)

        self.show()
    def loginclick(self):
        usr =self.usernameI.text()
        paswd =self.passwordI.text()

        if(self.Database.controlp(usr,paswd)):
                self.text.setText("Hoşgeldin {}".format(usr))
        else:
                self.text.setText("Yanlış kullanıcı adı veya şifre\nTekrar deneyiniz")



    def signinclick(self):
        usr = self.usernameI.text()
        paswd = self.passwordI.text()
        if(self.Database.controlu(usr)):
            self.text.setText("Bu kullanıcı adı mevcut")
        else:
            self.Database.adduser(usr,paswd)
            self.text.setText("Kullanıcı kaydedildi")






app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
