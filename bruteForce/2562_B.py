n_lst = []

for _ in range(9):
    n = int(input())
    n_lst.append(n)

max = -987654321
max_i = 0
for i in range(len(n_lst)):
    if n_lst[i] > max:
        max = n_lst[i]
        max_i = i+1

print(max)
print(max_i)

