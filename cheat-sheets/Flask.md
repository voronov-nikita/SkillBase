# Python Flask 

### **cheat sheet**

-------------------------

## **Содержание**
1. [About]()
2. [Основные методы и конструкции]()
3. [Useful Links]()

## **About**
*Flask* - это python бибилиотека, созданная для работы с  веб интерфейсами. По большей части на ней пишут веб-сервера и веб-приложения. Использование Flask может показаться однообразным и скучным, однако для полноценной разработки на нем требуется знать не только [Python](https://python.org), но так же [HTML](http://htmlbook.ru/html) и [CSS](http://htmlbook.ru/css) если дело доходит до визуального интерфейса.
Пример веб-приложения:
```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/about")
def about():
    return "About"

if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
```

## **Основные методы и конструкции**

## **Useful Links**
1. [python.org](https://python.org)
2. [flask.com](https://flask.palletsprojects.com/en/2.2.x/)
3. [htmlbook.ru/html](https://htmlbook.ru/html)
4. [htmlbook.ru/css](http://htmlbook.ru/css)


###### 08.04.2023