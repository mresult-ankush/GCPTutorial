from typing import List

def parse_student_data(data: str) -> tuple[str, List[int]]:
    try:
        parts = data.split(",")
        name = parts[0]
        grades = list(map(int, parts[1:]))
        return name, grades
    except Exception as e:
        raise ValueError(f"Invalid student record: {data}") from e

def average(grades: List[int]) -> float:
    return sum(grades) / len(grades)

def process_students(students: List[str]) -> None:
    for record in students:
        try:
            name, grades = parse_student_data(record)
            avg = average(grades)
            print(f"{name} has an average grade of {avg:.2f}")
        except ValueError as e:
            print(e)

student_records = [
    "Alice,90,80,70",
    "Bob,85,95,100",
    "InvalidStudentData"
]

process_students(student_records)
