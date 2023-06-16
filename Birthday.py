"""Вам потрібно реалізувати корисну функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.

У вас є список словників users, кожен словник у ньому обов'язково має ключі name та birthday. Така структура представляє модель списку користувачів з їх іменами та днями народження. name — це рядок з ім'ям користувача, а birthday — це datetime об'єкт, в якому записаний день народження.

Ваше завдання написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить у консоль (за допомогою print) список користувачів, яких потрібно привітати по днях.

Умови приймання
get_birthdays_per_week виводить іменинників у форматі:
Monday: Bill, Jill
Friday: Kim, Jan

Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
Для тестування зручно створити тестовий список users та заповнити його самостійно.
Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
Тиждень починається з понеділка."""

def get_birthdays_per_week (colegues_list: dict) -> str:

    pass


if __name__ == '__main__':

    from faker import Faker 
    from faker.providers import phone_number, profile

    from rich import print
    from rich.table import Table

    fake = Faker("uk-UA") # ukrainian legguage
    fake.add_provider(profile)
    fake.add_provider(phone_number)

    Faker.seed(1)


    for i in range(10):
        prof = fake.profile()
        phones = []
        for i in range(3):
            phones.append(fake.phone_number())
        print(prof['name'], prof['birthdate'], phones)

    from rich import print
    from rich.table import Table

    dct = {i: i ** 3 for i in range(10, 20)}

    table = Table(title="numbers")
    table.add_column("number", justify="right")
    table.add_column("cube", justify="left", style="magenta")

    for key, value in dct.items():
        table.add_row(str(key), str(value) * 3)

    print(table)