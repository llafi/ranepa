from validator import valid_number

def square(x):
    if not valid_number(x):
        raise ValueError("Нужно число")
    return x*x

print(square(4))
