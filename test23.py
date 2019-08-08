import sys


#adding commit
#stashing


sys.setrecursionlimit(3000)

def fact(n):
	if n == 0 :
		return 1
	else :
		return n * fact( n-1)

print(fact(0))
print(fact(5))		

def fact2(n) :
	if n == 0 :
		return 1
	else :
		return n * fact2(n-1)
	
print( fact2(50))