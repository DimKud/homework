print ('Добро пожаловать!')
key=input('Введите номер заметки:')
value=input('Введите информацию:')
zametka = {key : value}
while True:
    action=input('Чем могу помочь?: \n1. Посмотреть список задач \n2. Добавить задачу. \n3. Удалить задачу. \n4. Выделить задачу. \n5. Редактировать задачу. \n6. Выход.')
    if action == '1':
        for key, value in zametka.items():
            print(key, value)
    if action == '2':
        for action in '2':
            key_1 = input('введите номер заметки:')
            if key_1 in zametka:
                print('присвойте другое значение')
                continue
            else:
                volue_1=input('введите информацию:')
                zametka[key_1]=volue_1
                for key, value in zametka.items():
                    print(key, value)
    elif action == '4':
        big_zam = input('Номер записи которую необходимо отметить?:')
        zametka[big_zam] = '* ' + zametka.get(big_zam) + ' *'
        for key, value in zametka.items():
            print(key, value)
    elif action == '6':
        print('До свидания!)')
        break



