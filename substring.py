def count_occurrences(string, substring):
    
    return string.count(substring)

def main():
    
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to search for: ")
    occurrences = count_occurrences(main_string, substring)
    print(f"The substring '{substring}' occurs {occurrences} time(s) in the main string.")

if __name__ == "__main__":
    main()
