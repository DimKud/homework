def user(list1):
    while 2:
        if metod.isdigit():
            if metod=='1':
                print(list1.upper())
            elif metod=='2':
                print(list1.lower())
            elif metod=='3':
                print(list1.capitalize())
            elif metod == '4':
                print(len(list1))
            elif metod == '5':
                list2=input('Введите информацию которую хотите добавить:')
                list1=list1+list2
                print(list1)
            elif metod == '6':
                x=input('Какой символ вы хотите поменять?:')
                y=input('на что хотите заменить?:')
                list3=list1.replace(x,y)
                print(list1)
        return metod
list1= input('Добро пожаловать! Введите информацию:')
while 1 :
    metod=input('1-сделать все символы заглавными, 2-сделать все символы строчными, 3-сделать первый символ заглавным, 4-посчитать количество символов в строке, 5-добавить символ, 6-заменить символ, 7-Выйти из программы. ')
    list1=user(list1)
    if metod == '7':
        exit = input('Выход? 1-да, 2-нет')
        if exit == '1':
            break
        elif exit == '2':
            continue






