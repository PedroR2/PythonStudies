escolhas = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

def tabuleiro(escolha):
    print(escolha['7'] + '|' + escolha['8'] + '|' + escolha['9'])
    print('-+-+-')
    print(escolha['4'] + '|' + escolha['5'] + '|' + escolha['6'])
    print('-+-+-')
    print(escolha['1'] + '|' + escolha['2'] + '|' + escolha['3'])


def jogo():
    contador = 0
    print('voce quer ser X ou O')
    turno = input().upper()
    while turno != 'X' and turno != 'O':
        print('escolha entre X e O')
        turno = input().upper()
    print('a posicao deve ser escolhida tendo o teclado numerico como base')
    for i in range(10):
        tabuleiro(escolhas)
        print(turno, 'escolha sua posicao')
        posicao = input()
        if escolhas[posicao] == ' ':
            escolhas[posicao] = turno
            contador += 1
            print(contador)
            if contador >= 5:
                if escolhas['7'] == escolhas['8'] == escolhas['9'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
                elif escolhas['4'] == escolhas['5'] == escolhas['6'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
                elif escolhas['1'] == escolhas['2'] == escolhas['3'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
                elif escolhas['1'] == escolhas['4'] == escolhas['7'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
                elif escolhas['2'] == escolhas['5'] == escolhas['8'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
                elif escolhas['3'] == escolhas['6'] == escolhas['9'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
                elif escolhas['1'] == escolhas['5'] == escolhas['9'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
                elif escolhas['7'] == escolhas['5'] == escolhas['3'] != ' ':
                    tabuleiro(escolhas)
                    print(turno, 'ganhou')
                    print('fim de jogo')
                    break
            if contador == 9:
                print('empate')
            if turno == 'O':
                turno = 'X'
            else:
                turno = 'O'
        else:
            print('posicao invalida, escolha novamente')
            continue


jogo()
print('quer jogar dnv? (S/N)')
dnv = input()
if dnv == 's' or dnv == 'S':
    for i in escolhas.keys():
        escolhas[i] = ' '
    jogo()