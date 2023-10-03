angle = float(input("Enter an angle between -180° and 180°: "))

angle %= 360

if angle < 0:
    angle += 360

print(f"Equivalent angle between 0° and 360°: {angle}")