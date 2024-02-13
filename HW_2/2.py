n = int(input())
s = ""

for i in range(0, n):
    k = str(input())
    if k[:2] == "%%":
        k = k[2:]
    if k[:3] != "###":
        s += k + "\n"
print(s)
