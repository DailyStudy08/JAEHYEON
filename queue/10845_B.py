import sys

N = int(sys.stdin.readline())
Q = []
front = -1
for _ in range(N):
    try:
        temp = sys.stdin.readline().split()
        cmd = temp[0]
        n = int(temp[1])
    except:
        cmd = temp[0]
    
    if cmd == 'push':
        Q.append(n)
        front += 1
    elif cmd == 'pop':
        if Q:
            print(Q.pop(0))
            front -= 1
        else:
            print(-1)
    elif cmd == 'size':
        print(len(Q))
    elif cmd == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if Q:
            print(Q[len(Q) - 1])
        else:
            print(-1)
    