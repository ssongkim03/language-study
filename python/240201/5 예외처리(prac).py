# 문제

# 한 가게에서 고객의 주문을 처리하는 프로그램을 작성. 사용자로부터 주문한 제품의 가격과 수량을 입력받아서 총 주문 가격을
# 계산하는 프로그램을 작성. 그러나 다음과 같은 상황들은 예외 처리해야 한다.

# 1. 가격과 수량을 입력할 떄 숫자가 아닌 값이 입력되면 '올바른 숫자를 입력하세요.'라는 메시지가 나와야 한다.
# 2. 가격이 음수인 경우 '가격은 음수일 수 없습니다.'라는 메시지가 나와야 한다.
# 3. 수량이 음수인 경우 '수량은 음수일 수 없습니다.'라는 메시지가 나와야 한다.

try:
    price = int(input('제품의 가격을 입력하세요 : '))
    product = int(input('제품의 수량을 입력하세요 : '))

    if price < 0:
        raise ValueError('가격은 음수일 수 없습니다.')
        if product < 0:
            raise ValueError('수량은 음수일 수 없습니다.')
            sum = price * product
            print(f'총 주문 가격은 {sum}원입니다.')
except ValueError as e:
    print('올바른 숫자를 입력하세요.')
except Exception as e: # Exception : 모든 오류
    print('오류 발생', e)