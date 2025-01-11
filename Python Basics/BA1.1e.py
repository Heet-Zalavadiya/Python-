# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check for valid input (a cannot be zero)
if a == 0:
    print("This is not a quadratic equation because a = 0.")
else:
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check the discriminant to determine the nature of the roots
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + (discriminant)**0.5) / (2*a)
        root2 = (-b - (discriminant)**0.5) / (2*a)
        print(f"The roots of the equation are real and distinct:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    
    elif discriminant == 0:
        # One real root (repeated root)
        root = -b / (2*a)
        print(f"The root of the equation is real and repeated:")
        print(f"Root: {root}")
    
    else:
        # Two complex roots
        real_part = -b / (2*a)
        imaginary_part = ((-discriminant)**0.5) / (2*a)
        print(f"The roots of the equation are complex:")
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")
