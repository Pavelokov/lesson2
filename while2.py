"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
user_dict = {"Как дела?" : "Хорошо!",
        "Что делаешь?" : "Программирую",
        "Почему так поздно?" : "Потому что дурак",
        }

def ask_user_dict(questions):    
     while True:
        user_question = input("Вопрос: ")
        if user_question in questions:
            print(questions[user_question])
        elif user_question == "Пока":
            print("Пока")
            break

ask_user_dict(user_dict)