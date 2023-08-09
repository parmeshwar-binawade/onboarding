def decorator_function(a, b):
    def Inner_1(function_1):
        print("Summation of values - {}".format(a + b))


        return wrapper_1

    return Inner_1
def my_function(*args):
    for ele in args:
        print(ele)

decorator_function(22, 14)(my_function)