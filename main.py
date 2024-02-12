import pandas as pd
from selenium import webdriver
import time


# Ler mensagem
f = open("mensagem.txt","r")
message = f.read()
print(message)

# Carrega dados da planilha para um data frame e padroniza o número de telefone corrigindo problemas comuns
df = pd.read_excel("contatos.xlsx")
df['Number'] = df['Number'].str.replace(r'\D', '', regex=True)

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")

# Aguarda o usuário escanear o código QR
print("Escanee o código QR e pressione Enter.")
input()
print("Conectado!")

# Percorre o data frame enviando aos contatos a mensagem personalizada "Olá Name, ..."
for i, row in df.iterrows():
    print(row['Name'],row['Number'])

# Confirma que o login foi realizado

# Encerra o navegador
driver.quit()