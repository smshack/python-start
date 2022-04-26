"""
int     정수
float   실수
real    변수(실수부)
imag    변수(허수부)
conjugate   변수(켤레복소수)
16진수
"""
a = 10
b = -2.5
c = 1 + 2j
d = 0xDA # 218

print(a, type(a))
print(b, type(b))
print(c, c.real , c.imag, c.conjugate(), type(c))
print(d, type(d))

print(a + b, type(a + b))
print(c + d, type(c + d))