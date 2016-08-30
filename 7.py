def is_prime(x):
	for i in list(range(2,x-1)):
		if not x % i:
			return False
	else:
		return True


number_of_primes = 0
counter = 1

while number_of_primes <= 10000:
	counter +=1
	if is_prime(counter):
		number_of_primes += 1
		print(number_of_primes)

print(counter)
