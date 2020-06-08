#Importando bibliotecas que serão utilizados
import requests
import json
import hashlib
import html
import cgi
import cgitb
import os


#Acessando o arquivo JSON do desafio
get_json = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=777d8364b94bec6faf8133b9ea96a41e62b142b6')


#Salvando o arquivo JSON no modelo answer.json como solicitado

#1-Precisamos transformar o arquivo JSON em string
json_str = json.dumps(get_json.json())

#2-Salvamos a string gerada no passo anterior em um arquivo json
with open('answer.json', 'w') as f:
    f.write(json_str)


#Teste do arquivo get_json
get_json.json()


#Decifrando o código

#Criando variáveis
json_file = get_json.json()
num_casas = json_file['numero_casas']
str_decrypt = ''
lista_index_cifrado = list(range(len(json_file['cifrado'])))
counter = 0

#Criando uma lista com os caracteres do alfabeto 
list_car_num = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19, 't':20, 'u':21, 'v':22, 'w':23,'x':24, 'y':25, 'z':26}
list_car_letter = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}


#For para preencher a str_decrypt com os valores decriptografados            
for i in lista_index_cifrado:
    try:
        index_decrypt  = list_car_num[json_file['cifrado'][i]] - num_casas
        if index_decrypt < 1:
            index_decrypt = 26 + index_decrypt
        str_decrypt += list_car_letter[index_decrypt]
    except:
        str_decrypt += json_file['cifrado'][i]

json_file['decifrado'] = str_decrypt



#Resumo criptográfico com a biblioteca hashlib
json_file['resumo_criptografico'] = hashlib.sha1(str_decrypt.encode('utf-8')).hexdigest()


#Transformando json_file em string para podermos escrever o arquivo answer
json_str = json.dumps(json_file)

#Salvamos a string gerada no passo anterior em um arquivo json
with open('answer.json', 'w') as f:
    f.write(json_str)
    
answer = json_file
print(answer)


#Enviando a resposta
files = {'answer': ('answer.json', open('answer.json', 'rb'), 'json', {'Expires': '0'})}
response = requests.post(url, files=files)
print(response.text)

