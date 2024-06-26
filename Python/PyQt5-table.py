import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget



class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример табличного виджета")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

        self.initUI()

    def initUI(self):
        # Задаем заголовки столбцов
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Имя", "Фамилия", "Возраст"])

        # Добавляем данные в таблицу какой-то массив данных
        data = [
            ("Иван", "Иванов", 25),
            ("Петр", "Петров", 30),
            ("Мария", "Сидорова", 35)
        ]

        self.tableWidget.setRowCount(len(data))
        for i, (name, surname, age) in enumerate(data):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(name))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(surname))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(age)))

        # Растягиваем столбцы по содержимому
        self.tableWidget.resizeColumnsToContents()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableExample()
    window.show()
    sys.exit(app.exec_())
