# 딕셔너리를 리턴하는 함수를 선언. 반복되는 키 입력을 줄여준다.


def create_student(name, korean, math, eng, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "eng": eng,
        "science": science
    }


students = [
    create_student("연하진", 92, 98, 96, 98)
]
# 점수의 총합과 평균을 구하시오

for student in students:
    score = student['korean'] + student['math'] + student['eng'] + student['science']
    avg = score / 4

    print(student['name'], score, avg, sep='\t\t')