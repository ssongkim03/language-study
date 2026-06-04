# 문자열 str
# 문자열 자료형. 기본적으로 따옴표 묶어서 데이터를 표현
# 문자열을 한 글자이거나 여러 글자여도 작은 따옴표(')와 큰 따옴표(")를 모두 사용 가능
# 각 따옴표를 3개씩 사용하는 삼중 따옴표 (''' ''', """ """)도 사용 가능
# single line : 한 줄의 문자열
# multiple line : 여러 줄의 문자열

print(str(100)) # 정수 100을 문자열 '100'으로 변환
print(str(True)) # 논리 True를 문자열 'True'로 변환
print(type(str(3.14))) # 실수 3.14를 문자열 '3.14'로 변환

# 문자열 인덱싱 indexing
# 0번부터 시작
print()
s = 'hello'
print(s[1])
# 마이너스(-) 인덱스는 문자열 뒤에서부터 부여, 마지막 인덱스는 -1이 된다.
print(s[-5]) # h
print(s[0]) # h

# 문자열 슬라이싱 slicing
# 문자열 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용
# s[start:stop:step]
# start : 시작 인덱스를 지정, 생략하면 끝까지 추출
# stop : 종료 인덱스를 지정, 생략하면 끝까지 추출
# step : 인덱스의 증감값, 생략하면 1씩 변화
print()
s = 'banana'
print(s[0:3]) # ban / 종료 인덱스는 포함 X
print(s[0:6:2]) # bnn
print(s[0:6:3]) # ba
print(s[0:]) # 0: 0번째부터 시작해서 끝까지 출력
print(type(s))