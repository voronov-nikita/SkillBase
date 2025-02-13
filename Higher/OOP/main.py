# Задача №1
# n = int(input()); print(f"{str((n//60)%24).zfill(2)}:{str((n%60)).zfill(2)}")

# Задача №2
# s = input(); d, cur, k = dict(), s[0], 0
# for i in s:
#     if i == cur: k += 1 
#     else: d[cur], cur, k = k, i, 1
# else: d[cur] = k
# res = max(d, key=lambda x: d[x]); print(F"{res} repeat {d[res]} times")

# Задача №4
# n = int(input()); print("YES" if ((n%100!=0 and n%4==0) or n%400==0) else "NO")

def NOD(a, b) -> int:
    if a == b:
        return a
    if a > b:
        return NOD(a - b, b)
    return NOD(a, b - a)


a = 3
b = 23

print(NOD(a, b))

while a > 0 and b > 0:
    if a > b:
        a -= b
    elif b > a:
        b -= a
    else:
        break
print(a)
