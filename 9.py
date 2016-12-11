def is_sum(a,b,c):
	if a + b + c == 1000:
		return True

	else:
		return False

def is_pythagorean(a,b,c):
	if a**2 + b**2 == c**2:
		return True

	else:
		return False



for a in list(range(1,1000)):
	#print(a)
	for b in list(range(1,1000)):
		for c in list(range(1,1000)):
			#print("{} {} {}".format(a,b,c)) #debug info
			if is_sum(a,b,c) and is_pythagorean(a,b,c):
				print(a*b*c)
				break
