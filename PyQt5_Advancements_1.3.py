
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
        self.number = str("")
        #Put some code here
        
        self.LabelAnswer = qtw.QLabel(self)
        self.LabelNumber = qtw.QLabel(self)
        self.LabelOperation = qtw.QLabel(self)

        box = qtw.QVBoxLayout()
        box0 = qtw.QHBoxLayout()
        box1 = qtw.QHBoxLayout()
        box1p1 = qtw.QVBoxLayout()
        box1p1p1 = qtw.QHBoxLayout()
        box1p1p2 = qtw.QHBoxLayout()
        box1p1p3 = qtw.QHBoxLayout()
        box1p1p4 = qtw.QHBoxLayout()
        box1p2 = qtw.QVBoxLayout()

        self.Seven = qtw.QPushButton("7", clicked = lambda:PushSeven())

        def PushSeven() :
            self.number = str(self.number+"7")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Eight = qtw.QPushButton("8", clicked = lambda:PushEight())

        def PushEight() :
            self.number = str(self.number+"8")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Nine = qtw.QPushButton("9", clicked = lambda:PushNine())
        
        def PushNine() :
            self.number = str(self.number+"9")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Four = qtw.QPushButton("4", clicked = lambda:PushFour())
        
        def PushFour() :
            self.number = str(self.number+"4")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Five = qtw.QPushButton("5", clicked = lambda:PushFive())
        
        def PushFive() :
            self.number = str(self.number+"5")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Six = qtw.QPushButton("6", clicked = lambda:PushSix())
        
        def PushSix() :
            self.number = str(self.number+"6")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.One = qtw.QPushButton("1", clicked = lambda:PushOne())
        
        def PushOne() :
            self.number = str(self.number+"1")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Two = qtw.QPushButton("2", clicked = lambda:PushTwo())
        
        def PushTwo() :
            self.number = str(self.number+"2")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Three = qtw.QPushButton("3", clicked = lambda:PushThree())
        
        def PushThree() :
            self.number = str(self.number+"3")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Decimal = qtw.QPushButton(".", clicked = lambda:PushDecimal())
        
        def PushDecimal() :
            self.number = str(self.number+".")
            self.LabelAnswer.setText(f"{self.number}")
            return self.number
        
        self.Zero = qtw.QPushButton("0", clicked = lambda:PushZero())
        
        def PushZero() :
            self.number = str(self.number+"0")
            self.LabelAnswer.setText(f"{self.number}") 
            return self.number
        
        self.Negate = qtw.QPushButton("(-)", clicked = lambda:PushNegate())
        self.a = False
        def PushNegate() :
            if self.a == False :
                self.number = str("-"+self.number)
                self.LabelAnswer.setText(f"{self.number}")
                self.a = True
            else :
                self.number = str(self.number.replace("-", ""))
                self.LabelAnswer.setText(f"{self.number}")
                self.a = False
            return self.number
        
        self.Divide = qtw.QPushButton("/", clicked = lambda:PushDivide())

        def PushDivide() :
            self.number = str(self.number.replace(" x ", ""))
            self.number = str(self.number.replace(" + ", ""))
            self.number = str(self.number.replace(" / ", ""))
            self.number = str(self.number.replace(" - ", ""))
            self.number = str(self.number+" / ")
            self.LabelAnswer.setText(f"{self.number}") 
            return self.number

        self.Multiply = qtw.QPushButton("x", clicked = lambda:PushMultiply())

        def PushMultiply() :
            self.number = str(self.number.replace(" / ", ""))
            self.number = str(self.number.replace(" + ", ""))
            self.number = str(self.number.replace(" - ", ""))
            self.number = str(self.number.replace(" x ", ""))
            self.number = str(self.number+" x ")
            self.LabelAnswer.setText(f"{self.number}") 
            return self.number

        self.Minus = qtw.QPushButton("-", clicked = lambda:PushMinus())

        def PushMinus() :
            self.number = str(self.number.replace(" x ", ""))
            self.number = str(self.number.replace(" + ", ""))
            self.number = str(self.number.replace(" / ", ""))
            self.number = str(self.number.replace(" - ", ""))
            self.number = str(self.number+" - ")
            self.LabelAnswer.setText(f"{self.number}") 
            return self.number

        self.Plus = qtw.QPushButton("+", clicked = lambda:PushPlus())

        def PushPlus() :
            self.number = str(self.number.replace(" x ", ""))
            self.number = str(self.number.replace(" / ", ""))
            self.number = str(self.number.replace(" - ", ""))
            self.number = str(self.number.replace(" + ", ""))
            self.number = str(self.number+" + ")
            self.LabelAnswer.setText(f"{self.number}") 
            return self.number

        self.Equal = qtw.QPushButton("=", clicked = lambda:PushEqual())

        def PushEqual() :
            self.LabelAnswer.setText(f"{self.number}")

        self.Clear = qtw.QPushButton("clr", clicked = lambda:PushClear())

        def PushClear() :
            self.number = ""
            self.LabelAnswer.setText("0.0")
            return self.number

        box0.addWidget(self.LabelAnswer)
        self.LabelAnswer.setText("0")
        #self.LabelAnswer.setText("Hello Answer")
        self.LabelAnswer.setStyleSheet("text-align:right;")

        #box1p1.addWidget(self.LabelNumber)
        #self.LabelNumber.setText("Hello Number")
        #self.LabelNumber.setStyleSheet("background-color: orange")
        box1p1p1.addWidget(self.Seven)
        box1p1p1.addStretch()
        box1p1p1.addWidget(self.Eight)
        box1p1p1.addStretch()
        box1p1p1.addWidget(self.Nine)
        #box1p1p1.addStretch()
        box1p1p2.addWidget(self.Four)
        box1p1p2.addStretch()
        box1p1p2.addWidget(self.Five)
        box1p1p2.addStretch()
        box1p1p2.addWidget(self.Six)
        #box1p1p2.addStretch()
        box1p1p3.addWidget(self.One)
        box1p1p3.addStretch()
        box1p1p3.addWidget(self.Two)
        box1p1p3.addStretch()
        box1p1p3.addWidget(self.Three)
        #box1p1p3.addStretch()
        box1p1p4.addWidget(self.Decimal)
        box1p1p4.addStretch()
        box1p1p4.addWidget(self.Zero)
        box1p1p4.addStretch()
        box1p1p4.addWidget(self.Negate)

        #box1p2.addWidget(self.LabelOperation)
        #self.LabelOperation.setText("Hello Operation")
        #self.LabelOperation.setStyleSheet("background-color: red")

        box1p2.addWidget(self.Divide)
        box1p2.addWidget(self.Multiply)
        box1p2.addWidget(self.Minus)
        box1p2.addWidget(self.Plus)
        box1p2.addWidget(self.Equal)
        box1p2.addWidget(self.Clear)

        #hbox4.addStretch()


        #vbox.addStretch()
        
        #hbox.
        box.addLayout(box0)
        box.addLayout(box1)
        box1.addLayout(box1p1)
        box1.addLayout(box1p2)
        box1p1.addLayout(box1p1p1)
        box1p1.addLayout(box1p1p2)
        box1p1.addLayout(box1p1p3)
        box1p1.addLayout(box1p1p4)
        self.setLayout(box)
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