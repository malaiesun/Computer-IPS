def unique_even(L1):
#######################################
L2 = list(set(L1))
    even = [num for num in L2 if num % 2 == 0]
    return L2, even

l = []
for i in range (int(input())):
    l.append(int(input()))
    
L2, even = unique_even(l)
print(L2)
print(even)
