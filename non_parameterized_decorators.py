
def upper_letter(func):
    print("I am into upper letter function")
    def upper():
        print("I am in upper function")
        function=func()
        print("I am returning upper function")
        return function.upper()
    return upper
def display():
    print("I am in display function")
    return "hello"

result=upper_letter(display)
print(result())
