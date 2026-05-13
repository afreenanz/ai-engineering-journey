# ── Exercise 1: Even number filter ──────────────────────────
# Write a function that takes a list of numbers
# and returns only the even ones.
# Example: filter_evens([1,2,3,4,5,6]) → [2, 4, 6]

def filter_evens(numbers):
    return [num for num in numbers if num % 2 ==0]
print(filter_evens([1,2,3,4,5,6]))


# ── Exercise 2: Student class ────────────────────────────────
# Build a Student class with:
# - name and grade as attributes
# - a result() method that returns "pass" if grade >= 50, else "fail"
# - a __str__ method so print(student) shows something useful

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def result(self):
        if self.grade >= 50:
            return "pass"
        else:
            return "fail"

    def __str__(self):
        return f"Student({self.name}, {self.grade})"

s1 = Student("Alice", 85)
s2 = Student("Bob", 45)
print(s1)
print(s1.result())
print(s2.result())


# ── Exercise 3: File reader ──────────────────────────────────
# Write a function that reads a text file line by line
# and prints each line with its line number.
# Example output:
# 1: Hello world
# 2: This is line two

def read_file(filename):
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}: {line.strip()}")
with open("test.txt", "w") as f:
    f.write("Hello world\nThis is line two\nLine three here")

read_file("test.txt")