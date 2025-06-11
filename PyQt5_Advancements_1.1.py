
#PyQt5_Advancements
#Caleb Schear
#20250609-CS-PyQt5_Advancements.py

import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()








        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()