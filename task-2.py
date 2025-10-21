import random

# створення функції, яка генерує відсортований список унікальних випадкових чисел для лотереї 
# параметри функції: мін число - до 1, макс число - не більше 1000, вибрати кількість чисел - значення між мін і макс

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    
    # перевірка коректності вхідних даних
    if not (1 <= min <= max <= 1000):
        return [] # некоректні дані - повернення пустого списку
    if not (0 < quantity <= (max - min + 1)):
        return []
    else:
        ticket_numbers = random.sample(range(min, max + 1), quantity) # генерація унікальних випадкових чисел
    return sorted(ticket_numbers) # повернення відсортованого списку 

print(get_numbers_ticket(1, 49, 6)) # лотерея 6 із 49