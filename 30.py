nums = []

def operation(x):
	counter = 0
	for i in str(x):
		counter += int(i)**5
	return counter


for i in range(2,10**7):
	if i == operation(i):
		#print(i)
		nums.append(i)

print(sum(nums))
