numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for num1 in range(len(numbers)):
    if num1 == 0:
        continue
    is_prime = True
    for num2 in range(1, num1):
        if numbers[num1] % numbers[num2] == 0:
            is_prime = False
    if is_prime:
        primes.append(numbers[num1])
    else:
        not_primes.append(numbers[num1])


print(primes)
print(not_primes)