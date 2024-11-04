import math

N1 = float(input())
N2 = float(input())

A = math.floor(N1)
print(A)
print(math.factorial(A))

B = math.ceil(N2)
print(B)
print(math.factorial(B))

n1 = int(N1)
n2 = int(N2)

print(math.pow(n1,n2))
print(math.fmod(n1,n2))
print(math.gcd(n1,n2))
