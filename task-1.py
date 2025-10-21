from datetime import datetime

# створення функції, яка розраховує кількість днів між заданою датою і поточною датою
# оголошення функції, яка приймає один параметр date - рядок та повертає ціле число - кількість днів

def get_days_from_today(date: str) -> int:
    
# обробка винятку - неправильного формату вхідних даних:
    try:
        today=datetime.now().date() #поточна дата без часу
        input_date = datetime.strptime(date, "%Y-%m-%d").date() #перетворення вхідного рядка у дату
        days_from_today = today - input_date # різниця в днях між поточною і введеною датами 
        return days_from_today.days # функція повертає різницю у днях між датами; якщо введена дата пізніша за поточну - від'ємне число
    except ValueError: # у разі помилки введення даних
        print("Incorrect format, please input date as YYYY-MM-DD ")
    
# приклад використання функції
print(get_days_from_today("2025-10-15"))


