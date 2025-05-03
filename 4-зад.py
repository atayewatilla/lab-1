import random

# Создаем список из 10 случайных чисел от 1 до 100
numbers = [random.randint(1, 100) for _ in range(10)]
print(f"Исходный список: {numbers}")

# Находим максимальное и минимальное значение
max_num = max(numbers)
min_num = min(numbers)
print(f"Максимальное значение: {max_num}")
print(f"Минимальное значение: {min_num}")

# Вычисляем сумму всех элементов
sum_numbers = sum(numbers)
print(f"Сумма всех элементов: {sum_numbers}")

# Сортируем список по возрастанию
sorted_numbers = sorted(numbers)
print(f"Отсортированный список: {sorted_numbers}")