'''
*************************************************
|  PROJETO: Desafio Sistema Bancário com Python  |
|  AUTOR: Heliton Leal                           |
|  VERSÂO: 1.0                                   |
**************************************************
 '''

menu = '''
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor para Depositar: '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação Não realizada! O valor informado é inválido.')
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque: '))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saques_excedidos = numero_de_saques >= LIMITE_DE_SAQUES

        if saldo_excedido:
            print('Operação falhou! Você não tem saldo suficiente.')
        elif limite_excedido:
            print('Operação falhou! O valor do saque excede o limite.')
        elif saques_excedidos:
            print('Operação falhou! Número máximo de saques excedido.')
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_de_saques += 1
        else:
            print('Operação falhou! o valor informado é inválido.')

    elif opcao == 'e':
        print('\n************* EXTRATO *************')
        print('Sem Movimentações recentes.' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('==================================')
    elif opcao == 'q':
        break

    else:
        print('Operação Inválida! Favor escolher uma opção válida: ')