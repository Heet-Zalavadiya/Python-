# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print("Before swapping:")
print("tuple1:", tuple1)
print("tuple2:", tuple2)

# Swap the values of the two tuples without using a temporary variable
tuple1, tuple2 = tuple2, tuple1

print("\nAfter swapping:")
print("tuple1:", tuple1)
print("tuple2:", tuple2)
