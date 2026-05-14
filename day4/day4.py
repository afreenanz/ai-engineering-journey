from utils import read_json, write_json, summarise_students

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 40},
    {"name": "Charlie", "grade": 72},
    {"name": "Diana", "grade": 30},
    {"name": "Eve", "grade": 91},
]

if __name__ == "__main__":
    # Save students to a JSON file
    write_json("students.json", students)

    # Read it back
    loaded = read_json("students.json")
    print("Loaded:", loaded)

    # Print summary
    summary = summarise_students(loaded)
    print("Summary:", summary)