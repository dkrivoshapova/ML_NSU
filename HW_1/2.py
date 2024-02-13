n = int(input("Введите количество строк: "))
s = ""
for i in range(0, n):
    s += str(input()) + "\n"
if ("кот" or "Кот") in s:
    print("МЯУ")
else:
    print("НЕТ")
