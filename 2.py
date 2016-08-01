#!/usr/bin/python3
#List for all fibonaci numbers under 4 millons
fib = [1,2]# Starts with 1 and 2

for i in range(4000000):
	if fib[-1] < 4000000:#If the last element of fibonacci sequence is smaller than 4 million add to fibonacci sequence
		fib.append(fib[-1]+fib[-2]) #Add sum of last to fibonacci numbers to the list fib

evenfib = []#Declare empty list for even fibonacci sequence

for num in fib:#For all numbers in fibonacci sequence
	if num%2 ==0:#If they are even (divisible by 2)
		evenfib.append(num)#Add them to evenfib list

print(sum(list(evenfib)))#Print sum of evenfib numbers
