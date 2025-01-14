import os
import time
import webbrowser as web
import pyautogui as pg

from modules.image_search import ImageLocator
from modules.GUI_elements import bot_name, InputSearch, time_slider, connects_slider, pages_slider

def AutoBot(e):
    print(f"🤖 {str(bot_name.value)}, ligado e operando...")
    print(f"Setup Bot: Search={str(InputSearch.value)}, time={int(time_slider.value)}, connects={int(connects_slider.value)}, pages={int(pages_slider.value)}")
    try:
        pg.hotkey('win', 'd')
        pg.sleep(1.5)
        url = 'https://www.linkedin.com/'
        web.open(url)
        time.sleep(int(time_slider.value))
        pg.hotkey('ctrl', '0')
        pg.hotkey("f11")

        # Locate and interact with the search field
        image_path = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'search.png'))
        if image_path:
            image_path.start_search()
            pg.write(f"{str(InputSearch.value)}\n", interval=0.1)
            time.sleep(int(time_slider.value))

        # Locate people
        locator_people = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'people.png'))
        if locator_people:
            locator_people.start_search()
            time.sleep(int(time_slider.value))

        # Navigation and connections
        for p in range(int(pages_slider.value)):
            for c in range(1, int(connects_slider.value) + 1):
                locator_connect = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'connect.png'))
                locator_connect.start_search()

                locator_without = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'without note.png'))
                locator_without.start_search()

                locator_send = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'send.png'))
                locator_send.start_search()
                print(f"Connection: {c}")

            pg.scroll(-500)
            locator_next = ImageLocator(os.path.join('LinkedInAutoBot', 'src', 'assets', 'screen_elements', 'next.png'))
            locator_next.start_search()
            print(f"Page: {p}")

    except Exception as e:
        print(f"😤 The program encountered an error: {e}")
    finally:
        time.sleep(int(time_slider.value))
        pg.hotkey('f11')
        pg.hotkey('ctrl', '0')
        pg.hotkey('ctrl', 'w')
        print('🎉 Automation completed!')