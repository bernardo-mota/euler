def is_palindrome(n):
    """Input is an integer"""
    str_n = str(n)
    return str_n == str_n[::-1]

palindromes = []#List to be populated by ints

for a in range(999,100,-1):
    for b in range(999,100,-1):
        test = a*b
        if is_palindrome(test):
            palindromes.append(test)
            #print(test)

print(max(palindromes))

"""
906609

real    0m1.373s
user    0m1.356s
sys 0m0.008s



"""
