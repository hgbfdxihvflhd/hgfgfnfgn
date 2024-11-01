import sys
import pickle
from random import random, choice

from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from uiN9683253 import *


app=QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()








sys.exit(app.exec())