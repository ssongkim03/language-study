# 학생 성적 데이터
# 문제 1
# 다음과 같은 학생 성적 데이터를 포함하는 DataFrame을 생성하시오
import pandas as pd

#     이름  과목  성적
# 0   Alice 수학 90
# 1   Bob   영어 85
# 2   Clara 수학 92
# 3   David 과학 88
# 4   Emily 영어 78


# 문제 2 : '성적' 열을 기준으로 내림차순으로 DataFrame을 정렬하시오

# 문제 3 : 성적이 85점 이상인 학생들의 정보만을 포함하는 새로운 DataFrame을 생성하시오

# 문제 4 : 각 과목별 평균 성적을 계산

# 문제 5 : DataFrame에 '평균' 열을 추가하고, 각 학생의 성적과 해당 과목의 평균 성적간의 차이를 계산하여 저장하시오

# 주어진 데이터 프레임 df에는 Name "이름", Age (나이), Salary(월급) 열이 있다.
# 주어진 데이터 프레임은 다음과 같다.

#   Name    Age     Salary
#   Amy     25      3000
#   Bob     30      4000
#   Chad    35      5000
#   Dave    40      6000
#   Emma    45      7000

data = {'Name': ['Amy', 'Bob', 'Chad', 'Dave', 'Emma'],
      'Age': [25, 30, 35, 40, 45],
      'Salary': [3000, 4000, 5000, 6000, 7000]}

df = pd.DataFrame(data)

# 1. Salary 열의 평균값을 계산하시오

print(df['Salary'].mean(axis=0))

# 2. Age 열의 최댓값을 계산하시오

print(df['Age'].max())

# 3. Name 열에서 a를 포함한 이름만 선택하여 출력하시오

names_with_a = df[df['Name'].str.contains('a')]

# hint : .contains() 함수를 알아보고 만드시오

# .str : 문자열 데이터를 처리하기 위한 문자열 메서드를 제공해준다.
print(names_with_a['Name'])
