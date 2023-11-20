students = {}
#Добавление студента
def Add_students():
    new_name = input('Введите имя: ')
    new_age = int(input('Введите возраст: '))
    new_class = input('Введите класс студента: ')
    students[new_name] = {'Возраст': new_age, 'класс': new_class}
    print(students)

def Delete_students():
    print(students)
    del_students = input('Кого хотите удалить?: ')
    if del_students in students:
        students.pop(del_students)
        print('Студент успешно удаден!')
    else:
        print('Такого студента в списке нет!')

def Change_students():
    print(students)
    change = input('Введите имя студента которое хотите изменить: ')
    if change in students:
        students.pop(change)
        add_new_name = input('Введите новое имя студента:')
        add_age = int(input('Введите новый возраст:'))
        add_class = input('Введите новый класс: ')
        students[add_new_name] = {'Возраст': add_age, 'Класс': add_class }
    else:
        print('Такого студента нет в списке!')


while True:
    menu = int(input( '1 - Add_students\n2 - Delete_students\n3 - Change_students\n4 - List\n5 - Exit'  ))

    if menu == 1:
        Add_students()
    elif menu == 2:
        Delete_students()
    elif menu == 3:
        Change_students()
    elif menu == 4:
        print(students)
    elif menu == 5:
        print('Выберите действие!')
    else:
        pass

