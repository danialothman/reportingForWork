import pyautogui
import schedule
import time

def job():
   pyautogui.click(1042, 700); #click on typing space 
   pyautogui.typewrite('Hello, Dan here reporting for work'); 
   pyautogui.click(1332,695); #click send button

schedule.every().day.at("08:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
