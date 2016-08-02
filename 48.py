li = []
for i in list(range(1,1001)):
	res_str = str(i**i)
	newRes_str = res_str[-10:]
	del res_str
	li.append(int(newRes_str))

result = str(sum(li))
finalResult = result[-10:]
print("{} is the result of the series".format(finalResult))
