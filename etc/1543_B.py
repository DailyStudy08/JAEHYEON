expr = input()
f_str = input()

L = len(expr)
E = len(f_str)
idx = 0
cnt = 0
while True:
    for i in range(idx, L):
        if expr[i:i+E] == f_str:
            cnt += 1
            idx += E
            break
        else:
            idx += 1

    if idx >= L:
        break

print(cnt)