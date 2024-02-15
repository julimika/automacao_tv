from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time
from config import (username, password)

#fluxo de login
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    Page = browser.new_page()
    time.sleep(5)
    Page.goto("https://prd-tv-react.watch.tv.br/login-screen")
    time.sleep(5)
    Page.get_by_role("textbox", name="Digite seu e-mail").fill(username)
    Page.get_by_role("textbox", name="Digite sua senha").fill(password)
    Page.get_by_role("button", name="Entrar").click()
    time.sleep(5)
    Page.locator('xpath=//*[@id="App"]/section/div/div[1]/div').dblclick()
    time.sleep(10)
    #validação dos carrosséis da home
    Page.get_by_title("Canais Ao vivo")
    print("Retornando ao vivo")
    Page.get_by_title("Lançamentos")
    print("Retornando lançamentos")
    Page.get_by_title("Paramount")
    print("Paramount retornando")
    Page.get_by_title("Mais assistidos")
    print("Mais assistidos retornando")
    Page.get_by_title("CNN")
    print("CNN Retornando")
    Page.get_by_title("Awesomeness")   
    print("Awesomeness retornando")
    Page.get_by_title("Infantil")   
    print("Infantil retornando")
    Page.get_by_title("Sugestões para Você")   
    print("Sugestões para Você retornando")
    Page.get_by_title("Minha Lista")
    print("Minha lista retornando")
    
    Page.get_by_alt_text("Ícone do menu Filmes").click()
    time.sleep(5)

    
    

    