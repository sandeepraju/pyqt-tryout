import sys
from PyQt4.QtGui import *
from myapplication import *

def main():
   app = QApplication(sys.argv)
   window = MyApplication()
   window.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
   main()
