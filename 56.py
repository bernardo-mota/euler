maximum = 0

def power(a,b):
    
    li = []

    str_ab = str(a**b)
    
    for char in str_ab:
        li.append(int(char))
    
    return sum(li)


for a in range(100):
    for b in range(100):
        sum_of_alg = power(a,b)
        if sum_of_alg > maximum:
            maximum = sum_of_alg

print(maximum)
