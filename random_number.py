import random
def random_number(min_value, max_value):
    return random.randint(min_value, max_value)
min_value = 1
max_value = 100
random_number = random_number(min_value, max_value)
print(f"Random number between {min_value} and {max_value} is: {random_number}")
