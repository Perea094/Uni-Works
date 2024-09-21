# Diego Perea León
# A01708350

"""tiros = ['aguila', 'sol']
for a in tiros:
    for b in tiros:
        for c in tiros:
            print(a, b, c)

"""
e = []
for a in range(1,7):
    for b in range(1,7):
        print(a,b)
        c = a+b

        e.append(c)
        f = sum(e)/len(e)
print(f)