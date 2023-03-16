# проверка числа на простоту
def prost(x):
    for i in range(2, x // 2 + 1):
        if x%i==0:
            return False
    return True