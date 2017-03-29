def is_pandigital(n):
	n_str = str(n)
	for i in range(1, len(n_str)+1):
		if n_str.count(str(i)) != 1:
			return False
	else:
		return True

def is_prime(n):#Tested and working
	for i in range(2, 1+int(n**0.5)):
		if not n % i:
			return False
	else:
		return True

counter = 5
while True:
	counter += 1
	if is_pandigital(counter) and is_prime(counter):
		print(counter)

#Please wait a minute, output is the last line
