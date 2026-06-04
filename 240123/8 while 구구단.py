# 구구단 2단부터 9단까지 출력
# 각 단 앞에 제목, 마지막에 구분선을 넣어볼 것

# dan = 2
# n = 1
#
# while dan <= 9 :
#     n = 1
#     while n <= 9 :
#         print(f'{dan} x {n} = {dan * n}')
#         n += 1
#     print(f'구구단 {dan}단이 끝났습니다.')
#     dan += 1


# 임의의 정수를 입력받아 입력받은 정수가 입력되면 ex) : 3 -> 3단 출력

dan = int(input('정수를 입력하세요 : '))
n = 1
while n <= 9 :
    print(f'{dan} x {n} = {dan * n}')
    n += 1
