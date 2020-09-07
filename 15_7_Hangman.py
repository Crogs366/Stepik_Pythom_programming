import random

word_list = ['апельсин', 'погба', 'попугай', 'междометие', 'кальян', 'чебурашка', 'садовод']

def get_word(list):
    word = random.choice(list).upper()
    return word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = '*' * len(word)
    tries = 6
    guessed = False
    guessed_letters = []
    guessed_words = []

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print('Отгадываемое слово:', word_completion)
    print('У вас осталось попыток:', tries)
    
    while tries != 0:
        letter_word = ''
        while letter_word.isalpha() != True:
            letter_word = input('Введите букву или слово: ').upper()
            if letter_word.isalpha() == False:
                print('Вы ввели не верные данные, попробуйте еще раз!')
        while letter_word in guessed_letters or letter_word in guessed_words:
            print('Вы уже это писали. Попробуйте ещё раз!')
            letter_word = ''
            while letter_word.isalpha() != True:
                letter_word = input('Введите букву или слово: ').upper()
                if letter_word.isalpha() == False:
                    print('Вы ввели не верные данные, попробуйте еще раз!')
        if letter_word in word and len(letter_word) == len(word):
            guessed = True
            break
        if letter_word in word and len(letter_word) == 1:
            new_word_completion = ''
            for i in range(len(word)):
                if word[i] == letter_word:
                    new_word_completion += letter_word
                else:
                    new_word_completion += word_completion[i]
            word_completion = new_word_completion 
            print(word_completion)
            if word_completion == word:
                guessed = True
                break
            guessed_letters.append(letter_word)
        else:
            if len(letter_word) == 1:
                guessed_letters.append(letter_word)
            else: 
                guessed_words.append(letter_word)
            tries -= 1
            print(display_hangman(tries))
            print('Отгадываемое слово:', word_completion)
            print('У вас осталось', tries, 'попыток!')
    if guessed == True:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else: 
        print('Загаданное слово было', word)

new_game = ''
while new_game != 'нет':
    word = get_word(word_list)
    play(word)
    new_game = input('Хотите сыграть ещё раз? Да или нет: ').lower()
    while new_game != 'да' and new_game != 'нет':
        print('Напишите "да" или "нет"')
        new_game = input('Хотите сыграть ещё раз? Да или нет: ').lower()
    if new_game == 'да':
        new_game = ''
    else:
        new_game = 'нет'
        print('Возвращайся, если возникнут вопросы!')