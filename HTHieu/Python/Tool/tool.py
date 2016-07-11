import string
import sys
import socket

from PySide.QtCore import *
from PySide.QtGui import *
import paramiko
from paramiko.ssh_exception import NoValidConnectionsError


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(300, 300, 300, 100)
        self.layout = QFormLayout()
        self.setLayout(self.layout)
        self.item()
        self.login()

    def item(self):
        self.lblDomain = QLabel("Domain")
        self.lblUser = QLabel("User")
        self.lblPassword = QLabel("Password")
        self.txtDomain = QLineEdit()
        self.txtUser = QLineEdit()
        self.txtPassword = QLineEdit()
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.btnConnect = QPushButton("Connect")
        self.btnExit = QPushButton("Exit")
        self.lblPath = QLabel("Path")
        self.txtPath = QLineEdit()
        self.btnPath = QPushButton("Get File")
        self.btnNewconnect = QPushButton("New Connect")
        self.txtFind = QLineEdit()
        self.btnFind = QPushButton("Find")
        self.txtReplace = QLineEdit()
        self.btnReplace = QPushButton("Replace")
        self.txtEdit = QTextEdit()
        self.txtEdit.setStyleSheet("QTextEdit {color:blue}")
        self.btnSubmit = QPushButton("Submit")
        self.lable = QLabel()
        self.txtEdit.setMaximumSize(10000, 1000)
        self.txtEdit.setMinimumSize(500, 500)
        self.btnExit.setMaximumSize(100, 100)
        self.btnSubmit.setMaximumSize(100, 100)
        self.btnNewconnect.setMaximumSize(100, 100)
        self.layout.addRow(self.lblDomain, self.txtDomain)
        self.layout.addRow(self.lblUser, self.txtUser)
        self.layout.addRow(self.lblPassword, self.txtPassword)
        self.layout.addRow(self.btnConnect, self.btnExit)
        self.layout.addRow(self.lblPath, self.txtPath)
        self.layout.addRow(self.btnPath, self.btnNewconnect)
        self.layout.addRow(self.btnFind, self.txtFind)
        self.layout.addRow(self.btnReplace, self.txtReplace)
        self.layout.addRow(self.lable)
        self.layout.addRow(self.txtEdit)
        self.layout.addRow(self.btnSubmit)

    def invi(self):
        self.lblDomain.setVisible(False)
        self.lblPassword.setVisible(False)
        self.lblPath.setVisible(False)
        self.lblUser.setVisible(False)
        self.txtEdit.setVisible(False)
        self.txtDomain.setVisible(False)
        self.txtFind.setVisible(False)
        self.txtPassword.setVisible(False)
        self.txtPath.setVisible(False)
        self.txtUser.setVisible(False)
        self.txtReplace.setVisible(False)
        self.btnNewconnect.setVisible(False)
        self.btnSubmit.setVisible(False)
        self.btnFind.setVisible(False)
        self.btnConnect.setVisible(False)
        self.btnExit.setVisible(False)
        self.btnReplace.setVisible(False)
        self.btnPath.setVisible(False)
        self.lable.setVisible(False)

    def login(self):
        self.invi()
        self.lblDomain.setVisible(True)
        self.lblPassword.setVisible(True)
        self.lblUser.setVisible(True)
        self.txtDomain.setVisible(True)
        self.txtPassword.setVisible(True)
        self.txtUser.setVisible(True)
        self.btnExit.setVisible(True)
        self.btnConnect.setVisible(True)
        self.btnExit.clicked.connect(self.exit)
        self.btnConnect.clicked.connect(self.SSHconnect)
        self.show()

    def exit(self):
        return sys.exit(True)

    def SSHconnect(self):
        domain = str(self.txtDomain.text())
        user = str(self.txtUser.text())
        password = str(self.txtPassword.text())
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=domain, username=user, password=password)
        except paramiko.BadHostKeyException, e:
            msg.setText(str(e))
            msg.exec_()
        except paramiko.AuthenticationException, e:
            msg.setText(str(e))
            msg.exec_()
        except paramiko.SSHException, e:
            msg.setText(str(e))
            msg.exec_()
        except TypeError, e:
            msg.setText(str(e))
            msg.exec_()
        except socket.gaierror, e:
            msg.setText(str(e))
            msg.exec_()
        except NoValidConnectionsError, e:
            msg.setText(str(e))
            msg.exec_()
        except socket.error, e:
            msg.setText(str(e))
            msg.exec_()
        else:
            msg.setText("Connect success to %s with %s" % (domain, user))
            btn = QPushButton("OK")
            msg.addButton(btn, msg.YesRole)
            msg.exec_()
            self.connect(btn, SIGNAL("clicked()"), self.getPath())
            login = open("login", "w")
            login.write("%s,%s,%s" % (domain, user, password))
            login.close()
            client.close()

    def getPath(self):
        self.invi()
        self.lblPath.setVisible(True)
        self.txtPath.setVisible(True)
        self.btnNewconnect.setVisible(True)
        self.btnPath.setVisible(True)
        self.btnNewconnect.clicked.connect(self.home)
        self.btnPath.clicked.connect(self.getfile)
        self.show()

    def home(self):
        self.invi()
        self.lblDomain.setVisible(True)
        self.lblPassword.setVisible(True)
        self.lblUser.setVisible(True)
        self.txtDomain.setVisible(True)
        self.txtPassword.setVisible(True)
        self.txtUser.setVisible(True)
        self.btnExit.setVisible(True)
        self.btnConnect.setVisible(True)
        self.show()

    def getfile(self):
        path = self.txtPath.text()
        f = open("login", "r")
        out = f.read()
        f.close()
        data = out.split(",")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=data[0], username=data[1], password=data[2])
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        try:
            sftp = client.open_sftp()
            sftp.get(path, "temp")
        except IOError, e:
            msg.setText(str(e))
            msg.exec_()
        else:
            f1 = open("path", "w")
            f1.write(path)
            f1.close()
            self.txtFind.setVisible(True)
            self.txtReplace.setVisible(True)
            self.btnFind.setVisible(True)
            self.btnReplace.setVisible(True)
            self.btnSubmit.setVisible(True)
            self.txtEdit.setVisible(True)
            self.lable.setVisible(True)
            self.lable.setText("Success")
            f1 = open("temp", "r")
            data = f1.read()
            f1.close()
            sftp.close()
            client.close()
            self.txtEdit.setText(data)
            self.btnFind.clicked.connect(self.find)
            self.btnReplace.clicked.connect(self.replace)
            self.btnSubmit.clicked.connect(self.check)

    def find(self):
        key = self.txtFind.text()
        cursor = self.txtEdit.textCursor()
        if cursor == QTextCursor.End or self.txtEdit.find(key) == False:
            cursor.movePosition(QTextCursor.Start)
            self.txtEdit.setTextCursor(cursor)
        self.txtEdit.find(key)

    def replace(self):
        content = str(self.txtEdit.toPlainText())
        find = self.txtFind.text()
        replace = self.txtReplace.text()
        data = content.replace(find, replace, 1)
        self.txtEdit.setText(data)

    def check(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setText("Do you want to change current file ?")
        btn=QPushButton("OK")
        btn1=QPushButton("Cancel")
        msg.addButton(btn,QMessageBox.YesRole)
        msg.addButton(btn1,QMessageBox.RejectRole)
        btn.clicked.connect(self.putfile)
        msg.exec_()

    def putfile(self):
        content = self.txtEdit.toPlainText()
        user = open("login", "r").read()
        out = user.split(",")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=out[0], username=out[1], password=out[2])
        sftp = client.open_sftp()
        path = open("path", "r").read()
        open("temp", "w").write(content)
        sftp.put("temp", path)
        self.lable.setText("Change File Success")
        sftp.close()
        client.close()

app = QApplication(sys.argv)
GUI = Window()
sys.exit(app.exec_())
