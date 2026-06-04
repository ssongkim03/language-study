# 논리연산자
# 결과 값은 True 와 False 둘 중 하나
# a and b : a와 b 모두 참(True)이면 True, 아니면 False
# a or b : a와 b 중 하나라도 참(True)이면 True, 아니면 False
# Not a : a가 참(False), 거짓(True)

a = 10
b = 0

print(f'{a} > 0 and {b} > 0 : {a > 0 and b > 0}')
print(f'{a} > 0 or {b} > 0 : {a > 0 or b > 0}')
print(f'not {a} : {a, not a}')
print(f'not {b} : {b, not b}')