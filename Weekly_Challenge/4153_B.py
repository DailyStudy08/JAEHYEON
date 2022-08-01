
while True:
    tc = sorted(list(map(int, input().split())))
    if sum(tc) == 0:
        break
    
    a = tc[0]
    b = tc[1]
    c = tc[2]

    if c == (a**2 + b**2)**(1/2):
        print('right')
    else:
        print('wrong')


