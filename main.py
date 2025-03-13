from random import randint
from csv import reader

correct_words, translations = [], []
attempt = 1

file = open('data.csv', 'r')
csv = reader(file)
for row in csv:
    correct_words.append(row[0])
    translations.append(row[1])
file.close()

index = len(correct_words)
print("Hello! This is a vocabulary trainer.\n")

while len(correct_words) != 0:
    length = len(correct_words)
    words = ['' for i in range(length)]
    words.append(' ')
    score = 0

    for i in range(length):
        while words[index] != '':
            index = randint(0, length - 1)
        word = input(f'{i + 1}) "{translations[index]}" - ')
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
    if len(correct_words) > 0:
        attempt += 1
        save = input('\nDo you want to save the wrong words in the new CSV file? [Any key = Yes, n = No]: ')
        if save.lower() != 'n':
            file = open('new_data.csv', 'w+')
            for i in range(0, len(correct_words)):
                file.write(f'"{correct_words[i]}","{translations[i]}"\n')
            file.close()
    print()

print('Congratulations! You answered all words correctly.')