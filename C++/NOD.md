# Нахождение Наибольшего Общего Делителя на C++

```cpp

// 
// НОД - Наибольший Общий Делитель двух чисел
// Решение представлено рекурсивно, вычитанием и делением (алгоритм один и тот же)
// 

#include <iostream>

using namespace std;

// НОД вычитанием
int NodM(int a, int b)
{
    if (a == b)
        return a;
    if (a > b)
        return NodM(a - b, b);
    return NodM(a, b - a);
}

// НОД делением
int NodD(int a, int b)
{
    if (a == b)
        return a;
    if (a > b)
        return NodM(a % b, b);
    return NodM(a, b % a);
}

int main()
{

    int a, b;

    cout << "Введите a: ";
    cin >> a;
    cout << "Введите b: ";
    cin >> b;

    if (a <= 0 || b <= 0)
    {
        cout << "На ноль не получиться разделить.";
        return 0;
    }
    cout << "НОД вычитанием = " << NodM(a, b) << endl;
    cout << "НОД делением = " << NodD(a, b) << endl;

    return 0;
}

```

###### 08.11.2024