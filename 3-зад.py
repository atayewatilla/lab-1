# Запрашиваем число у пользователя
n = int(input("Введите число n: "))

# Выводим числа от n до 1 в обратном порядке
print(f"Числа от {n} до 1:")
current = n
while current >= 1:
    print(current, end=' ')
    current -= 1
print()

# Вычисляем факториал числа n
factorial = 1
counter = 1
while counter <= n:
    factorial *= counter
    counter += 1
print(f"Факториал {n}! = {factorial}")