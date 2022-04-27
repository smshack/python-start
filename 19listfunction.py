# 삽입 하는 함수
# append(x) 리스트 맨 마지막에 전달 인자를 추가
# insert(x,y) 리스트의 x번째 위치에 y 값을 추가,(한번에 하나씩 추가 가능)
# extend(x) 기존 리스트에 x를 합칩니다. 전달 인자에는 리스트만 입력 가능

numbers = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
print(numbers)

numbers.insert(3, [11, 12, 13])
print(numbers)

#append와 extend의 차이
numbers.extend(['a', 'b', 'c'])
print(numbers)
numbers.append(['a', 'b', 'c'])
print(numbers)

# 삭제하는 함수
# remove(x) 리스트에서 가장 처음 나오는 x 값을 삭제, 전달 인자를 리스트에서 찾을 수 없다면 오류 발생
# pop() 리스트의 마지막 요소를 반환한 뒤 리스트에서 삭제

numbers = [2, 4, 6, 8, 1, 3, 5, 7]
print(numbers)

numbers.insert(3, [11, 12, 13])
print(numbers)

numbers.remove(3)
print(numbers)
print(numbers.pop())
print(numbers)

# 요소들을 정렬하고 순서를 바꾸는 함수
# sort() 리스트의 요소를 순서대로 정렬함 전달인자 필요 없음
# reverse()리스트의 순서를 반대로 뒤집음 전달인자 필요 없음
evennumbers = [2, 4, 6, 8]
oddnumbers = [1, 3, 5, 7]
print(evennumbers, oddnumbers)

numbers = evennumbers + oddnumbers
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

# 리스트의 정보를 알아내는 함수
# index(x) 전달 인자가 리스트 안에 있으면해당 요소의 인덱스 값을 반환, 전달 인자를 리스트에서 찾을 수 없다면 오류 발생
# count(x) 리스트에있는 x 값의 개수를 반환

numbers = [1, 6, 7, 3, 5, 6, 8, 3, 3]

numbers.index(6)
print(numbers)
print(numbers.count(3))

list1 = [2,5,2,0,1]
list2 = [4,1,2]

list1.append(list2)
print(list1, len(list1))

"""
drawer = []
drawer[0] = "양말"
"""


drawer = []
drawer.append("양말")
print(drawer, drawer[0])

drawer = []

drawer.append("양말")
print(drawer, drawer[0])

drawer.extend(["속옷", "모자", "반팔", "바지"])
print(drawer)


drawer = ["양말", "속옷", "모자", "반팔", "바지"]
print(drawer)


drawer = ["양말", "속옷", "모자", "반팔", "바지"]

del drawer[3]
print(drawer)

drawer[3] = ""
print(drawer)

drawer[3] = "점퍼"
print(drawer)