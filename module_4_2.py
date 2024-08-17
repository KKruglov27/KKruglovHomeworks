def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()

#________________________________________________________________

def test_function(value1, value2):
    value1 = "Я value1 в области видимости функции test_function, пока что я строка"
    value2 = "Я value 2, в области видимости 'test_functions'"
    if isinstance(value1, str):
        print(value1)
    else:
        print("Тип этой переменной в 'inner_functions', уже не STR, он был изменен")
    print(value2)
    def inner_function():
        global value1
        nonlocal value2
        value1 = {"Я value1 в области видимости функции": "'test_function', я строка"}
        if isinstance(value1, str):
            print(value1)
        else:
            print("Тип этой переменной в 'inner_functions', уже не STR, он был изменен в данной подфункции.")
        value2 = "Я - value2, по моему сейчас я только в области видимости функции 'inner_function'."
        if isinstance(value2, str):
            print(value2)
        else:
            print("This value type is not defined. It's from inner_function.")
    inner_function()
    return value2

value1 = ""
value2 = ""


test1 = test_function(value1, value2)

#________________________________________________________________

value5 = 10
value6 = 50
def test_function(*args):
        value3 = value5 * value6
        value4 = value6 / value5
        print(value3, value4)
        def inner_function(*args):
            global value5
            global value6
            value6 = 100
            value5 = 20
            values3 = value5 * value6
            values4 = value6 / value5
            print(values3, value4)
        inner_function(*args)


test2 = test_function()


#________________________________________________________________


# def test_function():
#    def inner_function():
#        print("Я в области видимости функции test_function")
#    inner_function()


# inner_function()

# inner_function()
#    ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

# Кажется вызов подфункции в глобальном пространстве имен может быть осуществлен только
# с помощью родительской функции.