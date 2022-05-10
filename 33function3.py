# 반환 값
# 반환 값도 다른 언어에서는 어떤 자료형의 값을 몇개 반환할 것인지 선언할 때 명시해야 하고 선언한 대로 반환
# 파이썬은 반환 값 자체를 함수에 명시하지 않고 return
# 굉장히 직관적이지만, 최소한 반환 값에 맞게 함수를 호출하면서 같은 개수의 변수를 할당해야 규칙은 지켜야 함

# 반환 값과 할당하는 변수 개수가 동일해야하는 상황
def calculator(a, b) :
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div

res1, res2, res3, res4 = calculator(10, 2)
print(res1, res2, res3, res4)

# 함수에서 하나의 리스트를 만환하기 때문에 하나의 변수로 값을 할당 가능
def calculator(a, b) :
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return [sum, sub, mul, div]

reslist = calculator(10, 2)
print(reslist)

## 반환값들은 사실 하나다
# 파이썬은 반환값이 여러 개 일 때 자동으로 튜플로 반환
def calculator(a, b) :
    sum = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return sum, sub, mul, div

reslist = calculator(10, 2)
print(reslist, type(reslist))

# return은 함수를 종료함과 동시에값을 반환하는 키워드
def division(a, b) :
	if b == 0 :
		return
	else :
		res = a / b
		
	print("division")
	return res

result = division(10, 3)
print(result)

result = division(10, 0)
print(result)