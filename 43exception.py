## 예외처리란
"""
프로그램 실행 중 특정 상황에 발생할 수 있는 예외의 경우를 미리 생각해서
그것을 처리할 수 있는 코드를 삽입해 주는 것
"""

# SyntaxError
## 잘못된 문법이나 표현을 사용했을 때 발생

"""
  File "/home/smart/practice/python/start/41module.py", line 1
    import .calcultor
           ^
SyntaxError: invalid syntax
"""

# IndentationError
# 파이썬에서 굉장히 중요한 들여쓰기가 잘못되었을 때 발생
# if true:
# print "hi"
"""
    print "hi"
    ^
IndentationError: expected an indented block
"""

# ZeroDivisionError
# 0을 다른 숫자로 나누려 했을 때 발생


## 오류 예외처리 하기
# try ~ except
"""
try:
    실행할 코드
except 에러이름 as 메세지변수:
    에러발생시 실행할 코드
"""
try:
  10 / 0
except ZeroDivisionError as e:
  print(e)


try:
  10 / 2
except ZeroDivisionError as e:
  print(e)
else:
  print("Success!")


try:
  10 / 0
except ZeroDivisionError as e:
  print(e)
else:
  print("Success!")
finally:
	print("ZeroDivisionError Check")