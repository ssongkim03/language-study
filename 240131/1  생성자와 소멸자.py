# 생성자와 소멸자

# 1. 생성자

class Candy:
    def set_info(self,shape,color):
        self.shape = shape
        self.color = color
    def print_info(self):
        print(f'모양 : {self.shape}, color : {self.color}')

satang = Candy()
satang.set_info('원','초록색')

# satang = Candy() 코드가 실행되면서 satang 인스턴스(객체)가 생성되는데 이 때는 인스턴스에 저장된 모양과 생상
# 정보가 없음.
# 1) 인스턴스 생성 후에 set_info() 메서드를 호출해서
# 2) 값을 지정할 수 있는 메서드를 호출

# 값을 가진 인스턴스를 생성하기 위해 생성자를 이용
# 생성자는 인스턴스를 생성할 때 자동으로 호출되는 특별한 메서드
# 모든 클래스는 __init()__ 라는 이름을 가진 생성자를 가지고 있다.
# __init()__ 메서드(생성자)는 인스턴스가 생성될 때 자동으로 호출되기 때문에 인스턴스 변수의 초기화 용도로 사용

# **__init()__
# 새로운 인스턴스가 만들어질 때 자동으로 호출되는 메서드.
# 생성자는 아님. 생성자는 '__new__'이고, 생성자가 객체를 메모리에

class Candy():
    def __init__(self,shape,color):
        self.shape = shape
        self.color = color

satang = Candy('circle','brown')

# 2. 소멸자
# 인스턴스가 생성될 때 자동으로 호출되는 생성자와 마찬가지로
# 인스턴스가 소멸될 때 자동으로 호출되는 메서드
# 소멸자는 __del__()

class Sample:
    def __init__(self):
        print('인스턴스가 생성됩니다.')
    def __del__(self):
        print('인스턴스가 소멸됩니다.')

sample = Sample()
print(123)
del sample # 소멸자를 즉시 명령
print(456)

