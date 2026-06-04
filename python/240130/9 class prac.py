class watch:
    def __init__(self, watch):
        self.watch = Watch

    def What(self):
        input('시간을 입력하세요 : ')

    def see(self):
        print(f'계산된 시간은 {time}입니다.')

watch = Watch() # 객체의 생성
watch.What() # 클래스 내의 함수 호출 : 시간을 입력받는 호출
watch.see() # 클래스 내의 함수 호출 : 계산된 시간을 출력하는 호출
