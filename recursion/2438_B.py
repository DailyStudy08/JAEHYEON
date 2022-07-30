S = int(input())

def print_star(N):
    if N == S+1:
        return

    s = ''
    s += '*' * N
    print(s)

    return print_star(N+1)

print_star(1)