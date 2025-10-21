
import re

# функція нормалізує телефонні номери до стандартного формату
# функція приймає рядок з телефонним номером, повертає нормалізований телефонний номер у вигляді рядка
# додає код '+38' за потреби

def normalize_phone(num: str) -> str:
    cleaned = re.sub(r'[^\d+]', '', num.strip()) # видаляє всі символи, крім цифр та '+'

    # якщо номер починається з '0'
    if cleaned.startswith('0'):
        cleaned = '+38' + cleaned
    # якщо номер починається з '380'
    elif cleaned.startswith('380'):
        cleaned = '+' + cleaned 
    # якщо номер починається з '+', без змін
    elif cleaned.startswith('+'):
        pass
    # в інших випадках додає '+38' перед номером
    else:
        cleaned = '+38' + cleaned

    return cleaned
    
# приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

standart_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", standart_numbers)
