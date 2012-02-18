import sys, urllib2
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyApplication(QWidget):
   def __init__(self):
	  #The the super class constructor
	  QWidget.__init__(self) 
	  
	  #set the layout of the current widget
	  self.layout = QVBoxLayout(self)

	  #creating widgets & adding them to the layout created
	  self.label = QLabel("IMDB Fetcher",self)
	  self.layout.addWidget(self.label)

	  self.edit = QLineEdit("",self)
	  self.edit.setPlaceholderText("Enter a movie name")
	  self.layout.addWidget(self.edit)

	  #a single line like this can create and any widget to the 
	  #layout provided we no more need the reference to it
	  self.fetch = QPushButton("Fetch!",self)
	  self.layout.addWidget(self.fetch)
	  self.connect(self.fetch, SIGNAL("clicked()"),\
			        self, SLOT(self.slotFetchData()))

	  #set the geometry if required
	  #self.setGeometry(300, 300, 250, 500)

	  #setting window title
	  #self.setWindowTitle('Icon')
	  #setting window icon
	  #self.setWindowIcon(QIcon('web.png'))

   def slotFetchData(self):
	  qDebug("hello...?")
	  response = urllib2.urlopen("http://www.imdbapi.com?t=avatar" + str(self.edit.text()))
	  response = eval(response.read())
	  tempHLayout = QHBoxLayout(self)
	  #if response == Parse Error -> display error
	  #if response ==
	  #QWebKit()
	  tempHLayout.addWidget(QLabel("Title: ", self))
	  tempHLayout.addWidget(QLabel(response["Title"],self))
	  self.layout.addItem(tempHLayout)
   
