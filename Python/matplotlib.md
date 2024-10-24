# MatPlotLib 
### **cheat sheet**

-------------------------

## Содержание
1. [About](https://github.com/voronov-nikita/useful-parts-of-code/blob/main/cheat-sheets/matplotlib.md#about)
2. [Основные методы](https://github.com/voronov-nikita/useful-parts-of-code/blob/main/cheat-sheets/matplotlib.md#%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D1%8B)
3. [Графики (примеры)]()
4. [Диаграммы (примеры)]()
5. [Таблицы (примеры)]()
6. [Useful Links](https://github.com/voronov-nikita/useful-parts-of-code/blob/main/cheat-sheets/matplotlib.md#useful-links)

## About

<font color="green"><b>matplotlib</b></font> - python библиотека для визуализации полученных данных в виде графиков, диаграмм и таблиц. По умолчанию она не встроена, для установки требуется прописать:

```bash
# Windows
pip install matplotlib

# Linux
pip3 install matplotlib
```

Для использования matplotlib требуются основные знания по математике и математической статистике.

```python 
import matplotlib.pyplot as plt

x = [i for i in range(-100, 100)]
y = [i**2 for i in x]

plt.plot(x, y)
plt.show()

```

<font color="grey">
Пример написания простой параболы (квадратичная функция f(x)=x**2).
</font>

## Основные методы
1. <font color="yellow"> plot() </font> - принимает два аргумента: массив значений по оси X, массив значений по оси Y. **Строит <u>график</u> функции** по этим точкам из двух массивов.

2. <font color="yellow"> bar() </font> - принимает два аргумента: массив значений для оси X, массив значений для оси Y. **Строит <u>столбчатую диаграмму </u>** по полученным данным.

3. <font color="yellow"> pie() </font> - строит **круговую диаграмму**.

4. <font color="yellow"> table() </font> - Строит табилы. На входе имеет:
    - **cellText** список текстов в ячейках
    - **cellColours** список цвета фона ячеек
    - **cellLoc** выравнивание текста
        ```python
        plt.table(cellLoc="left")
        plt.table(cellLoc="center") 
        plt.table(cellLoc="right") 
        ```
    - **bbox** список с элементом - ограничивающая рамка, в которую будет помещена таблица. Список содержит: _[xmin, ymin, width, height]_.
    - **edges** вид краев ячеек.
5. <font color="yellow"> subplots() </font> - помогает изобразить фигуру в виде графиков _(подграфики)_. На вход получает:
    - **ncols/nrows** столбцов/строк в сетке подграфика. 
    - **sharex/sharey** ипользуются для управления общими осями в координатной плоскости.
    - **squeeze** - по умолчанию False, но если True, то вернет сокращенный массив координат
    - **subplot_kw** - требуется передать словарь с ключом, названием подзаголовка.


## Графики (примеры)
```python
# импортируем модуль
import matplotlib.pyplot as plt


# задаем функцию y = f(x)
def f(x):
    return x


# задаем массив точек
x = [i for i in range(-100, 100)]
y = [f(i) for i in x]

plt.plot(x, y)
plt.show()
```

![image1]()

```python
# импортируем модуль
import matplotlib.pyplot as plt


# задаем функцию y = f(x)
def f(x):
    return x**2


# задаем массив точек
x = [i for i in range(-100, 100)]
y = [f(i) for i in x]

plt.plot(x, y)
plt.grid()  # здесь создали сетку
plt.show()
```

![image2](/cheat-sheets/img/2.png)

## Диаграммы (примеры)
```python
import matplotlib.plot as plt



```

## Useful Links:
1. [python.org](https://python.org)
2. [matplotlib.org](https://matplotlib.org)
3. [pypi.org](https://pypi.org)

###### 02.04.2023

