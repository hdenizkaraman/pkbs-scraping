import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pyautogui

signature = """
___  ________    ______ _____ _   _ _____ 
|  \/  | ___ \   |  _  \  ___| \ | |  _  |
| .  . | |_/ /   | | | | |__ |  \| | | | |
| |\/| |    /    | | | |  __|| . ` | | | |
| |  | | |\ \ _  | |/ /| |___| |\  \ \/' /
\_|  |_|_| \_(_) |___/ \____/\_| \_/\_/\_

"""


class PalmeAutomation():
    def __init__(self, acc_role, acc_mail, acc_password, bookId, startpoint, endpoint):
        self.acc_role = acc_role
        self.acc_mail = acc_mail
        self.acc_password = acc_password
        self.bookid = bookId
        self.startpoint = startpoint
        self.endpoint = endpoint

        self.browser = webdriver.Chrome("chromedriver.exe")
    
    def startPalmeAcc(self):
        self.browser.get("https://kurumsalbasariseti.palmeyayinevi.com/ogrenci-giris")
        Select(self.browser.find_element(By.ID ,"ProvinceList")).select_by_visible_text("İSTANBUL")
        pyautogui.press("enter")
        time.sleep(1)
        Select(self.browser.find_element(By.ID ,"DistrictList")).select_by_visible_text("KARTAL")
        pyautogui.press("enter")
        time.sleep(1)
        Select(self.browser.find_element(By.ID ,"SchoolList")).select_by_visible_text("Fatin Rüştü Zorlu Anadolu Lisesi")
        pyautogui.press("enter")
        time.sleep(1)
        self.browser.find_element(By.ID, "StudentNumberOrEmail").send_keys(self.acc_mail)
        self.browser.find_element(By.ID, "Password").send_keys(self.acc_password)
        self.browser.find_element(By.XPATH, "//*[@id='form0']/div[2]/div[2]/div[3]/div[2]/button").click()
        return "ACCESS GRANTED"

    def findProduct(self):
        self.browser.get(f"https://kurumsalbasariseti.palmeyayinevi.com/MobileApp/BookPortal/BookDetails?bookId={self.bookid}")
        time.sleep(5)
        imageid = self.startpoint
        time.sleep(5)
        while imageid <= self.endpoint:
            print("in loop")
            scriptanchor = self.browser.find_element(By.ID, "test_"+str(imageid))
            self.browser.execute_script("arguments[0].click();", scriptanchor)
            time.sleep(2)
            try: 
		imageurl = self.browser.find_element(By.XPATH, '//*[@id="imageanswerbox"]/img').get_attribute("src")
            except: 
                teacherlook = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[3]/div/div/a[2]')
		self.browser.execute_script("arguments[0].click();", teacherlook)
                continue

            self.browser.execute_script(f'window.open("{imageurl}","_blank");')
            self.browser.switch_to.window(window_name=self.browser.window_handles[-1])

            pyautogui.hotkey("ctrl", "s")
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.hotkey("ctrl", "w")
            
            self.browser.switch_to.window(window_name=self.browser.window_handles[0])
            imageid += 1





print(signature, "\n"*4, "-"*50, "\nMagician: Deniz Karaman\n", "-"*50)
mail = str(input("\n>>>>Okul Numaranız: "))
passw = str(input("\n\n>>>>Şifreniz: "))
bookid = str(input("\n>>>>Kitap Numarası: "))
startpoint = int(input("\n>>>>Başlangıç Noktası: "))
endpoint = int(input("\n>>>>Bitiş Noktası: "))


me = PalmeAutomation(None, mail, passw, bookid, startpoint, endpoint)
me.startPalmeAcc()
me.findProduct()
