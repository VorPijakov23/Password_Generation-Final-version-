# Импортируем необходимые модули
import random
import string
from colorama import Fore  # Модуль для окрашивания вывода в консоль
#  Например, вывода ошибок красного цвета или паролей зелёного цвета


def generate_letters_password(length, quantity):
    """Функция для генерации паролей вида "Только буквы разного регистра\""""
    answer = []
    for i in range(quantity):
        letters = string.ascii_letters  # Вписываем необходимые символы для генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_alphanumeric_password(length, quantity):
    """Функция для генерации паролей вида "Буквы разного регистра и цифры\""""
    answer = []
    for i in range(quantity):
        letters = string.ascii_letters + string.digits  # Вписываем необходимые символы для генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_complex_password(length, quantity):
    """Функция для генерации паролей вида "Буквы, цифры и спецсимволы\""""
    answer = []
    for i in range(quantity):
        letters = string.ascii_letters + string.digits + string.punctuation  # Вписываем необходимые символы для
        # генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_uppercase_and_digits_password(length, quantity):
    """Функция для генераций паролей вида 'Буквы в верхнем регистре и цифры'"""
    answer = []
    for i in range(quantity):
        letters = string.ascii_uppercase + string.digits  # Вписываем необходимые символы для
        # генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_lowercase_and_digits_password(length, quantity):
    """Функция для генераций паролей вида 'Буквы в нижнем регистре и цифры'"""
    answer = []
    for i in range(quantity):
        letters = string.ascii_lowercase + string.digits  # Вписываем необходимые символы для
        # генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_mixed_case_and_special_chars_password(length, quantity):
    """Функция для генераций паролей вида 'Буквы разного регистра и спецсимволы'"""
    answer = []
    for i in range(quantity):
        letters = string.ascii_uppercase + string.punctuation  # Вписываем необходимые символы для
        # генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_digits_and_special_chars_password(length, quantity):
    """Функция для генераций паролей вида 'Цифры и спец символы'"""
    answer = []
    for i in range(quantity):
        letters = string.digits + string.punctuation  # Вписываем необходимые символы для
        # генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def generate_only_digits_password(length, quantity):
    """Функция для генераций паролей вида 'Только цифры'"""
    answer = []
    for i in range(quantity):
        letters = string.digits  # Вписываем необходимые символы для
        # генерации пароля
        result = ''.join(random.choice(letters) for _ in range(length))  # Генерируем символ
        answer.append(result)  # Добавляем в список сгенерированный символ
    return answer


def router_password_generate(length, pass_type, quantity):
    """Функция определяющая какой тип пароля выбрал пользователь"""
    if pass_type == "1":  # Тип "Только буквы разного регистра"
        return generate_letters_password(length, quantity)
    elif pass_type == "2":  # Тип "Буквы разного регистра и цифры"
        return generate_alphanumeric_password(length, quantity)
    elif pass_type == "3":  # Тип "Буквы, цифры и спецсимволы"
        return generate_complex_password(length, quantity)
    elif pass_type == "4":  # Тип "Буквы в верхнем регистре и цифры"
        return generate_uppercase_and_digits_password(length, quantity)
    elif pass_type == "5":  # Тип "Буквы в нижнем регистре и цифры"
        return generate_uppercase_and_digits_password(length, quantity)
    elif pass_type == "6":  # Тип "Буквы разного регистра и спецсимволы"
        return generate_uppercase_and_digits_password(length, quantity)
    elif pass_type == "7":  # Тип "Цифры и спец символы"
        return generate_uppercase_and_digits_password(length, quantity)
    elif pass_type == "8":  # Тип "Только цифры"
        return generate_uppercase_and_digits_password(length, quantity)

    else:  # Вывод ошибки
        return Fore.RED + 'Произошла ошибка!'


def main():
    """Главная функция выполняющая роль соединителя кода в одно целое"""
    print(Fore.LIGHTYELLOW_EX + "Добро пожаловать в Генератор Сложных Паролей!")
    print("У нас есть несколько типов паролей, которые мы можем создать:" + Fore.RESET)
    possible_commands = {  # Словарь необходимый для вывода возможных команд
        "1": Fore.LIGHTCYAN_EX + "Только буквы разного регистра" + Fore.RESET,
        "2": Fore.LIGHTCYAN_EX + "Буквы разного регистра и цифры" + Fore.RESET,
        "3": Fore.LIGHTCYAN_EX + "Буквы, цифры и спецсимволы" + Fore.RESET,
        "4": Fore.LIGHTCYAN_EX + "Буквы в верхнем регистре и цифры" + Fore.RESET,
        "5": Fore.LIGHTCYAN_EX + "Буквы в нижнем регистре и цифры" + Fore.RESET,
        "6": Fore.LIGHTCYAN_EX + "Буквы разного регистра и спецсимволы" + Fore.RESET,
        "7": Fore.LIGHTCYAN_EX + "Цифры и спец символы" + Fore.RESET,
        "8": Fore.LIGHTCYAN_EX + "Только цифры" + Fore.RESET
    }
    for key, value in possible_commands.items():
        print(f'{key}: {value}')  # Вывод словаря с командами
    print(Fore.RESET)  # Сбрасываем настройки цвета текста
    user_choice = input('Введите тип пароля (1-8): ')  # Ввод типа пароля
    if user_choice in possible_commands:  # Проверка на корректность ввода
        long = int(input("Введите длину пароля (от 4 до 30 символов): "))  # Ввод длины пароля
        if 4 <= long <= 30:
            quantity = int(input("Введите количество генераций паролей (не больше 40): "))  # Ввод количества
            # генераций пароля
            if 1 <= quantity <= 40:  # Проверка на корректность ввода
                password = router_password_generate(long, user_choice, quantity)
                print(Fore.LIGHTWHITE_EX + "Сгенерированные пароли:" + Fore.RESET)
                for i in password:
                    print(Fore.GREEN + i)  # Вывод сгенерированный паролей
            else:
                print(Fore.RED + "Количество генераций задано неправильно!")  # Вывод ошибки
        else:
            print(Fore.RED + "Длина не подходит под нужные параметры!")  # Вывод ошибки
    else:
        print(Fore.RED + 'Такой команды нет в списке!')  # Вывод ошибки


if __name__ == '__main__':  # Этот блок кода выполняет функцию точки входа в программу
    """Конструкция "if name == 'main':" используется, чтобы определить, выполняется ли файл напрямую как основной 
    скрипт, или же он импортируется как модуль, и в зависимости от этого выполнить соответствующий код или действия."""
    try:  # Если код работает без ошибок, то код переходит в блок "try"
        main()  # Запускаем главную функцию "main"
    except KeyboardInterrupt:
        """Блок "except" запускается когда пользователь досрочно закрывает программу. Тип ошибки KeyboardInterrupt"""
        print(Fore.RED + 'Преждевременный выход из программы')  # Вывод сообщения заменяющего ошибку досрочного
        # закрытия программы
