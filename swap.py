def swap(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    # Swapping
    temp = a
    a = b
    b = temp
    print(f"After swap: a = {a}, b = {b}")
    return a, b
swap(5,10)