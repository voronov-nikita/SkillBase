# Сигмоидальная функция активации

Сигмоидная функция активации — это нелинейная функция, которая преобразует входное значение в диапазоне от отрицательной бесконечности до положительной бесконечности в значение от 0 до 1. 1

Математически она выражается формулой: σ(x) = 1 / (1 + e^{-x}), где e — основание натурального логарифма.

Преимущества сигмоидной функции активации:

Гладкая градация. Обеспечивает плавный переход выходных значений, что полезно для предсказания вероятностей.
Дифференцируемость. Функция дифференцируема в любой точке, что позволяет использовать её в методах градиентного спуска при обучении нейронных сетей.
Выходные значения между 0 и 1. Это делает её удобной для задач, где требуется вероятностный вывод, как в бинарной классификации.
Недостатки:

Исчезающий градиент. В областях, где |x| очень велик, производная функции становится очень мала, что приводит к исчезающему градиенту и замедляет обучение.
Нецентрированный вывод. Выходы сигмоиды не центрированы вокруг нуля, что может привести к смещению весов в нейронной сети.
Эта функция активации часто используется в нейронных сетях для задач бинарной классификации.

https://habr.com/ru/articles/727506/
https://ru.wikipedia.org/wiki/Функция_активации
https://www.geeksforgeeks.org/derivative-of-the-sigmoid-function/

https://yandex.ru/video/preview/15058614780761438259
https://yandex.ru/video/preview/16186752016150478893
https://yandex.ru/video/preview/1447520426521895826
https://yandex.ru/video/preview/11776438336217535498