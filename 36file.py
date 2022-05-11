# 파일 열기/ 생성 및 쓰기
"""
파일 객체 이름= open("파일 경로/ 파일이름","파일 열기 모드") 형식
파일을 열고 다 썼다면 반드시 닫아줘야 함
r 읽기 모드 - 파일을 읽기만 할 때 사용
w 쓰기 모드 - 파일에 내용을 새로 작성할 때 사용
a 추가 모드 - 파일의 마지막 부분에 내용을 추가할 때 사용
"""
import pathlib
import os
print('현재 파일 경로')
print(pathlib.Path(__file__))
print('현재 파일 디렉터리 경로')
print(pathlib.Path(__file__).parent)
print('현재 파일 경로')
print(pathlib.Path(__file__).parent.absolute())
print(f"{pathlib.Path(__file__).parent}/test")
# testdirpath = "{0}/test".format(pathlib.Path(__file__).parent)
testdirpath = f"{pathlib.Path(__file__).parent}/test"
testfilepath = f"{testdirpath}/test.txt"
print(testdirpath)
os.makedirs(testdirpath, exist_ok=True)

f = open(testfilepath,'w')
for i in range(1, 11) :
    sentence = "%d번째 줄입니다.\n" %i
    f.write(sentence)
f.close()

f = open(testfilepath,'r')
a = open(testfilepath, 'r')
for i in range(1,11) :
    data = a.readline() #파일을 닫기 전까지 한 줄 읽고
    print(data) #한 줄 출력
a.close()


a = open(testfilepath, 'r')
data = a.read() #전체 문자열을 그대로 읽어들임
print(data)
a.close()

a = open(testfilepath, 'r')
while 1 :
    line = a.readline()
    if not line : break #line이 None이 되면(=false) 반복문 탈출
    print(line)
a.close()



f = open(testfilepath, 'a')
for i in range(2, 5) :
    data = "%d번째 줄입니다 추가.\n" %i
    f.write(data)
f.close()

a = open(testfilepath, 'r')
lines = a.read()
a.close()
print(lines)

list = []

while 1 :
    data = input("빈칸을 입력하면 입력을 종료합니다.")
    if not data : break
    list.append(data)

print(list)