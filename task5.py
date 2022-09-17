### Программа по реализации RLE-алгоритма

def remove_duplicates(any_string):
    """Функция по удалению повторяющихся элементов в строке.
    Аргумент - введенная пользователем строка"""
    if isinstance(any_string, str):
        return ''.join([any_string[i] for i in range(len(any_string) - 1)
        if any_string[i + 1] != any_string[i]] + [any_string[-1]])

with open("input.txt", "w") as input_file:
    user_string = str(input("Введите исходную строку: "))
    user_string.strip()
    input_file.write(user_string)

with open("output.txt", "w") as output_file:
    result_string = remove_duplicates(user_string)
    output_file.write(result_string)