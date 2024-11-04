import math
###############################################
l = []
for i in range(int(input())):
    l.append(eval(input()))
print(math.fsum(l)) #print(sum(l)) also works
print(int(math.sqrt(l[0])))
