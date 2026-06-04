# 다음은 컴퓨터가 주사위를 던지면 사용자가 주사위의 숫자를 맞히는 프로그램입니다.
# 사용자가 맞힐 때까지 게임은 계속됩니다.

import random

number = random.randint(1,6)

while True:
    user = int(input('주사위 값은 얼마일까요? : '))
    if number == user:
        print(f'{user}! 정답입니다.')
        break
    else:
        if user > number:
            print('오답입니다. 다시 시도하세요.')
            print('다운')
        else:
            print('오답입니다. 다시 시도하세요.')
            print('업')