print('Bem-vindo ao exercício de condicionais\n')

print('1.Par ou Impar')
print('2.Idade')
print('3.usuario e senha')
print('4.Plano cartesiano\n')
opcao = int(input('Escolha uma das opções acima para realizar uma ação: '))


match opcao:
    case 1:
        escolha = int(input('Escolha um número: '))
        if escolha % 2 == 0:
            print('O número escolhido é par!')
        else:
            print('O número escolhido é impar!')
    case 2:
        idade = int(input('Informe sua idade: '))
        if idade >=0 and idade <= 12:
            print('Você está categorizado nas idades 0 à 12 anos!')
        elif idade >= 13 and idade <= 18:
            print('Você está categorizado nas idades 13 à 18 anos!')
        else:
            print('Você está com idade acima dos 18 anos')
    case 3:
            usuario = input('Informe um nome de usuário: ')
            senha = int(input('informe uma senha: '))
            if usuario == usuario and senha == senha:
                print('Login e senha corretos, podemos prosseguir!')
            else:
                print('Usuário ou Senha incorreto(s)')  
    case 4:
        planX = int(input('Informe o valor de X:'))
        planY = int(input('Informe o valor de Y:'))
        
        if planX>0 and planY>0:
            print('Os valores informados estão no 1º quadrante')
        elif planX<0 and planY>0:
            print('Os valores informados estão no 2º quadrante')
        elif planX<0 and planY<0:
            print('Os valores informados estão no 3º quadrante')
        elif planX>0 and planY<0:
            print('Os valores informados estão no 4º quadrante')
        else:
            print('O ponto está localizado no eixo ou origem')
