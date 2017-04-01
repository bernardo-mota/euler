def f(x):
	res = 0
	for char in str(x):
		res += int(char)**2
	return res

def f_has_89(x,treshold):
	results = set()
	for i in range(treshold):#Do it treshold times
		results.add(x)
		x = f(x)

	if 89 in results:
		return True
	else:
		return False


how_many = 0
i = 0
while i < 10**7:
	i += 1
	if f_has_89(f(i),15):
		how_many += 1
		#print(how_many)#debug

print(how_many)
"""The answer is 8581146, it took more than 1 min to run.
I don't know why, but this script's output (08581146) begnins with a 0.
The decrease the time maybe you could decrease the treshold (line 23, col 20)
"""
