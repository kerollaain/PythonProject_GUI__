import os
import sys

LABS_DIR = "labs"
LAB_FILE = "lab{num}/lab{num}.py"
README_FILE = "lab{num}/README.md"

def list_labs():
    if not os.path.exists(LABS_DIR):
        print("\nПапка з лабораторними не знайдена.")
        return

    labs = sorted([d for d in os.listdir(LABS_DIR) if d.startswith("lab") and os.path.isdir(os.path.join(LABS_DIR, d))])
    if not labs:
        print("\nЛабораторні роботи не знайдено.")
        return

    print("\nДоступні лабораторні роботи:")
    for lab in labs:
        lab_number = lab.replace("lab", "")
        readme_path = os.path.join(LABS_DIR, lab, "README.md")
        description = "Опис недоступний"
        if os.path.isfile(readme_path):
            with open(readme_path, "r", encoding="utf-8") as f:
                description = f.readline().strip()
        print(f"{lab_number}. {lab} - {description}")

def run_lab(lab_number):
    lab_path = os.path.join(LABS_DIR, LAB_FILE.format(num=lab_number))
    if not os.path.isfile(lab_path):
        print(f"\nЛабораторну роботу {lab_number} не знайдено.")
        return

    print(f"\nЗапуск лабораторної роботи {lab_number}...")
    try:
        exec(open(lab_path).read(), {})
        print("\nЛабораторну виконано успішно!")
    except Exception as e:
        print(f"\nПомилка при виконанні лабораторної роботи {lab_number}: {e}")

def print_usage():
    print("\nВикористання:")
    print("  python cli.py list                 # Список лабораторних робіт")
    print("  python cli.py run <номер_роботи>   # Запуск лабораторної роботи")

def main():
    if len(sys.argv) < 2:
        print("\nПомилка: команда не вказана.")
        print_usage()
        return

    command = sys.argv[1]

    if command == "list":
        list_labs()
    elif command == "run":
        if len(sys.argv) < 3:
            print("\nПомилка: номер лабораторної роботи не вказано.")
            print_usage()
        else:
            run_lab(sys.argv[2])
    else:
        print(f"\nПомилка: невідома команда '{command}'.")
        print_usage()

if __name__ == "__main__":
    main()

