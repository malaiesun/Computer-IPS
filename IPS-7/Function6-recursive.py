if len(L)==1:
        return L[0]
    else:
        return L.pop()*product(L)

L = []
for i in range(int(input())):
    L.append(int(input()))

print(L)
print(product(L))
