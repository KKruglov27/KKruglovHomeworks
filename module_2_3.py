my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
end = len(my_list)

while index < end:
    if my_list[index] > 0:
        print(my_list[index])
    index += 1
    if index == end:
        break
    if my_list[index] == 0 or my_list[index] < 0:
        continue