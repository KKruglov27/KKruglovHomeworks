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
        value1 = {"Я value1 в области видимости функции": "'test_function', я строка"}
        value2 = "Я - другая value2, по моему сейчас я только в области видимости функции 'inner_function'."
        if isinstance(value1, str):
            print(value1)
        else:
            print("Тип этой переменной в 'inner_functions', уже не STR, он был изменен в данной подфункции.")
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