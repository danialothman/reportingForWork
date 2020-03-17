import pyautogui
import schedule
import time

#use pyautogui.position() to determine position of mouse cursor on display then enter the positions below
#(1042, 700) and (1332,695) is an example, replace them with your own postions

def job():
   pyautogui.click(1042, 700); #click on Whatsapp message typing space 
   pyautogui.typewrite('Hello, Dan here reporting for work'); 
   pyautogui.click(1332,695); #click send button

#job is scheduled to execute to run at 8:30AM everyday
schedule.every().day.at("08:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
