# Antud koodi eesmärk on aotumaattestida Google-i otsingumootorit Seleniumi abil.
# Testimiseks minnakse lehele 'https://google.com' ning otsinguribale sisestatakse 'neti.ee'.
# Otsing käivitatakse ning avatakse esimene otsingu tulemus.
# Kui tulemuse pealkiri vastab 'neti.ee' pealehe pealkirjale ning väljastatakse 'JUHHHUUUUUU', võib testitulemust lugeda õnnestunuks.

# Vajalikke teekide importimine
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Testimiseks kasutatakse Google Chrome brauserit
browser = webdriver.Chrome()

# Kood 'proovib' jooksutada järgmist koodilõiku 
try:
    # Brauseri aken avatakse ning minnakse lehele 'https://google.com'
    browser.get('https://www.google.com')
    # Väljastatakse Lehe pealkiri
    print(f'Title: {browser.title}')
    
    # Paus, et leht laadida jõuaks
    time.sleep(1)
    
    # Otsitakse kõpsistega nõustumise nupp ja vajutatakse seda
    cookies = browser.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
    cookies.click()
    
    # Otsitakse Google-i otsinguväli ja sisestatakse 'neti.ee'
    search = browser.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search.send_keys('neti.ee')
    
    # Otsitakse üles nupp, et käivitada otsing, ja vajutatakse seda
    button = browser.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    button.click()
    
    # Paus, et leht laadida jõuaks
    time.sleep(1)
    
    # Avatakse esimene otsingutulemus
    element = browser.find_element (By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
    element.click()
    
    # Väljastatakse Lehe pealkiri
    print(f'Title: {browser.title}')
    
    # Kui lehe pealkirjaks on 'NETI - Eesti Interneti Kataloog ja Otsingusüsteem', väljastatakse 'JUHHHUUUUUU'
    if browser.title == 'NETI - Eesti Interneti Kataloog ja Otsingusüsteem':
        print('JUHHHUUUUUU')

# Kui tekib mingi tõrge, väljastatakse 'Error'
except:
    print('Error')

# Peale 10 sekundit suletakse brauseri aken
time.sleep(10)
browser.quit()