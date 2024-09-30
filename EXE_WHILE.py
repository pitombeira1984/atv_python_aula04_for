while True:
    print('\nMenu:')
    print('1. Diga Olá')
    print('2. Diga Adeus')
    print('Diga "sair" para terminar o programa.')

    opcao = input('EScolha uma opção:')

    if opcao == '1':
        print('Olá!')
    elif opcao == '2':
        print('Adeus!')
    elif opcao.lower() == 'sair':
        print('Encerrando o Programa.')
        break
    else:
        print('Opção inválida, tente novamente.')
