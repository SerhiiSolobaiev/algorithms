import sys

from math import ceil
my_list = []
def karatsuba(x, y):
	x = str(x)
	y = str(y)
	n = max(len(x),len(y))
	#print n
	if n <= 1:
		return int(x)*int(y)
	else:
		x = leveling(x,n)
		y = leveling(y,n)
		n_2 = n / 2
		
		a = int(x[:n_2])
		b = int(x[n_2:])
		c = int(y[:n_2])
		d = int(y[n_2:])
		
		print "-----------------------a = ",a," b = ",b," c = ",c," d = ",d
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_bc = karatsuba((a + b), (c + d)) - ac - bd
		my_list.append(ad_bc)
		print "n = ",n, " n/2 = ",n/2
		n_2 = int(ceil(n / 2.0))
		print "n_2 = ",n_2
		return (10**(n) * ac)  + (10**n_2 * ad_bc) + bd
     
def leveling(numb,n):
	numb = str(numb)
	length = len(numb)
	numb = "0"*(n-length) + numb
	return numb
	
x = 1234
y = 5678
a = karatsuba(x,y)

print a
print my_list
print my_list.count(12)