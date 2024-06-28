# Aqui, resolvi praticar a interação com o usuário.

nome=input('Qual é o seu nome?')
print('Que bom te ver por aqui ',nome)
idade=input('Qual é a sua idade?')
print('Com {} anos {} você tem muitas coisas legais para aprender!'.format(idade,nome))
resposta=input('Vamos descobrir alguns resultados de operações matemáticas?')
if resposta == 'não':
    print('ok então!')
else:
    print('Então vamos trabalhar com dois valores.')

    x=int(input('Digite um valor: '))
    y=int(input('Digite outro valor: '))
    s=x+y
    z=x-y
    m=x*y
    d=x/y
    e=x**2
    f=y**2

    print('='*30)
    print('A soma de {} e {} é: {}'.format(x,y,s))
    print('='*30)
    print('A subtração de {} e {} é: {}'.format(x,y,z))
    print('='*30)
    print('A multiplicação de {} e {} é: {}'.format(x,y,m))
    print('='*30)
    print('A divisão de {} e {} é: {}'.format(x,y,d))
    print('='*30)
    print('O resultado de {} elevado à 2 é: {}'.format(x,e))
    print('='*30)
    print('O resultado de {} elevado à 2 é: {}'.format(y,f))
    print('='*30)





