import os



print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)                              #(""" """): Pular várias linhas.

print('1.Cadastrar restaurante')     #Print: exibir informação.
print('2.Listar restaurantes')
print('3.Ativar restaurante')
print('4.Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))    #INPUT: puxar informação do usuário.  #INT: transformar o resultado de string para número inteiro.

def finalizar_app():                                          #DEF: função
     os.system('cls')                         #Limpando a tela quando cair na opção 4.
     print('Finalizando o app\n')           #\n: pulando linha.

if opcao_escolhida == 1 :        # == COMPARAÇÃO.
    print ('Cadastrar restaurante')
elif opcao_escolhida == 2 :           # ELIF : else.
    print ('Listar restaurante')
elif opcao_escolhida == 3 :
     print ('Ativar restaurante')        
else:          
    finalizar_app()


