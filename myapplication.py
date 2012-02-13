import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyApplication(QMainWindow):
   def __init__(self):
	  QMainWindow.__init__(self)
	  self.mainWindow = QMainWindow(self)
	  self.layout = QVBoxLayout()
	  self.layout.addWidget(QLabel("HelloWorld"))
	  self.layout.addWidget(QLineEdit("hello"))
	  self.mainWindow.setLayout(self.layout)
	  self.setGeometry(300, 300, 250, 500)
	  self.setWindowTitle('Icon')
	  self.setWindowIcon(QIcon('web.png'))
	  self.setCentralWidget(self.mainWindow)
   
