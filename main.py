from services import UsuarioService, ElogioService, ReclamacaoService

UsuarioService = UsuarioService.UsuarioService()
ElogioService = ElogioService.ElogioService()
ReclamacaoService = ReclamacaoService.ReclamacaoService()

#Usuario = Ant
#Senha = 1234

isLoggedIn = False

while True:
    print('Digite 1 para fazer login')
    print('Digite 2 para se cadastrar')
    print('Digite 3 para sair\n')
    opcao = int(input(f'\033[1;34mDigite sua opção:\033[m '))

    if opcao == 1:
        print('-' * 70)
        loginUsuario = input(f'\033[1;34mDigite seu usuario:\033[m ')
        loginSenha = input(f'\033[1;34mDigite sua senha:\033[m ')
        print('-' * 70)
        login = UsuarioService.findUserbyUsuario(loginUsuario)
        
        if len(login) > 0:
            
            if loginUsuario == login[0][2] and loginSenha == login[0][3]:
                isLoggedIn = True
                print(f'\033[1;32mLogin Bem Sucedido!\033[m')
                break
            
            else:
                print('-' * 70)
                print(f'\033[1;31mUsuario não encontrado com as informações fornecidas!\033[m')
                print('-' * 70)

        else:
            print('-' * 70)
            print(f'\033[1;31mUsuario não encontrado com as informações fornecidas!\033[m')
            print('-' * 70)
    
    elif opcao == 2:
        print('-' * 70)
        cadastrarNome = input(f'\033[1;34mDigite seu nome:\033[m ')
        cadastrarUsuario = input(f'\033[1;34mDigite seu usuario:\033[m ')
        cadastrarSenha = input(f'\033[1;34mDigite sua senha:\033[m ')
        print(f'\033[1;32mCadastro Realizado com Sucesso\033[m')
        print('-' * 70)
        UsuarioService.saveUsuario(cadastrarNome, cadastrarUsuario, cadastrarSenha)
    
    elif opcao == 3:
        print(f'\033[1;34mSaiu!\033[m')
        exit(0)
    

while isLoggedIn == True:

    print('-' * 70)
    print(f'\033[1;34m Seja bem vindo à ouvidoria da Celgon\033[m')
    print('-' * 70)
    print('Menu do Sistema\n')
    print('Opcões: \n')
    print('Digite 1 para cadastrar uma ocorrencia')
    print('Digite 2 para ver as listas de ocorrencia')
    print('Digite 3 para excluir algum item das listas')
    print('Digite 4 para apagar uma das listas')
    print('Digite 5 para sair\n')
    opcao = int(input(f'\033[1;34mDigite a sua opção:\033[m '))



    if opcao == 1:
        print(f'\033[1;34mQual ocorrencia deseja criar:\033[m\n')
        print('Digite 1 para Elogio')
        print('Digite 2 para Reclamação\n')
        ocorrencia = int(input(f'\033[1;34mDigite sua opção:\033[m '))
        
        if ocorrencia == 1:
            valor = input(f'\033[1;34mDigite seu Elogio:\033[m ')
            print(f'\033[1;32mElogio Registrado.\033[m')
            ElogioService.saveElogio(valor, login[0][0])
        
        elif ocorrencia == 2:
            valor = input(f'\033[1;34mDigite a sua Reclamação:\033[m ')
            print(f'\033[1;32mReclamação Registrada.\033[m')
            ReclamacaoService.saveReclamacao(valor, login[0][0])
        
        else:
            print(f'\033[1;31mOpção inválida!\033[m')
        


    elif opcao == 2:
        print(f'\033[1;34mQual lista você deseja visualizar:\033[m\n')
        print('Digite 1 para lista de Elogios')
        print('Digite 2 para lista de Reclamções\n')
        opcaoLista = int(input(f'\033[1;34mDigite sua opção:\033[m '))

        if opcaoLista == 1:
            for  i in ElogioService.findElogioByUsuarioId(login[0][0]):
                print(f'id: {i[0]} | elogio: {i[1]}')
            print('\033[1;34mFim da Lista.\033[m')
        
        elif opcaoLista == 2:
            for i in ReclamacaoService.findReclamacaoByUsuarioId(login[0][0]):
                print(f'id: {i[0]} | reclamação: {i[1]}')
            print(f'\033[1;34mFim da Lista.\033[m')
        
        else:
            print(f'\033[1;31mOpção inválida!\033[m')
        


    elif opcao == 3:
        print(f'\033[1;34mEscolha uma lista:\033[m\n')
        print('Digite 1 para Elogio')
        print('Digite 2 para Reclamação\n')
        opcaoListaExcluir = int(input(f'\033[1;34mDigite qual a lista desejada:\033[m '))
        
        if opcaoListaExcluir == 1:
            for i in ElogioService.findElogioByUsuarioId(login[0][0]):
                print(f'id: {i[0]} | elogio: {i[1]}')
            itemExcluido = int(input(f'\033[1;34mDigite qual valor da lista você deseja apagar:\033[m '))
            ElogioService.deleteElogioById(itemExcluido)
            print(f'\033[1;34mO item selecionado foi apagado.\033[m')
        
        elif opcaoListaExcluir == 2:
            for i in ReclamacaoService.findReclamacaoByUsuarioId(login[0][0]):
                print(f'id: {i[0]} | reclamação: {i[1]}')
            itemExcluido = int(input(f'\033[1;34mDigite qual valor da lista você deseja apagar:\033[m '))
            ReclamacaoService.deleteReclamacaoById(itemExcluido)
            print(f'\033[1;34mO item selecionado foi apagado.\033[m')
        
        else:
            print(f'\033[1;31mOpção inválida!\033[m')
        


    elif opcao == 4:
        print(f'\033[1;34mQual lista você deseja apagar?\033[m\n')
        print('Digite 1 para Elogio')
        print('Digite 2 para reclamação\n')
        opcaoApagarLista = int(input(f'\033[1;34mDigite a sua opção:\033[m '))

        if opcaoApagarLista == 1:
            ElogioService.deleteAllElogio()
            print(f'\033[1;34mSua lista de Elogio foi apagada.\033[m')
        
        elif opcaoApagarLista == 2:
            ReclamacaoService.deleteAllReclamacao()
            print(f'\033[1;34mSua lista de Reclamações foi apagada.\033[m')
        
        else:
            print(f'\033[1;31mOpção inválida.\033[m')
        


    elif opcao == 5:
        isLoggedIn == False
        print(f'\033[1;34mPor favor, avalie o nosso atendimento com uma nota de 0 a 10.\033[m')
        nota = input('Qual a sua nota para o nosso atendimento: ')
        print(f'\033[1;34mObrigado pela sua atenção, a Celgon agradece!\033[m')
        print('-' * 70)
        exit(0)
    


    else:
        print(f'\033[1;31mOpção inválida!\033[m')