def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Input list with duplicates
input_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
unique_list = remove_duplicates(input_list)
print("List after removing duplicates:", unique_list)
