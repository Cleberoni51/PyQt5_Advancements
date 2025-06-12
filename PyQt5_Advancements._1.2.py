#PyQt5_Advancements
#Caleb Schear
#20250609-CS-PyQt5_Advancements.py

import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc

class MainWindow(qtw.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(1000,250)
        self.setWindowTitle("PyQt5")
        self.label = qtw.QLabel(self)
        self.label.setText("Hello World")
        font = qtg.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.move(50,20)

def main():
    app = qtw.QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()