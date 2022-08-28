f_str = input()
L = len(f_str)

for one in range(97, 123):
    s = chr(one)
    if s in f_str:
        print(f_str.index(s), end=' ')
    else:
        print(-1, end=' ')



