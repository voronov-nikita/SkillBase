# Numpy
### **cheat sheet**

-----------------------

## Содеражние
1. [About](https://github.com/voronov-nikita/useful-parts-of-code/blob/main/cheat-sheets/numpy.md#about)
2. [Основные методы]()
3. [Useful Links]()

## **About**

**Numpy** - python библиотека, которая используется практически повсюду. Во всех, так или иначе, крупных проетах присутсвует данная библиотека. Она предназначена для наиболее быстрого и качественного использования [массивов python](https://pythonist.ru/massiv-v-python/#:~:text=%D0%92%20Python%20%D0%BC%D0%B0%D1%81%D1%81%D0%B8%D0%B2%D1%8B%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%BA%D0%BE%D0%BD%D1%82%D0%B5%D0%B9%D0%BD%D0%B5%D1%80%D1%8B,%D0%BF%D0%BE%D0%BC%D0%BD%D0%B8%D1%82%D1%8C%20%D0%BE%20%D0%BC%D0%B0%D1%81%D1%81%D0%B8%D0%B2%D0%B0%D1%85%20%D0%B2%20Python.). Особенностью массивов numpy - это то, что с ними можно проводить математические опрации, т.к умножение, сложение и т.д. Еще в массивах от numpy можно проводить фильтрацию. К примеру:
```python 
import numpy as np

ls = np.array([10, 20 , 30, 40])
print(ls > 20)
# >>> [False, False, True, True], dtype=bool
```

## **Основные методы**

1. numpy.array(list) - из вхрдящего массива _list_ сделает numpy массив со всеми его состовляющими и особенностями.
2. list_numpy.min() - из numpy массива ищет минимальный элемент. Если в качестве параметра указать ```axis=0```, то вернет список из наименьшего числа в каждом столбце. А если указать ```axis=1```, то список из наименьших в строках.
3. list_numpy.max() - работает аналогично list_numpy.min(), но ищет максимальное число в массиве.
4. list_numpy.mean() - вернет среднее значение по numpy массиву.
> Среднее алгеброическое. Т.е суммирует все числа и делит на их количество.
5. Математические функции тригонометрии:
    1. numpy.sin(a) - вернет синус от числа _a_;
    2. numpy.cos(a) - вернте косинус от числа _a_;
    3. numpy.tg(a) - вернте тангенс от числа _a_;
    4. numpy.ctg(a)- вернте котангенс от числа _a_;

    > То же самое можно провернуть и с обратными функциями по типу арктангенса, арккосинуса и другие. Принцип действия тот же, что и указан выше. 

6. numpy.random() -
7. list_numpy.sum() - вернет сумму всех значений массива.
8. numpy.arange(n) - 

## **Useful Links**
1. [python.org](https://python.org)
2. [numpy.org](https://numpy.org)
3. [pypi.org](https://pypi.org)
4. [pythonworld.ru (часть 1)](https://pythonworld.ru/numpy/1.html)
5. [pythonworld.ru (часть 2)](https://pythonworld.ru/numpy/2.html)
6. [pythonworld.ru (часть 3)](https://pythonworld.ru/numpy/3.html)
7. [pythonworld.ru (часть 4)](https://pythonworld.ru/numpy/4.html)

###### 09.04.2023