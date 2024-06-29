#import math ---> biblioteca completa
#a funcionalidade quando baixa a biblioteca, chama math.funcionalidade: math.pow(x,y)
#outro exemplo: raiz=math.sqrt(x)

#Se não quiser a biblioteca completa:
#from math import sqrt ---> raíz quadrada
#from math import ceil (arredonda pra cima) ou floor (arredonda pra baixo)
#from math import trunc ---> elimina depois da vírgula
#from math import pow ---> potenciação
#from math import factorial ---> fatorial de um número

# import otimizado:
from math import sqrt,ceil
num = int(input("Digite um número: "))
raiz = sqrt(num)
print("A raiz de {} é {}.".format(num,ceil(raiz)))

# import completo:
# import math
# num = int(input("Digite um número: "))
# raiz = math.sqrt(num)
# print("A raiz de {} é {}.".format(num,math.ceil(raiz)))
