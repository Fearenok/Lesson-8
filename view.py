def get_op():
    op = int(input("1 - Добавить студента\n 2 - добавить предмет\n 3 - добавит оценку\n 4 - показать весь список\n 5 - показать конкретного студента\n 6 - выход\n"))
    return op


def input_student():
    name = input("Введите имя и фамилию: ")
    return name


def input_less():
    less = input("Введите предмет: ")
    return less


def get_mark():
    name = input("Введите фамилию: ")
    less = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name, less, mark


def input_student_table():
    name = input("Введите имя и фамилию студента для просмотра оценок: ")
    return name
