import json

# Function 1: read a JSON file and return its contents as a Python object
def read_json(filepath):
    with open(filepath, "r") as f:
        return json.load(f)

# Function 2: write a Python object to a JSON file (pretty printed)
def write_json(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

# Function 3: given a list of student dicts, return summary stats
# Returns a dict with: total, passed, failed, average_grade
# A student passes if grade >= 50
def summarise_students(students):
    total = len(students)
    passed = sum(1 for s in students if s["grade"] >= 50)
    failed = total - passed
    average_grade = sum(s["grade"] for s in students) / total if total > 0 else 0
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "average_grade": average_grade
    }