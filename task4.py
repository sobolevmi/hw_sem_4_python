d = dict({
    "б": "а", "в": "б", "г": "в",
    "д": "г", "е": "д", "ё": "е",
    "ж": "ё", "з": "ж", "и": "з",
    "й": "и", "к": "й", "л": "к",
    "м": "л", "н": "м", "о": "н",
    "п": "о", "р": "п", "с": "р",
    "т": "с", "у": "т", "ф": "у",
    "х": "ф", "ц": "х", "ч": "ц",
    "ш": "ч", "щ": "ш", "ъ": "щ",
    "ы": "ъ", "ь": "ы", "э": "ь",
    "ю": "э", "я": "ю", "а": "я"})

def decryption(user_dictionary, user_decryp_string):
    user_decryption_string = ""
    for i in user_decryp_string:
        if i in user_dictionary.keys():
            user_decryption_string = user_decryption_string + user_dictionary.get(i)
    return user_decryption_string

with open("file_task_4.txt", "w") as user_file:
    chiper_string = str(input("Зашифрованный текст: "))
    user_file.write("Зашифрованный текст: " + chiper_string + "\n")
    decryp = decryption(d, chiper_string)
    user_file.write("Расшифровка: " + decryp)