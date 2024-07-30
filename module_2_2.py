first = int(input('num1 : '))
second = int(input('num 2: '))
third = int(input('num 3: '))

#
if (first == second) and (first == third) and (second == third):
    print(3)
elif (first == second) or (first == third) or (second == third):
    print(2)
elif first != second and first != third and second != third:
    print(0)
