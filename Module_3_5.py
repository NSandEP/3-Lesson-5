def get_multiplied_digits(number):       #Создание функции get_multiplied_digits
    str_number = str(number)             #Создание переменной str_number и запись строкового представления(str) числа number
    first = int(str_number[0])           #Cоздание переменной first и запись в неё первого символа из str_number в числовом представлении(int)
    if len(str_number) > 1:              #Условие
        return first * get_multiplied_digits(int(str_number[1:]))        #Возвращаем значение
    elif int(str_number[1:]) != 0:
        return first


result = get_multiplied_digits(40203)    #Ввод значения
print(result)                            #Вывод результата
result2 = get_multiplied_digits(402030)  #Ввод значения
print(result2)                           #Вывод результата
