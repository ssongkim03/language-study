# 오늘의 스케쥴을 입력하면 그 내용이 모두 파일에 보관되는 프로그램이다.
# 스케쥴을 입력하지 않고 enter를 누르면 프로그램은 종료된다.
# 생성되는 파일의 이름은 현재 날짜이고 확장자는 txt입니다.
# '2024-02-01.txt' 와 같은 형식을 갖추고 있습니다. // 참고 : 오늘은 2월 1일이지만 내일 실행을 할 때는 2월 2일이 찍히도록 해야 한다.
# hint : time 모듈을 불러오시오 // time.strftime 을 검색해 보고 사용하시오.

import datetime

now = datetime.datetime.now()
time = now.strftime('%Y-%m-%d')

while True:

    print('스케쥴을 입력하세요.')
    s = input('')
    file = open(f'./output/{time}', 'wt', encoding='utf-8')
    file.write(s)
    break
