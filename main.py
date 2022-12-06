from tkinter import *
from PIL import Image, ImageTk
from Cookie_Class import BakeCookies

LB_FONT = ("Helvetica", 14, "bold")
AN_FONT = ("Helvetica", 15, "normal")


class CookieBot:
    def __init__(self, window):
        self.window = window
        self.window.title("Cookie Bot")
        self.window.geometry("330x580")
        self.window.configure(bg="gainsboro")

        bot_image = Image.open("IMG/bot.jpg")
        bot_photo = ImageTk.PhotoImage(bot_image)
        self.bot_label = Label(self.window, image=bot_photo)
        self.bot_label.image = bot_photo
        self.bot_label.place(x=5, y=5, width=320, height=180)

        # ========================= CENTRAL FRAME ========================= #
        self.central_frame = Frame(self.window, bd=1, highlightthickness=1, relief=RIDGE, bg="gainsboro")
        self.central_frame.place(x=5, y=195, width=320, height=370)

        self.final_score = Label(self.central_frame, text="", font=("Helvetica", 13, "normal"), justify="center", bd=1,
                                 highlightthickness=1, relief=RIDGE, wraplength=280, bg="gainsboro")
        self.final_score.place(x=5, y=5, width=305, height=80)

        self.info = Label(self.central_frame, text="Choose Item, You want to Buy During Playing!", font=AN_FONT,
                          justify="center", bd=1, highlightthickness=1, relief=RIDGE, wraplength=280)
        self.info.place(x=5, y=90, width=305, height=60)

        grand_image = Image.open("IMG/grand.jpg")
        grand_photo = ImageTk.PhotoImage(grand_image)
        self.grand_monther = Button(self.central_frame, image=grand_photo, bd=1, highlightthickness=1, relief=RIDGE,
                                    command=self.grandma_method)
        self.grand_monther.image = grand_photo
        self.grand_monther.place(x=5, y=155, width=70, height=70)

        fact_image = Image.open("IMG/factory.jpg")
        fact_photo = ImageTk.PhotoImage(fact_image)
        self.factory = Button(self.central_frame, image=fact_photo, bd=1, highlightthickness=1, relief=RIDGE,
                              command=self.factory_method)
        self.factory.image = fact_photo
        self.factory.place(x=83, y=155, width=70, height=70)

        mine_image = Image.open("IMG/mine.jpg")
        mine_photo = ImageTk.PhotoImage(mine_image)
        self.mine = Button(self.central_frame, image=mine_photo, bd=1, highlightthickness=1, relief=RIDGE,
                           command=self.mine_method)
        self.mine.image = mine_photo
        self.mine.place(x=162, y=155, width=70, height=70)

        ship_image = Image.open("IMG/ship.jpg")
        ship_photo = ImageTk.PhotoImage(ship_image)
        self.ship = Button(self.central_frame, image=ship_photo, bd=1, highlightthickness=1, relief=RIDGE,
                           command=self.shipment_method)
        self.ship.image = ship_photo
        self.ship.place(x=240, y=155, width=70, height=70)

        self.all = Button(self.central_frame, text="Everything", font=LB_FONT, justify="center", bd=1,
                          highlightthickness=1, relief=RIDGE, wraplength=280, bg="powder blue", fg="dark slate gray",
                          command=self.everything_method)
        self.all.place(x=5, y=230, width=305, height=40)

        self.chosen = Label(self.central_frame, text="", font=AN_FONT, bg="gainsboro", fg="maroon",
                            justify="center", bd=1, highlightthickness=1, relief=RIDGE, wraplength=280)
        self.chosen.place(x=5, y=275, width=305, height=50)

        self.play = Button(self.central_frame, text="Play", font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                           bg="navy", fg="light cyan", command=self.play_method)
        self.play.place(x=5, y=330, width=95, height=30)

        self.clean = Button(self.central_frame, text="Clean", font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                            bg="pale green", command=self.refresh_method)
        self.clean.place(x=107, y=330, width=100, height=30)

        self.close = Button(self.central_frame, text="Exit", font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                            bg="sandy brown", command=self.close_method)
        self.close.place(x=214, y=330, width=95, height=30)

    # =============================== FUNCTIONALITY =================================== #
    def close_method(self):
        self.window.destroy()

    def grandma_method(self):
        self.chosen.config(text="I want GrandMother")

    def factory_method(self):
        self.chosen.config(text="I want Factory")

    def mine_method(self):
        self.chosen.config(text="I want Mine")

    def shipment_method(self):
        self.chosen.config(text="I want Shipment")

    def everything_method(self):
        self.chosen.config(text="I want Everything")

    def refresh_method(self):
        self.final_score.config(text="", bg="gainsboro")
        self.chosen.config(text="", bg="gainsboro")

    def play_method(self):
        if len(self.chosen.cget("text")) > 0:
            bot_tool = BakeCookies()
            if self.chosen.cget("text") == "I want GrandMother":
                bot_tool.buy_grandmother()
                cookies = bot_tool.get_baked_cookies()
                scores = bot_tool.get_my_score()
                self.final_score.config(text=f"Result: {cookies} cookies, {scores} points and \nGrandMother",
                                        bg="pale green")

            elif self.chosen.cget("text") == "I want Factory":
                bot_tool.buy_factory()
                cookies = bot_tool.get_baked_cookies()
                scores = bot_tool.get_my_score()
                self.final_score.config(text=f"Result: {cookies} cookies, {scores} points and \nFactory",
                                        bg="pale green")

            elif self.chosen.cget("text") == "I want Mine":
                bot_tool.buy_mine()
                cookies = bot_tool.get_baked_cookies()
                scores = bot_tool.get_my_score()
                self.final_score.config(text=f"Result: {cookies} cookies, {scores} points and \nMine",
                                        bg="pale green")
            elif self.chosen.cget("text") == "I want Shipment":
                bot_tool.buy_ship()
                cookies = bot_tool.get_baked_cookies()
                scores = bot_tool.get_my_score()
                self.final_score.config(text=f"Result: {cookies} cookies, {scores} points and \nShipment",
                                        bg="pale green")

            elif self.chosen.cget("text") == "I want Everything":
                bot_tool.buy_everything()
                cookies = bot_tool.get_baked_cookies()
                scores = bot_tool.get_my_score()
                self.final_score.config(text=f"Result: {cookies} cookies, {scores} points \nGrandMother, Factory, Mine "
                                             f"and Shipment",
                                        bg="pale green")
        else:
            pass


def launch_app():
    app = Tk()
    CookieBot(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
