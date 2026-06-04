import random
from datetime import *

number = random.randint(1,100)
print('updown 게임을 시작합니다.')
start = datetime.now()

while True:
    user = int(input('어떤 값일까요? '))
    if number == user:
        end = datetime.now()
        value = end - start
        value = value.total_seconds()
        print(f'정답입니다. 걸린 시간 {value}')
        print('시스템을 종료합니다.')
        break
    else:
        if user > number:
            print('오답입니다. 다시 입력해 주세요')
            print('다운')
        else:
            print('오답입니다. 다시 입력해 주세요')
            print('업')