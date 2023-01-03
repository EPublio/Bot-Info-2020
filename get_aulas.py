from selenium import webdriver
from time import sleep
import login

def get_aulas():
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

    def fxpath(string):
        macaco = nav.find_element_by_xpath(string)
        return macaco
    def fname(string):
        macaco = nav.find_element_by_name(string)
        return macaco
    
    nav.get(login.link_calendario)
    fxpath('//*[@id="identifierId"]').send_keys(login.email)
    fxpath('//*[@id="identifierNext"]/div/button/span').click()
    sleep(2)
    fname('password').send_keys(login.senha)
    fxpath('//*[@id="passwordNext"]/div/button/span').click()
    sleep(3)

    aulas_nomes = []
    #funcional YvjgZe
    aulas = nav.find_elements_by_class_name('YvjgZe')
    for elmnt in range(len(aulas)):
        aulas_nomes.append(aulas[elmnt].text)
    sleep(1)
    nav.quit()

    #FORMATAÇÃO

    a = aulas_nomes
    dias_semana = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sábado"]
    com_aula = []
    for x in range(len(a)):
        def filtrar(strings):
            dia = str(strings)
            dia = dia.replace("\n",", ")
            dia = dia.strip()
            dia = dia.split(", ")
            return dia
        
        dia = filtrar(a[x])
        len_dia = len(filtrar(dia))
 
        if len_dia == 3:
            inside = []
            inside.append(f"{dias_semana[x]} - {dia[2]}")
            inside.append("Nenhuma aula")
        else:
            inside = []
            i = 0
            n = 4
            num_aulas_dia = filtrar(a[x][0:1]) 
            nad = int(num_aulas_dia[0])
            inside.append(f"{dia[1].title()} - {dia[2]}")
            while i < nad:
                inside.append(f"{dia[n]} - {dia[n-1]}")
                i = i + 1
                n = n + 8
        com_aula.append(inside)
    print("aulas recarregadas.")
    return com_aula


