months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

months_eng = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Novem', 'Decem']

# 문제 : 출력결과를 보고, enumerate를 사용해서 출력하시오.

for month, day in enumerate(months):
    print(f'{month + 1}월 = {day}일')

month = 1
for i in months:
    print(f'{month}월 = {i}일')
    month += 1

for idx, dat in enumerate(months):
    print(f'{months_eng[idx]} = {day}일')

