# Код для авторизации в PyQt5

```python

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Авторизация")
        self.setGeometry(100, 100, 300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label_username = QLabel("Имя пользователя:")
        self.layout.addWidget(self.label_username)

        self.lineEdit_username = QLineEdit()
        self.layout.addWidget(self.lineEdit_username)

        self.label_password = QLabel("Пароль:")
        self.layout.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.lineEdit_password)

        self.button_login = QPushButton("Войти")
        self.layout.addWidget(self.button_login)
        self.button_login.clicked.connect(self.login)

        # Массив пользователей и паролей
        self.users = {"user1": "password1", "user2": "password2", "user3": "password3"}

    # функция проверки правильности и соответствия пароля к аккаунту
    def login(self):
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()

        # действия при успешной и ошибочной авторизации
        if username in self.users and self.users[username] == password:
            print("Успешная авторизация")
            self.close()
            # Здесь можно добавить код для перехода на следующее окно при успешной авторизации
        else:
            print("Ошибка авторизации")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())


```