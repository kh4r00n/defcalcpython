print('-=' * 30)
print('Calculadora em Python')
print('-=' * 30)

def add(x, y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print('\nSelecione o número da operação desejada:  \n')
print('1 - Soma')
print('2 - Substração')
print('3 - Multiplicação')
print('4 - Divisão')


while True:
    escolha = str(input('Digite sua opão: '))
    while escolha not in '1,2,3,4':
        print('Opção inválida. Digite novamente')
        escolha = str(input('Digite sua opão: '))

    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digit o segundo número: '))


    if escolha == '1':
        print('\n')
        print(f'{num1} + {num2} é igual a = {add(num1, num2)}')
        print('\n')
    elif escolha == '2':
        print('\n')
        print(f'{num1} - {num2} é igual a = {subtract(num1, num2)}')
        print('\n')

    elif escolha  == '3':
        print('\n')
        print(f'{num1} * {num2} é igual a = {multiply(num1, num2)}')
        print('\n')

    elif escolha == '4':
        if num2 == 0:
            print('Erro! Um número não pode ser divido por 0')
        else:
            print('\n')
            print(f'{num1} / {num2} é igual a = {divide(num1, num2)}')
            print('\n')

    else:
        print('\nOpção inválida')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer Continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print('Calculadora encerrada. Volte sempre!')