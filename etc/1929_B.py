# 소수 : 1과 자기 자신 외에 약수를 가지지 않는 1보다 큰 자연수

# 약수 : 어떤 수를 나누었을 때 나머지가 0인 수
import sys
M, N = map(int, sys.stdin.readline().split())


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return num


for n in range(M, N+1):

    if is_prime(n):
        print(n)

print(100**0.5)