import os     #Chamando algum comando da biblioteca.


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

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))    #INPUT: puxar informação do usuário.  #INT: transformar o resultado de string para número inteiro.

        if opcao_escolhida == 1 :        # == COMPARAÇÃO.
            print ('Cadastrar restaurante')
        elif opcao_escolhida == 2 :           # ELIF : else.
            print ('Listar restaurante')
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
