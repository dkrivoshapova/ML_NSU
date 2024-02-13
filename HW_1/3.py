f = str(input())
max = ""
min = f
k = 0
while f != "стоп":
    if len(f) > len(max):
        max = f
    if len(f) < len(min):
        min = f
    f = str(input())

for letter in min:
    if letter in max:
        k += 1
if k == len(min):
    print("ДА")
else:
    print("НЕТ")
