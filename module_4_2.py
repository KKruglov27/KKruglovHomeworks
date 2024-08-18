def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()

print()


def test_function(prev_type):
    if isinstance(prev_type, str):
        print(prev_type)
    else:
        print("Тип этой переменной в области видимости 'test_function', уже не STR, он был изменен")
    print()
    def inner_function(prev_type):
        new_type = {"Я value1 в области видимости функции": "'test_function', по моему я все так же строка"}
        prev_type = new_type
        if isinstance(prev_type, str):
            print(prev_type)
        else:
            print("Тип этой переменной в подфункции 'inner_functions' уже не STR, он был изменен в данной подфункции.")
    inner_function(prev_type)


value1 = "Я в области видимости функции test_function, пока что я строка"
test_function(value1)

print()
#________________________________________________________________


def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

# inner_function()

# inner_function()
#    ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

# Вызов подфункции в глобальном пространстве имен может быть осуществлен только
# с помощью родительской функции.

#________________________________________________________________

def test_function(line):
    new_line = "Я в области видимости функции test_function"
    def inner_function(new_line):
        return inner_function()


def test_func(line):
    print(line)


test_func("Я в области видимости функции test_function")


def in_func(new_line):
    print(new_line)


in_func("Я не в области видимости функции test_function")