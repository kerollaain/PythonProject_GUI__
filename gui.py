import os
import PySimpleGUI as sg
import subprocess

def get_lab_list(labs_folder="labs"):
    """Зчитує список лабораторних робіт у вказаній папці."""
    labs = []
    if os.path.exists(labs_folder):
        for folder in os.listdir(labs_folder):
            lab_path = os.path.join(labs_folder, folder)
            if os.path.isdir(lab_path):
                lab_script = os.path.join(lab_path, f"{folder}.py")
                readme_file = os.path.join(lab_path, "README.md")
                if os.path.exists(lab_script):
                    labs.append({
                        "name": folder,
                        "script": lab_script,
                        "readme": readme_file if os.path.exists(readme_file) else None
                    })
    return labs

def read_readme(file_path):
    """Зчитує вміст README.md, якщо файл існує."""
    if file_path and os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Опис відсутній."

def main():
    sg.theme("LightBlue")

    labs = get_lab_list()

    layout = [
        [sg.Text("Список лабораторних робіт:", font=("Arial", 14))],
        [sg.Listbox(values=[lab['name'] for lab in labs], size=(30, 10), key="-LAB_LIST-", enable_events=True)],
        [sg.Text("Опис лабораторної роботи:", font=("Arial", 12))],
        [sg.Multiline(size=(50, 15), key="-DESCRIPTION-", disabled=True)],
        [
            sg.Button("Запустити", key="-RUN-"),
            sg.Button("Вийти", key="-EXIT-")
        ]
    ]

    window = sg.Window("Лабораторні роботи", layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "-EXIT-":
            break

        if event == "-LAB_LIST-":
            selected_lab = values["-LAB_LIST-"]
            if selected_lab:
                lab_name = selected_lab[0]
                lab_info = next((lab for lab in labs if lab["name"] == lab_name), None)
                if lab_info:
                    description = read_readme(lab_info["readme"])
                    window["-DESCRIPTION-"].update(description)

        if event == "-RUN-":
            selected_lab = values["-LAB_LIST-"]
            if selected_lab:
                lab_name = selected_lab[0]
                lab_info = next((lab for lab in labs if lab["name"] == lab_name), None)
                if lab_info:
                    try:
                        subprocess.run(["python", lab_info["script"]], check=True)
                    except Exception as e:
                        sg.popup_error(f"Помилка при запуску: {e}")

    window.close()

if __name__ == "__main__":
    main()
