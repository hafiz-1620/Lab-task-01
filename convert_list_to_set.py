def list_to_set(input_list):
    return set(input_list)
def main():
   
    input_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
    result_set = list_to_set(input_list)
    print("Converted Set:", result_set)

if __name__ == "__main__":
    main()
