def custom_write(file_name, info):
    file_a = open('file_name', 'w', encoding='utf-8')
    for line in info:
        file_a.write(f'{line}\n')
    file_a.close()
    file_r = open('file_name', 'r', encoding='utf-8')
    count = 1
    result_dict = {}
    while True:
        line_byte = file_r.tell()
        line_str = file_r.readline().strip()
        if not line_str:
            break
        else:
            result_dict.update({(count, line_byte): line_str})
            count += 1
    return result_dict

info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
        ]

result = custom_write('file_name', info)
for elem in result.items():
    print(elem)

# Как же мне здесь мог пригодиться метод seek?
