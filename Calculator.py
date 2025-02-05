from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QTextEdit, QPushButton, QVBoxLayout, QMainWindow, QFileDialog, QVBoxLayout, QMenuBar, QFontDialog, QInputDialog, QToolBar
from PySide6.QtGui import QIcon, QAction, QFont
from PySide6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(self)
        self.font = QFont("Arial", 500 )
        name = "viewport"
        content ="width=device-width , initial-scale = 1.0"
        self.setWindowTitle("Calculator")
        self.resize(700,568)
        self.color
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.font
        self.text_edit.setGeometry(10,10,680,50)


        self.button = QPushButton("+" , self)
        self.button.setGeometry(10,100,20,20)
        self.button.clicked.connect(self.add)
        self.button = QPushButton("-" , self)
        self.button.setGeometry(70,100,20,20)
        self.button.clicked.connect(self.subtract)
        self.button = QPushButton("/" , self)
        self.button.setGeometry(50,100,20,20)
        self.button.clicked.connect(self.divide)
        self.button = QPushButton("X" , self)
        self.button.setGeometry(30,100,20,20)
        self.button.clicked.connect(self.multiply)
    def add(self):
        self.text_edit.setReadOnly(True)
        self.text_edit.setText("+")
    def subtract(self):
        self.text_edit.setReadOnly(True)
        self.text_edit.setText("-")
    def multiply(self):
        self.text_edit.setReadOnly(True)
        self.text_edit.setText("*")
    def divide(self):
        self.text_edit.setReadOnly(True)
        self.text_edit.setText("/")


def run_application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_application()