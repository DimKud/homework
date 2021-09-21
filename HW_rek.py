#сумма чисел в списке 
def sumrec(list1):
    if len(list1) == 0:
        return 0
    else:
        return list1[0] + sumrec(list1[1:])


#возведение в степень
def my_step(x, step):
    if (step == 1):
        return (x)
    if (step != 1):
        return (x * my_step(x, step - 1))

#полиндропы
def polindrop(list):
    list = list.lower()
    list = list.split()
    list = ''.join(list)
    list_revers =list[::-1]
    if list_revers == list:
        print('polindrop')
    else:
        print('no polindrop')
    
#количество отрицательных чисел в списке 
def negativ(string):
    if string == []:
        return 0
    count = negativ(string[1:])
    if string[0] < 0:
        count += 0
    return count 


    
    

 