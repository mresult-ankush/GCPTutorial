from typing import List

def read_employees(file_path: str) -> List[str]:
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: File not found.")
        return []

def calculate_bonus(salary: float, rate: float = 0.10) -> float:
    return salary * rate

def process_employees(file_path: str) -> None:
    lines = read_employees(file_path)
    for line in lines:
        try:
            name, salary_str = line.split(",")
            salary = float(salary_str)
            bonus = calculate_bonus(salary)
            print(f"Name: {name}, Salary: {salary}, Bonus: {bonus}")
        except ValueError:
            print(f"Skipping invalid line: {line}")

process_employees("employees.txt")
