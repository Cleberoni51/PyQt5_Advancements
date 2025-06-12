
#PyQt5_Advancements
#Caleb Schear
#20250609-CS-PyQt5_Advancements.py

import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        def ButtonPush() :
            my_label.setText(f'Hey {my_entry.text()}, its certainly been awhile hasnt it')
            my_entry.setText("")

        #Add a Title for your Widget
        self.setWindowTitle("Name Maker 10,000")

        #set Vertical Layout
        self.setLayout(qtw.QVBoxLayout())

        #create a label
        my_label = qtw.QLabel("Hey...you, I didn't catch your name, what was it again?")
        my_label.setFont(qtg.QFont("Helvetica", 18))
        self.layout().addWidget(my_label)

        #create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        #create a button
        my_button = qtw.QPushButton("enter", clicked = lambda:ButtonPush())
        self.layout().addWidget(my_button)

        self.show()


app = qtw.QApplication([])
mw = MainWindow()

app.exec_()