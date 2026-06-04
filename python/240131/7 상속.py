# 상속
# 1. 상속이란
# 어떤 클래스가 가지고 있는 기능을 그대로 물려받아서 사용할 수 있는 클래스를 말한다.
# 다른 클래스의 기능을 물려받을 때 상속받는다라는 표현을 사용
# 그래서 상속 단계에 있는 클래스를 표현할 때 부모 클래스와 자식 클래스 하는 말을 사용

# 부모 클래스 : 상속해 주는 클래스 / 슈퍼 클래스 super class, 기반 클래스 base class
# 자식 클래스 : 상속 받는 클래스 / 서브 클래스 sub class, 파생 클래스 derived class

# 2. 상속 관계 구현
# 기본적으로 두 클래스가 상관 관계에 놓이려면 IS-A 관계가 성립되어야 한다
# IS-A 관계란 '~은 ~이다'로 해설할 수 있는 관계를 의미
# 학생은 사람이다. Student is a Person. 처럼 해석되는 것이 IS-A 관계
# 이 때 Student는 서브 클래스가 되고, Person은 슈퍼 클래스가 됨

# 컴퓨터 과학에서 상속은 is-a 관계를 갖고 있을 때 사용
# is-a 관계는 직원은 사람이다, 자동차는 차량이다.
# has-a 관계는 상속이 아니라 구성으로 구현함.

# 객체 지향 프로그래밍을 처음 접하면 두 클래스가 어떤 관계를 갖고 있을 때, 반드시 상속 관계가 만들어져야 한다고
# 생각하는 경우가 많다.
# is-a 관계를 가질 경우에는 상속, has-a 관계를 가질 경우에는 구성을 사용한다고 구분해서 생각하면
# 어떤 경우에 상속을 활용해야 할지 쉽게 구분.

# 서브 클래스를 구현할 때는 괄호 안에 어떤 슈퍼 클래스를 상속받는지 명시
# 상속 관계에 놓인 서브 클래스는 마치 자신의 것처럼 슈퍼 클래스의 기능을 사용할 수 있다.

class Person:  # 슈퍼 클래스
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(self.name + '가 ' + food + '를 먹습니다.')


class Student(Person):  # 서브 클래스
    def __init__(self, name, school):
        super().__init__(name)  # super() : 슈퍼 클래스의 생성자를 실행
        self.school = school

    def study(self):
        print(self.name + '는 ' + self.school + '에서 공부를 합니다.')


potter = Student('해리포터', '호그와트')
potter.eat('감자')
potter.study()


# 서브 클래스의 init()
# 서브 클래스의 생성자를 구현할 때는 반드시 슈퍼 클래스의 생성자를 먼저 호출하는 코드를 작성해야 한다.
# super라는 키워드는 슈퍼 클래스를 의미

class Computer:
    def __init__(self):
        print('슈퍼 클래스의 생성자가 실행되었습니다.')


class NoteBook(Computer):

    def __init__(self):
        super().__init__()
        print('서브 클래스의 생성자가 실행되었습니다.')


n = NoteBook()

