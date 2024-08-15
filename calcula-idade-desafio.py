nome = input('Digite o seu nome: ')
while not nome.strip().isalpha():
    nome = input('Nome não pode estar vazio e deve conter apenas letras. Por favor, digite um nome válido: ')

dataNascimento = False

while not dataNascimento:
    try:
        anoNascimento = int(input('Digite o seu ano de nascimento: '))
        anoAtual = 2024
        idade = anoAtual - anoNascimento
        if 1922 <= anoNascimento <= 2021:
            print(f'Olá {nome}, você completou ou completará {idade} anos em {anoAtual}')
            dataNascimento = True
        else:
            print('ERRO: O ano precisa ser entre 1922 e 2021')
    except ValueError:
        print('ERRO: O valor digitado precisa ser um número.')
