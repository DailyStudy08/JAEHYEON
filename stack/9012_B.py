N = int(input())

for _ in range(N):
    vps = input()

    stack = []
    top = -1
    for v in range(len(vps)):
        if not stack:
            stack.append(vps[v])
            top += 1
        else:
            if vps[v] == ')' and stack[top] == '(':
                stack.pop()
                top -= 1
            elif vps[v] == ')' and stack[top] != '(':
                stack.append(vps[v])
                top += 1
            else:
                stack.append(vps[v])
                top += 1
    
    if stack:
        print('NO')
    else:
        print('YES')