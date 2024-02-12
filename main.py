import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Ler mensagem
f = open("mensagem.txt","r")
message = f.read()
print(message)

# Carrega dados da planilha para um data frame e padroniza o número de telefone corrigindo problemas comuns
df = pd.read_excel("contatos.xlsx")
df['Number'] = df['Number'].str.replace(r'\D', '', regex=True) # **devo varrer numeros e corrigir** fazer
#df['Number']  = df['Number'] .astype(int)
df = df.dropna(subset=['Number']) # remove NAN
print(df)

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
    
    #print(row['Name'],row['Number'])
    try:
    # Encontre o campo de pesquisa e digite o número
        #search_box = driver.find_element("xpath", "//p[@class='selectable-text copyable-text iq0m558w g0rxnol2']")
        search_box = driver.find_element("xpath", "//div[@title='Caixa de texto de pesquisa']")
        time.sleep(2)
        search_box.send_keys(row['Number'])
        time.sleep(2)
        search_box.send_keys(Keys.ENTER)

        time.sleep(2)

        # Encontre o campo de mensagem e escreve
        message_box = driver.find_element("xpath", "//div[@title='Digite uma mensagem']")
        message_box.send_keys("Olá " + row['Name'] + "," + message)
        message_box.send_keys(Keys.ENTER)

        time.sleep(2)
    except:
        print("salvar contato dos clientes não contactados eu outro aquivo")

print("Mensagens Enviadas!")

# Encerra o navegador
driver.quit()