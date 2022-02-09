import hfunc

n_outputs = 7
x0, x1, x2, x3 = [int(input("Enter 0 or 1 for x" + str(x) + ": ")) for x in range(4)]

# LFSR polynomial = x^4 + x^3 + x + 1
for i in range(n_outputs):
    print(x3, end=' ')
    x0, x1, x2, x3 = x3 ^ x2 ^ x0, x0, x1, x2
