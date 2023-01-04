from selenium import webdriver
from time import sleep
import login 


def get_tarefas():
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    nav = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
    # nav = webdriver.Chrome()

    def fxpath(string):
        macaco = nav.find_element_by_xpath(string)
        return macaco
    def fname(string):
        macaco = nav.find_element_by_name(string)
        return macaco
    def fclass(string):
        macaco = nav.find_element_by_class_name(string)
        return macaco

    link = "https://sigaa.ifsc.edu.br/sigaa/public/home.jsf"
    nav.get(link)
    fxpath('//*[@id="acesso"]/ul/li[2]/a').click()
    sleep(1)
    fname('user.login').send_keys('login.login')
    fname('user.senha').send_keys(login.senha)
    fxpath('//*[@id="conteudo"]/div[3]/form/table/tfoot/tr/td/input').click()
    sleep(1)
    nav.refresh()
    sleep(1)

    xd = nav.find_elements_by_xpath('//*[@id="avaliacao-portal"]/table/tbody')

    aaa = []
    tarefas = []
    for x in xd: 
        aaa.append(x.text)
    aaa = aaa[0].split("\n")

    i = 0
    while i < len(aaa):
        hora = aaa[i]
        conteudo = aaa[i+1]
        msg = str(hora)+" - "+ str(conteudo)
        tarefas.append(msg)
        i = i + 2
    print("tarefas recarregadas.")
    return tarefas

