import random
from collections import Counter

def generate_random_phrase():
    list1 = ["Великий", "Маленький", "Швидкий", "Повільний"]
    list2 = ["собака", "кіт", "птах", "жираф"]
    list3 = ["бігає", "спить", "летить", "стрибає"]
    word1 = random.choice(list1)
    word2 = random.choice(list2)
    word3 = random.choice(list3)
    return f"{word1} {word2} {word3}"

def analyze_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    total_chars_with_spaces = len(text)
    total_chars_without_spaces = len(text.replace(" ", "").replace("\n", ""))
    words = text.split()
    total_words = len(words)
    unique_words = set(words)
    total_unique_words = len(unique_words)
    word_counts = Counter(words)
    words_with_one_occurrence = sum(1 for count in word_counts.values() if count == 1)

    return {
        "total_chars_with_spaces": total_chars_with_spaces,
        "total_chars_without_spaces": total_chars_without_spaces,
        "total_words": total_words,
        "total_unique_words": total_unique_words,
        "words_with_one_occurrence": words_with_one_occurrence
    }

def find_longest_repeated_sequence(words, seq_length=3):
    sequences = [' '.join(words[i:i+seq_length]) for i in range(len(words) - seq_length + 1)]
    sequence_counts = Counter(sequences)
    repeated_sequences = {seq: count for seq, count in sequence_counts.items() if count > 1}
    if repeated_sequences:
        longest_sequence = max(repeated_sequences, key=len)
        return longest_sequence, repeated_sequences[longest_sequence]
    return None
