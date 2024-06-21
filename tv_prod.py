from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
import time
from config import (username, password)

#fluxo de login
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    Page = browser.new_page();

    Page.goto("https://prd-tv-react.watch.tv.br")
    Page.get_by_role("button", name="Entrar").click()
    time.sleep(5)
    Page.get_by_role("button", name="Login por email e senha").click()
    Page.get_by_role("textbox", name="Digite seu email").fill(username)
    Page.get_by_role("textbox", name="Digite sua senha").fill(password)
    # Page.set_viewport_size({"width": 1920, "height": 1080})
    Page.get_by_role("button", name="Entrar").click()
    time.sleep(5)
    Page.locator('xpath=//*[@id="App"]/section/div/div[1]/div').dblclick()
    time.sleep(10)

    #validação carrosséis da home
    def check_visibility(Page, carousels):
        visibility = {}
        for carousel in carousels:
            element = Page.query_selector(f"text={carousel}")
            visibility[carousel] = element is not None and element.is_visible() if element else False
        return visibility

    carousels = [
        "Canais Ao vivo",
        "Continuar assistindo",
        "Lançamentos",
        "Paramount",
        "Mais assistidos",
        "Para maratonar",
        "CNN",
        "Tramas emocionantes",
        "Infantil", 
        "SUgestões para Você",
        "Minha Lista"
    ] 

    visibility_status = check_visibility(Page, carousels)

    for carousel, is_visible in visibility_status.items():
        print(f"Carrossel '{carousel}' está retornando?: {is_visible}")   

  


    time.sleep(5)

    
    

    