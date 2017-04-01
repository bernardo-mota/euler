def tri(n):#tested and working, returns correct int
	return int(n*(n+1)/2)

#def divs(n):# D = N\{1} # We need a more efficient algorithm
#	counter = 2 #because every number is divisible by 1 and itself
#	for i in range(2, int((n+1)/2) ):
#		if n % i == 0:#If n is evenly divisible by i
#			counter += 1
#	return counter

#def divs(n):
#	"""Returns how many divisors"""
#	divisors = 2 #Every number is divisible by 1 and itself
#	for i in range(2,n):
#		if n % i == 0:
#			divisors += 1
#	return divisors 	

def divs(n):
	divisors = set ()
	for i in range(1,int(n**0.5)+1):
		if not n % i:
			divisors.add(i)
			divisors.add(n//i)
	return len(divisors)
			


num = 8
while divs(tri(num)) < 500:
	num +=1
	print(divs(tri(num)))
	#print(tri(num))

print(tri(num))
