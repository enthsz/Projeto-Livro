def cadastrar_livro(id, lista): 
    id = 0 
    while True: 
        id+=1 
        print('--'*20) 
        print('--'*10, 'MENU CADASTRAR LIVRO', '--'*10) 
        nome_livro = input('Por favor entre com o nome do livro: ') 
        autor = input('Por favor entre com o autor do livro: ') 
        editora = input('Por favor entre com a editora do livro: ') 
        dic = { 
            'ID': id, 
            'Nome do livro': nome_livro, 
            'Autor do Livro': autor, 
            'Editora': editora, 
        } 
        lista.append(dic) 
        continuar = input("Deseja cadastrar outro livro? (s/n): ").lower() 
        if continuar.lower() != 's': 
            break 

def consultar_livro(livros): 
    while True: 
        print('--'*20) 
        print('--'*10, 'MENU CONSULTAR LIVRO', '--'*10) 
        print('1 - Consultar Todos os livros\n2 - Consultar por Id\n3 - Consultar por Autor\n4- Retornar ao menu') 
        escolha = input('Digite uma opção: ') 
        print('--------') 
        if escolha == '1': 
            if not livros: 
                print('Não há livros cadastrados') 
            else: 
                for idx, livro in enumerate(livros, start=1): 
                    for chave, valor in livro.items(): 
                        print(f'{chave}: {valor}') 
                    print() 
        elif escolha == '2': 
            escolha_id = input('Escolha o livro pelo ID: ') 
            livro_encontrado = False 
            for livro in livros: 
                if str(livro['ID']) == escolha_id: 
                    print('Livro encontrado:') 
                    for chave, valor in livro.items(): 
                        print(f'{chave}: {valor}') 
                    livro_encontrado = True 
                    break 
            if not livro_encontrado: 
                print('Livro não encontrado.') 
        elif escolha == '3': 
            escolha_autor = input('Escolha o autor pelo escrevendo o nome dele: ') 
            autor_encontrado = False 
            for livro in livros: 
                if livro['Autor do Livro'] == escolha_autor: 
                    print('Autor encontrado:') 
                    for chave, valor in livro.items(): 
                        print(f'{chave}: {valor}') 
                    autor_encontrado = True 
                    break 
            if not autor_encontrado: 
                print('Autor não encontrado.') 
        elif escolha == '4': 
            break 
        else: 
            print("Opção inválida. Por favor, escolha uma opção válida.") 
            continue 

def remover_livro(livros): 
    while True: 
        print('--'*20) 
        print('--'*10, 'MENU REMOVER LIVRO', '--'*10) 
        remover = input('Digite o ID do livro a ser removido(0 para desistir): ') 
        if remover.lower() == '0': 
            break     
        livro_encontrado = False 
        for livro in livros: 
            if str(livro['ID']) == remover: 
                livros.remove(livro) 
                livro_encontrado = True 
                print(f"Livro com ID {remover} removido com sucesso.") 
                break 

        if not livro_encontrado: 
            print('Livro não encontrado. Tente outro ID.') 
            remover = input('Digite o ID do livro a ser removido: ') 
        continuar = input("Deseja remover outro livro? (s/n): ").lower() 
        if continuar.lower() != 's': 
            break 

listar_livro = [] 
id_global = 0 
while True: 
    print('Bem vindo a Livraria do Enthony Ruan') 
    print('--'*28) 
    print('--'*10, 'MENU PRINCIPAL', '--'*10) 
    print('Escolha a opção desejada') 
    print('1 - Cadastrar Livro\n2 - Consultar Livro(s)\n3 - Remover Livro\n4 - Sair') 
    escolha = input('O que voce deseja fazer: ') 
    if escolha == '1': 
        cadastrar_livro(id_global, listar_livro) 
    elif escolha == '2': 
        consultar_livro(listar_livro) 
    elif escolha == '3': 
        remover_livro(listar_livro) 
    elif escolha == '4': 
        break 
    else: 
        print('Nao existe esse comando tente novamente') 