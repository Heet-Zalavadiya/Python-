import math

def volume_of_cube(side):
    return side**3

def volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

def volume_of_cylinder(radius,height):
    return math.pi * radius**2 * height

if __name__ == "__main__":

    print("Welcome to the Volume Calculator")

    print("Choose a shape:")
    print("1. Cube")
    print("2. Sphere")
    print("3. Cylinder")

    shape_choice = int(input("Enter the number of shape (1/2/3):"))

    if shape_choice == 1:
        side = float(input("Enter the side length of the cube:"))
        volume = volume_of_cube(side)
        print(f"The volume of the cube is {volume:.2f} cubic units.")

    elif shape_choice == 2:
        radius = float(input("Enter the radius of the sphere :"))
        volume = volume_of_sphere(radius)
        print(f"The volume of the sphere is {volume:.2f} cubic units.")

    elif shape_choice == 3:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        volume = volume_of_cylinder(radius, height)
        print(f"The volume of the cylinder is {volume:.2f} cubic units.")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        
