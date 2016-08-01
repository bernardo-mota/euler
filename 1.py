#!/usr/bin/python3
#List where numbers divisible by 3 or 5 will be added
li = []# It is still empty

for i in range(1000):#for loop to check all numbers from 0 to 999 if they are divisible
  if i%3==0 or i%5==0:#if i is divisible by 3 or 5
    li.append(i)#Add number to list li which meet criterea

print(sum(li))#print the sum of list li (numbers under 1000 divisible by 3 or 5)
