import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyApplication(QWidget):
   def __init__(self):
	  #The the super class constructor
	  QWidget.__init__(self) 
	  
	  #set the layout of the current widget
	  self.layout = QVBoxLayout(self)

	  #creating widgets & adding them to the layout created
	  self.label = QLabel("GSoC",self)
	  self.layout.addWidget(self.label)

	  self.edit = QLineEdit("KDE",self)
	  self.layout.addWidget(self.edit)

	  #a single line like this can create and any widget to the 
	  #layout provided we no more need the reference to it
	  self.layout.addWidget(QPushButton("hello",self))
	  
	  #set the geometry if required
	  #self.setGeometry(300, 300, 250, 500)

	  #setting window title
	  #self.setWindowTitle('Icon')

	  #setting window icon
	  #self.setWindowIcon(QIcon('web.png'))
   
