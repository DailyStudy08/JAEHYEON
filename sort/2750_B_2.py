# bubble_sort
N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)

L = len(lst)
for i in range(L):
    for j in range(0, L - 1 - i):
        if lst[j] > lst[j + 1]:
            tmp = lst[j]
            lst[j] = lst[j + 1]
            lst[j + 1] = tmp

for k in lst:
    print(k)