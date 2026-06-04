# 국어, 영어, 수학 점수를 각각 입력받아서 평균을 구하고, 평균이 80점 이상이면 '합격',
# 아니면 '불합격'을 출력하는 프로그램을 구현하세요

# 실행 예)
# 국어 점수를 입력 : 85
# 영어 점수를 입력 : 83
# 수학 점수를 입력 : 81

# 평균은 83.0이고, 결과는 합격입니다.

korean = int(input('국어 점수를 입력하세요 : '))
english = int(input('영어 점수를 입력하세요 : '))
math = int(input('수학 점수를 입력하세요 : '))

average = (korean + english + math) / 3
result = '합격' if average >= 80 else '불합격'

if  average >= 80 :
    print(f'평균은 {average}이고, 결과는 {result}입니다.')
else :
    print(f'평균은 {average}이고, 결과는 {result}입니다.')