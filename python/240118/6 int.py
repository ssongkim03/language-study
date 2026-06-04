# 정수 int

# int() 함수를 이용하면 다른 자료형의 값을 정수형 데이터롤 변환이 가능하다.
print(int(1.9)) # 1 / 1.9의 소수점(.9) 이하를 제거하여 정수 1로 변환
print(int(True)) # 1 / True는 1로 변환
print(int(False)) # 0 / False는 0으로 변환
print(int('100')) # 100 / 문자열 '100'을 정수 100으로 변환
print(type(100)) # type : 안에 들어간 내용의 데이터 타입을 알아볼 수 있다.

# 10진수를 2진수, 8진수, 16진수로 변환하는 방법
print()
n = 95
print(type(n))
print(bin(n)) # 2진수로 변환
print(oct(n)) # 8진수로 변환
print(hex(n)) # 16진수로 변환

