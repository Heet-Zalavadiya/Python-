# Define a tuple
my_tuple = (1, 2, 3, 4, 5)

print("Original tuple:", my_tuple)

try:
    # Attempt to modify the tuple (this will raise an error)
    my_tuple[2] = 100
except TypeError as e:
    print("Error:", e)

print("Tuple after attempting to modify:", my_tuple)
