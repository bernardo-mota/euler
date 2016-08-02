import math# math.factorial()



def sumOfFacts(resultInt):
	resultStr = str(resultInt)
	li = []
	newli = []
	for i in resultStr:
		li.append(i)
	for i in li:
		newli.append(math.factorial(int(i)))
	del li
	return sum(newli)
	del newli

counter = 3
listOfGoodNums = []

while True:
	counter += 1
	if sumOfFacts(counter) == counter:
		listOfGoodNums.append(counter)
		print("{} is a corious number".format(counter))
		print("{} is the sum of curious numbers until now".format(sum(listOfGoodNums)))
