import cv2
import time
import pyautogui as pg
from pyscreeze import ImageNotFoundException

class ImageLocator:
    def __init__(self, img_path, max_attempts=1, search_interval=1, confidence=0.8):
        self.img_path = img_path
        self.max_attempts = max_attempts
        self.search_interval = search_interval
        self.confidence = confidence
        self.attempts = 0

    def start_search(self):
        while True:
            try:
                # Recebe a imagem a ser procurada
                template = cv2.imread(self.img_path)

                # Localiza o elemento na tela
                result = pg.locateAllOnScreen(template, confidence=self.confidence)

                # Se o elemento encontrado
                position = next(result, None)  # Obtém o próximo resultado ou None se não houver mais
                if position: # Obtém a posição do canto da imagem
                    corner_x = position[0]
                    corner_y = position[1]
                    
                    pg.moveTo(corner_x, corner_y, duration=1)
                    pg.leftClick()
                    print("Elemento localizado!")
                    print(f"Posição: {position}")
                    break
            
            except ImageNotFoundException as e:
                print(f"Erro: {e}")
                print("Buscando..")
 
            if self.attempts >= self.max_attempts:
                print(f"Elemento não encontrado após {self.max_attempts + 1} tentativas de busca!")
                break

            time.sleep(self.search_interval)
            self.attempts += 1