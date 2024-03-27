def get_cats_info(path):
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    cat_id, name, age = line.strip().split(',')
                    cat_info = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_info)
                except ValueError:
                    print(f"Помилка: некоректні дані у файлі: {line.strip()}")

        return cats_info
    except FileNotFoundError:
        print(f"Помилка: файл не знайдено за шляхом {path}")
        return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []


# Приклад використання з поданим шляхом
cats_info = get_cats_info(
    r"C:\Users\User\Desktop\My_repo\module4\cats_file.txt")
print(cats_info)
