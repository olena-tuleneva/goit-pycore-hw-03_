# створення функції для організації привітань з днем народження, яка повертає список днів народження вперед на 7 днів включно поточну дату
# функція з параметром - словник, який містить ім'я користувача та день народження
# функція повертає список словників, де кожен має (ключ name) та дату привітання (ключ congratulation_date), дані якого у форматі рядка 'рік.місяць.дата'

from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()  # визначення поточної дати
    upcoming_birthdays = [] 

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()  # конвертація рядка у дату
        birthday_this_year = birthday.replace(year=today.year)  # дата народження у поточному році

        # якщо день народження вже минув цього року — переносимо на наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # обчислення різниці у днях
        days_diff = (birthday_this_year - today).days

        # якщо день народження протягом наступних 7 днів (включно з поточним)
        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year

            # якщо припадає на суботу чи неділю — переносимо на понеділок
            if congratulation_date.weekday() == 5:  # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:  # неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

#приклад використання:
users = [
    {"name": "John Doe", "birthday": "1985.10.23"},
    {"name": "Jane Smith", "birthday": "1990.10.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
