# 파일과 파일 입출력의 필요성
nums = input("두 수를 띄어쓰기로 입력하세요:").split()
nums = list(map(int, nums)) #nums의 요소를 한 번에 int로 변환
result = 0
cal = input("""
1. +
2. -
3. *
4. /
""")

if cal == "1":
    result = nums[0] + nums[1]
elif cal == "2":
    result = nums[0] - nums[1]
elif cal == "3":
    result = nums[0] * nums[1]
elif cal == "4":
    result = nums[0] / nums[1]
else :
    print("잘못된 입력입니다.")    
print(result)

# 위 예제처럼 계산기는 값을 입력하고 기능을 선택하면 연산 결과를 출력하며, 끄고 켤 때마다 모든 값은 초기화됨
# 코드를 분석하기 앞서 
# map 함수를 간단히 설명하자면 리스트, 문자열 등에 포함된 요소를 한번에 연산/ 함수처리하는 함수
def func(a) :
    return a + 1

nums = [1,2,3,4,5]	# 집합인자(튜플, 리스트, 문자열) 모두 가능
nums = list(map(func, nums)) # map(함수, 집합인자, ..) 형태
print(nums)

# 우리가 알고있는 대부분의 프로그램은 이전 기록 했던 값을 가져와서 그 정보를 읽어와 쓰는 경우가 많음
# 파일 읽기 쓰기에 대한 기본적인 내용을 알아야 함
