'''
Create a list of N integers repesenting the urea value of a diabetic patients for N months.
The sum of the urea value of N months represent the urea concentration.
The square root of the first month value gives the urea rate.
Print the urea concentration.
Print the urea rate.
'''
n = int(input())
l1 = []
for i in range(n):
    x = float(input())
    l1.append(x)
print(math.fsum(l1))
print(math.floor(math.sqrt(l1[0])))
