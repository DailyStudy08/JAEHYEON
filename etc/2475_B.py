# 검증수 : 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지
# 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어짐

lst = map(int, input().split())

result = list(number ** 2 for number in lst)

ans = sum(result) % 10
print(ans)