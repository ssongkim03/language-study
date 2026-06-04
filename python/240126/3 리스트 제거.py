# 다음은 리스트에 포함된 잘못된 데이터를 모두 제거하는 프로그램이다
# 리스트에 저장된 정상 데이터는 모두 'a'를 포함한 문자열이며, 그렇지 않은 경우 잘못된 데이터입니다
#
a_list = ['avove','cookie','app','about','bisket','apple','april','banana']

a_list = [item for item in a_list if 'a' in item]
# 리스트 컴프리헨션 : for + if문을 사용하여 새로운 리스트를 만드는 구문

# for item in a_list : 각 요소에 대해 반복
# if 'a' in item : 만약 현재 요소가 'a'가 포함되어 있는지 검사
# item for item in a_list if 'a' in item : 각 요소에 대해 반복 -> 만약 'a'가 있다면 해당 item 변수를 새 리스트에 포함

# [expression for item in iterable if condition]
# expression : 새로운 리스트의 각 요소에 대한 표현식
# item은 iterable 에서 반복되는 각 요소를 나타내는 부분
# iterable : 반복 가능한 객체(리스트,튜플,집합,문자열)
# if condition : 조건식 : 참인 경우에 expression 리스트에 포함


print(a_list)