if n == 0:
            return 1
    else:
        r = n % 10
        rem = n // 10
        return r * product(rem)
num = int(input())
prod = product(num)
print(prod)
if prod % 2 == 0:
    print('Congratulations')
else:
    print('Try again')
