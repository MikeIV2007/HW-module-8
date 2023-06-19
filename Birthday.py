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

import datetime
import calendar
from rich import print
from rich.table import Table
import calendar


# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# print(seventh_day_2020.weekday())   # 1

def find_next_monday()->datetime:
    #some_day = datetime.now()
    some_day = datetime.date(year=2023, month=12, day=25)
    week_day = calendar.weekday(some_day.year, some_day.month, some_day.day)
    if week_day == 0:
        #next_monday = datetime(some_day.year, some_day.month, some_day.day +7)
        next_monday = some_day + datetime.timedelta(days=7)

        return next_monday
    else:
        for i in range (7):
            #some_day = datetime(some_day.year, some_day.month, some_day.day +1)
            some_day = some_day + datetime.timedelta(days=1)
            week_day = calendar.weekday(some_day.year, some_day.month, some_day.day)
            if week_day == 0:
                next_monday = some_day
                return next_monday
            else:
                continue
def one_week_range(next_monday: datetime) -> datetime:
    #start_of_range = datetime(next_monday.year, next_monday.month, next_monday.day-2)
    start_of_range = next_monday - datetime.timedelta(days=2) 
    #end_of_range = datetime(next_monday.year, next_monday.month, next_monday.day+4)
    end_of_range = next_monday + datetime.timedelta(days=4)
    return start_of_range, end_of_range

def birthday_dict_in_range(range: datetime, colleagues_dict: dict) -> dict:
    birthday_dict = {}
    #print (colleagues_dict)

    for name, birthday in colleagues_dict.items():
        #print(name, birthday)
        #print (range[0], range[1])
        if range[0].month == 12 and range[1].month == 1:
            if birthday.month == 12:
                birthday_year_12 = range[0].year
                birthday_12 = datetime.date(birthday_year_12, birthday.month, birthday.day)
                #print (birthday_12)
                if range[0] <=  birthday_12 <= range[1]:
                    print (range[0], range[1])
                    print(name, birthday_12)
                    print (True)
                    birthday_dict[name] = birthday
            if birthday.month == 1:
                birthday_year_1 = range[1].year
                birthday_1 = datetime.date(birthday_year_1, birthday.month, birthday.day)
                #print (birthday_12)
                if range[0] <=  birthday_1 <= range[1]:
                    print (range[0], range[1])
                    print(name, birthday_12)
                    print (True)
                    birthday_dict[name] = birthday
            #return birthday_dict
        else:

            if range[0].month <=  birthday.month <= range[1].month:
                print (birthday.month)
                if range[0].day <=  birthday.day <= range[1].day:
                    weekday = calendar.weekday(birthday.year, birthday.month, birthday.day)
                    #print (weekday ,name, birthday)
                    birthday_dict[name] = birthday
    return birthday_dict

def print_table(birthday_dict: dict)-> print:

    current_year = (datetime.now()).year
    #birthday_dict = dict(sorted(birthday_dict.items(), key=lambda item: item[1]))

    table = Table(title="\nNEXT WEEK BERTHDAYS")
    table.add_column("Day of week", justify="left")
    table.add_column("Colleague Name", justify="left")
    table.add_column("Birthday", justify="center", style="magenta")

    i = 1
    for key, value in birthday_dict.items():

        day_of_week = calendar.weekday(current_year, value.month, value.day)
         
        if day_of_week == 0 or day_of_week == 5 or day_of_week == 6:
            if i == 1:
                day_of_week = 'Monday'
                table.add_row(day_of_week, str(key), str(value))
                i +=1
            else:
                day_of_week = ''
                table.add_row(day_of_week, str(key), str(value))

    i = 1
    for key, value in birthday_dict.items():

        day_of_week = calendar.weekday(current_year, value.month, value.day)

        if day_of_week == 1:
            if i == 1:
                day_of_week = 'Tuesday'
                table.add_row(day_of_week, str(key), str(value))
                i +=1
            else:
                day_of_week = ''
                table.add_row(day_of_week, str(key), str(value))

    i = 1
    for key, value in birthday_dict.items():

        day_of_week = calendar.weekday(current_year, value.month, value.day)

        if day_of_week == 2:
            if i == 1:
                day_of_week = 'Wednesday'
                table.add_row(day_of_week, str(key), str(value))
                i += 1
            else:
                day_of_week = ''
                table.add_row(day_of_week, str(key), str(value))

    i = 1
    for key, value in birthday_dict.items():

        day_of_week = calendar.weekday(current_year, value.month, value.day)                

        if day_of_week == 3:
            if i == 1:
                day_of_week = 'Thursday'            
                table.add_row(day_of_week, str(key), str(value))
                i += 1
            else:
                day_of_week = ''
                table.add_row(day_of_week, str(key), str(value))

    i = 1
    for key, value in birthday_dict.items():

        day_of_week = calendar.weekday(current_year, value.month, value.day)   

        if day_of_week == 4:
            if i == 1:
                day_of_week = 'Friday'
                table.add_row(day_of_week, str(key), str(value))
                i += 1
            else:
                day_of_week = ''
                table.add_row(day_of_week, str(key), str(value))                

    return print(table)


def get_birthdays_per_week (colleagues_dict: dict) -> None:
    calendar.setfirstweekday(calendar.MONDAY) #monday 0 - sundey 6
    #firthtweekday = calendar.firstweekday()
    #weekday = calendar.weekday(year, month, day)
    #print (colleagues_dict)
    
    next_monday = find_next_monday()
    print (next_monday)
    range = one_week_range( next_monday)
    print (range)
    birthday_dict = birthday_dict_in_range(range, colleagues_dict)
    print (birthday_dict)
    print_table (birthday_dict)

    # for name, birthday in colleagues_dict.items():
 
      
    #     if range[0].month <=  birthday.month <= range[1].month:
    #         #print (birthday.month)
    #         if range[0].day <=  birthday.day <= range[1].day:
    #             weekday = calendar.weekday(birthday.year, birthday.month, birthday.day)
    #             print (weekday ,name, birthday)
        #print (name, birthday, year, day, month, weekday)

    #weekday = calendar.weekday(year=current_date.year, month=current_date.month, day=current_date.day )
    #next_week_start= 
 
   


# table:
#     dct = {i: i ** 3 for i in range(10, 20)}

#     table = Table(title="numbers")
#     table.add_column("number", justify="right")
#     table.add_column("cube", justify="left", style="magenta")

#     for key, value in dct.items():
#         table.add_row(str(key), str(value) * 3)


#     return print(table)


if __name__ == '__main__':

    from faker import Faker 
    from faker.providers import profile

    fake = Faker("uk-UA") # ukrainian legguage
    fake.add_provider(profile)
    
    #Faker.seed(1) #1 for constant dict
    
    def create_test_colleagues_dict():
        colleagues_dict = {}

        for i in range(200):
            prof = fake.profile()
            #print(type(prof['name']))
            #print(type(prof['birthdate']))
        
            #print (type(birthday))
            birthday = prof['birthdate']
            colleagues_dict[prof['name']] = birthday
            #print(prof['name'], prof['birthdate'])
        #print (birthday)  
        return colleagues_dict
    
    colleagues_dict = create_test_colleagues_dict()


        

    get_birthdays_per_week (colleagues_dict)





   # dct = {i: i ** 3 for i in range(10, 20)}

    # table = Table(title="numbers")
    # table.add_column("number", justify="right")
    # table.add_column("cube", justify="left", style="magenta")

    # for key, value in dct.items():
    #     table.add_row(str(key), str(value) * 3)

    # print(table)