import csv
f = open("p099_base_exp.txt")#path to file
csv_reader = csv.reader(f)

#row_number = 0
calculations = []
for row in csv_reader:
	calculations.append(int(row[0])**int(row[1]))
	print(len(calculations))


max_power = max(calculations)
result = calculations.index(max_power)

print(result+1)#because indexes start on 0
