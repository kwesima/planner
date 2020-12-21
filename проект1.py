import sys

from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QTableView, QTextBrowser, QCalendarWidget
from PyQt5.QtWidgets import QLabel, QLineEdit, QTimeEdit


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.dates = {}

        self.setGeometry(100, 100, 700, 400)
        self.setWindowTitle('Личный планировщик')

        self.calendar = QCalendarWidget(self)
        self.calendar.setGeometry(QRect(370, 70, 300, 200))

        self.time = QTimeEdit(self)
        self.time.setGeometry(QRect(370, 40, 300, 20))

        self.item = QLineEdit(self)
        self.item.setGeometry(QRect(370, 290, 300, 20))
        self.item.setText("Введите дело")

        self.values = QTextBrowser(self)
        self.values.setGeometry(QRect(30, 70, 300, 200))

        self.add_item = QPushButton(self)
        self.add_item.setGeometry(QRect(30, 290, 300, 20))
        self.add_item.setText("Добавить дело")
        self.add_item.clicked.connect(self.add_now)

    def add_now(self):
        data_of_item = self.calendar.selectedDate().getDate()

        if int(data_of_item[1]) <= 9:
            data_of_item = (data_of_item[0], '0' + str(data_of_item[1]), data_of_item[-1])
        if int(data_of_item[2]) <= 9:
            data_of_item = (data_of_item[0], str(data_of_item[1]), '0' + str(data_of_item[-1]))

        line_edit = self.item.text()

        self.dates[
            f'{data_of_item[0]}-{data_of_item[1]}-{data_of_item[2]}-{self.time.time().toString()}'] = line_edit

        self.values.clear()
        for key in sorted(self.dates.keys()):
            self.values.append(f'{key} - {self.dates[key]}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window1()
    ex.show()
    sys.exit(app.exec())
