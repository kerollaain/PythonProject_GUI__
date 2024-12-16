import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import re

def task1():
    x = np.linspace(-2, 5, 500)
    y = x * np.sin(5 * x)

    plt.plot(x, y, label=r'$Y(x) = x \cdot \sin(5x)$', color='blue')
    plt.xlabel('x')
    plt.ylabel('Y(x)')
    plt.title('Графік функції $Y(x) = x \\cdot \\sin(5x)$')
    plt.legend()
    plt.grid(True)
    plt.savefig('plot_variant1.png', dpi=300)
    plt.show()

def task2():
    text = "Приклад тексту для аналізу частоти появи літер у Python"
    processed_text = ''.join(filter(str.isalpha, text.lower()))
    letter_counts = Counter(processed_text)
    letters = list(letter_counts.keys())
    frequencies = list(letter_counts.values())

    plt.bar(letters, frequencies, color='skyblue', edgecolor='black')
    plt.xlabel('Літери')
    plt.ylabel('Частота')
    plt.title('Гістограма частоти появи літер у тексті')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.savefig('letter_frequency_histogram.png', dpi=300)
    plt.show()

def task3():
    text = """
    Що це таке? Це приклад тексту! Текст може містити різні речення...
    Ось ще кілька: як ти? Це звичайне речення. А це — окличне!
    """

    normal_sentences = len(re.findall(r'[^.!?]+\.', text))
    question_sentences = len(re.findall(r'[^.!?]+\?', text))
    exclamatory_sentences = len(re.findall(r'[^.!?]+!', text))
    ellipsis_sentences = len(re.findall(r'[^.!?]+\.\.\.', text))

    categories = ["Звичайні", "Питальні", "Окличні", "З трикрапкою"]
    frequencies = [normal_sentences, question_sentences, exclamatory_sentences, ellipsis_sentences]

    plt.bar(categories, frequencies, color=['blue', 'green', 'red', 'purple'])
    plt.xlabel("Типи речень")
    plt.ylabel("Частота")
    plt.title("Частота різних типів речень у тексті")
    plt.savefig("sentence_frequency_histogram.png", dpi=300)
    plt.show()

def main():
    print("Лабораторна робота 7:")
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()
