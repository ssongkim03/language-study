# 학생 리스트를 선정. 딕셔너리 요소로 가진 리스트

students = [
    {"name": "연하진", 'Korean': 92, "Math": 98, "Eng": 96, "science": 98},
    {"name": "구지연", 'Korean': 75, "Math": 87, "Eng": 94, "science": 95},
    {"name": "나선주", 'Korean': 85, "Math": 78, "Eng": 95, "science": 84},
    {"name": "윤아린", 'Korean': 93, "Math": 91, "Eng": 75, "science": 88},
    {"name": "윤명월", 'Korean': 75, "Math": 88, "Eng": 97, "science": 96},

]

# 학생을 한명씩 반복하면서 출력


for student in students:
    score = student['Korean'] + student['Math'] + student['Eng'] + student['science']
    avg = score / 4
    print(student['name'])

    print(student['name'], score, avg, sep='\t\t')
    # 점수의 총합과 평균을 구하시오
