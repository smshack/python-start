# 집합 함수
# 집합과 사용할 수 있는 함수
# 교집합 &, intersection()
# 합집합 | ,union()
# 차집합 -, difference()

s1 = set([2,4,6,8,10]) 
s2 = set([1,2,3,4,5,6,7,8])

interset = s1 & s2 #교집합
print(interset)
print(s1.intersection(s2), s2.intersection(s1)) #함수 사용
print(s1) #s1의 값이 바뀌는 것이 아님

uniset = s1 | s2 #합집합
print(uniset)
print(s1.union(s2)) 
print(s1) #s1의 값이 바뀌는 것이 아님

difset1 = s1 - s2 #어떤 집합에서 어떤 집합을 빼느냐에 따라 다른 결괏값
difset2 = s2 - s1
print(difset1)
print(difset2)

# set.add(a) 집합 set에 a 값을 추가
# set.update([a,b,c,d,...]) 집합 set에 여러 개의 값을 추가함
# remove set.remove(a) 집합 set에 a 값을 삭제합니다

s1 = {1, 2, 3, 4}

s1.add("hello")
print(s1)

s1.add(10)
print(s1)

s1.add((1,2,3)) #add() 사용 시 튜플/문자열은 값 하나로 인식
print(s1)


s1.update(['a', 'b', 'c']) #set()과 같이 여러 값을 한 요소로 저장
s1.update((11,12))
print(s1)

s1.update("zyx") #s1.add("hello")와의 차이
print(s1)

s1.remove("hello") #하나의 값만 제거 가능
print(s1)