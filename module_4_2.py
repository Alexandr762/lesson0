def test_function():
    def  inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()

inner_function()# возникает ошибка, потому что  inner_function() находится за пределами видимости test_function()