input_string = input("Введіть рядок: ")

if len(input_string) >= 20:
    result = input_string[19:]

    print("Зріз рядка від 20-го символа і до кінця:", result)
else:
    print("Рядок має недостатню довжину для виконання операції зрізу.")
