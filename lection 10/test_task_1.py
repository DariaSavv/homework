# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string

def generate_random_name():
    while True:
        words_1 = random.randint(1, 15)
        words_2 = random.randint(1, 15)
        letters = string.ascii_lowercase
        letters_1 = ''
        letters_2 = ''
        for i in range(words_1):
            letters_1 += random.choice(letters)
        for i in range(words_2):
            letters_2 += random.choice(letters)
        yield f"{letters_1} {letters_2}"


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))