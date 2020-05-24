#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Opção 1: Twilio


# In[ ]:


from twilio.rest import Client


# In[ ]:


client = Client()


# In[ ]:


from_whatsapp_number='whatsapp:+5511951280054'
to_whatsapp_number='whatsapp:+5521980591606'


# In[ ]:


client.messages.create(body='É só um test, meu irmão!!!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)


# In[ ]:


#--------------------------------------------------------------------------------


# In[ ]:


#Opção 2: Selenium


# In[ ]:


import json
import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options


# In[ ]:


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


# In[ ]:


#--------------------------------------------------------------------------------


# In[ ]:





# In[ ]:





# In[ ]:




