# 기본 형식
# for 요소 in {세트}
# 반복실행

for item in {'가위','바위','보'}:
    print(item)

# 2. 딕셔너리
# key와 value의 조합이라 다른 자료형과 다른 방식으로 사용을 한다.

# key만 출력
print()

person =  {'name':'에밀리','age':20,'주소':'대구'}
for item in person:
    print(item)

print()

# value 출력

for key, value in person.items():
    print(f'{key} : {value}')