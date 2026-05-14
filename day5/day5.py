import json

# Exercise 1: Safe file reader
# Read a JSON file and return its contents.
# Handle these specific errors gracefully (don't crash, print a useful message):
# - File doesn't exist
# - File exists but contains invalid JSON
# - Any other unexpected error
# Return None if any error occurs.

def safe_read_json(filepath):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' contains invalid JSON.")
        return None
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None


# Exercise 2: Safe student loader
# Given a list of raw data (could be anything, not always valid),
# return only valid student dicts.
# A valid student dict has: "name" (string) and "grade" (int or float)
# Skip invalid entries silently.

def clean_students(raw_data):
    valid_students = []
    for item in raw_data:
        if isinstance(item, dict):
            name = item.get("name")
            grade = item.get("grade")
            if isinstance(name, str) and isinstance(grade, (int, float)):
                valid_students.append(item)
    return valid_students

# Exercise 3: Robust grade calculator
# Given a list of student dicts, calculate the class average.
# Handle: empty list, missing "grade" key, non-numeric grade values
# Return 0.0 if no valid grades exist.

def class_average(students):
    valid_grades = [s["grade"] for s in students if "grade" in s and isinstance(s["grade"], (int, float))]
    return sum(valid_grades) / len(valid_grades) if valid_grades else 0.0


# Exercise 3: Robust grade calculator
# Given a list of student dicts, calculate the class average.
# Handle: empty list, missing "grade" key, non-numeric grade values
# Return 0.0 if no valid grades exist.

def class_average(students):
    valid_grades = [s["grade"] for s in students if "grade" in s and isinstance(s["grade"], (int, float))]
    return sum(valid_grades) / len(valid_grades) if valid_grades else 0.0
     


if __name__ == "__main__":
    # Test safe_read_json
    print(safe_read_json("students.json"))       # should work if day4 ran
    print(safe_read_json("nonexistent.json"))    # should print error, return None
    print(safe_read_json("day5.py"))             # invalid JSON, should handle it

    # Test clean_students
    raw = [
        {"name": "Alice", "grade": 85},
        {"name": "Bob"},                          # missing grade
        {"grade": 72},                            # missing name
        "not a dict at all",                      # wrong type
        {"name": "Eve", "grade": "ninety"},       # invalid grade type
        {"name": "Diana", "grade": 30},
    ]
    print(clean_students(raw))

    # Test class_average
    print(class_average([]))
    print(class_average([{"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 55}]))