L = [5, 8, 6, 3, 8, 7, 7, 12]
L1 = []
for i in L:
    L1.append(i)
print(L1)

L = [5, 8, 6, 3, 8, 7, 7, 12]
L1=[i for i in L]
print(L1)

L = [5, 8, 6, 3, 8, 7, 7, 12]
L1=[i+3 for i in L]
print(L1)

L = [5, 8, 6, 3, 8, 7, 7, 12]
L1=[i+3 for i in L if i%2==0]
print(L1)

L = [5, 8, 6, 3, 8, 7, 7, 12]
L1=[i for i in L if i%2==0]
print(L1)
