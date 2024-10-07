def operation(N,m):
#############################
multiples = [str(N * i) for i in range(1, m + 1)]
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    return multiples, factorial


multiples, factorial = operation(int(input()), int(input()))

print(" ".join(multiples))
print(factorial)
