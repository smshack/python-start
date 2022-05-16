# 오류를 회피하는 방법
try:
  10 / 0
except ZeroDivisionError:
  pass

"""
pass 
를 사용하면아무일도 없던것 처럼 오류 회피 가능
"""
# 오류를 일부러 발생시키는 방법
# 프로그래밍을 하다보면 의도적으로 오류를 발생시켜야 하는 상황이 있음


try:
  raise NameError
except NameError:
  print("NameError occurred")