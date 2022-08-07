T = int(input())

for _ in range(T):
    temp = list(input().split())
    R = int(temp[0])
    S = temp[1]
    
    for el in S:
    
        print(el * R, end='')

    print()
