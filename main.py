from telas import *
from os import system
from time import sleep


def choose_highlighter():
    system('cls')
    while True:
        try:  #  detectar caso de erro de digitação
            first_player = input('first player choose the marker X or O?\n')
            if first_player == 'X' or first_player == 'O':
                print('Carregando...')
                break
        except:
            print('\nDigite novamente!\nValor inválido.\n')

    if first_player == 'X':
        second_player = 'O'
    else:
        second_player = 'X'
    return first_player, second_player


def cont_items(lista):
    cont1 = 0;  cont2 = 0; result = 0
    for i in lista:
        if i == '1':
            cont1 += 1
        if i == '2':
            cont2 += 1
    if cont1 == 3:
        result = True
    if cont2 == 3:
        result = True
    return result


def end_game(player):
    system('cls')
    if player == '1':
        print('Congratulation player one, your win.')
    elif player == '2':
        print('Congratulations player two, your win.')
    return True


line_dic = [['A1','A2','A3'], ['B1','B2','B3'], ['C1','C2','C3']]
col_dic = [['A1','B1','C1'], ['A2','B2','C2'], ['A3','B3','C3']]
diago_dic = [['A1','B2','C3'], ['A3','B2','C1']]
glob_list = [line_dic, col_dic, diago_dic]


def game_state(op, choose):  # choose pode ser '1' ou qual quer valor
    for two_dimensional in glob_list:
        for list_simple in two_dimensional:
            for i, value in enumerate(list_simple):
                if value == op and choose == '1':
                    list_simple[i] = choose
                    if cont_items(list_simple):
                        return end_game('1')
                elif value == op and choose == '2':
                    list_simple[i] = choose
                    if cont_items(list_simple):
                        return end_game('2')
    return False


def choice(operation):
    if operation == 1:
        game()
    elif operation == 2:
        pass
        # rank()
    else:
        print("Invalid Operation!")


def game():
    l_c = {'A1': 'A1','A2': 'A2','A3': 'A3',
            'B1': 'B1','B2': 'B2','B3': 'B3',
            'C1': 'C1','C2': 'C2','C3': 'C3'}
    first_player, second_player = choose_highlighter()
    cont = 0
    while True:
        system('cls')
        cont += 1

        frame()
        terminal_middel(f' {l_c["A1"]}  |  {l_c["A2"]}  |  {l_c["A3"]}  ')
        terminal_middel('------|------|------')
        terminal_middel(f' {l_c["B1"]}  |  {l_c["B2"]}  |  {l_c["B3"]}  ')
        terminal_middel('------|------|------')
        terminal_middel(f' {l_c["C1"]}  |  {l_c["C2"]}  |  {l_c["C3"]}  ')
        frame()

        # checar se ganhou ou se ainda existe espaço vazio
        char_list = ['A','B','C']
        number_list = ['1','2','3']
        dic_count = 0
        for char in char_list:
            for number in number_list:
                if l_c[char+number] == 'X' or l_c[char+number] == 'O':
                    dic_count += 1
        if dic_count == 9:
            print("Game tied\nEnd Game!")

        if cont % 2 != 0:
            line_column = input("\n<<< FIRST PLAYER >>>\nChoose row and column ex:B2\n")
            l_c[line_column] = first_player + ' '
            if game_state(line_column, '1'):
                break
        else:
            line_column = input("\n<<< SECOND PLAYER >>>\nChoose row and column ex:A3\n")
            l_c[line_column] = second_player + ' '
            if game_state(line_column, '2'):
                break
        if line_column == '0':
            break

        #  meio de checar quais lugares ainda se pode jogar, e não permitir se tiverem jogado ou se não ouver mais lugares
        #  definir quem é o ganhador, quando faltar apenas um lugar, já direciona para esse último lugar



welcome()
choice(home_screen())