"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


user_dict = {"Как дела?" : "Хорошо!",
        "Что делаешь?" : "Программирую",
        "Почему так поздно?" : "Потому что дурак",
        }

def ask_user_dict(questions):    
     while True:
        try:
            user_question = input("Вопрос: ")
            if user_question in questions:
                print(questions[user_question])
            elif user_question == "Пока":
                print("Пока")
                break
        except KeyboardInterrupt:
            print('Жаль, пока')
            break
    
ask_user_dict(user_dict)
