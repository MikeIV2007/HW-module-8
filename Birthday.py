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

from datetime import datetime
from rich import print
from rich.table import Table
import calendar


# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020.weekday())   # 1

def find_next_monday()->datetime:
    some_day = datetime.now()
    week_day = calendar.weekday(some_day.year, some_day.month, some_day.day)
    if week_day == 0:
        next_monday = some_day + 7
        return next_monday
    else:
        for i in range (7):
            some_day = datetime(some_day.year, some_day.month, some_day.day +1)
            week_day = calendar.weekday(some_day.year, some_day.month, some_day.day)
            if week_day == 0:
                next_monday = some_day
                return next_monday
            else:
                continue


def get_birthdays_per_week (colleagues_dict: dict) -> str:
    calendar.setfirstweekday(calendar.MONDAY) #monday 0 - sundey 6
    firthtweekday = calendar.firstweekday()
    #weekday = calendar.weekday(year, month, day)
    print (colleagues_dict)
    nw_birhtday_dict = {}
    next_monday = find_next_monday()
    print (next_monday)

    for name, birthday in colleagues_dict.items():
 
        year = birthday.year
        day = birthday.day
        month = birthday.month
        weekday = calendar.weekday(year, month, day)
        print (name, birthday, year, day, month, weekday)

    #weekday = calendar.weekday(year=current_date.year, month=current_date.month, day=current_date.day )
    #next_week_start= 
 
   


# table:
    # dct = {i: i ** 3 for i in range(10, 20)}

    # table = Table(title="numbers")
    # table.add_column("number", justify="right")
    # table.add_column("cube", justify="left", style="magenta")

    # for key, value in dct.items():
    #     table.add_row(str(key), str(value) * 3)


    # return print(table)


if __name__ == '__main__':

    from faker import Faker 
    from faker.providers import profile

    fake = Faker("uk-UA") # ukrainian legguage
    fake.add_provider(profile)
    
    Faker.seed(1)
    
    def create_test_colleagues_dict():
        colleagues_dict = {}

        for i in range(10):
            prof = fake.profile()
            #print(type(prof['name']))
            #print(type(prof['birthdate']))
        
            #print (type(birthday))
            birthday = prof['birthdate']
            colleagues_dict[prof['name']] = birthday
            #print(prof['name'], prof['birthdate'])
        print (birthday)  
        return colleagues_dict
    
    colleagues_dict = create_test_colleagues_dict()

    # colleagues_dict ={
    #     'Христина Зінчук': date(2020, 6, 4),
    #     'Нестор Авраменко': date(1954, 7, 23),
    #     'Валентин Копитко': date(1989, 11, 19),
    #     'Мирон Філіпенко': date(1936, 6, 13),
    #     'Мартин Засенко': date(1923, 2, 14),
    #     'пані Вікторія Каденюк': date(1985, 8, 17),
    #     'Веніямин Ґалаґан': date(1981, 2, 20),
    #     'Святослав Єфименко': date(1965, 7, 16),
    #     'Ірина Дерегус': date(1946, 2, 12),
    #     'Лариса Лупій': date(2020, 10, 28)
    # }
        

    get_birthdays_per_week (colleagues_dict)





   # dct = {i: i ** 3 for i in range(10, 20)}

    # table = Table(title="numbers")
    # table.add_column("number", justify="right")
    # table.add_column("cube", justify="left", style="magenta")

    # for key, value in dct.items():
    #     table.add_row(str(key), str(value) * 3)

    # print(table)