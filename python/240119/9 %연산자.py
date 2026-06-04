# % 연산자
name = 'Kai'
print('내 이름은 %s입니다.' %name)  # %s : string(문자열을 받는다.)
print('내 이름은',name,'입니다',sep='')
print('내 이름은' + name + '입니다')

height = 120.5
print('내 키는 %fcm입니다.' % height) # %f : float (실수형)

weight = 23.55
print('내 몸무게는 %.1fkg입니다.' % weight) # .1f : 소수점 1자리까지 받겠다.

year, month, day = 2024, 1, 19
print('내 생일은 %d년 %d월 %d일 입니다.' % (year,month,day))
# %d : decimal (정수값을 받겠다.) (십진법)

