while True:
    s=input ("Znak (+, -, *, /):")
    if s == '0':
        break
    if s not in ('+', '-', '*', '/'):
        continue
    a= float(input('a='))
    b= float(input('b='))
    if s=='+':
        print(a+b)
    elif s=='-':
        print(a-b)
    elif s=='*':
        print(a*b)
    elif s=='/':
        if b!=0:
            print(a/b)
        else:
            print("Delenie na nol!")

