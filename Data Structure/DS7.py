# Function to convert a space-separated string to a set of integers without using map
def input_set():
    user_input = input("Enter elements of the set (space-separated): ")
    # Create an empty set
    result_set = set()
    # Split the input string and convert each element to an integer and add it to the set
    for item in user_input.split():
        result_set.add(int(item))  # Convert to integer and add to set
    return result_set

# Get two sets from the user
set1 = input_set()
set2 = input_set()

# Calculate the union and intersection
union_set = set1 | set2  # Union using the | operator
intersection_set = set1 & set2  # Intersection using the & operator

# Print the results
print("Set 1:", set1)
print("Set 2:", set2)
print("Union of Set 1 and Set 2:", union_set)
print("Intersection of Set 1 and Set 2:", intersection_set)

