import time

word = input("Enter the word to search: ")
count = 0
with open("TXT.txt", "r") as file:
    for line in file:
        if word.lower() in line.lower():
            count += 1
print(f"\nThe word '{word}' occurs in {count} lines")

time.sleep(3)
with open("output_file.txt", "w") as f:
    f.writelines(word)
print(f"\nThe word '{word}' has been written to 'output_file.txt'")
