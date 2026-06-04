class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    def __str__(self):
        return f'{self.name} in born'

    def __del__(self):
        print(f'{self.name} is dead')

    @classmethod
    def get_population(cls):
        return cls.count




man = Person('james')
print(man)
woman = Person('emily')
print(woman)
print(f'전체 인구수 : {Person.get_population()}명')
del man
print(f'전체 인구수 : {Person.get_population()}명')
