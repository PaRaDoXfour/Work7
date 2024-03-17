def display_dictionary(dictionary):
    """Функція виводить вміст словника на екран."""
    for key, value in dictionary.items():
        print(key, ':', value)

def add_entry(dictionary, key, value):
    """Функція додає нову пару ключ-значення до словника."""
    dictionary[key] = value

def remove_entry(dictionary, key):
    """Функція видаляє елемент зі словника за вказаним ключем."""
    if key in dictionary:
        del dictionary[key]
    else:
        print("Учня з прізвищем", key, "не знайдено.")

def sort_dictionary_by_values(dictionary):
    """Функція сортує словник за значеннями (зростанням) і повертає відсортований словник."""
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict

def sort_dictionary_by_values_revers(dictionary):
    """Функція сортує словник за значеннями (зменшенням) і повертає відсортований словник."""
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))  # Змінено параметр reverse на True
    return sorted_dict

def sort_dictionary_by_keys(dictionary):
    """Функція сортує словник за ключами і повертає відсортований словник."""
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

def find_students_shorter_than_new_student(student_heights, new_student_height):
    """Функція знаходить учнів, чиї зрости менше заданого значення."""
    shorter_students = [name for name, height in student_heights.items() if height < new_student_height]
    return shorter_students

def find_insert_position(student_heights, new_student_height):
    """Функція знаходить позицію для вставки нового учня відповідно до його зросту."""
    sorted_keys = sorted(student_heights.keys(), key=lambda x: student_heights[x])
    for i, key in enumerate(sorted_keys):
        if student_heights[key] > new_student_height:
            return i, key
    return len(sorted_keys), None

def find_insert_position_by_name(student_heights, new_student_name):
    """Функція знаходить позицію для вставки нового учня відповідно до алфавітного порядку прізвищ."""
    sorted_keys = sorted(student_heights.keys())
    for i, key in enumerate(sorted_keys):
        if key > new_student_name:
            return i, key
    return len(sorted_keys), None

def find_closest_height(student_heights, new_student_height):
    """Функція знаходить учня, чий зріст найближчий до заданого значення."""
    closest_student = min(student_heights, key=lambda x: abs(student_heights[x] - new_student_height))
    return closest_student

def input_student_heights(n):
    """Функція заповнює словник інформацією про учнів (прізвище та зріст), запитуючи дані у користувача."""
    student_heights = {}
    for i in range(n):
        name = input("Введіть прізвище учня: ")
        height = int(input("Введіть зріст учня: "))
        student_heights[name] = height
    return student_heights

def input_new_student_height():
    """Функція запитує користувача ввести зріст нового учня."""
    return int(input("Введіть зріст нового учня: "))

def menu():
    """Функція виводить на екран головне меню та зчитує вибір користувача."""
    print("\nМеню:")
    print("1. Додати учня")
    print("2. Видалити учня")
    print("3. Переглянути список учнів")
    print("4. Переглянути список учнів за відсортованими ключами")
    print("5. Переглянути список учнів за відсортованим зростом(спаданням)")
    print("6. Переглянути список учнів за відсортованим зростом(зростанням)")
    print("7. Знайти учнів, зріст яких менше росту новенького")
    print("8. Знайти позицію для вставки новенького учня")
    print("9. Знайти учня, зріст якого найменше відрізняється від росту новенького")
    print("0. Вийти з програми")
    choice = input("Виберіть опцію: ")
    return choice

def main():
    """Головна функція програми."""
    student_heights = {}
    while True:
        choice = menu()
        if choice == '1':
            name = input("Введіть прізвище учня: ")
            height = int(input("Введіть зріст учня: "))
            add_entry(student_heights, name, height)
            print("Учень", name, "доданий.")
        elif choice == '2':
            name = input("Введіть прізвище учня для видалення: ")
            remove_entry(student_heights, name)
        elif choice == '3':
            print("\nСписок учнів:")
            display_dictionary(student_heights)
        elif choice == '4':
            print("\nСписок учнів за відсортованими ключами:")
            sorted_student_heights = sort_dictionary_by_keys(student_heights)
            display_dictionary(sorted_student_heights)
        elif choice == '5':
            print("\nСписок учнів за відсортованим зростом(спаданням):")
            sorted_student_heights = sort_dictionary_by_values_revers(student_heights)
            display_dictionary(sorted_student_heights)
        elif choice == '6':
            print("\nСписок учнів за відсортованим зростом(зростанням):")
            sorted_student_heights = sort_dictionary_by_values(student_heights)
            display_dictionary(sorted_student_heights)
        elif choice == '7':
            new_student_height = input_new_student_height()
            shorter_students = find_students_shorter_than_new_student(student_heights, new_student_height)
            print("Прізвища учнів, зріст яких менше росту новенького:", shorter_students)
        elif choice == '8':
            new_student_name = input("Введіть прізвище нового учня: ")
            new_student_height = input_new_student_height()
            insert_position, insert_key = find_insert_position(student_heights, new_student_height)
            print("Прізвище учня, після якого слід записати новенького:", insert_key)
        elif choice == '9':
            new_student_height = input_new_student_height()
            closest_height_student = find_closest_height(student_heights, new_student_height)
            print("Прізвище учня, зріст якого найменше відрізняється від росту новенького:", closest_height_student)
        elif choice == '0':
            print("Програма завершена.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
