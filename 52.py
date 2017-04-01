def cond(x,multiplier):
	li_a = []
	li_b = []

	for i in range(10):
		li_a.append(str(x).count(str(i)))
		li_b.append(str(multiplier*x).count(str(i)))

	if li_a == li_b:
		return True
	else:
		return False

i = 1
while True:
	i +=1
	if cond(i,2) and cond(i,3) and cond(i,4) and cond(i,5) and cond(i,6):
		break

print(i)
#The result is 142857, took less than 5 s on my machine.
