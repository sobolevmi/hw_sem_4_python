# Программа по замене записанных в файл имен учеников на запись этих имен заглавными буквами
# в случае наличия у ученика среднего балла больше 4"
def numbers(user_string):
    """Функция по извлечению чисел из строки.
    Авгумент user_string - строка, в которой содержатся сведения о ФИО ученика и его среднем балле"""
    user_list = list()
    for i in user_string.split():
        try:
            user_list.append(int(i))
        except ValueError:
            pass
    return user_list

def up(any_string):
    """Программа по переводу записи строки в верхний регистр в случае наличия в строке числа больше 4
    Аргумент any_string - строка, содержащая имя ученика и его средний балл"""
    k = numbers(any_string)
    if int(k[0]) > 4:
        any_string = any_string.upper()
    return any_string

with open("students_task3.txt", "w") as file:
    line_1 = up("Ангела Меркель 5\n")
    line_2 = up("Андрей Валетов 5\n")
    line_3 = up("Фредди Меркьюри 3\n")
    line_4 = up("Анастасия Пономарева 4\n")

    file.write(line_1)
    file.write(line_2)
    file.write(line_3)
    file.write(line_4)



