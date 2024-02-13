def Artek(s, n):
    s = s.split(', ')
    artek = []
    for e in s:
        if e[-1] == '5':
            artek.append(e[:-2])
    artek = sorted(artek)
    if len(artek) > n:
        return (", ".join(artek[0:n]))
    else:
        return (", ".join(artek))


s = str(input())  # список студентов
n = int(input())  # количество заявок
b = Artek(s, n)
print(b)
