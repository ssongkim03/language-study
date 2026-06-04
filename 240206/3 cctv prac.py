# 다음은 지시사항에 따라 서울특별시 마포구에 설치된 CCTV의 개수를 구하는 프로그램을 구현하세요.
import csv

# 지시사항
# 1. cctv.csv 파일을 읽습니다.
# 2. 모든 라인에 존재하는 카메라 개수를 합한 결과를 출력합니다.
# 5번 째 데이터가 카메라 대수입니다.

# 실행 예 :
# 서울특별시 마포구에 설치된 CCTV는 총 2167대 입니다.

# with open('./input/cctv.csv','r') as csvfile:
#     datas = csv.DictReader(csvfile)
#     total_cctv = 0
#     for data in datas:
#         total_cctv += int(data['카메라대수'])
#
# print(f'서울 특별시 마포구에 설치된 CCTV는 총 {total_cctv}입니다.')

# with open('./input/국민연금공단_해외주식 투자정보_20211231.csv', 'r') as csvfile:
#     datas = csv.DictReader(csvfile)
#     for data in datas:
#         print(data['종목명'])

# with open('./input/한국인터넷진흥원_피싱사이트 URL_20221130.csv', 'r',encoding='utf-8') as csvfile:
#     datas = csv.DictReader(csvfile)
#     for data in datas:
#          print(data['홈페이지주소'])

# with open('./input/경찰청 대구광역시경찰청_관서별 112신고 현황_20221231.csv', 'r') as csvfile:
#     datas = csv.DictReader(csvfile)
#     total = 0
#     for data in datas:
#          total += print(data['중요범죄'])
# print(total)

# 문제 : 2019~2022년까지 중부경찰서에서 112신고 현황 중 중요범죄에 대한 건수의 총합을 구해보시오

with open('./input/경찰청 대구광역시경찰청_관서별 112신고 현황_20221231.csv', 'r') as csvfile:
    datas = csv.DictReader(csvfile)
    total = 0
    total2 = 0
    for data in datas:
         if '중부경찰서' in data['구분']:
             total += int(data['중요범죄'])
         if '수성경찰서' in data['구분']:
             total2 += int(data['질서유지'])

print(total)
print(f'2019 ~ 2022까지의 수성경찰서에서 질서유지건으로 112신고가 들어온 건수는 {total2}건 입니다.')


