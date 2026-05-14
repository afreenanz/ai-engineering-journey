# Exercise 1: Given a list of student names with duplicates,
# return a sorted list with duplicates removed.
# Example: ["Alice", "Bob", "Alice", "Charlie", "Bob"] → ["Alice", "Bob", "Charlie"]

def unique_sorted(names):
    return sorted(set(names))


# Exercise 2: You have a list of dictionaries representing students.
# Return only students who passed (grade >= 50), sorted by grade descending.
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 40},
    {"name": "Charlie", "grade": 72},
    {"name": "Diana", "grade": 30},
    {"name": "Eve", "grade": 91},
]

def passing_students(students):
    return sorted([s for s in students if s["grade"] >= 50], key=lambda x: x["grade"], reverse=True)


# Exercise 3: Count how many times each word appears in a string.
# Example: "the cat sat on the mat" → {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count


if __name__ == "__main__":
    print(unique_sorted(["Alice", "Bob", "Alice", "Charlie", "Bob"]))
    print(passing_students(students))
    print(word_count("the cat sat on the mat"))