import random

# Генерируем список из 20 случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(20)]
print(f"Сгенерированный список: {numbers}")

# Выводим все четные числа
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Четные числа: {even_numbers}")

# Выводим все числа, которые делятся на 3
divisible_by_3 = [num for num in numbers if num % 3 == 0]
print(f"Числа, делящиеся на 3: {divisible_by_3}")

# Вычисляем среднее арифметическое
average = sum(numbers) / len(numbers)
print(f"Среднее арифметическое: {average:.2f}")