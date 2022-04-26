# 리스트 연산 또한 문자열 연산과 동일 기능을수행
evennumbers = [2, 4, 6, 8, 10]
oddnumbers = [1, 3, 5, 7, 9]

numbers = evennumbers + oddnumbers
print(numbers)
print(numbers * 4)

# 리스트 수정
"""
문자열은 Immutable 타입이기에 인덱싱으로 값을 수정할 수 없으나, 리스트에서는 얼마든지 가능함
먼저 요소를 수정하려면 "리스트 이름[인덱스값 = 수정값]" 형식으로 코딩해야함
"""

numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[4] = 100
print(numbers)

numbers[2] = "hello"
print(numbers)

numbers[0] = numbers[9] #인덱스 9를 인덱스 0에 대입
print(numbers)

numbers[8] = ['a', 'b', 'c'] #리스트 전체를 형태 유지하며 대입
print(numbers)


numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

numbers[4:5] = [80]
print(numbers)
# [2, 4, 6, 8, 80, 1, 3, 5, 7, 9]
numbers[2:6] = "hello"
print(numbers)
# [2, 4, 'h', 'e', 'l', 'l', 'o', 3, 5, 7, 9]
numbers[2:3] = ['a','b','c'] 
print(numbers)

numbers[8] = ['a', 'b', 'c'] #리스트 전체를 형태 유지하며 대입
print(numbers)

numbers[:] = [1]
print(numbers)


# 리스트 삭제
numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

#값만 삭제
numbers[3] = ""
print(numbers)

numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]

a = "goorm"

#공간까지 삭제
del numbers[4]
print(numbers)

del numbers[:5]
print(numbers)

#객체 자체를 삭제
del a