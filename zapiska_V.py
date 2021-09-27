import json
zapiska=[]

def strike(text):
    i = 0
    new_text = ''
    while i < len(text):
        new_text = new_text + (u'\u0336' + text[i])
        i = i + 1
    return(new_text)

def strike_task(task):
    return strike(task["text"]) if task["is_done"] else task["text"]

def update_task_is_done(number):
    task = zapiska[number]
    task["is_done"] = not task["is_done"]
    return task

def valid_zapiska_number(number):
    return number.isdigit() and 0 < int(number) <= len(zapiska)  

def yes_zapiska_choice(func):
    def wrapper(*arges, **kwargs):
        while True:
            result = func(*arges, **kwargs)
            y = input(f' Вы хотите добавить еще одну задачу? (y/n) ')
            if y in ('Y', 'y'):
                continue
            else:
                break
        return result
    return wrapper
            
    
def add_zapis(text):
    zapis = {
        "text": text,
        "is_done": False
    }
    zapiska.append(zapis)
    return zapis

def update_zapiska_text(number, text):
    zapis = zapiska[number]
    zapis["text"] = text
    return zapis

def print_zapiska():
    i = 1
    print('Список задач:')
    for task in zapiska:
        print(f'{i}. {strike_task(task)}')
        i += 1
    return True

@yes_zapiska_choice
def print_add_zapis_list():
    while True:
        print_zapiska()
        text = input('Введите новую задачу: ')
        task = add_zapis(text)
        return 

@yes_zapiska_choice
def print_update_zapiska_is_done():
    while True:
        print_zapiska()
        number = input('Введите номер задачи которую хотите отметить: ')
        if not valid_zapiska_number(number):
            print('Неверный номер задачи, попробуйте еще раз\n')
            continue
        number = int(number)
        task = update_task_is_done(number - 1)
        return 

@yes_zapiska_choice
def print_delete_zapiska():
    while len(zapiska):
        print_zapiska()
        number = input('Введите номер задачи которую хотите удалить: ')
        if not valid_zapiska_number(number):
            print('Неверный номер задачи, попробуйте еще раз\n')
            continue
        number = int(number)
        task = delete_zapis(number - 1)
        return True

def delete_zapis(number):
    task = zapiska.pop(number)
    return task

def print_update_zapiska():
    while True:
        print_zapiska()
        number = input('Введите номер задачи, которую необходимо редактировать: ')
        if not valid_zapiska_number(number):
            print('Неверный номер задачи, попробуйте еще раз\n')
            print_zapiska()
            continue
        number = int(number)
        text = input('Введите текст, на который хотите изменить: ')
        task = update_zapiska_text(number - 1, text)
        return 


def my_filter_print():
    text_filter = input ('что ищем?: ')
    out_filter = filter(lambda x: text_filter in x, zapiska)
    return print("Результат поиска:", list(out_filter))


def save_list_zametka():
    with open(input('Название файла: '), 'w') as name_file:
       json.dumps(zapiska,name_file)
    return True
       

def open_save():
    with open(input('Название файла: '), 'r') as name_file:
        global zapiska
        zapiska = json.loads(name_file)
    return print_zapiska
    
def zapiska_exit():
    y = input('Вы хотите выйти? (y/n) ')
    if y in ('y', 'Y'):
        exit()

choices={
    "1": print_add_zapis_list,
    "2": print_zapiska,
    "3": print_update_zapiska_is_done,
    "4": print_delete_zapiska,
    "5": print_update_zapiska,
    "6": my_filter_print,
    "7": save_list_zametka,
    "8": open_save,
    "0": zapiska_exit
}

chek= """
Опции меню:\n
1. Добавить заметку.
2. Показать список заметок.
3. Отметить.
4. Удаление заметки.
5. Редактировать задачу.
6. Поиск по именни.
7. сохранить заметки.
8. открыть файл.
0. Выход.\n
"""

while True:
    chek_number = input(chek)
    choice = choices.get(chek_number)
    if not choice:
        print('Неправильный номер меню, попробуйте еще раз')
        continue
    choice()