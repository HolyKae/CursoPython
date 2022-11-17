from selenium import webdriver
from selenium.webdriver.chrome.options import Options


browser = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


def OS():
    import utils
    utils.login()
    utils.filtrarOS()
    utils.excluirOS()


OS()
