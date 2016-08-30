import math

def is_prime(x):
	for i in list(range(2, int(math.sqrt(x)+1) )):
		if not x % i:
			return False
	else:
		return True


sum_of_primes = 0
counter = 2

while counter < 2000000:
	if is_prime(counter):
		sum_of_primes += counter
		print(counter)
	counter +=1

print(sum_of_primes)
