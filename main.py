import sys

from time import sleep

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QGridLayout, QPushButton
from PyQt6.QtCore import QSize, Qt
from pathlib import Path
from PyQt6.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # i can do all UI things in another function named initUI but idc

        # window
        self.setWindowTitle("Calculator")
        self.setFixedSize(QSize(500, 600))
        self.setWindowIcon(QIcon("icon.png"))

        # idk where to put memory so:
        self.memory = []

        # display
        self.result = "0"
        self.resultLabel = QLabel(self.result)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.resultLabel.setFixedSize(200, 100)
        self.resultLabel.setObjectName("answerField") # for qss file

        # layout to put all buttons in it
        self.layout = QGridLayout()

        # adding display to layout
        self.layout.addWidget(self.resultLabel)

        # creating container to add layout into it and put it into central widget
        self.container = QWidget()
        self.container.setLayout(self.layout)
        # !bg here
        self.setCentralWidget(self.container)

        # creating number buttons
        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")
        btn5 = QPushButton("5")
        btn6 = QPushButton("6")
        btn7 = QPushButton("7")
        btn8 = QPushButton("8")
        btn9 = QPushButton("9")
        btn0 = QPushButton("0")

        # number buttons logic
        btn1.clicked.connect(lambda: self.numberPressed("1"))
        btn2.clicked.connect(lambda: self.numberPressed("2"))
        btn3.clicked.connect(lambda: self.numberPressed("3"))
        btn4.clicked.connect(lambda: self.numberPressed("4"))
        btn5.clicked.connect(lambda: self.numberPressed("5"))
        btn6.clicked.connect(lambda: self.numberPressed("6"))
        btn7.clicked.connect(lambda: self.numberPressed("7"))
        btn8.clicked.connect(lambda: self.numberPressed("8"))
        btn9.clicked.connect(lambda: self.numberPressed("9"))
        btn0.clicked.connect(lambda: self.numberPressed("0"))

        # creating operator buttons
        btnAdd = QPushButton("+")
        btnSub = QPushButton("-")
        btnMul = QPushButton("*")
        btnDiv = QPushButton("/")
        btnPow = QPushButton("^")
        btnEq = QPushButton("=")
        btnClr = QPushButton("C")
        btnMS = QPushButton("MS")
        btnMR = QPushButton("MR")
        btnDot = QPushButton(".")

        # operator buttons logic
        btnAdd.clicked.connect(lambda: self.operatorPressed("+"))
        btnSub.clicked.connect(lambda: self.operatorPressed("-"))
        btnMul.clicked.connect(lambda: self.operatorPressed("*"))
        btnDiv.clicked.connect(lambda: self.operatorPressed("/"))
        btnPow.clicked.connect(lambda: self.operatorPressed("^"))
        btnEq.clicked.connect(self.equalsPressed)
        btnClr.clicked.connect(self.clearPressed)
        btnDot.clicked.connect(self.dotPressed)
        btnMS.clicked.connect(self.MSpressed)
        btnMR.clicked.connect(self.MRpressed)

        # putting numbers into grid
        self.layout.addWidget(btn1, 4, 0)
        self.layout.addWidget(btn2, 4, 1)
        self.layout.addWidget(btn3, 4, 2)
        self.layout.addWidget(btn4, 3, 0)
        self.layout.addWidget(btn5, 3, 1)
        self.layout.addWidget(btn6, 3, 2)
        self.layout.addWidget(btn7, 2, 0)
        self.layout.addWidget(btn8, 2, 1)
        self.layout.addWidget(btn9, 2, 2)
        self.layout.addWidget(btn0, 5, 1)

        # putting operators into grid
        self.layout.addWidget(btnAdd, 4, 3)
        self.layout.addWidget(btnSub, 3, 3)
        self.layout.addWidget(btnMul, 2, 3)
        self.layout.addWidget(btnDiv, 1, 3)
        self.layout.addWidget(btnPow, 1, 1)
        self.layout.addWidget(btnEq, 5, 2)
        self.layout.addWidget(btnClr, 5, 3)
        self.layout.addWidget(btnMS, 1, 2)
        self.layout.addWidget(btnMR, 1, 0)
        self.layout.addWidget(btnDot, 5, 0)

        # the only way i found to align answer field to the right xd
        self.layout.addWidget(self.resultLabel, 0, 2)

        # some things with positioning of buttons (connected with qss file also)
        self.layout.setContentsMargins(50, 50, 50, 50)
        self.layout.setHorizontalSpacing(15)

    # function "what to do when number pressed"
    def numberPressed(self, number):
        if self.resultLabel.text() == "0":
            self.resultLabel.setText(number)
        else:
            self.resultLabel.setText(self.resultLabel.text() + number)

    # function "what to do when operator pressed"
    def operatorPressed(self, operator):
        self.result = float(self.resultLabel.text())
        self.resultLabel.setText("0")
        self.operator = operator

    # function "what to do when equals pressed"
    def equalsPressed(self):
        try:
            if self.operator == "+":
                self.result += float(self.resultLabel.text())
            elif self.operator == "-":
                self.result -= float(self.resultLabel.text())
            elif self.operator == "*":
                self.result *= float(self.resultLabel.text())
            elif self.operator == "/":
                self.result /= float(self.resultLabel.text())
            elif self.operator == "^":
                self.result **= float(self.resultLabel.text())
            self.resultLabel.setText(str(self.result))
        except:
            self.resultLabel.setText("ERROR")

    # function "what to do when C pressed"
    def clearPressed(self):
        self.result = 0
        self.operator = ""
        self.resultLabel.setText("0")

    # function "what to do when . pressed"
    def dotPressed(self):
        displayRN = self.resultLabel.text()
        if displayRN[-1] == ".": # to avoid solo dot entering
            pass
        else:
            self.resultLabel.setText(f'{displayRN}.')

    # function "what to do when MS pressed"
    def MSpressed(self):
        displayRN = self.resultLabel.text()
        if not self.memory:
            self.memory.append(displayRN)
            self.resultLabel.setText(f"MEMORY: {displayRN}")
            sleep(1)
            self.resultLabel.setText("0")
        else:
            self.resultLabel.setText("MEMORY IS FULL")

    def MRpressed(self):
        displayRN = self.resultLabel.text()
        if self.memory:
            if displayRN != "0":
                self.resultLabel.setText(f"{displayRN}{self.memory.pop()}")
            else:
                self.resultLabel.setText(f"{self.memory.pop()}")
        else:
            self.resultLabel.setText("MEMORY IS EMPTY")

if __name__ == "__main__":
    # !main() - to do cause imo entering the app with main() including some features is better
    app = QApplication(sys.argv)
    app.setStyleSheet(Path("design.qss").read_text())
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())