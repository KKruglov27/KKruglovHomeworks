def get_sum_elems(node):
    sum = 0
    for elem in node:
        if type(elem) == int:
            sum += elem
            continue
        if type(elem) == str:
            sum += len(elem)
            continue
        if isinstance(elem, dict):
            for key, val in elem.items():
                if type(key) == int:
                    sum += key
                if type(key) == str:
                    sum += len(key)
                if type(val) == int:
                    sum += val
                if type(val) == str:
                    sum += len(val)
        else:
            sum += get_sum_elems(elem)
    return sum

result = get_sum_elems(node = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
])

print(result)