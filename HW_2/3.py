n = int(input())
s_list = []

for i in range(0, n):
    s_list.append(int(input()))

p = int(input())
q = int(input())

count = 0
s = 0  # sum numbers
for e in s_list:
    count += 1
    if (count >= p) and (count <= q):
        s += e
print(s)
