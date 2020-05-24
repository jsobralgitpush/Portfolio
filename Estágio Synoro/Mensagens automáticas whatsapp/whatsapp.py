
##############################################################
#USANDO A FERRAMENTA TWILlIO
##############################################################

from twilio.rest import Client



client = Client()


from_whatsapp_number='whatsapp:+5511951280054'
to_whatsapp_number='whatsapp:+5521980591606'



client.messages.create(body='É só um test, meu irmão!!!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)



##############################################################
#USANDO O SELENIUM
##############################################################

import json
import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options



base_url = 'https://web.whatsapp.com/'
workdir = os.getcwd()
chrome = workdir+'\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir="+workdir+"\profile\wpp")
driver = webdriver.Chrome(chrome, chrome_options=options)
driver.get(base_url)
sleep(15)

#procurando a lupa de contatos
nome_contato = 'Diogo'
caixa_de_pesquisa = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
caixa_de_pesquisa.send_keys(nome_contato)
sleep(5)

contato = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[12]/div/div/div[2]/div[1]/div[1]/span/span')
contato.click()
 
mensagem = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
mensagem.send_keys('Testando mensagem :)')

enviar_mensagem = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span')
enviar_mensagem.click()

##############################################################
#USANDO O CHAT-API
##############################################################


import json
import requests

class WABot():
    def __init__(self):
        self.APIUrl = 'privado'
        self.token = 'privado'

    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"phone": chatID, "body": text}
        answer = self.send_requests('sendMessage', data)
        return answer

    def send_link(self, phone, body, preview, title):
        data = {"phone": phone, "body": body, "previewBase64": preview, "title": title}
        answer = self.send_requests('sendLink', data)
        return answer

    def send_image(self, phone, body, filename, caption):
        data = {"phone": phone, "body": body, "filename": filename, "caption": caption}
        answer = self.send_requests('sendFile', data)
        return answer


#Envio de mensagem de texto
myphone = 5521980591606
body = "www.seufelix.com.br"
teste.send_message(myphone, body)

#Envio de imagem
myphone = 5521980591606
body_one = "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg"
filename = "teste.jpg"
caption = "Voilá"
print(teste.send_image(myphone, body_one, filename, caption))