powers = []

for a in range(2,101):
    for b in range(2,101):
        a_b = a**b
        b_a = b**a

        if not a_b in powers:
            powers.append(a_b)

        if not b_a in powers:
            powers.append(b_a)

print(len(powers))
