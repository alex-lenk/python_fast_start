# coding : utf-8

answer = input("Кто сегодня хочет поработать? (Y/N)")

if answer == 'Y' or answer == 'y':
    print ("Выберите цифру, которая подходит для работы сегодня")
    select = int(input("Изучать python: 1, изучать JAVA: 2 = "))
    if select == 1:
        print ("Начинаем изучать питон")
    elif select == 2:
        print ("Изучаю ДЖАВА")
    else:
        print ("Вы не указали одну из двух цифр")
elif answer == "N" or answer == 'n':
    print ('Тогда досвидания')
else:
    print ('Вы дали непонятный ответ')
