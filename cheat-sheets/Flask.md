# Python Flask 

### **cheat sheet**

-------------------------

## **Содержание**
1. [About](https://github.com/voronov-nikita/useful-parts-of-code/blob/main/cheat-sheets/Flask.md#about)
2. [Основные методы и конструкции](https://github.com/voronov-nikita/useful-parts-of-code/blob/main/cheat-sheets/Flask.md#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B-%D0%B8-%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%86%D0%B8%D0%B8)
3. [Useful Links](https://github.com/voronov-nikita/useful-parts-of-code/blob/main/cheat-sheets/Flask.md#useful-links)

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

1. __Декоратор ```@app.route()```__ - используется для выполнения действеия программы под определенным индексом страницы. Пример:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def index():
        return "Hello, Flask"

    if __name__=="__main__":
        app.run()
    ```
    В этом примере при переходе на главную старницу (главная страница -> "domen.ru/") на экране будет отображенанадпись "Hello, Flask". Таким образом, меняя имя внутри декоратора в соответсвии со страницами, будет оторажаться разная информация.

2. Метод ```jsonify()``` - преобразует полученный словарь в [*json*](https://ru.wikipedia.org/wiki/JSON), который позже можно будет счиатть с помощью того же python requests.
    ```python
    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route('/json-example')
    def index():
        data = {
            "one" : 1,
            "two" : 2,
            "Hello" : "world"
        }
        return jsonify(data)

    if __name__=="__main__":
        app.run()
    ```
    В этом примере при переходе на страницу "/json-example" python словарь _data_ преобразуется в json формат и отобразиться на странице.
3.  

## **Useful Links**
1. [python.org](https://python.org)
2. [flask.com](https://flask.palletsprojects.com/en/2.2.x/)
3. [htmlbook.ru/html](https://htmlbook.ru/html)
4. [htmlbook.ru/css](http://htmlbook.ru/css)


###### 09.04.2023