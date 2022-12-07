from lab1 import function

house = {
    1: {(50, 2): 'Пусто'},
    2: {(70, 3): 'Вся возможная мебель'},
    3: {(40, 1): 'Стол, телевизор, детская мебель'},
    4: {(90, 6): 'Пусто'},
    5: {(30, 1): 'Пусто'},
}


def command_edit():
    print("Input edit or add floor:", end=' ')
    floor = function.check_correct_int_input()
    print("Input square:", end=' ')
    square = function.check_correct_int_input()
    print("Input count rooms:", end=' ')
    count_rooms = function.check_correct_int_input()
    print("Input things:", end=' ')
    things = str(input())
    house[floor] = {(square, count_rooms): things}


def show():
    for key, value in house.items():
        print("Floor: ", key, "\n", "Square: ", tuple(value.keys())[0][0], "\n", "Count rooms: ",  tuple(value.keys())[0][1], "\n", "Things: ", value[tuple(value.keys())[0]])
        print("--------------------------------------------")


def run_product_list_cmd_client():
    while True:
        cmd = input('Input command: ')

        if cmd == 'help':
            CMDS = [
                'help - print all commands',
                'show - print all house',
                'edit and add - edit floor',
                'quit - quit the system'
            ]
            print('\n'.join(CMDS))
        elif cmd == 'quit':
            print('See you soon!')
            break
        elif cmd == 'edit':
            command_edit()
        elif cmd == 'show':
            show()
        else:
            print('Unknown command')


run_product_list_cmd_client()