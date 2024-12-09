import random
import string
def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
def main():
    length = int(input("Enter the length of the random string: ")) 
    result = generate_random_string(length)
      
    print(f"Random String of length {length}: {result}")

if __name__ == "__main__":
    main()
