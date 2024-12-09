def toggle_case(s):
   
    return s.swapcase()

def main():   
    user_input = input("Enter a string: ")
    
    toggled_string = toggle_case(user_input)
    
    print(f"Toggled case: {toggled_string}")

if __name__ == "__main__":
    main()
