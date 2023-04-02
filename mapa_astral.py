from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import func_bot

def ver_mapa_astral():
    voltar = 1
    while voltar != 0:
        # Captar dados
        
        nome = str(input('Digite seu nome: \n'))

        dia_mes = func_bot.nascimento()
        dia = int(dia_mes[:2])
        mes = int(dia_mes[3:])
        ano = int(func_bot.ano_nascimento())

        hora_minuto = func_bot.hora_nascimento()
        hora = int(hora_minuto[0:2])
        minuto = int(hora_minuto[3:])
        cidade = str(input('Digite a cidade em que você nasceu:\n'))
        estado = str(input('Digite o estado em que você nasceu:\n'))
        
        '''
        nome = 'Caio'
        dia = 15
        mes = 2
        ano = 1996
        hora = 8
        minuto = 24
        cidade = 'Fortaleza'
        estado = 'Ceará'
        '''

        print('\n\nAguarde enquanto alinho seus dados com seus astros.\n\n')

        #options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        #driver = webdriver.Chrome(chrome_options=options)
        driver = webdriver.Chrome()




        # Acessar o site
        driver.get('https://astro.cafeastrology.com/natal.php')

        # Preencher o nome
        preencher_nome = driver.find_element(By.XPATH,
                                    '/html/body/div[3]/div/div[2]/form/div/div[1]/input[5]').send_keys(nome)

        # Preencher gênero
        sem_genero = driver.find_element(By.XPATH,
                                    '/html/body/div[3]/div/div[2]/form/div/div[1]/input[8]').click()

        # Preencher a data de nascimento
        dia_nascimento = driver.find_element(By.XPATH,
                                        '/html/body/div[3]/div/div[2]/form/div/div[1]/select[2]')
        for x in range(dia - 1):
            dia_nascimento.send_keys(Keys.DOWN)

        mes_nascimento = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div/div[2]/form/div/div[1]/select[1]')
        for x in range(mes - 1):
            mes_nascimento.send_keys(Keys.DOWN)

        ano_nascimento = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div/div[2]/form/div/div[1]/select[3]')
        if ano > 2000:
            for x in range(ano - 2000):
                ano_nascimento.send_keys(Keys.DOWN)
        elif ano < 2000:
            for x in range(2000 - ano):
                ano_nascimento.send_keys(Keys.UP)
        elif ano == 2000:
            ano_nascimento.send_keys(ano)


        # Preencher a hora de nascimento
        preencher_hora = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div/div[2]/form/div/div[1]/select[4]')
        if hora > 12:
            for x in range(hora - 12):
                preencher_hora.send_keys(Keys.DOWN)
        elif hora < 12:
            for x in range(12 - hora):
                preencher_hora.send_keys(Keys.UP)
        elif hora == 12:
            preencher_hora.send_keys(hora)

        preencher_minutos = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div/div[2]/form/div/div[1]/select[5]')
        for x in range(minuto):
            preencher_minutos.send_keys(Keys.DOWN)

        # Preencher a Cidade de Nascimento

        preencher_cidade = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div/div[2]/form/div/div[1]/div/div[1]/input').send_keys(cidade)

        preencher_estado = driver.find_element(By.XPATH,
                                            '/html/body/div[3]/div/div[2]/form/div/div[1]/div/div[1]/select')
        driver.implicitly_wait(10)
        preencher_estado.send_keys(cidade + ", " + estado)

        # Preencher idioma
        #preencher_idioma = driver.find_element(By.XPATH,
        #                                    '/html/body/div[3]/div/div[2]/table/tbody/tr/td/form/table/tbody/tr[5]/td/select')
        #for x in range(14):
        #    preencher_idioma.send_keys(Keys.DOWN)


        # Clicar no botão
        Submit = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/div/div[2]/input')
        Submit.click()


        mapa = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[3]').text

        ascendente = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/h6[11]').text

        sol = mapa[(mapa.find('Sun ')):(mapa.find('Moon'))]
        lua = mapa[(mapa.find('Moon ')):]
        #.replace('Mercurio', 'Mercúrio').replace('Venus', 'Vênus').replace('Nodo N', 'Nodo Lunar Norte')


        print(sol, end='')
        print(ascendente)
        print(lua)

        while True:
            outro = int(input('\n[1] Verificar outro mapa.\n'
                '[0] Retornar ao menu\n'))
            if outro == 1:
                print('')
                break
            elif outro == 0:
                print('')
                voltar = 0
                pass
            break