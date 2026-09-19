institutions = {
    "Ліцей_№1": ["школа", 520],
    "Політехнічний": ["технікум", 340],
    "Гімназія_№5": ["школа", 610],
    "Будівельне": ["училище", 215],
    "ЗОШ_№12": ["школа", 450],
    "Медичний": ["технікум", 400]
}

def print_dict(data):
    print("\n--- Вміст словника ---")
    if not data:
        print("Словник порожній.")
    for key, value in data.items():
        print(f"Заклад: {key} - Тип: {value[0]}, Учнів: {value[1]}")

def add_record(data):
    print("\n--- Додавання запису ---")
    while True:
        key = input("Введіть назву навчального закладу: ").strip()
        if not key:
            print("Помилка: Назва не може бути порожньою. Спробуйте ще раз.")
            continue
        if key in data:
            print("Помилка: такий заклад вже існує в базі! Введіть іншу назву.")
            continue
        break

    valid_types = ["школа", "технікум", "училище"]
    while True:
        type_inst = input("Введіть тип закладу (школа, технікум або училище): ").strip().lower()
        if type_inst in valid_types:
            break
        else:
            print("Помилка: введено неправильний тип закладу. Дозволено лише: школа, технікум або училище.")

    while True:
        try:
            students_count = int(input("Введіть кількість учнів: "))
            if students_count <= 0:
                print("Помилка: кількість учнів має бути більше нуля.")
                continue
            break
        except ValueError:
            print("Помилка вводу: кількість учнів має бути цілим додатним числом!")

    data[key] = [type_inst, students_count]
    print(f"\nЗапис '{key}' успішно додано!")

def delete_record(data):
    print("\n--- Видалення запису ---")
    while True:
        key = input("Введіть назву закладу для видалення (або '0' для відміни): ").strip()
        if key == '0':
            print("Видалення скасовано.")
            break
        try:
            del data[key]
            print(f"Запис '{key}' успішно видалено!")
            break
        except KeyError:
            print("Помилка: закладу з такою назвою не знайдено в словнику! Спробуйте ще раз.")

def print_sorted(data):
    print("\n--- Відсортований словник (за назвами закладів) ---")
    if not data:
        print("Словник порожній.")
        return
    for key in sorted(data.keys()):
        print(f"Заклад: {key} - Тип: {data[key][0]}, Учнів: {data[key][1]}")

def solve_task(data):
    print("\n--- Загальна кількість учнів шкіл ---")
    total_school_students = 0
    for key, value in data.items():
        if value[0].lower() == "школа":
            total_school_students += value[1]
    print(f"Всього учнів у школах: {total_school_students}")

def edit_record(data):
    print("\n--- Редагування запису ---")
    key = input("Введіть назву закладу для редагування (або '0' для відміни): ").strip()
    if key == '0':
        print("Редагування скасовано.")
        return
    if key not in data:
        print(f"Помилка: заклад '{key}' не знайдено в словнику!")
        return
    while True:
        try:
            new_count = int(input(f"Введіть нову кількість учнів для закладу '{key}': "))
            if new_count <= 0:
                print("Помилка: кількість учнів має бути більше нуля.")
                continue
            data[key][1] = new_count
            print(f"Дані успішно оновлено! Тепер у закладі '{key}' {new_count} учнів.")
            break
        except ValueError:
            print("Помилка вводу: кількість учнів має бути цілим додатним числом!")

def find_min_max(data):
    print("\n--- Заклади з найбільшою та найменшою кількістю учнів ---")
    if not data:
        print("Словник порожній.")
        return

    min_key = min(data, key=lambda k: data[k][1])
    max_key = max(data, key=lambda k: data[k][1])

    print(f"Найменше учнів: {min_key} ({data[min_key][1]} учнів)")
    print(f"Найбільше учнів: {max_key} ({data[max_key][1]} учнів)")

def main():
    while True:
        print("\nГОЛОВНЕ МЕНЮ")
        print("1. Вивести всі значення словника")
        print("2. Додати новий запис")
        print("3. Видалити запис")
        print("4. Переглянути відсортований словник")
        print("5. Розрахувати загальну кількість учнів шкіл")
        print("6. Відредагувати дані існуючого закладу")
        print("7. Знайти заклади з найбільшою/найменшою кількістю учнів")
        print("8. Вийти з програми")

        choice = input("Оберіть дію (1-8): ").strip()

        if choice == '1':
            print_dict(institutions)
        elif choice == '2':
            add_record(institutions)
        elif choice == '3':
            delete_record(institutions)
        elif choice == '4':
            print_sorted(institutions)
        elif choice == '5':
            solve_task(institutions)
        elif choice == '6':
            edit_record(institutions)
        elif choice == '7':
            find_min_max(institutions)
        elif choice == '8':
            print("Роботу завершено!")
            break
        else:
            print("\nНекоректний вибір. Будь ласка, введіть число від 1 до 8.")

if __name__ == "__main__":
    main()


# ЗАВДАННЯ ДЛЯ КОМАНДИ:
# 1. Оля: Реалізувати функцію редагування даних (наприклад, зміна кількості учнів у існуючому закладі). Додати виклик функції як пункт меню 7.
# 2. Коля: Реалізувати функцію пошуку закладу з найбільшою та найменшою кількістю учнів (вивести їх назви). Додати виклик функції як пункт меню 8.
# 3. Вова: Реалізувати функцію фільтрації за типом (вивід на екран списку лише шкіл, або лише технікумів за запитом користувача). Додати виклик функції як пункт меню 9.
