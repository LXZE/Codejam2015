import re
from fractions import gcd
def lcm(numbers):
    return reduce(lambda x, y: (x*y)/gcd(x,y), numbers, 1)
f = open("B-large.in","r")
w = open("output_blarge.txt","w")
num = f.readline()
for i in range(0,int(num)):
	barber,atN = [long(l) for l in f.readline().split()]
	speed = [int(l) for l in f.readline().split()]
	res = 1
	l = []
	for k,s in enumerate(speed):
		l.append(k+1)
	numLcm = lcm(speed)
	t = 1
	while t<numLcm:
		for iSpeed,s in enumerate(speed):
			if t%s == 0:
				l.append(iSpeed+1)
		t+=1
	res = l[(atN%len(l))-1]
	print("Case #{0}: {1} ".format(i+1,res))
	w.write("Case #{0}: {1}\n".format(i+1,res))
w.close()