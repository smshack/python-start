# 딕셔너리에서 유용한 함수
# x.keys() 딕셔너리 x의 key만 모아 객체 형식 dict_keys([key1, key2,..])으로 반환
# x.values()  x의 value만 모아 객체 형식 dict_values([key1, key2,..])으로 반환
# x.items() 딕셔너리 x 의 key와 value를 튜플로 묶어 dict_items([key1,value1],[key2,value2],...) 형식으로 반환
# x.clear()딕셔너리의 모든 값을 삭제
#x.get(key) x[key]와 같음
# key in x  key 값이 x 딕셔너리에 존재하는지 판별하는 키워드

#중복 저장 되지 않고 "num" : 4로 수정
mem = {"김구름": 25, "박에듀": 23, "온라인": 24}
mem = {"김구름": 25, "박에듀": 23, "온라인": 24}
print(mem.keys())
names = list(mem.keys()) #새로운 리스트 변수에 초기화

names.append("윤레벨")
print("새로운 리스트",names)
print("원래 딕셔너리에서 key 모음", list(mem.keys()))
print(mem.values())
print(list(mem.values()))
print("key와 value를 튜플로", mem.items())
print(mem.get("정판교", "없습니다"), mem.get("온라인", "없습니다"))

exist = '박에듀' in mem #굉장히 직관적인 용법
print(exist)

exist = '한바로' in mem
print(exist)

mem.clear()
print(mem) #빈 딕셔너리 출력