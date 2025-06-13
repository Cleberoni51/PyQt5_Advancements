
#PyQt5_Advancements
#Caleb Schear
#20250612-CS-PyQt5_Advancements_1.3.py

import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import PyQt5.QtCore as qtc


class MainWindow(qtw.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(1000,250)
        self.setWindowTitle("PyQt5")
        #self.label = qtw.QLabel(self)
        #self.label.setText("Hello World")
        font = qtg.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        #self.label.setFont(font)
        #self.label.move(50,20)

        #Add a Title for your Widget
        self.setWindowTitle("Caleb's Calculator")
        

        #Put some code here

        self.b0 = qtw.QPushButton("Button0")
        self.b1 = qtw.QPushButton("Button1")
        self.b2 = qtw.QPushButton("Button2")
        self.b3 = qtw.QPushButton("Button3")
        self.b4 = qtw.QPushButton("Button4")
        self.b5 = qtw.QPushButton("Button5")
        self.b6 = qtw.QPushButton("Button6")
        self.b7 = qtw.QPushButton("Button7")
        self.b8 = qtw.QPushButton("Button8")
        self.b9 = qtw.QPushButton("Button9")
        self.b10 = qtw.QPushButton("Button10")
        self.b11 = qtw.QPushButton("Button11")
        self.b12 = qtw.QPushButton("Button12")
        self.b13 = qtw.QPushButton("Button13")
        self.b14 = qtw.QPushButton("Button14")
        self.b15 = qtw.QPushButton("Button15")
        self.b16 = qtw.QPushButton("Button16")
        self.b17 = qtw.QPushButton("Button17")
        self.b18 = qtw.QPushButton("Button18")
        self.b19 = qtw.QPushButton("Button19")


        hbox1 = qtw.QHBoxLayout()
        hbox2 = qtw.QHBoxLayout()
        hbox3 = qtw.QHBoxLayout()
        hbox4 = qtw.QHBoxLayout()
        vbox = qtw.QVBoxLayout()

        hbox1.addWidget(self.b1)
        hbox1.addStretch()
        hbox1.addWidget(self.b2)
        hbox1.addStretch()
        hbox1.addWidget(self.b3)
        hbox1.addStretch()
        hbox1.addWidget(self.b4)

        vbox.addStretch()

        hbox2.addWidget(self.b5)
        hbox2.addStretch()
        hbox2.addWidget(self.b6)
        hbox2.addStretch()
        hbox2.addWidget(self.b7)
        hbox2.addStretch()
        hbox2.addWidget(self.b8)

        vbox.addStretch()

        hbox3.addWidget(self.b9)
        hbox3.addStretch()
        hbox3.addWidget(self.b10)
        hbox3.addStretch()
        hbox3.addWidget(self.b11)
        hbox3.addStretch()
        hbox3.addWidget(self.b12)

        vbox.addStretch()

        hbox4.addWidget(self.b13)
        hbox4.addStretch()
        hbox4.addWidget(self.b14)
        hbox4.addStretch()
        hbox4.addWidget(self.b15)
        hbox4.addStretch()
        hbox4.addWidget(self.b16)

        vbox.addStretch()
        
        #hbox.
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        self.setLayout(vbox)
        #Yep right there


def main():
    app = qtw.QApplication(sys.argv)
    ex = MainWindow()
    win = qtw.QWidget()
    grid = qtw.QGridLayout()
    ex.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()