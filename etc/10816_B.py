# N : 갖고 있는 카드의 수
N = int(input())
# 숫자 카드에 적혀있는 정수
cards = list(map(int, input().split()))
# 정수 M 개
M = int(input())
# 몇 개 갖고있는 숫자 카드인지 구해야할 수들
find_cards = list(map(int, input().split()))
card_dict = {}
for card in cards:
    if not (card in card_dict):
        card_dict[card] = 1
    else:
        card_dict[card] += 1

# print(card_dict)

for card in find_cards:
    if card_dict.get(card):
        print(card_dict.get(card), end=' ')
    else:
        print(0, end=' ')
#


#
# students = ['박해피', '이영희', '조민지', '조민지',
#             '김철수', '이영희', '이영희', '김해킹',
#             '박해피', '김철수', '한케이', '강디티',
#             '조민지', '박해피', '김철수', '이영희',
#             '박해피', '김해킹', '박해피', '한케이', '강디티']
#
# student_dict = {}
#
# for student in students:
#
#     if not (student in student_dict):
#         student_dict[student] = 1
#     else:
#         student_dict[student] += 1
# answer = list(student_dict)
# print(answer)
