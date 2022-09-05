# # https://programmers.co.kr/skill_checks/415532

# def check(num, cnt):
#     if cnt == 500:
#         return -1
#     if num == 1:
#         return cnt
    
#     if num % 2 == 0:
#         new_num = num / 2
#         return check(new_num, cnt + 1)
#     elif num % 2 == 1:
#         new_num = (num * 3) + 1
#         return check(new_num, cnt + 1)
    

# def solution(num):
#     answer = 0
#     if num == 1:
#         return answer
    
#     answer = check(num, 0)
    
#     return answer



a = 13
b = 17
print(list(range(a,b)))