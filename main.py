while True:
# entrada de dados
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))

    print('LISTA DE FILMES')
    print('Sala 1 - Titanic - Classificação Indicativa 12 anos.')
    print('Sala 2 - Vivendo a Vida Adoidado - Classificação Indicativa 16 anos.')
    print('Sala 3 - Forrest Gump - Classificação Indicativa 18 anos.')
    print('Sala 4 - O Resgate do Soldado Ryan - Classificação Indicativa 21 anos.')
    print('Sala 5 - De Volta Para o Futuro 3 - Classificação Indicativa 10 anos.')

    sala = int(input('Informe a sala desejada: '))
    
    match sala:
        case 1:
            print(f'Filme escolhido por {nome}: Titanic.')
            if idade < 12:
                print('Proibida a entrada')
            else:
                print('Bom Filme')
                break
        case 2:
            print(f'Filme escolhido por {nome}: Vivendo a Vida Adoidado.')
            if idade < 16:
                print('Proibida a entrada')
            else:
                print('Bom Filme')
        case 3:
            print(f'Filme escolhido por {nome}: Forrest Gump.')
            if idade < 18:
                print('Proibida a entrada')
            else:
                print('Bom Filme')
        case 4:
            print(f'Filme escolhido por {nome}: O Resgate do Soldado Ryan.')
            if idade < 21:
                print('Proibida a entrada')
            else:
                print('Bom Filme')
        case 5:
            print(f'Filme escolhido por {nome}: De Volta Para o Futuro 3.')
            if idade < 10:
                print('Proibida a entrada')
            else:
                print('Bom Filme')
        case _:
            print('Filme inexistente.')
            