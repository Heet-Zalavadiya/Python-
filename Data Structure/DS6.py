# Define a list with duplicate elements
my_list = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 5]

# Convert the list to a set to remove duplicates, then convert it back to a list
unique_list = list(set(my_list))

# Print the original list and the list with duplicates removed
print("Original list:", my_list)
print("List after removing duplicates:", unique_list)
