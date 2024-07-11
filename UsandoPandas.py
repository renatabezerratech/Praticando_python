#-----------------------Algumas anotações--------------------------------------------------------
# pip install pandas
# pip install openpyxl numpy
#A new release of pip is available: 24.1.1 -> 24.1.2
#[notice] To update, run: C:\Users\rsbez\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.12_qbz5n2kfra8p0\python.exe -m pip install --upgrade pip

#------------------------------------------------------------------------------------------------
# Importante, quando estiver trabalhando com Pandas, lembrar que para o python cada linha é um index
# Exemplo dentro de um for: for linha in tabela.index:
# Lembrando que para o python ':' é o comando faça
#------------------------------------------------------------------------------------------------
# Para localizar informações use .loc[]
# Exemplo tabela.loc[linha, coluna]
#------------------------------------------------------------------------------------------------
import numpy as np
import pandas as pd

tabelaParaPandas_df = pd.read_excel("ParaPandas.xlsx")
print(tabelaParaPandas_df)   # No jupiter use display
