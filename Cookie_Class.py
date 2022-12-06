from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class BakeCookies:
    def __init__(self):
        self.my_service = Service("C:/Zoo_Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.my_service)
        self.driver.get("http://orteil.dashnet.org/experiments/cookie/")

    def get_baked_cookies(self):
        baked = self.driver.find_element(By.ID, "cps")
        my_bake = baked.text.split()[-1].strip()
        return my_bake

    def get_my_score(self):
        score = self.driver.find_element(By.ID, "money")
        my_score = score.text.strip()
        if "," in my_score:
            my_score = my_score.replace(",", "")
        return int(my_score)

    def get_grand_mother(self):
        grand_mother = self.driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
        grand_price = grand_mother.text.split()[-1].strip()
        return int(grand_price)

    def get_factory(self):
        factory = self.driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
        factory_price = factory.text.split()[-1].strip()
        return int(factory_price)

    def get_mine(self):
        mine = self.driver.find_element(By.CSS_SELECTOR, "#buyMine b")
        mine_price = mine.text.split()[-1].strip()
        if "," in mine_price:
            mine_price = mine_price.replace(",", "")
        return int(mine_price)

    def get_ship(self):
        ship = self.driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
        ship_price = ship.text.split()[-1].strip()
        if "," in ship_price:
            ship_price = ship_price.replace(",", "")
        return int(ship_price)

    # =============================== FUNCTIONALITY ========================== #
    def just_click(self, number):
        cookie_button = self.driver.find_element(By.ID, "cookie")
        for boom in range(number):
            cookie_button.click()

    def pause_app(self):
        sleep(5)

    def buy_grandmother(self):
        grand_mother_price = self.get_grand_mother()
        self.just_click(grand_mother_price + 20)
        grand_mother_button = self.driver.find_element(By.ID, "buyGrandma")
        grand_mother_button.click()
        self.pause_app()

    def buy_factory(self):
        factory_price = self.get_factory()
        self.just_click(factory_price + 5)
        factory_button = self.driver.find_element(By.ID, "buyFactory")
        factory_button.click()
        self.pause_app()

    def buy_mine(self):
        mine_price = self.get_mine()
        self.just_click(mine_price)
        mine_button = self.driver.find_element(By.ID, "buyMine")
        mine_button.click()
        self.pause_app()

    def buy_ship(self):
        ship_price = self.get_ship()
        self.just_click(ship_price - 1000)
        ship_button = self.driver.find_element(By.ID, "buyShipment")
        ship_button.click()
        self.pause_app()

    def buy_everything(self):
        self.buy_grandmother()
        self.buy_factory()
        self.buy_mine()
        self.buy_ship()
        sleep(10)
