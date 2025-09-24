# Task 1

try:
    file = open("Assignment-4/sample.txt", "r")
    line_number = 1
    for line in file:
        print(f"line {line_number}: {line.strip()}")
        line_number += 1
    file.close()
except FileNotFoundError:
    print("Error: The sample.txt was not found")



# Task 2

text_to_write = input("Enter text to write to the file: ")
with open("Assignment-4/output.txt", "w") as file:
    file.write(text_to_write)
print("Data successfully written to output.txt.")


text_to_append = input("Enter additional text to append: ")
with open("Assignment-4/output.txt", "a") as file:
    file.write(" " + text_to_append)
print("Data successfully appended.")


with open("Assignment-4/output.txt", "r") as file:
    final_content = file.read()
print("Final content of output.txt:", final_content)
