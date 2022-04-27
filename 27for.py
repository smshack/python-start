# for 문의 활용
# 초기식, 조건식, 조건 변화식을 이용해 반복문을 실행
#  range로 인덱싱으로 리스트나 튜플등을 활성할 수 있음

l = [1,3,5,6,7]

for i in range(len(l)) :
    print(l[i])

dic = {"human":"사람", "dog" : "강아지", "carrot" : "당근"}

oddnums = (1, 3, 5, 7, 9)
evennums = [6, 8, 10, 22, 50]
str = "Hello goorm!"

for i in oddnums :
    print(i, end = ' ')
print()
    
for i in evennums :
    print(i, end = ' ')
print()

for i in str :
    print(i , end = ' ')
print()

for key, val in dic.items() :
    print(key, val, end = ' ')
print()

#  print 함수 안에서 end =" " 를 작성하면출력시 끝에서 개행하지 않고 end의 키워드인 공백을 삽입한 뒤에 데이터를 이어서 출력
#  print() 함수는 반복 실행 시 모든 요소를 개행해서 출력하기 때문에 데이터를 한 줄에 표현하고자 한다면 end 용법을 사용해야 함
# for key, val in dic.items(): 을 통해 조건식의 변수를 여러 개 사용 가능
# 딕셔너리에 사용할 때는 items라는 객체로 접근해야 됨

for num in [1,2,3,4,5,6,7] :
    print(num)
    
for num in [1,2,3,4,5,6,7] :
    print(num, end = ',')
print()

# 첫번째 for문을 동작시키면 리스트의 모든 요소를 개행하여 출력하지만,
# end 용법을 사용하면 ','을 이용하면 한줄에 표현할 수 있음을 확인

# 조건식에는 여러 값을 한번에 사용 가능
# 딕셔너리 사용시 주의할 점 딕셔너리는 key와 value가 쌍으로 있을 뿐 , 두 값이 튜플과 리스트 처럼 묶여 있지 않기 대문에 dic.items()로
# 딕셔너리를 아이템 객체로 변환하여 key와 value를 묶은 뒤 key, val 변수로 접근해야 함
nums1 = [[1, 2, 3], [4, 5, 6], ['a', 'b', 'c']]
nums2 = [(1,2), (3, 4)]

for i, j, k in nums1 :
    print(i, j, k)

print()

for i, j in nums2 :
    print(i, j)

fruits = {"apple" : "red", "banana" : "yellow", "grape" : "purple", "melon" : "green"}

for color in fruits.values():
    print(color, end = ' ')
print()

for fruit in fruits.keys():
    print(fruit, end = ' ')
print()

for fruit, color in fruits.items():
    print("%s의 색은 %s" %(fruit, color), end = ', ')