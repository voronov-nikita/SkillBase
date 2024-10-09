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