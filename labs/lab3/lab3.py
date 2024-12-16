import os
import csv

def create_file(group_name, students):
    with open(f"{group_name}.txt", "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print(f"Файл '{group_name}.txt' створено.")

def read_file(file_name):
    if not os.path.exists(file_name):
        print(f"Файл '{file_name}' не існує.")
        return []
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = [(row[0], float(row[1])) for row in reader]
    return data

def append_to_file(file_name, students):
    if not os.path.exists(file_name):
        print(f"Файл '{file_name}' не існує. Створюємо новий.")
        create_file(file_name.replace(".txt", ""), students)
        return
    with open(file_name, "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(students)
    print(f"Дані додано у файл '{file_name}'.")

def find_files_in_directory(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    print(f"Файли у каталозі '{directory}': {files}")
    return files

def search_in_file(file_name, student_name):
    students = read_file(file_name)
    for student, grade in students:
        if student == student_name:
            return student, grade
    return None

def sort_file(file_name):
    students = read_file(file_name)
    if not students:
        print(f"Файл '{file_name}' порожній або не існує.")
        return
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    with open(file_name, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(sorted_students)
    print(f"Дані у файлі '{file_name}' відсортовано.")

def main():
    students_group1 = [("Олена", 85.5), ("Андрій", 72.0), ("Марія", 95.3)]
    students_group2 = [("Василь", 65.4), ("Юлія", 88.8), ("Ігор", 74.5)]
    create_file("group1", students_group1)
    create_file("group2", students_group2)
    append_to_file("group1.txt", [("Олександр", 78.0)])
    print("Дані з файлу 'group1.txt':", read_file("group1.txt"))
    student = search_in_file("group1.txt", "Марія")
    print(f"Результат пошуку: {student}" if student else "Студента не знайдено.")
    sort_file("group1.txt")
    print("Дані після сортування:", read_file("group1.txt"))
    find_files_in_directory(".")

if __name__ == "__main__":
    main()
