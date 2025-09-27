# Task 1

students = {
    'Ravi' : 95,
    'Kiran': 76,
    'Lucky':67,
    'Alice': 85
}
name = input("Enter the student's name: ")

if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print('Student not found')


# Task 2

numbers = [1,2,3,4,5,6,7,8,9,10]
first_five = numbers[:5]
reversed_five = first_five[::-1]

print(f"Original list: {numbers}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {reversed_five}")