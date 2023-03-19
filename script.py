import pandas as pd
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

usuario = "YourUsername"
senha = "YourPassword"

#for Firefox users 
from webdriver_manager.firefox import GeckoDriverManager
browser= webdriver.Firefox(executable_path=GeckoDriverManager().install())

def login():
    browser.get("https://twitter.com/i/flow/login")
    time.sleep(3)
    browser.find_element("xpath","//input[@name='text']").click()
    time.sleep(0.1)
    browser.find_element("xpath","//input[@name='text']").send_keys(usuario)
    time.sleep(0.1)
    browser.find_element("xpath","(//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0'])[3]").click()
    time.sleep(2)
    browser.find_element("xpath","//input[@name='password']").send_keys(senha)
    time.sleep(0.1)
    browser.find_element("xpath","(//div[@class='css-901oao r-1awozwy r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0'])[3]").click()
login()
users=[]
i=0
time.sleep(3)
browser.get("https://twitter.com/VivianneMiedema/followers")

last_height = browser.execute_script("return document.body.scrollHeight")

session_id = browser.session_id

# Loop até que o tamanho da janela não mude mais
while True:
    # Descer o scroll
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Aguardar o conteúdo carregar
    time.sleep(2)

    html=browser.page_source
    soup=BeautifulSoup(html)
    usernames=soup.find_all('a',class_="css-4rbku5 css-18t94o4 css-1dbjc4n r-1loqt21 r-1wbh5a2 r-dnmrzs r-1ny4l3l")

    for j in usernames:
        users.append(j.text)
    
    # Verificar o tamanho da janela
    new_height = browser.execute_script("return document.body.scrollHeight")

    # Se o tamanho da janela não mudou, significa que não há mais conteúdo para ser carregado
    if new_height == last_height:
        checagem = input("continuar ou parar?")
        if checagem == "continuar":
            checagem = 0
        if checagem == "parar":
            break
            
    # Atualizar o tamanho da janela
    last_height = new_height

df=pd.DataFrame(users,columns=["Users"])
df=df.drop_duplicates()
df.to_excel("output2.xlsx")  

