from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'

browser = Firefox()

browser.get('https://curso-python-selenium.netlify.app/exercicio_02.html')
sleep(5)


verification = True

while verification:

    browser.find_element(By.ID, 'ancora').click()

    ps = browser.find_elements(By.TAG_NAME, 'p')

    num = ps[1].text

    num_esperado = num[17:]

    for p in ps:

        if p.text == f'Você ganhou: {num_esperado}':
            print('VOCÊ VENCEU')

            verification = False

            break