n = int(input())
s_list = []
for i in range(0, n):
    s_list.append(int(input()))
s_list = sorted(s_list)
s_list.reverse()
print(s_list)
