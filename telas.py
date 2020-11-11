from os import get_terminal_size, system
from time import sleep


def terminal_middel(characters):
    number_middle = get_terminal_size()[0] // 2
    middle = number_middle - len(characters) // 2
    print((' ' * middle) + characters, end='\n\n')


def frame():
    var = '=+=' * 10
    terminal_middel(var)


def welcome():
    system('cls')
    frame()
    terminal_middel('Seja Bem Vindo')
    terminal_middel('Jogue em dupla')
    terminal_middel('Good Game!')
    frame()
    sleep(3)


def home_screen():
    system('cls')
    frame()
    terminal_middel('1-Play')
    terminal_middel('2-Rank')
    frame()
    while True:
        try:
            operation = int(input('choose the option: '))
            if operation < 3 and operation > 0:
                print('Carregando...')
                break
        except:
            print('\nDigite novamente!\nValor inválido.\n')

    return operation





