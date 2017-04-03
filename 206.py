""" 1_2_3_4_5_6_7_8_9_0 """#9 underscores, abcdefghi

#Answer is 1929374254627488900
#It took 602 s to run this program on my machine

for i in range(1010101010,1389026623+1):
	s = str(i**2)
	if s[-1] == "0":
		if s[-3] == "9":
			if s[-5] == "8":
				if s[-7] == '7':
					if s[-9] == '6':
						if s[-11] == '5':
							if s[-13] == '4':
								if s[-15] == '3':
									if s[-17] == '2':
										if s[-19] == '1':
											print(i)
											break




#def is_square(n):#TODO this function
#	if sqrt(n) - int(sqrt(n)) == 0:
#		return True
#	else:
#		return False

# 1929394959697989990 is the max value, its int(sqrt) is 1389026624


#initial = 1020304050607080900 #_ replaced with 0

#for a in range(10):
#	print(a)#debug
#	for b in range(10):
#		for c in range(10):
#			for d in range(10):
#				for e in range(10):
#					for f in range(10):
#						for g in range(10):
#							for h in range(10):
#								for i in range(10):
#									if is_square(initial +a*10 +b*10**3 +c*10**5 +d*10**7  + e*10**9 +f*10**11 +g*10**13 +h*10**15 +i*10**17):
#										print("The result is 1{}2{}3{}4{}5{}6{}7{}8{}9{}0".format(i,h,g,f,e,d,c,b,a))
#
