def print_params(a=1, b='строчка', c=True):
    print(a, b, c)


print_params(a='теперь тут строчка', c=False, b=11+11)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list = ['isistese python', ('start', 'suffix', 'end'), {14, 56, 56,6, 56, 6, 77.56, 14}]
values_dict = {'a': 1, 'b': 'строчка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [101.101, '<- Слева число и справа так же число ->', 42]
print_params(*values_list_2)



#def dobavlenie_v_ryckzack(moi_ryckzack=[]):
#dobavlenie_v_ryckzack()
# Ошибка

def dobavlenie_v_ryckzack(a='moi',b='veshichki', moi_ryckzack=None):
    if moi_ryckzack is None:
        moi_ryckzack = []
        moi_ryckzack.append(b)
    print(a, *(moi_ryckzack), 'teper v ryckzacke')

dobavlenie_v_ryckzack()