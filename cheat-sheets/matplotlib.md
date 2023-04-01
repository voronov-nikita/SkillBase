# MatPlotLib 
### **cheat sheet**

-------------------------

## Содержание
1. [About]()
2. [Основные методы]()
3. [Графики (примеры)]()
4. [Диаграммы (примеры)]()
5. [Таблицы (примеры)]()
6. [Useful Links]()

## About
<font color="green">**matplotlib**</font> - python библиотека для визуализации полученных данных в виде графиков, диаграмм и таблиц. По умолчанию она не встроена, для установки требуется прописать:
```Terminal
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

3. <font color="yellow"> pie() </font>

# Useful Links:
1. [python.org](https://python.org)
2. [matplotlib.org](https://matplotlib.org)
3. [pypi.org](https://pypi.org)

###### 01.04.2023

