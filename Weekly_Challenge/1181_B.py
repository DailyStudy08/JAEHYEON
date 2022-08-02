N = int(input())

lst = []
for _ in range(N):
    s = input()

    lst.append(s)

Lst = sorted(list(set(lst)))

Lst.sort(key=len)

for el in Lst:
    print(el)