import textwrap

def menu():
    menu = '''\n
=========menu=========
[1]\t depositar
[2]\t sacar
[3]\t extrato
[4]\t nova conta
[5]\t novo usuario
[6]\t listar contas7

[7]\t sair
 => '''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f'deposito: \R$ {valor:.2f}\n'
        print('\n=== deposito realizado com sucesso! ===')

    else:
        print('\n@@@ Operacao falhou,informa valor valido! @@@')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n@@@ Operacao falhou! Voc nao tem saldo suficiente. @@@')

    elif excedeu_limite:
        print('\n@@@ Operacao falhou! O valor do saque excede o limite. @@@')

    elif excedeu_saques:
        print('\n@@@ Operacao falhou! Numero maximo de saques excedido. @@@')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_saques += 1
    else:
        print('\n@@@ Operacao falhou! O valor informado e invalido. @@@')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('==========================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF(somente numero):')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\n@@@ Ja existe usuario com esse CPF! @@@')
        return
    
    nome = input('informe o nome completo: ')
    data_nascimento = input('informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereco(logradouro, nro - bairro - cidade / sigla do estado)')

    usuarios.append({'nome':nome, 'data de nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})

    print('=== Usuario criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf']== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('informe seu cpf:')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n=== conta criada com sucesso===')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\n -- usuario nao encontrado, criacao de conta encerrado')

def listar_contas(contas):
     for conta in contas:
        linha = f'''\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print('=' * 100)
        print(textwrap.dedent(linha))

    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ''
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == '2':
            valor = float(input('Informe o valor do saque: '))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == '4':
            criar_usuario(usuarios)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == '6':
            listar_contas(contas)

        elif opcao == '7':
            break

        else:

            print('Operacao invalida, por favor selecione novamente a operacao desejada')




main()