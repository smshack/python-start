# set 중복과 순서가 없는 집합
"""
집합은 수학시간에 배운 집합의 특징을 그대로 구현한 자료형이며 
특정 상황에서 매우 유용하게 사용됨
{} 중괄호를 이용하여 바로 선언 및 초기화 하여 생성 가능
1. 요소의 순서가 없다
2. 중복되는 값을 한개만 저장한다
3. 딕셔너리는 key만 저장한다
"""

s1 = {3, 2, 5, 1, 8, 4, 3} #집합으로 바로 선언 및 초기화
print(s1, type(s1))

"""
집합에는 순서와 중복이 없다
리스트 혹은 튜플에 속한 요소의 중복을 제거하기 위한 필터로 사용
순서가 없어 인덱싱과 슬라이싱을 사용할 수 없음
만약에 인덱싱이나 슬라이싱을 사용해야 하는 경우 집합을 다시 리스트 혹은 튜플로 변환해야 함
"""
str = "Hello goorm!!!"
print(str, type(str))

s0 = set(str) 
print(s0, type(s0))

l = ['a', 'a', 'c', "goorm", "hello", 10, 30, 30]
print(l, type(l))

s1 = set(l) 
print(s1, type(s1))

d = {"Anna":25, "Bob": 23}
print(d, type(d))

s2 = set(d)
print(s2, type(s2))

t = (190,)
print(t, type(t))

s3 = set(t)
print(s3, type(s3))
"""
집합의 자료형 변환
"""
str = "Hello goorm!!!"
print(str, type(str))

s0 = set(str) 
print(s0, type(s0))

newstr = tuple(s0)
print(newstr, newstr[4], newstr[5:], type(newstr)) #인덱싱, 슬라이싱 가능

l = [1,2,3,4,5,6,7,8]
print(l, type(l))

s1 = set(l)
print(s1, type(s1))

newlist = list(s1)
print(newlist, newlist[4], newlist[:-5], type(newlist))