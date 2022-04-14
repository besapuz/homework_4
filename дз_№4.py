words_easy = {"family": "семья",
              "hand": "рука",
              "people": "люди",
              "evening": "вечер",
              "minute": "минута"
              }

words_medium = {"believe": "верить",
                "feel": "чувствовать",
                "make": "делать",
                "open": "открывать",
                "think": "думать"
                }

words_hard = {"rural": "деревенский",
              "fortune": "удача",
              "exercise": "упражнение",
              "suggest": "предлагать",
              "except": "кроме"
              }

levels = {0: "Нулевой",
          1: "Так себе",
          2: "Можно лучше",
          3: "Норм",
          4: "Хорошо",
          5: "Отлично"}
answers = {}
words = {}
print('Выберите уровень сложности.\nЛегкий, средний, сложный.')
level = input().lower()

if level == 'легкий' or level == 'лёгкий':  # ответы из словаря
    words = words_easy
elif level == 'средний':
    words = words_medium
elif level == 'сложный':
    words = words_hard
print('Выбран уровень сложности, мы предложим 5 слов, подберите перевод.')
print('Нажмите Enter')
input()  # по условию задачи

for key in words.keys():
    list_value = str(words[key])
    if len(words[key]) < 5:  # корректные оконания
        letters = 'буквы'
    else:
        letters = 'букв'
    print(f'{key}, {len(words[key])} {letters}, начинается на {list_value[0]}...')

    answer = input()
    if answer == words[key]:
        print(f'Верно, {key.capitalize()} — это {words[key]}.')
        answers[key] = True
    else:
        print(f'Неверно. {key.capitalize()} — это {words[key]}.')
        answers[key] = False
    print()

correct_answers = []  # словарь для подсчета правильных ответов
print('Правильно отвечены слова:')
for k in answers:
    if answers[k]:
        print(k)
        correct_answers.append(k)
print()
print('Неправильно отвечены слова:')
for k_false in answers:
    if not answers[k_false]:
        print(k_false)
print()
print(f'Ваш ранг:\n{levels[len(correct_answers)]}')
