# Vou criar uma variável para receber um valor digitado pelo usuário;
# Em seguida, através do comando type, vou descobrir o tipo primitivo (dado básico, nativo da linguagem);
# Em python, podem ser dados nativos: int, float, str, bool;
# Ocorrerá um problema: um valor retornado do comando input sempre será srt (string):

x = input('Digite qualquer coisa: ')
print('O tipo primitivo desse valor é: ', type(x))

# O que fazer para descobrir seu tipo então???
# Pode fazer testes através de perguntas que retornam um valor bool:

print('É um valor inteiro? ',x.isnumeric())
print('É um valor decimal? ',x.isdecimal())
print('É um valor alfanumérico? ',x.isalnum())
