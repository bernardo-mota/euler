num = 600851475143
print("The result is the last number printed on screen. Please wait a few seconds")
while True:
    for i in range(2,num//2+1):
        if not num % i:
            num = num / i
            print(i)
