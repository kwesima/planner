import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QTableView
from PyQt5.QtWidgets import QLabel, QLineEdit
from PyQt5.uic.properties import QtWidgets

list_of_cases = {}


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Личный планировщик')

        self.add_task = QLineEdit("Напишите своё дело", self)
        self.add_task.setGeometry(QRect(200, 50, 200, 50))

        self.choice_category = QComboBox(self)
        self.choice_category.setGeometry(QRect(200, 120, 200, 50))
        self.choice_category.addItem("Важное")
        self.choice_category.addItem("Второстепенное")
        self.choice_category.addItem("Неважное")
        self.choice_category.addItem("Срочное")
        self.choice_category.addItem("Обычное")

        self.btn_go = QPushButton(self)
        self.btn_go.setGeometry(QRect(200, 190, 200, 50))
        self.btn_go.setText("Добавить дело")
        self.btn_go.clicked.connect(self.change)

        self.btn_ok = QPushButton(self)
        self.btn_ok.setGeometry(QRect(200, 260, 200, 50))
        self.btn_ok.setText("Все дела добавлены!")
        self.btn_ok.clicked.connect()

    def change(self):
        global list_of_cases
        curr_text = str(self.choice_category.currentText())
        if curr_text in list_of_cases.keys:
            list_of_cases[curr_text].append(self.add_task.text())
        else:
            list_of_cases[curr_text] = []


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
