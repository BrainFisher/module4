import os


def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    name, salary = line.strip().split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Помилка: некоректні дані у файлі: {line.strip()}")

        if count == 0:
            return 0, 0  # Якщо файл порожній або містить тільки некоректні дані

        average = total / count
        return total, average
    except FileNotFoundError:
        print(f"Помилка: файл не знайдено за шляхом {path}")
        return 0, 0
    except Exception as e:
        print(f"Помилка: {e}")
        return 0, 0


# Приклад використання з поданим шляхом
total, average = total_salary(
    r"C:\Users\User\Desktop\My_repo\module4\salary_file.txt")
print(f"Загальна сума заробітної плати: {
      total}, Середня заробітна плата: {average}")
