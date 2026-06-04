# 딕셔너리를 리턴하는 함수를 선언. 반복되는 키 입력을 줄여준다.


def create_student(name, korean, math, eng, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "eng": eng,
        "science": science
    }

# 학생을 처리하는 함수를 선언
def student_get_sum(student):
    return student["korean"] + student["math"] + student["eng"] + student["science"]

def student_get_average(student): # 평균 구함
    return student_get_sum(student)/4

def student_to_string(student): # 학생 정보 출력
    return print(f'{student["name"], student_get_sum(student), student_get_average(student)}')

students = [
    create_student("연하진", 92, 98, 96, 98)
]

for student in students:
    print(student)
    student_to_string(student)