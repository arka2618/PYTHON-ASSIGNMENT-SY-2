with open("file.txt", "r") as file:
    lines = file.readlines()
    print("File lines: ", lines)
    print("\n")

line_count = len(lines)
first_two_lines = lines[:2]

with open("Output file.txt", "w") as file:
    file.writelines(first_two_lines)

print("Total lines in input file:", line_count)
print(f"Extracted lines: {first_two_lines}")