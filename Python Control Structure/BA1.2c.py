# Input angle from the user
angle = float(input("Enter an angle in degrees: "))

# Classifying the angle
if angle <= 0 or angle >= 360:
    print("Invalid angle")
elif angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif angle < 180:
    print("Obtuse angle")
else:
    print("Invalid angle")  # Angles 180 and 360 are not valid for classification
