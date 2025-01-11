import math

# Function to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

# Main program
if __name__ == "__main__":
    # Get user input for the radius
    radius = float(input("Enter the radius of the sphere: "))
    
    # Calculate the volume using the function
    volume = calculate_sphere_volume(radius)
    
    # Output the result
    print(f"The volume of the sphere with radius {radius} is {volume:.2f} cubic units.")
