import os     #Chamando algum comando da biblioteca.

restaurantes = ['Pizzaria', 'Churrascaria']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")                              #(""" """): Pular várias linhas.

def exibir_opcoes():
    print('1.Cadastrar restaurante')     #Print: exibir informação.
    print('2.Listar restaurantes')
    print('3.Ativar restaurante')
    print('4.Sair\n')

def finalizar_app():                                          #DEF: função
    os.system('cls')                         #Limpando a tela quando cair na opção 4.
    print('Finalizando o app\n')           #\n: pulando linha.

def opcao_invalida():
    print('Opção inválida\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)                         #colocar o nome dentro da lista   
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    input('\nDigite uma tecla para voltar ao menu inicial.')
    main()      

def listar_resturantes():
    os.system('cls')
    print('Listando os restaurantes\n')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    input('\nDigite uma tecla para voltar ao menu inicial.')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))    #INPUT: puxar informação do usuário.  #INT: transformar o resultado de string para número inteiro.

        if opcao_escolhida == 1 :        # == COMPARAÇÃO.
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :           # ELIF : else.
            listar_resturantes()
        elif opcao_escolhida == 3 :
            print ('Ativar restaurante')
        elif opcao_escolhida == 4 :
            finalizar_app()   
        else:          
            opcao_invalida()
    except:
        opcao_invalida()        

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':     #Nós não queremos que ele seja importado por outros arquivos.
    main()
