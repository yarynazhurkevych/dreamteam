string = input("Enter a string: ")

distinct_characters = []

for char in string:
    if char not in distinct_characters:
        distinct_characters.append(char)

num_of_distinct_characters = len(distinct_characters)

print(f"Number of distinct characters in the string: {num_of_distinct_characters}")
