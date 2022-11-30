"""Polynomial calculator

INPUT
x c(n) c(n-1) ... c(0)

OUTPUT
c(n)x^n + c(n-1)x^(n-1) + ... + c(0)
"""

while True:
	x,y,*s=map(int, input().split())

	for n in s:
		y*=x
		y+=n

	print(y)
