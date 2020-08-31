import random
import os

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
used_letters = []


def vyvod(level):
    levels = [
        '',
        '/|\\',
        ' | \n | \n | \n/|\\',
        '  ___ \n | \n | \n | \n/|\\',
        '  ___\n |   |\n |  \n |  \n | \n/|\\',
        '  ___\n |   |\n |   0\n |  \n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n | \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n |  / \n/|\\',
        '  ___\n |   |\n |   0\n |  /|\\\n |  / \\\n/|\\',
    ]
    if 0 <= level <= 10:
        print(levels[level])
    else:
        raise TypeError('Incorrect level')


def rand_hod():
    yield 'привет'
    with open('word_rus.txt', 'r', encoding='UTF-8') as file:
        file = file.readlines()
        while True:
            random_slowo = random.choice(file)
            yield random_slowo.strip()


def create_word_field(word):
    secret_word = len(word) * '_'
    secret_word = list(secret_word)
    return secret_word


def make_move(field, used, word):
    while True:
        new_letter = input('Введи букву которой еще не было: ')
        new_letter = new_letter.lower()
        if len(new_letter) == 1 and new_letter in alphabet and new_letter not in used:
            if new_letter in word:
                for i in range(len(word)):
                    if word[i] == new_letter:
                        field[i] = new_letter
                used.append(new_letter)
                return [field, used, word, True]
            used.append(new_letter)
            return [field, used, word, False]
        else:
            print('Вы ввели не корректные данные.Введите еще раз')


def winning_or_loosing(field, game_number):
    if "_" not in field:
        return True
    elif game_number >= 10:
        return False


words = rand_hod()
word = next(words)
field_word = create_word_field(word)
game_number = 0
print('Мы загадали слово.')

while True:
    print('Загаданное слово: ', ' '.join(field_word))
    vyvod(game_number)
    print('Использованные буквы: ', ' '.join(used_letters))
    field_word, used_letters, word, in_word = make_move(field_word, used_letters, word)

    if not in_word:
        game_number += 1

    is_win = winning_or_loosing(field_word, game_number)
    if is_win:
        print('Вы победили: ')
        print(word)
        break

    if is_win == False:
        print('Вы проиграли: ')
        vyvod(game_number)
        print(word)
        break
    os.system('cls')
