import sys

N = int(sys.stdin.readline())

stack = []
for _ in range(N):
    
    C = sys.stdin.readline().split()
    cmd = C[0]

    if len(C) == 2:
        cmd = C[0]
        item = int(C[1])

    if cmd == 'push':
        stack.append(item)
    
    if cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    
    if cmd == 'size':
        print(len(stack))
    
    if cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    
    if cmd == 'top':
        if stack:
            L = len(stack) - 1
            print(stack[L])
        else:
            print(-1)

        