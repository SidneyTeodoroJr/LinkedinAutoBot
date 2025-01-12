import os
import time
import webbrowser as web
import pyautogui as pg

from modules.image_search import *

def AutoBot(e, pages, connect, search):
    name_bot=str(input('Digite um nome para o bot'))
    search= str(input('Qual o termo de pesquisa? '))

    Time= int(input("Time click"))
    connect= int(input('Quantas conexões deseja fazer? '))
    pages=int(input('Quantas páginas deseja percorrer? '))

    print(f'🤖 {name_bot}, ligado e operando...')

    try:
        url = 'https://www.linkedin.com/'
        web.open(url)
        pg.sleep(Time) # 5
        pg.hotkey('ctrl', '0')
        pg.sleep(Time) # 1.5
        pg.hotkey("f11")

        # search
        image_path = os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'search.png')
        home_position = pg.locateCenterOnScreen(image_path, confidence=0.8)
        if home_position:
            pg.moveTo(home_position, duration=1)
            pg.leftClick()
            pg.write(f"{search} \n", interval=0.1)
            time.sleep(2.5)

        # navigation
        locator_people = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'people.png'))
        locator_people.start_search()
        pg.sleep(Time) # 2.5

        for p in range(1, pages):
            pg.sleep(Time) # 1.5
            for c in range(1, connect):
                locator_connect = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'connect.png'))
                locator_connect.start_search()

                locator_send = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'send.png'))
                locator_send.start_search()
                print(f"Conexão {c}")

            pg.scroll(-500)

            pg.sleep(Time) # 1.5
            locator_next = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'next.png'))
            locator_next.start_search()

            print(f"Pagina {p}")

    except Exception:
        print('😤 O programa encontrou um erro, tente novamente!')
    finally:
        time.sleep(2.5)
        pg.hotkey('f11')
        pg.hotkey('ctrl', '0')
        print('🎉 Automação finalizada!')