def find_min_five_elements(arr):
    if len(arr) < 5:
        return sorted(arr)
    else:
        return sorted(arr)[:5]

def calculate_average(arr):
    if not arr:
        return None
    return sum(arr) / len(arr)

if __name__ == "__main__":
    numbers = [33, 10, 55, 7, 14, 90, 1, 22, 6, 3]
    min_five = find_min_five_elements(numbers)
    print("Перші п'ять мінімальних елементів:", min_five)
    average = calculate_average(numbers)
    print("Середнє арифметичне:", average)
