# Take input coefficients a, b, and c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
D = b**2 - 4*a*c

# Find the roots using the quadratic formula
if D > 0:
    # Two real roots
    root1 = (-b + (D)**0.5) / (2 * a)
    root2 = (-b - (D)**0.5) / (2 * a)
    print(f"The roots are real and distinct: {root1} and {root2}")
elif D == 0:
    # One real root (repeated)
    root = -b / (2 * a)
    print(f"The root is real and repeated: {root}")
else:
    # Two complex roots
    real_part = -b / (2 * a)
    imaginary_part = (abs(D)**0.5) / (2 * a)
    print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
