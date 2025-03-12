from random import randint
from csv import reader

correct_words = []
translations = []
attempt = 1

with open('data.csv') as csv_file:
    csv_reader = reader(csv_file)
    for row in csv_reader:
        correct_words.append(row[0])
        translations.append(row[1])

index = len(correct_words)
print("Hello! This is a vocabulary trainer.")

while len(correct_words) != 0:
    length = len(correct_words)
    max_len = len(max(translations, key = len)) + 1
    words = ['' for i in range(length)]
    words.append(' ')
    score = 0

    for i in range(length):
        while words[index] != '':
            index = randint(0, length - 1)

        comparison = max_len - len(translations[index])
        comparison = 1
        word = input(f'"{translations[index]}"{" " * comparison}- ')
        if word == '':
            word = ' '
        words[index] = word

    print()
    deleted_words = []
    
    for i in range(length):
        print(f'"{words[i]}" - {translations[i]} ', end = '')

        if words[i].lower() != correct_words[i].lower():
            print(f'(Correct answer - {correct_words[i]})')

        else:
            print()
            score += 1
            deleted_words.append(correct_words[i])
    
    for i in deleted_words:
        index = correct_words.index(i)
        del correct_words[index]
        del translations[index]

    print(f'\nThe result of the attempt #{attempt}:\n    {score} / {length}')
    attempt += 1
    input()

print('Congratulations! You answered all words correctly.')