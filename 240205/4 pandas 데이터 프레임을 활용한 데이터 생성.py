import pandas as pd

data = {'Name': ['John', 'Mike', 'Sarah', 'Kate'],
        'Math': [90, 80, 95, 75],
        'English': [85, 90, 92, 88],
        'Science': [92, 88, 78, 80]}

df = pd.DataFrame(data)

# 각 학생의 총점을 계산하고 싶다.

df['Total'] = df['Math'] + df['English'] + df['Science']
print(df)

# numpy 배열 데이터를 입력해 생성한 DAtaFrame 데이터의 예
import numpy as np

data_list = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
d1 = pd.DataFrame(data_list)
print(d1)

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
index_date = pd.date_range('2024-02-05', periods=4)
columns_list = ['A', 'B', 'C']
d2 = pd.DataFrame(data, index=index_date, columns=columns_list)
print(d2)

# 딕셔너리 타입으로 2차원 데이터를 입력한 예
table_data = {'연도': [2017, 2018, 2019, 2020, 2021],
              '지사': ['한국', '한국', '미국', '한국', '일본'],
              '고객수': [200, 250, 450, 300, 500]}
d3 = pd.DataFrame(table_data)
print(d3)

d4 = pd.DataFrame(table_data, columns=['지사', '고객수', '연도'])
print(d4)

