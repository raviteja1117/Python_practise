def add(a, b):
    sum_value = a+b
    # print(sum_value)
    return sum_value


def subtract(a, b):
    subtract_value=a-b
    # print(subtract_value)
    return subtract_value


def multiply(a, b):
    multiply_value = a*b
    # print(multiply_value)
    return multiply_value


def division(a, b):
    division_value = a / b
    # print(division_value)
    return division_value

def operate(func, x, y):
    result = func (x, y)
    return result

print(operate(division, 2, 4))

# waste of time
"""
input_function = input("Enter your function values?")
while input_function !='finish':
    print(operate(input_function,2, 4))
    input_function=input("Enter your function values?")
    # add input, "add"
    # '1' int('1')=1
    """
