def menu():
    print(f'''
{'=' * 40}
{'Sistema Bancário V2'.center(40)}
{'=' * 40}

[1] Depositar
[2] Sacar
[3] Extrato
[4] Nova Conta
[5] Listar Contas
[6] Novo Usuário
[7] Sair
''')

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito de R${valor:.2f}\n'
        print(f'Deposito realizado com sucesso.')
    else:
        print('O valor digitado é inválido.')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, saques, limite_saques, limite_valor):
    if valor < 0:
        print('O valor digitado é inválido.')
    elif valor > saldo:
        print('Você não tem saldo suficiente para realizar essa operação.')
    elif valor > limite_valor:
        print('Você não tem autorização para sacar esse valor.')
    elif saques >= limite_saques:
        print('Você excedeu o número de saques diários.')
    else:
        saques += 1
        saldo -= valor
        extrato += f'Saque de R${valor:.2f}\n'
        print('Saque realizado com sucesso.')
    return saldo, extrato, saques

def historico(saldo, /, *, extrato):
    print(f'Seu saldo é R${saldo:.2f}.\n')
    print(f'{extrato}' if extrato else 'Ainda não foram realizadas operações nessa conta.')

def criar_usuario(usuarios):
    cpf = input('Digite o seu CPF (somente números): ')

def main():
    menu()
    saldo = 0
    extrato = ''
    saques = 0
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500
    usuarios = []
    contas = []
    while True:
        opcao = input('\n' + 'Digite a operação que deseja realizar: ')
        if opcao == '1':
            valor = float(input('Informe o valor que deseja depositar: '))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor que deseja sacar: '))
            saldo, extrato, saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                saques=saques,
                limite_saques=LIMITE_SAQUES,
                limite_valor=LIMITE_VALOR
            )
            
        elif opcao == '3':
            historico(saldo, extrato=extrato)

        elif opcao == '4':
            ...

        elif opcao == '5':
            ...

        elif opcao == '6':
            ...

        elif opcao == '7':
            print('Obrigado por utilizar nossos serviços. Até mais!')
            break

        else:
            print('Opção inválida.')

main()