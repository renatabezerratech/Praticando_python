import os
lista_arquivos = os.listdir("arquivos")
#print(lista_arquivos)
for arquivos in lista_arquivos:
    if ".txt" in arquivos:
        if "22" in arquivos:
        print("movimentar para pasta 22")