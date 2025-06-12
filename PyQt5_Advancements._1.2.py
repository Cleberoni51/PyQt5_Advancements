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
        #self.label = qtw.QLabel(self)
        #self.label.setText("Hello World")
        font = qtg.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        #self.label.setFont(font)
        #self.label.move(50,20)

        #Add a Title for your Widget
        self.setWindowTitle("Caleb's Calculator")

        #set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        #def SevenFunc():

        grid = qtw.QGridLayout()

        seven_button = qtw.QPushButton("7")#, clicked = lambda:SevenFunc())
        #self.layout().addWidget(seven_button)
        self.grid.addWidget(seven_button, 1,1)
        eight_button = qtw.QPushButton("8")#, clicked = lambda:EightFunc())
        #self.layout().addWidget(eight_button)
        grid.addWidget(eight_button, 1,2)
        nine_button = qtw.QPushButton("9")#, clicked = lambda:NineFunc())
        #self.layout().addWidget(nine_button)
        grid.addWidget(nine_button, 1,3)
        divide_button = qtw.QPushButton("/")#, clicked = lambda:DivideFunc())
        #self.layout().addWidget(divide_button)
        grid.addWidget(divide_button, 1,4)


        four_button = qtw.QPushButton("4")#, clicked = lambda:FourFunc())
        #self.layout().addWidget(four_button)
        grid.addWidget(four_button)
        five_button = qtw.QPushButton("5")#, clicked = lambda:FiveFunc())
        #self.layout().addWidget(five_button)
        grid.addWidget(five_button)
        six_button = qtw.QPushButton("6")#, clicked = lambda:SixFunc())
        #self.layout().addWidget(six_button)
        grid.addWidget(six_button)
        multiply_button = qtw.QPushButton("x")#, clicked = lambda:MulitplyFunc())
        #self.layout().addWidget(multiply_button)
        grid.addWidget(multiply_button)


        one_button = qtw.QPushButton("1")#, clicked = lambda:OneFunc())
        #self.layout().addWidget(one_button)
        grid.addWidget(one_button)
        two_button = qtw.QPushButton("2")#, clicked = lambda:TwoFunc())
        #self.layout().addWidget(two_button)
        grid.addWidget(two_button)
        three_button = qtw.QPushButton("3")#, clicked = lambda:ThreeFunc())
        #self.layout().addWidget(three_button)
        grid.addWidget(three_button)
        minus_button = qtw.QPushButton("-")#, clicked = lambda:MinusFunc())
        #self.layout().addWidget(minus_button)
        grid.addWidget(minus_button)


        zero_button = qtw.QPushButton("0")#, clicked = lambda:ZeroFunc())
        #self.layout().addWidget(zero_button)
        grid.addWidget(zero_button)
        decimal_button = qtw.QPushButton(".")#, clicked = lambda:DecimalFunc())
        #self.layout().addWidget(decimal_button)
        grid.addWidget(decimal_button)
        negate_button = qtw.QPushButton("(-)")#, clicked = lambda:NegateFunc())
        #self.layout().addWidget(negate_button)
        grid.addWidget(negate_button)
        plus_button = qtw.QPushButton("+")#, clicked = lambda:PlusFunc())
        #self.layout().addWidget(plus_button)
        grid.addWidget(plus_button)


        equals_button = qtw.QPushButton("=")#, clicked = lambda:EqualsFunc())
        #self.layout().addWidget(equals_button)
        grid.addWidget(equals_button)

def main():
    app = qtw.QApplication(sys.argv)
    #ex = MainWindow()
    win = qtw.QWidget()
    grid = qtw.QGridLayout()
    win.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()