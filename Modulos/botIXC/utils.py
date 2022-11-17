from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

browser = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def login():
    browser.get('https://ixc.sistemarbtelecom.net.br/login.php')
    browser.maximize_window()
    assert 'Login IXCsoft' in browser.title
    email = browser.find_element("xpath", "//input[contains(@type, 'email')]")
    senha = browser.find_element("xpath", "//input[contains(@type, 'password')]")
    entrar = browser.find_element("xpath", "//button[contains(@id, 'entrar')]")
    email.send_keys('rodrigo@rbtelecom.net.br' + Keys.RETURN)
    senha.send_keys('Rodrigo2022' + Keys.RETURN)
    entrar.click()
    time.sleep(5)


def filtrarOS():
    browser.find_element("xpath", "//div[contains(@id, 'menu76420e3e2ec10bca79d6bfcc6356354c')]").click()
    time.sleep(1)
    browser.find_element("xpath", "//a[contains(@rel, 'su_oss_chamado')]").click()
    time.sleep(2)
    browser.find_element("xpath", "//input[contains(@id, 'tipo_dE')]").click()
    time.sleep(1)
    d1 = browser.find_element("xpath", "//input[contains(@type, 'text') and contains(@id, 'data1')]")
    d1.click()
    d1.click()
    time.sleep(0.5)
    d1.send_keys('01/01/2022' + Keys.RETURN)
    time.sleep(2)
    d2 = browser.find_element("xpath", "//input[contains(@type, 'text') and contains(@id, 'data2')]")
    d2.click()
    d2.click()
    time.sleep(0.5)
    d2.send_keys('31/07/2022' + Keys.RETURN)
    time.sleep(2)
    browser.find_element("xpath", "//input[@value = 'OK']").click()
    time.sleep(2)


def excluirOS():
    while True:
        browser.find_element("xpath", "//span[.='Ações']").click()
        browser.find_element("xpath", "//li[.='Finalizar']").click()
        time.sleep(2)
        msg = browser.find_element("xpath", "//textarea[@id = 'mensagem']")
        msg.click()
        msg.send_keys('Backlog da importação')
        id = browser.find_element("xpath", "//input[@name = 'id_tecnico']")
        id.click()
        id.send_keys('37')
        msg.click()
        time.sleep(1)
        browser.find_element("xpath", "//button[.='Salvar']").click()
        time.sleep(3)

