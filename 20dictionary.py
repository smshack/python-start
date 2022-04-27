# 딕셔너리 자료형
# 딕셔너리에는순서가존재하지 않음
# key: value 형태로 값을 저장
dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
print(dic1)

dic2 = dict(apple = "사과", bird = "새", bug = "벌레")
print(dic2)

dic = {}

dic["apple"] = "사과"
dic["grape"] = "포도"
dic["fruits"] = ["바나나", "딸기", "오렌지"]
print(dic)

dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
print(dic1)

del dic1["bug"]
print(dic1)
#중복 저장 되지 않고 "num" : 4로 수정
dic = {"num":3}
dic["num"] = 4

#dic[[1]] = True -> 리스트는 key로 저장할 수 없음
dic[False] = 0

#value는 어느 값이든 저장 가능
dic[True] = [1, 10, 100] 
dic["nums"] = {"one":1, "two":2}
print(dic)