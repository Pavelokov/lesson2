"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def assess(list):
    a = 0
    b = 0
    for value in list:
        a += sum(value['scores'])
        b += len(value['scores'])
        print("Средний балл класса {} равен: {}.".format(value['school_class'], sum(value['scores']) / len(value['scores'])))
    print("Средний балл по школе: {}.".format(a / b))

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

list = [{'school_class': '1a', 'scores': [1,2,3,4,5]},
                {'school_class': '2a', 'scores': [2,3,4,5,1]},
                {'school_class': '3a', 'scores': [5,5,5,5,4]},
                {'school_class': '4a', 'scores': [3,2,1,3]},
                {'school_class': '5a', 'scores': [4,4,3,3,3]},
                {'school_class': '6a', 'scores': [5,5,4]},
                {'school_class': '7a', 'scores': [1,1,1,2,1,1,1]}
        ]

assess(list)
    
if __name__ == "__main__":
    main()
