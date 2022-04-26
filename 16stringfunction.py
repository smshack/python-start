# count()  전달 인자의 문자 개수를 반환
# find() 함수의 대상이 되는 문자열에 전달 인자와 같은 문자가 있는지 찾고 , 그 문자가 처음 발견된 인덱스 값을 반환, 만약 전달 인자가 문자열 내에 없다면 -1 반환
# index() find() 와 같은 역할을 수행하나 , 전달 인자가 문자열 내에 없으면 오류 발생
# join 전달 인자 사이에 함수의 대상이 되는 문자열을 삽입
# upper() / lower()  함수의 대상이 되는 문자열을 대문자ㄹ/ 소문자로 변환
# Istrip() / rstrip() 함수의 대상이 되는 문자열의 가장 왼쪽 / 오른쪽 공백을모두 삭제
# strip() 함수의 대상이 되는 문자열의 양쬭에 있는 한칸 이상의 공백 모두 삭제
# replace(전달인자1,전달인자2) 함수의 대상이 되는 문자열에서 잔달 인자1과 동일한 부분을 찾아 전달 인자2로 교체
# split() 함수의 대상이 되는 문자열을 전달 인자 기준으로 쪼개 리스트로 반환 
str = " Hello goorm! I study Python.  "

num = str.count(' ') #빈칸의 개수
print("빈칸의 개수는 %d입니다." %num)
print("처음 등장하는 'l'의 인덱스 값은 %d입니다." %str.find('l')) 
print("Good day에서 처음 등장하는 'y'의 인덱스 값은 %d입니다." %"Good day".index('y'))

print(" ".join(str))
print(str.upper())
print(str.lower())
print(str.lstrip())
print(str.rstrip())
print(str.replace('Python', 'C'))
print(str.split())

sentence = "I like studying Python" 
print(len(sentence), len("goorm"))