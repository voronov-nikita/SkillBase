# Шейкерная сортировка

## Как работает сортировка?

**Шейкерная сортировка** (также известная как двунаправленная пузырьковая сортировка или сортировка перемешиванием) — разновидность пузырьковой сортировки.

Принцип шейкерной сортировки:

- Список разбивается на три части — левую, рабочую и правую.

- Обработка рабочей части происходит за два прохода — прямой и обратный. Обратный проход осуществляется справа налево и перетаскивает минимальный элемент из рабочей части к концу левого подсписка.
- Границы рабочей части массива (то есть части массива, где происходит движение) устанавливаются в месте последнего обмена на каждой итерации.
- Просмотр массива осуществляется до тех пор, пока все элементы не встанут в порядке возрастания (убывания). Количество просмотров элементов массива определяется моментом упорядочивания его элементов.

## Реализация

```cpp

// функция сортиовки массива, Шейкерной сортировкой
void shakerSort(int ls[], int n) {
    
    bool swapped = true;
    int start = 0;
    int end = n - 1;

    while (swapped) {
        swapped = false;

        // Проход слева направо
        for (int i = start; i < end; i++) {
            if (ls[i] > ls[i + 1]) {
                swap(ls[i], ls[i + 1]);
                swapped = true;
            }
        }

        // выходим из цикла, если не произошло изменений
        if (!swapped)
            break;

        // Подготовка к следующему проходу справа налево
        swapped = false;
        end--;

        // Проход справа налево
        for (int i = end - 1; i >= start; i--) {
            if (ls[i] > ls[i + 1]) {
                swap(ls[i], ls[i + 1]);
                swapped = true;
            }
        }

        start++;
    }
}

```

###### 08.11.2024