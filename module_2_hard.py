numbers = int(input('Введите число: '))

cipher = str()

for num1 in range(1, numbers):
    for num2 in range(num1 + 1, numbers):
        summa = num1 + num2
        if numbers % summa == 0:
            cipher += str(num1) + str(num2)

print(cipher)