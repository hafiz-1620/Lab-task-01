def convert_decimal(num):
    binary = bin(num)  
    octal = oct(num)   
    hexadecimal = hex(num)  
    return binary, octal, hexadecimal
decimal_num = int(input("Enter a decimal number: "))
binary, octal, hexadecimal = convert_decimal(decimal_num)
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")
