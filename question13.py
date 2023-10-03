length_in_cm = float(input("Enter a length in centimeters: "))

if length_in_cm < 0:
    print("The entry is invalid")
else:
    length_in_inches = length_in_cm / 2.54
    print(f"Length in inches: {length_in_inches}")