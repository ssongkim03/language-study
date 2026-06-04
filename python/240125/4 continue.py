# continue문
# 반복문의 시작 지점으로 제어의 흐름을 옮기는 역할
# 반복에서 제외하거나 생략하고 싶은 코드가 존재할 때 사용

# 1에서 100 사이의 모든 정수를 합하는데 3의 배수만 제외
# total = 0
# for i in range(1, 101):
#    if i % 3 == 0: # 3의 배수인지 확인
#        continue
#     total += i
# print(total)

# continue를 사용하지 않고 3의 배수는 제외해서 문제를 풀어보시오.

total = 0
for i in range(1, 101):
    if i % 3 != 0:
        total += 1
print(total)

print(list(range(10))) # 리스트 형식으로 10개 찍어낸다.

# len() : 함수에 전달된 객체의 길이(항목 수)를 반환
print()
li = ['a','b','c','d']
print(len(li))

d = {'a':'apple','b':'banana'}
print((len(d))) # 2 / 딕셔너리는 '키:값'으로 구성된 한 쌍을 하나의 데이터로 본다

print(len(range(10)))
print(len(range(1,10)))

# range() 함수와 리스트의 길이를 구하는 len() 함수를 함께 사용하면 리스트의 인덱스를 생성 가능

seasons = ['봄','여름','가을','겨울']
seasons_eng = ['spring','summer','fall','winter']

# len(seasons) = 지금은 4를 넣는 것과 같다.
for idx in range(len(seasons)):
    print(f'{seasons[idx]} / {seasons_eng[idx]}')

# sorted() : 전달된 반복 가능 객체의 오름차순 정렬결과를 반환
# reverse=True : 옵션을 추가할 경우 내림차순 정렬 결과를 반환

print()
my_list2 = ['b','c','a','d']
print(sorted(my_list2))

my_list = [6,3,1,2,5,4]
print(sorted(my_list))
print(sorted(my_list,reverse=True))

# zip() : 전달된 여러 개의 반복가능객체의 각 요소를 튜플로 묶어서 반환
# 전달된 반복가능객체들의 길이가 서로 다르면 길이가 짧은 반복가능객체 기준으로 동작
print()

names = ['james','emily','amanda']
scores = [60,70,80]
for student in zip(names,scores):
    print(student)

# 튜플은 언패킹이 가능하다. 그래서 다음과 같은 모습으로 구성 가능

for name, score in zip(names,scores):
    print(f'{name}의 점수는 {score}입니다.')

for a,b in zip(seasons,seasons_eng):
    print(f'{a}의 계절은 {b}입니다.')
    