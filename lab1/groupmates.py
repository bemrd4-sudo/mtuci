# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# список студентов
groupmates = [
    {
        "name": u"Алексей",
        "group": "2256",
        "age": 19,
        "marks": [4, 4, 5, 5, 4]
    },
    {
        "name": u"Оксана",
        "group": "2256",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Настя",
        "group": "2257",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Кирилл",
        "group": "2255",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Дима",
        "group": "2258",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    },
    {
        "name": u"Александр",
        "group": "2255",
        "age": 18,
        "marks": [3, 4, 5, 4, 5]
    }
]

# функция для вывода всех студентов
def print_students(students):
    # заголовок таблицы
    print u"Имя студента".ljust(15) + u"Группа".ljust(8) + u"Возраст".ljust(8) + u"Оценки".ljust(20)
    print "-" * 60
    
    for s in students:  # s вместо student, короче
        # выводим строку с данными
        print s["name"].ljust(15) + s["group"].ljust(8) + str(s["age"]).ljust(8) + str(s["marks"]).ljust(20)
        
        # считаем средний балл
        avg = sum(s["marks"]) / float(len(s["marks"]))
        print u"  средний балл: " + str(round(avg, 2))
        print ""  # пустая строка для разделения
    
    print "\n"

# фильтрация по среднему баллу
def filter_by_avg(students, min_avg):
    filtered = []
    
    for s in students:
        avg = sum(s["marks"]) / float(len(s["marks"]))
        if avg >= min_avg:
            # добавляем студента и его средний балл
            s_copy = s.copy()
            s_copy["avg"] = avg
            filtered.append(s_copy)
    
    return filtered

# вывод отфильтрованных студентов
def print_filtered(students):
    if not students:
        print u"нет студентов с таким баллом"
        return
    
    print u"Имя студента".ljust(15) + u"Группа".ljust(8) + u"Возраст".ljust(8) + u"Оценки".ljust(20)
    print "-" * 60
    
    for s in students:
        print s["name"].ljust(15) + s["group"].ljust(8) + str(s["age"]).ljust(8) + str(s["marks"]).ljust(20)
        if "avg" in s:
            print u"  ср. балл: " + str(round(s["avg"], 2))
        print ""

# основная программа
print u"Все студенты:"
print_students(groupmates)

# ввод числа
while True:
    try:
        sys.stdout.write(u"введи минимальный балл (можно с запятой): ")
        sys.stdout.flush()
        a = raw_input()
        min_avg = float(a)
        break
    except:
        print u"ошибка, попробуй еще"

print u"Студенты с баллом >= " + str(min_avg) + ":"

filtered = filter_by_avg(groupmates, min_avg)
print_filtered(filtered)