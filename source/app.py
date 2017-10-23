import sys
import os
from PyQt4 import QtGui
import subprocess
import main
import socket
REMOTE_SERVER = "www.google.com"

class Mainframe(QtGui.QMainWindow, main.Ui_MainWindow):
    #
    # def __init__(self):
    #     super(self.__class__, self).__init__()


    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pentestBtn.clicked.connect(self.installPentest)
        self.studentBtn.clicked.connect(self.installStudent)
        self.designBtn.clicked.connect(self.installDesign)
        self.devBtn.clicked.connect(self.installDev)


    def run_command(self,command):
        p = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return iter(p.stdout.readline, b'')

    def installPentest(self):
        command = ['gksu ./bin/hack']
        for line in self.run_command(command):
            self.label_7.setText(line)
            print(line)

    def installStudent(self):
        command = ['gksu ./bin/student']
        for line in self.run_command(command):
            self.label_7.setText(line)
            print(line)

    def installDesign(self):
        command = ['gksu ./bin/design']
        for line in self.run_command(command):
            self.label_7.setText(line)
            print(line)

    def installDev(self):
        command = ['gksu ./bin/developer']
        for line in self.run_command(command):
            self.label_7.setText(line)
            print(line)

def is_connected():
  try:
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False


def apps():
    app = QtGui.QApplication(sys.argv)
    mainpage = Mainframe()
    mainpage.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    apps()
