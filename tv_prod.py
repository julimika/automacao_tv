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
    
    # time.sleep(5)
    # # page.getByLabel('profile-name').click('Mika PROD')
    # # time.sleep(5)
    # Page.get_by_role("p", name="Mika PROD").click()
