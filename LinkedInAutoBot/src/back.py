import os
import time
import webbrowser as web
import pyautogui as pg
from modules.image_search import ImageLocator

def AutoBot(bot_name, search, time_click, connect, pages):
    print(f"🤖 {bot_name}, ligado e operando...")

    try:
        url = 'https://www.linkedin.com/'
        web.open(url)
        pg.sleep(time_click)
        pg.hotkey('ctrl', '0')
        pg.sleep(time_click)
        pg.hotkey("f11")

        # Locate and interact with the search field
        image_path = os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'search.png')
        home_position = pg.locateCenterOnScreen(image_path, confidence=0.8)
        if home_position:
            pg.moveTo(home_position, duration=1)
            pg.leftClick()
            pg.write(f"{search}\n", interval=0.1)
            time.sleep(2.5)

        # Navigation and connections
        for p in range(1, pages + 1):
            pg.sleep(time_click)
            for c in range(1, connect + 1):
                locator_connect = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'connect.png'))
                locator_connect.start_search()

                locator_send = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'send.png'))
                locator_send.start_search()
                print(f"Conexão {c}")

            pg.scroll(-500)
            print(f"Página {p}")

    except Exception as e:
        print(f"😤 O programa encontrou um erro: {e}")
    finally:
        time.sleep(1)
        pg.hotkey('f11')
        pg.hotkey('ctrl', '0')
        print('🎉 Automação finalizada!')