f = open("file.txt", "r")
content_readlines = f.readlines()
print("File lines: ", content_readlines)
f.close()
first_two_lines = content_readlines[:2]

with open("output_file.txt", "w") as f:
    f.writelines(first_two_lines)
