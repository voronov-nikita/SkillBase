a = [10, 12, 14, 18, 22, 63, 2, 0, 77]  # список любых чисел 10-ной сиситемы счисления!!
def function(ls:list):
    if len(ls) == 0:
        return 
    elif len(set(ls)) == 1:
        return ls[0]
    else:
        m = None  # минимальное
        n = None  # пред-минимальное
        g = None  # пред-пред-минимальное
        for i in a:
            if i != m and i != n and i != g:  # эллемент не встречался в списке ранее
                if m is None or i < m:   # меняем на > для нахождения максимального значения
                    g = n
                    n = m
                    m = i
                elif n is None or i < n:
                    g = n
                    n = i
                elif g is None or i < g:
                    g = i
        # вернет кортеж
        return m, n, g