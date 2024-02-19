import os     #Chamando algum comando da biblioteca.

restaurantes = [{'nome': 'Praça', 'categoria':'Japones', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria':'Pizzaria','ativo': True},
                {'nome': 'Cantina', 'categoria':'Italiano', 'ativo': False}]

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
    exibir_subtitulo('Finalizar app')
    #os.system('cls')                         #Limpando a tela quando cair na opção 4.
    #print('Finalizando o app\n')           #\n: pulando linha.

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu. ')
    main()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    #---restaurantes.append(nome_do_restaurante)                         #colocar o nome dentro da lista  
    restaurantes.append(dados_do_restaurante) 
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()   

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes:
        nome_restaurante = restaurante ['nome']
        categoria = restaurante['categoria']
        ativo = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()


def escolher_opcao():
    try:       # captura erros de valor e converte para inteiro.
        opcao_escolhida = int(input('Escolha uma opção: '))    #INPUT: puxar informação do usuário.  #INT: transformar o resultado de string para número inteiro.

        if opcao_escolhida == 1 :        # == COMPARAÇÃO.
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 :           # ELIF : else.
            listar_restaurantes()
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
