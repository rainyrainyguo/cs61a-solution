def trace1(fn):
	"""Return a version of fn"""
	def traced(x):
		print('Calling', fn, 'on argument',x)
		return fn(x)
	return traced

def gcd(m,n):
    """Returns the largest k that divides m and n
    >>> gcd(12,8)
    4
    """
    if n%m==0:
    	return m
    elif m<n:
    	return gcd(n,m)
    else:
    	return gcd(m-n,n)

def curry2(f):
 	def g(x):
 		def h(y):
 			return f(x,y)
 		return h
 	return g


def square(x):
	return x*x
square=trace1(square)

@trace1
def sum_squares_up_to(n):
	k=1
	total=0
	while k<=n:
		total,k=total+square(k),k+1
	return total

def rational(n,d):
	"""Construct a rational number that represents N/D."""
	return [n,d]
def numer(x):
	return x[0]
def denom(x):
	return x[1]

def count(s,value):
	total,index=0,0
	for element in s:
		if element == value:
			total=total+1
	return total

