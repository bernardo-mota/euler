
li = []#Define List

for i in list(range(101)):#Generate list 1, 2, 3 ... 100
	li.append(i*i)#Add the squared numbers

print(sum(list(range(101)))**2 - sum(li))
