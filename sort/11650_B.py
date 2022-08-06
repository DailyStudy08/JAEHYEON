N = int(input())

coors = []
for _ in range(N):
    coor = list(map(int, input().split()))

    coors.append(coor)

# coors.sort(key = lambda n: (n[0], n[1]))
coors.sort()
print(coors)

for c in coors:
    c1 = list(map(str, c))
    print((' ').join(c1))