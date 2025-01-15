import cv2
import time
import pyautogui as pg
from pyscreeze import ImageNotFoundException

class ImageLocator:
    def __init__(self, img_path, max_attempts=1, search_interval=1.5, duration=1.5, confidence=0.8):
        self.img_path = img_path
        self.max_attempts = max_attempts
        self.search_interval = search_interval
        self.confidence = confidence
        self.duration = duration
        self.attempts = 0

    def start_search(self):
        while True:
            try:
                # Receive the image to be searched
                template = cv2.imread(self.img_path)

                # Locate the element on the screen
                result = pg.locateAllOnScreen(template, confidence=self.confidence)

                # If the element found
                position = next(result, None)  # Get the next result or None if there are no more
                if position: # Get the corner position of the image
                    corner_x = position[0]
                    corner_y = position[1]
                    
                    pg.moveTo(corner_x, corner_y, self.duration)
                    pg.leftClick()
                    print("Localized element!")
                    print(f"Position: {position}")
                    break
            
            except ImageNotFoundException as e:
                print(f"Erro: {e}")
                print("Searching...")
 
            if self.attempts >= self.max_attempts:
                print(f"Element not found after {self.max_attempts + 1} search attempts!")
                break

            time.sleep(self.search_interval)
            self.attempts += 1