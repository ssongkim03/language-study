# if : 조건문

# 1. if문
# if 조건식 :
#           조건식의 결과가 True일 때 실행

num = 15
if num > 0 :
    print('양수') # 조건식이 True라서 실행된다.

if True :
    print('참')

if False :
    print('틀렸다')

# 들여쓰기 identation 규칙
# 1. 공백 space나 탭 tap을 이용하여 들여쓰기를 수행
# 2. 공백의 개수는 상관 x
# 3. 탭은 1개만 사용
# 4. 동일 구역에서 들여쓰기는 통일해야 한다. 공백과 탭을 혼용하여 사용할 수 없고 들여쓰기 수준도 동일해야 한다.
# 5. 주로 사용하는 들여쓰기는 공백 4개, 공백 1개, 탭 1개

if num > 0 : print('양수') # 실행문이 하나면 한 줄 코드도 가능

# 2. if-else문

num = -1
if num >= 0 :
    print('양수')
else :
    print('음수')

# 3. if-elif문
# if 조건식 1 :
#           조건식 1의 결과가 True일 때 실행
# elif 조건식 2 :
#               조건식 1의 결과가 False이고, 조건식 2의 결과가 True일 때 실행
# elif 조건식 3 :
# #               조건식 1의 결과가 False이고, 조건식 2의 결과가 False이고, 조건식 3의 결과가 True일 때 실행
# else :
#       조건식 1,2,3의 결과가 모두 False이면 실행

print()

score = 56

if score >= 80 :
    print('상')
elif score >= 50 :
    print('중')
else :
    print('하')

if score >= 80 :
    print('상')
else :
    if score >= 50 :
        print('중')
    else :
        print('하')

