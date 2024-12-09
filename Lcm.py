def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
# Function to compute the LCM
def lcm(x, y):
    return (x * y) // gcd(x, y)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")
