# It is a single-deck Blackjack game, one player versus computer, without split option

# Import modules
import tkinter as tk
import random

class MainApplication(tk.Tk):
    """Main class of Blackjack Game. 
    Consist bottom frame, bet frame and game frame. App window geometry.
    """
    def __init__(self):
        super().__init__()

        # Adjusting the window
        width_of_window = 1012
        height_of_window = 609
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width_of_window / 2))
        y_coordinate = int((screen_height / 2) - (height_of_window / 2) - 30)
        self.geometry(
            f"{width_of_window}x{height_of_window}+{x_coordinate}+{y_coordinate}"
        )
        self.resizable(width=False, height=False)  # Resizable of a window
        
        self.title("Blackjack")  # Title of an application

        self.withdraw()  # Hidding a window (Firstly only Toplevel apperas)
        self.new_window()  # Opening new window (FirstWindow as a TopLevel)

        # Game play variables
        self.bet_value = tk.IntVar()
        self.info_msg = tk.StringVar()
        self.bets = tk.IntVar()
        self.wins = tk.IntVar()
        self.losses = tk.IntVar()

        # Open bet and bottom frames
        self.make_bet_frame()
        self.make_bottom_frame()

    # Making a bottom frame
    def make_bottom_frame(self):
        self.bottom_frame = tk.Frame(self, bg="#1c2941", height=55, width=1012)
        self.bottom_frame.pack(side='bottom')

        self.botton_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/bottom_img.png"
        )
        self.bottom_img_label = tk.Label(self.bottom_frame, image=self.botton_img, bg="#1c2941")
        self.bottom_img_label.pack(fill="both", expand=1)

        #Coins image next to balance
        self.coin_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/coin.png"
        )
        self.coin_label = tk.Label(self.bottom_frame, image=self.coin_img)
        self.coin_label.place(x=865, y=6)
        self.coin_label.config(bg="#283753")

        # Player balance value, imported from First Window (typed by player)
        self.player_balance_value_label = tk.Label(self.bottom_frame, textvariable=self.first_window.player_balance, font=("Titillium Web", 12))
        self.player_balance_value_label.config(fg="white", bg="#283753")
        self.player_balance_value_label.place(x=905, y=13)

        # Player name label, imported from First Window
        self.player_name_value_label = tk.Label(self.bottom_frame, textvariable=self.first_window.player_name, font=("Titillium Web", 12), width=22)
        self.player_name_value_label.config(fg="white", bg="#1c2941", anchor="center")
        self.player_name_value_label.place(x=240, y=13)

        # Information Label message next to player name
        self.info_msg_label = tk.Label(self.bottom_frame, textvariable=self.info_msg, font=("Titillium Web", 12), width=32)
        self.info_msg_label.config(bg="#1c2941", fg="white", anchor="center")
        self.info_msg_label.place(x=470, y=13)
        self.info_msg.set("Please make a bet.")

        # Stats button
        self.stats_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/stats_bttn.png")
        self.stats_bttn = tk.Button(self.bottom_frame, command=self.stats)
        self.stats_bttn.config(
            image=self.stats_img,
            borderwidth=-10,
            bg="#283753",
            activebackground="#283753",
        )
        self.stats_bttn.place(x=40, y=10)

        # quit button
        self.quit_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/quit_bttn.png")
        self.quit_bttn = tk.Button(self.bottom_frame, command=lambda : [self.destroy()])
        self.quit_bttn.config(
            image=self.quit_img,
            borderwidth=-10,
            bg="#283753",
            activebackground="#283753",
        )
        self.quit_bttn.place(x=125, y=10)

    # Stats method show message with numer of bts, wins and losses
    def stats(self):
        self.info_msg.set("Bets: {}  |  Wins: {}  |  Losses: {}  ".format(self.bets.get(), self.wins.get(), self.losses.get()))
        self.info_msg_label.after(2000, lambda : [self.info_msg.set("")])

    # Making a bet frame method
    def make_bet_frame(self):
        self.bet_frame = tk.Frame(self, bg="#1c2941", width=1012, height=554)
        self.bet_frame.pack()

        self.background_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/game_background_img.png"
        )
        self.back_ground_img_label = tk.Label(self.bet_frame, image=self.background_img, bg="#1c2941")
        self.back_ground_img_label.pack(fill="both", expand=1)

        # Bet value Label and variable
        self.bet_value_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/bet_value_img.png")
        bet_value_label_bg = tk.Label(self.bet_frame)
        bet_value_label_bg.config(image=self.bet_value_img, bg="#1c2941", borderwidth=-5)
        bet_value_label_bg.place(x=462, y=300)

        bet_value_label = tk.Label(self.bet_frame, textvariable=self.bet_value, font=("Titillium Web", 12), width=5)
        bet_value_label.config(fg="white", bg="#1c2941", anchor="center")
        bet_value_label.place(x=478, y=310)

        # Chips coins buttons
        self.coin_button_1_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/1.png")
        self.coin_button_1 = tk.Button(self.bet_frame, command=lambda : [self.bet_value.set(self.bet_value.get()+1), self.check_bet_val()])
        self.coin_button_1.config(
            image=self.coin_button_1_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.coin_button_1.place(x=233, y=435)

        self.coin_button_5_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/5.png")
        coin_button_5 = tk.Button(self.bet_frame, command=lambda : [self.bet_value.set(self.bet_value.get()+5), self.check_bet_val()])
        coin_button_5.config(
            image=self.coin_button_5_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        coin_button_5.place(x=344, y=435)

        self.coin_button_10_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/10.png")
        coin_button_10 = tk.Button(self.bet_frame, command=lambda : [self.bet_value.set(self.bet_value.get()+10), self.check_bet_val()])
        coin_button_10.config(
            image=self.coin_button_10_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        coin_button_10.place(x=455, y=435)

        self.coin_button_25_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/25.png")
        coin_button_25 = tk.Button(self.bet_frame, command=lambda : [self.bet_value.set(self.bet_value.get()+25), self.check_bet_val()])
        coin_button_25.config(
            image=self.coin_button_25_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        coin_button_25.place(x=565, y=435)

        self.coin_button_100_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/100.png")
        coin_button_100 = tk.Button(self.bet_frame, command=lambda : [self.bet_value.set(self.bet_value.get()+100), self.check_bet_val()])
        coin_button_100.config(
            image=self.coin_button_100_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        coin_button_100.place(x=676, y=435)

        # Deal, Clear bet, Bet 2x buttons
        self.clear_bet_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/clear_bet_img.png")
        clear_bet_bttn = tk.Button(self.bet_frame, command=self.clear_bet)
        clear_bet_bttn.config(
            image=self.clear_bet_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        clear_bet_bttn.place(x=302, y=375)

        self.deal_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/deal_img.png")
        deal_bttn = tk.Button(self.bet_frame, command=self.deal)
        deal_bttn.config(
            image=self.deal_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        deal_bttn.place(x=442, y=375)

        self.bet2x_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/bet2x_img.png")
        bet2x_bttn = tk.Button(self.bet_frame, command=self.bet_2x)
        bet2x_bttn.config(
            image=self.bet2x_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        bet2x_bttn.place(x=582, y=375)

    # Clearing bet value
    def clear_bet(self):
        self.bet_value.set(0)
        self.info_msg.set("Please make a bet.")

    # Multiplying bet by 2
    def bet_2x(self):
        self.bet_value.set(self.bet_value.get()*2)
        self.check_bet_val()

    # Checking bet value, player cannot bet more than 5000$ or its balance
    def check_bet_val(self):
        if self.bet_value.get() > 5000:
            self.bet_value.set(5000)
            self.info_msg.set("You cannot bet more than 5000 $!")

        elif self.bet_value.get() > self.first_window.player_balance.get():
            self.bet_value.set(self.first_window.player_balance.get())
            self.info_msg.set("You cannot bet more than yours balance!")

    # Making a deal 
    def deal(self):
        if self.bet_value.get() > 0:
            self.bets.set(int(self.bets.get()+1))
            self.bet_frame.destroy() # Closing bet frame
            self.bottom_frame.destroy() # Closing bottom frame
            self.make_game_frame() # Opening game frame
            self.first_window.player_balance.set(self.first_window.player_balance.get()-self.bet_value.get()) # Reducing balance by bet value
        else:
            self.info_msg.set("Please make a bet.")

    # Making a game frame
    def make_game_frame(self):
        self.game_frame = tk.Frame(self, bg="#1c2941", width=1012, height=554)
        self.game_frame.pack()

        self.game_background_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/game_background_img.png"
        )
        self.game_back_ground_img_label = tk.Label(self.game_frame, image=self.game_background_img, bg="#1c2941")
        self.game_back_ground_img_label.pack(fill="both", expand=1)

        self.make_bottom_frame() # Opening game frame (Getting right poistioning of frames)
        self.info_msg.set("")

        # Player decision buttons
        self.hit_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/hit_img.png")
        self.hit_bttn = tk.Button(self.game_frame, command=self.hit)
        self.hit_bttn.config(
            image=self.hit_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.hit_bttn.place(x=303, y=480)

        self.stand_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/stand_img.png")
        self.stand_bttn = tk.Button(self.game_frame, command=self.computer_move)
        self.stand_bttn.config(
            image=self.stand_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.stand_bttn.place(x=441, y=480)

        self.double_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/double_img.png")
        self.double_bttn = tk.Button(self.game_frame, command=self.double)
        self.double_bttn.config(
            image=self.double_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.double_bttn.place(x=579, y=480)
    
        # Cards imgages
        #Aces
        self.ace_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ace_spade_img.png"
        )
        self.ace_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ace_heart_img.png"
        )
        self.ace_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ace_club_img.png"
        )
        self.ace_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ace_diamond_img.png"
        )
        #Kings
        self.king_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/king_spade_img.png"
        )
        self.king_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/king_heart_img.png"
        )
        self.king_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/king_club_img.png"
        )
        self.king_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/king_diamond_img.png"
        )
        #Queens
        self.queen_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/queen_spade_img.png"
        )
        self.queen_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/queen_heart_img.png"
        )
        self.queen_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/queen_club_img.png"
        )
        self.queen_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/queen_diamond_img.png"
        )
        #Jacks
        self.jack_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/jack_spade_img.png"
        )
        self.jack_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/jack_heart_img.png"
        )
        self.jack_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/jack_club_img.png"
        )
        self.jack_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/jack_diamond_img.png"
        )
        #Tens
        self.ten_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ten_spade_img.png"
        )
        self.ten_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ten_heart_img.png"
        )
        self.ten_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ten_club_img.png"
        )
        self.ten_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/ten_diamond_img.png"
        )
        #Nines
        self.nine_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/nine_spade_img.png"
        )
        self.nine_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/nine_heart_img.png"
        )
        self.nine_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/nine_club_img.png"
        )
        self.nine_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/nine_diamond_img.png"
        )
        #Eights
        self.eight_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/eight_spade_img.png"
        )
        self.eight_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/eight_heart_img.png"
        )
        self.eight_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/eight_club_img.png"
        )
        self.eight_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/eight_diamond_img.png"
        )
        #Sevens
        self.seven_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/seven_spade_img.png"
        )
        self.seven_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/seven_heart_img.png"
        )
        self.seven_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/seven_club_img.png"
        )
        self.seven_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/seven_diamond_img.png"
        )
        #Sixes
        self.six_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/six_spade_img.png"
        )
        self.six_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/six_heart_img.png"
        )
        self.six_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/six_club_img.png"
        )
        self.six_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/six_diamond_img.png"
        )

        #Fives
        self.five_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/five_spade_img.png"
        )
        self.five_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/five_heart_img.png"
        )
        self.five_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/five_club_img.png"
        )
        self.five_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/five_diamond_img.png"
        )

        #Fours
        self.four_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/four_spade_img.png"
        )
        self.four_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/four_heart_img.png"
        )
        self.four_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/four_club_img.png"
        )
        self.four_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/four_diamond_img.png"
        )

        #Threes
        self.three_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/three_spade_img.png"
        )
        self.three_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/three_heart_img.png"
        )
        self.three_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/three_club_img.png"
        )
        self.three_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/three_diamond_img.png"
        )

        #Twos
        self.two_spade_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/two_spade_img.png"
        )
        self.two_heart_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/two_heart_img.png"
        )
        self.two_club_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/two_club_img.png"
        )
        self.two_diamond_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/two_diamond_img.png"
        )

        # Hiden

        self.hidden_card_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/cards/hidden_card_img.png"
        )

        # # Cards labels
        ace_spade = tk.Label(self.game_frame, image=self.ace_spade_img, bg="#1c2941", borderwidth=-10)
        ace_heart = tk.Label(self.game_frame, image=self.ace_heart_img, bg="#1c2941", borderwidth=-10)
        ace_club = tk.Label(self.game_frame, image=self.ace_club_img, bg="#1c2941", borderwidth=-10)
        ace_diamond = tk.Label(self.game_frame, image=self.ace_diamond_img, bg="#1c2941", borderwidth=-10)

        king_spade = tk.Label(self.game_frame, image=self.king_spade_img, bg="#1c2941", borderwidth=-10)
        king_heart = tk.Label(self.game_frame, image=self.king_heart_img, bg="#1c2941", borderwidth=-10)
        king_club = tk.Label(self.game_frame, image=self.king_club_img, bg="#1c2941", borderwidth=-10)
        king_diamond = tk.Label(self.game_frame, image=self.king_diamond_img, bg="#1c2941", borderwidth=-10)

        queen_spade = tk.Label(self.game_frame, image=self.queen_spade_img, bg="#1c2941", borderwidth=-10)
        queen_heart = tk.Label(self.game_frame, image=self.queen_heart_img, bg="#1c2941", borderwidth=-10)
        queen_club = tk.Label(self.game_frame, image=self.queen_club_img, bg="#1c2941", borderwidth=-10)
        queen_diamond = tk.Label(self.game_frame, image=self.queen_diamond_img, bg="#1c2941", borderwidth=-10)

        jack_spade = tk.Label(self.game_frame, image=self.jack_spade_img, bg="#1c2941", borderwidth=-10)
        jack_heart = tk.Label(self.game_frame, image=self.jack_heart_img, bg="#1c2941", borderwidth=-10)
        jack_club = tk.Label(self.game_frame, image=self.jack_club_img, bg="#1c2941", borderwidth=-10)
        jack_diamond = tk.Label(self.game_frame, image=self.jack_diamond_img, bg="#1c2941", borderwidth=-10)

        ten_spade = tk.Label(self.game_frame, image=self.ten_spade_img, bg="#1c2941", borderwidth=-10)
        ten_heart = tk.Label(self.game_frame, image=self.ten_heart_img, bg="#1c2941", borderwidth=-10)
        ten_club = tk.Label(self.game_frame, image=self.ten_club_img, bg="#1c2941", borderwidth=-10)
        ten_diamond = tk.Label(self.game_frame, image=self.ten_diamond_img, bg="#1c2941", borderwidth=-10)

        nine_spade = tk.Label(self.game_frame, image=self.nine_spade_img, bg="#1c2941", borderwidth=-10)
        nine_heart = tk.Label(self.game_frame, image=self.nine_heart_img, bg="#1c2941", borderwidth=-10)
        nine_club = tk.Label(self.game_frame, image=self.nine_club_img, bg="#1c2941", borderwidth=-10)
        nine_diamond = tk.Label(self.game_frame, image=self.nine_diamond_img, bg="#1c2941", borderwidth=-10)

        eight_spade = tk.Label(self.game_frame, image=self.eight_spade_img, bg="#1c2941", borderwidth=-10)
        eight_heart = tk.Label(self.game_frame, image=self.eight_heart_img, bg="#1c2941", borderwidth=-10)
        eight_club = tk.Label(self.game_frame, image=self.eight_club_img, bg="#1c2941", borderwidth=-10)
        eight_diamond = tk.Label(self.game_frame, image=self.eight_diamond_img, bg="#1c2941", borderwidth=-10)

        seven_spade = tk.Label(self.game_frame, image=self.seven_spade_img, bg="#1c2941", borderwidth=-10)
        seven_heart = tk.Label(self.game_frame, image=self.seven_heart_img, bg="#1c2941", borderwidth=-10)
        seven_club = tk.Label(self.game_frame, image=self.seven_club_img, bg="#1c2941", borderwidth=-10)
        seven_diamond = tk.Label(self.game_frame, image=self.seven_diamond_img, bg="#1c2941", borderwidth=-10)

        six_spade = tk.Label(self.game_frame, image=self.six_spade_img, bg="#1c2941", borderwidth=-10)
        six_heart = tk.Label(self.game_frame, image=self.six_heart_img, bg="#1c2941", borderwidth=-10)
        six_club = tk.Label(self.game_frame, image=self.six_club_img, bg="#1c2941", borderwidth=-10)
        six_diamond = tk.Label(self.game_frame, image=self.six_diamond_img, bg="#1c2941", borderwidth=-10)

        five_spade = tk.Label(self.game_frame, image=self.five_spade_img, bg="#1c2941", borderwidth=-10)
        five_heart = tk.Label(self.game_frame, image=self.five_heart_img, bg="#1c2941", borderwidth=-10)
        five_club = tk.Label(self.game_frame, image=self.five_club_img, bg="#1c2941", borderwidth=-10)
        five_diamond = tk.Label(self.game_frame, image=self.five_diamond_img, bg="#1c2941", borderwidth=-10)

        four_spade = tk.Label(self.game_frame, image=self.four_spade_img, bg="#1c2941", borderwidth=-10)
        four_heart = tk.Label(self.game_frame, image=self.four_heart_img, bg="#1c2941", borderwidth=-10)
        four_club = tk.Label(self.game_frame, image=self.four_club_img, bg="#1c2941", borderwidth=-10)
        four_diamond = tk.Label(self.game_frame, image=self.four_diamond_img, bg="#1c2941", borderwidth=-10)

        three_spade = tk.Label(self.game_frame, image=self.three_spade_img, bg="#1c2941", borderwidth=-10)
        three_heart = tk.Label(self.game_frame, image=self.three_heart_img, bg="#1c2941", borderwidth=-10)
        three_club = tk.Label(self.game_frame, image=self.three_club_img, bg="#1c2941", borderwidth=-10)
        three_diamond = tk.Label(self.game_frame, image=self.three_diamond_img, bg="#1c2941", borderwidth=-10)

        two_spade = tk.Label(self.game_frame, image=self.two_spade_img, bg="#1c2941", borderwidth=-10)
        two_heart = tk.Label(self.game_frame, image=self.two_heart_img, bg="#1c2941", borderwidth=-10)
        two_club = tk.Label(self.game_frame, image=self.two_club_img, bg="#1c2941", borderwidth=-10)
        two_diamond = tk.Label(self.game_frame, image=self.two_diamond_img, bg="#1c2941", borderwidth=-10)

        self.hidden_card = tk.Label(self.game_frame, image=self.hidden_card_img, bg="#1c2941", borderwidth=-10)

        # Cards list contains all of possible cards
        self.cards = [ace_spade, ace_heart, ace_club, ace_diamond,
                king_spade, king_heart, king_club, king_diamond,
                queen_spade, queen_heart, queen_club, queen_diamond,
                jack_spade, jack_heart, jack_club, jack_diamond,
                ten_spade, ten_heart, ten_club, ten_diamond,
                nine_spade, nine_heart, nine_club, nine_diamond,
                eight_spade, eight_heart, eight_club, eight_diamond,
                seven_spade, seven_heart, seven_club, seven_diamond,
                six_spade, six_heart, six_club, six_diamond,
                five_spade, five_heart, five_club, five_diamond,
                four_spade, four_heart, four_club, four_diamond,
                three_spade, three_heart, three_club, three_diamond,
                two_spade, two_heart, two_club, two_diamond
        ]

        # Point list consist all of the cards with the same point value
        self.point_1_or_11 = [ace_spade, ace_heart, ace_club, ace_diamond]
        self.point_10 = [king_spade, king_heart, king_club, king_diamond,
                queen_spade, queen_heart, queen_club, queen_diamond,
                jack_spade, jack_heart, jack_club, jack_diamond,
                ten_spade, ten_heart, ten_club, ten_diamond
                ]
        self.point_9 = [nine_spade, nine_heart, nine_club, nine_diamond]
        self.point_8 = [eight_spade, eight_heart, eight_club, eight_diamond]
        self.point_7 = [seven_spade, seven_heart, seven_club, seven_diamond]
        self.point_6 = [six_spade, six_heart, six_club, six_diamond]
        self.point_5 = [five_spade, five_heart, five_club, five_diamond]
        self.point_4 = [four_spade, four_heart, four_club, four_diamond]
        self.point_3 = [three_spade, three_heart, three_club, three_diamond]
        self.point_2 = [two_spade, two_heart, two_club, two_diamond]

        # List which contain player cards
        self.player_cards = []

        # Player points variables
        self.player_points_ace_1 = tk.IntVar()
        self.player_points_ace_11 = tk.IntVar()
        self.pc = tk.IntVar()
        self.pc.set(1)
        self.px = 470 # X of second player card
        self.py = 288 # Y of second player card

        # While loop which takes randomly 2 cards for a player and add its point to the card value variables
        i = 0
        while i < 2:
            card_1_2 = self.cards[random.randrange(0,len(self.cards))]

            if card_1_2 in self.player_cards:
                continue

            else:
                self.player_cards.append(card_1_2)
                if i == 0:
                    self.player_cards[i].place(x=450, y=280)
                    i += 1
                elif i == 1:
                    self.player_cards[i].place(x=470, y=288)
                    self.player_cards[i].lift()
                    i += 1


                if card_1_2 in self.point_1_or_11:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 1)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 11)
                elif card_1_2 in self.point_10:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 10)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 10)
                elif card_1_2 in self.point_9:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 9)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 9)
                elif card_1_2 in self.point_8:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 8)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 8)
                elif card_1_2 in self.point_7:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 7)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 7)
                elif card_1_2 in self.point_6:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 6)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 6)
                elif card_1_2 in self.point_5:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 5)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 5)
                elif card_1_2 in self.point_4:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 4)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 4)
                elif card_1_2 in self.point_3:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 3)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 3)
                elif card_1_2 in self.point_2:
                    self.player_points_ace_1.set(self.player_points_ace_1.get() + 2)
                    self.player_points_ace_11.set(self.player_points_ace_11.get() + 2)

        
        self.player_ace_check = [True if k in self.point_1_or_11 else False for k in self.player_cards]

        self.point_value_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/point_value_img.png")
        self.points_label_bg = tk.Label(self.game_frame)
        self.points_label_bg.config(image=self.point_value_img, bg="#1c2941", borderwidth=-5)
        self.points_label_bg.place(x=380, y=280)

        if (self.player_ace_check[0] and self.player_ace_check[1]) == True:
            self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=6)
            self.player_points_label.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label.place(x=385, y=280)

        elif (self.player_ace_check[0] or self.player_ace_check[1]) == True:
            self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=1)
            self.player_points_label.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label.place(x=388, y=280)

            self.player_points_label_2 = tk.Label(self.game_frame, text=' /', font=("Titillium Web", 8), width=1)
            self.player_points_label_2.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label_2.place(x=399, y=280)

            self.player_points_label_3 = tk.Label(self.game_frame, textvariable=self.player_points_ace_11, font=("Titillium Web", 8), width=1)
            self.player_points_label_3.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label_3.place(x=413, y=280)

        else:
            self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=6)
            self.player_points_label.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label.place(x=385, y=280)

        # List which contain computer cards
        self.computer_cards = []

        # Computer points variables
        self.computer_points_ace_1 = tk.IntVar()
        self.computer_points_ace_11 = tk.IntVar()
        self.cc = tk.IntVar()
        self.cc.set(1)
        self.cx = 470
        self.cy = 88

        self.first_computer_points_ace_1 = tk.IntVar()
        self.first_computer_points_ace_11 = tk.IntVar()

        # While loop which takes randomly 2 cards for a computer and add its point to the card value variables, also adding points for both computer cards (To check if it have a blackjack)
        j = 0
        while j < 2:
            comp_card_1_2 = self.cards[random.randrange(1,len(self.cards))]
            if comp_card_1_2 not in (self.player_cards and self.computer_cards):
                self.computer_cards.append(comp_card_1_2)

                if j == 0:
                    self.computer_cards[j].place(x=450, y=80)
                    self.hidden_card.lift()
                    j += 1
                elif j == 1:
                    self.hidden_card.place(x=470, y=88)
                    self.hidden_card.lift()
                    j += 1

                if comp_card_1_2 in self.point_1_or_11:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 1)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 11)
                elif comp_card_1_2 in self.point_10:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 10)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 10)
                elif comp_card_1_2 in self.point_9:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 9)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 9)
                elif comp_card_1_2 in self.point_8:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 8)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 8)
                elif comp_card_1_2 in self.point_7:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 7)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 7)
                elif comp_card_1_2 in self.point_6:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 6)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 6)
                elif comp_card_1_2 in self.point_5:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 5)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 5)
                elif comp_card_1_2 in self.point_4:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 4)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 4)
                elif comp_card_1_2 in self.point_3:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 3)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 3)
                elif comp_card_1_2 in self.point_2:
                    self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 2)
                    self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 2)
            else:
                continue

        # Adding points from a first computer card
        if self.computer_cards[0] in self.point_1_or_11:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 1)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 11)
        elif self.computer_cards[0] in self.point_10:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 10)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 10)
        elif self.computer_cards[0] in self.point_9:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 9)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 9)
        elif self.computer_cards[0] in self.point_8:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 8)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 8)
        elif self.computer_cards[0] in self.point_7:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 7)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 7)
        elif self.computer_cards[0] in self.point_6:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 6)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 6)
        elif self.computer_cards[0] in self.point_5:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 5)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 5)
        elif self.computer_cards[0] in self.point_4:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 4)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 4)
        elif self.computer_cards[0] in self.point_3:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 3)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 3)
        elif self.computer_cards[0] in self.point_2:
            self.first_computer_points_ace_1.set(self.first_computer_points_ace_1.get() + 2)
            self.first_computer_points_ace_11.set(self.first_computer_points_ace_11.get() + 2)

        # Checking if computer has ace
        self.computer_ace_check = [True if l in self.point_1_or_11 else False for l in self.computer_cards]

        # Computer point image in background
        self.comp_point_bg_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/point_value_img.png")
        self.comp_point_bg_img_lb = tk.Label(self.game_frame)
        self.comp_point_bg_img_lb.config(image=self.comp_point_bg_img, bg="#1c2941", borderwidth=-5)
        self.comp_point_bg_img_lb.place(x=380, y=80)

        # If computer has ace at the first card x/x label points
        if (self.computer_ace_check[0] == True):
            self.first_computer_points_label = tk.Label(self.game_frame, textvariable=self.first_computer_points_ace_1, font=("Titillium Web", 8), width=1)
            self.first_computer_points_label.config(fg="white", bg="#283753", anchor="center")
            self.first_computer_points_label.place(x=388, y=80)

            self.first_computer_points_label_2 = tk.Label(self.game_frame, text=' /', font=("Titillium Web", 8), width=1)
            self.first_computer_points_label_2.config(fg="white", bg="#283753", anchor="center")
            self.first_computer_points_label_2.place(x=399, y=80)

            self.first_computer_points_label_3 = tk.Label(self.game_frame, textvariable=self.first_computer_points_ace_11, font=("Titillium Web", 8), width=1)
            self.first_computer_points_label_3.config(fg="white", bg="#283753", anchor="center")
            self.first_computer_points_label_3.place(x=413, y=80)

        else:
            self.first_computer_points_label = tk.Label(self.game_frame, textvariable=self.first_computer_points_ace_1, font=("Titillium Web", 8), width=6)
            self.first_computer_points_label.config(fg="white", bg="#283753", anchor="center")
            self.first_computer_points_label.place(x=385, y=80)


        self.computer_points_label = tk.Label(self.game_frame, textvariable=self.computer_points_ace_1, font=("Titillium Web", 8), width=1)
        self.computer_points_label.config(fg="white", bg="#283753", anchor="center")

        self.computer_points_label_2 = tk.Label(self.game_frame, text=' /', font=("Titillium Web", 8), width=1)
        self.computer_points_label_2.config(fg="white", bg="#283753", anchor="center")

        self.computer_points_label_3 = tk.Label(self.game_frame, textvariable=self.computer_points_ace_11, font=("Titillium Web", 8), width=1)
        self.computer_points_label_3.config(fg="white", bg="#283753", anchor="center")

        self.double_check()
        self.first_round_check()

    # Checking if player can make a double bet, in not it change label to OFF
    def double_check(self):
        if self.first_window.player_balance.get() < self.bet_value.get()*2:
            self.double_bttn.destroy()
            self.double_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/double_off_img.png")
            self.double_bttn = tk.Button(self.game_frame)
            self.double_bttn.config(
            image=self.double_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
            self.double_bttn.place(x=649, y=480)

    # Methid check if there is a BJ during first round
    def first_round_check(self):
        # if player and comp has BJ at 1 RUND
        if self.player_points_ace_11.get() == 21 and self.computer_points_ace_11.get() == 21:
            self.info_msg.set("You won {} $!".format(int(self.bet_value.get()+self.bet_value.get())))
            self.first_window.player_balance.set(int(self.first_window.player_balance.get()+self.bet_value.get()))
            self.hidden_card.destroy()
            self.computer_cards[1].place(x=470, y=88)
            self.computer_cards[1].lift()
            self.first_computer_points_label.destroy()
            self.computer_points_label.place(x=388, y=80)
            self.computer_points_label_2.place(x=399, y=80)
            self.computer_points_label_3.place(x=413, y=80)
            self.wins.set(int(self.wins.get()+1))
            self.make_new_bet()

        elif self.computer_points_ace_11.get() == 21:
            self.info_msg.set("You lost {} $!".format(int(self.bet_value.get())))
            self.hidden_card.destroy()
            self.computer_cards[1].place(x=470, y=88)
            self.computer_cards[1].lift()
            self.first_computer_points_label.destroy()
            self.computer_points_label.place(x=388, y=80)
            self.computer_points_label_2.place(x=399, y=80)
            self.computer_points_label_3.place(x=413, y=80)
            self.losses.set(int(self.losses.get()+1))
            self.make_new_bet()

        elif self.player_points_ace_11.get() == 21:
            self.info_msg.set("You won {} $!".format(int(self.bet_value.get()+self.bet_value.get()+self.bet_value.get()/2)))
            self.first_window.player_balance.set(int(self.first_window.player_balance.get()+(self.bet_value.get()+self.bet_value.get()+self.bet_value.get()/2)))
            self.wins.set(int(self.wins.get()+1))
            self.make_new_bet()

    # Hit button method, 1 more card for a player, disable split and double buttons. After getting a new card checking win/lost
    def hit(self):
        self.pc.set(self.pc.get()+1)
        self.px += 20
        self.py += 8

        self.double_bttn.destroy()

        self.double_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/double_off_img.png")
        self.double_bttn = tk.Button(self.game_frame)
        self.double_bttn.config(
            image=self.double_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.double_bttn.place(x=579, y=480)

        card = self.cards[random.randrange(1,len(self.cards))]

        if card not in (self.player_cards and self.computer_cards):
            self.player_cards.append(card)

            while True:
                if len(self.player_cards) == self.pc.get()+1:
                    self.player_cards[self.pc.get()].place(x=self.px, y=self.py)
                    self.player_cards[self.pc.get()].lift()
                    break
                else:
                    self.player_cards.append(card)
                    continue

            if (self.player_cards[self.pc.get()] in self.point_1_or_11 and self.player_points_ace_1.get() <= 10 and ((self.player_cards[0] or self.player_cards[1]) not in self.point_1_or_11)):
                self.player_points_label.destroy()
                self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=1)
                self.player_points_label.config(fg="white", bg="#283753", anchor="center")
                self.player_points_label.place(x=388, y=280)

                self.player_points_label_2 = tk.Label(self.game_frame, text=' /', font=("Titillium Web", 8), width=1)
                self.player_points_label_2.config(fg="white", bg="#283753", anchor="center")
                self.player_points_label_2.place(x=399, y=280)

                self.player_points_label_3 = tk.Label(self.game_frame, textvariable=self.player_points_ace_11, font=("Titillium Web", 8), width=1)
                self.player_points_label_3.config(fg="white", bg="#283753", anchor="center")
                self.player_points_label_3.place(x=413, y=280)

            if card in self.point_1_or_11:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 1)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 11)
            elif card in self.point_10:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 10)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 10)
            elif card in self.point_9:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 9)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 9)
            elif card in self.point_8:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 8)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 8)
            elif card in self.point_7:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 7)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 7)
            elif card in self.point_6:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 6)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 6)
            elif card in self.point_5:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 5)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 5)
            elif card in self.point_4:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 4)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 4)
            elif card in self.point_3:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 3)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 3)
            elif card in self.point_2:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 2)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 2)

        if ((self.player_cards[0] in self.point_1_or_11 and self.player_cards[1] not in self.point_1_or_11 and self.player_points_ace_11.get() > 21)):
            self.player_points_label.destroy()
            self.player_points_label_2.destroy()
            self.player_points_label_3.destroy()
            self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=6)
            self.player_points_label.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label.place(x=385, y=280)

        elif ((self.player_cards[1] in self.point_1_or_11 and self.player_cards[0] not in self.point_1_or_11 and self.player_points_ace_11.get() > 21)):
            self.player_points_label.destroy()
            self.player_points_label_2.destroy()
            self.player_points_label_3.destroy()
            self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=6)
            self.player_points_label.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label.place(x=385, y=280)

        self.win_or_lost_check()

    # Doubled bet, only 1 more card then comp decision
    def double(self):
        self.decision_buttons_off()
        self.bet_value.set(self.bet_value.get()*2)

        card_db = self.cards[random.randrange(1,len(self.cards))]
        if card_db not in (self.player_cards and self.computer_cards):
            self.player_cards.append(card_db)
            self.player_cards[2].place(x=490, y=296)
            self.player_cards[2].lift()

            if (self.player_cards[2] in self.point_1_or_11 and self.player_points_ace_1.get() <= 10 and ((self.player_cards[0] or self.player_cards[1]) not in self.point_1_or_11)):
                self.player_points_label.destroy()
                self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=1)
                self.player_points_label.config(fg="white", bg="#283753", anchor="center")
                self.player_points_label.place(x=388, y=280)

                self.player_points_label_2 = tk.Label(self.game_frame, text=' /', font=("Titillium Web", 8), width=1)
                self.player_points_label_2.config(fg="white", bg="#283753", anchor="center")
                self.player_points_label_2.place(x=399, y=280)

                self.player_points_label_3 = tk.Label(self.game_frame, textvariable=self.player_points_ace_11, font=("Titillium Web", 8), width=1)
                self.player_points_label_3.config(fg="white", bg="#283753", anchor="center")
                self.player_points_label_3.place(x=413, y=280)

            if card_db in self.point_1_or_11:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 1)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 11)
            elif card_db in self.point_10:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 10)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 10)
            elif card_db in self.point_9:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 9)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 9)
            elif card_db in self.point_8:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 8)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 8)
            elif card_db in self.point_7:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 7)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 7)
            elif card_db in self.point_6:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 6)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 6)
            elif card_db in self.point_5:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 5)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 5)
            elif card_db in self.point_4:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 4)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 4)
            elif card_db in self.point_3:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 3)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 3)
            elif card_db in self.point_2:
                self.player_points_ace_1.set(self.player_points_ace_1.get() + 2)
                self.player_points_ace_11.set(self.player_points_ace_11.get() + 2)

        if ((self.player_cards[0] in self.point_1_or_11 and self.player_cards[1] not in self.point_1_or_11 and self.player_points_ace_11.get() > 21)):
            self.player_points_label.destroy()
            self.player_points_label_2.destroy()
            self.player_points_label_3.destroy()
            self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=6)
            self.player_points_label.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label.place(x=385, y=280)

        elif ((self.player_cards[1] in self.point_1_or_11 and self.player_cards[0] not in self.point_1_or_11 and self.player_points_ace_11.get() > 21)):
            self.player_points_label.destroy()
            self.player_points_label_2.destroy()
            self.player_points_label_3.destroy()
            self.player_points_label = tk.Label(self.game_frame, textvariable=self.player_points_ace_1, font=("Titillium Web", 8), width=6)
            self.player_points_label.config(fg="white", bg="#283753", anchor="center")
            self.player_points_label.place(x=385, y=280)

        self.win_or_lost_check()
        self.computer_move()

    
    def win_or_lost_check(self):
    # Method will check if player wins or not
        if self.player_points_ace_1.get() > 21:
            self.info_msg.set("You lost {} $!".format(int(self.bet_value.get())))
            self.losses.set(int(self.losses.get()+1))
            self.make_new_bet()

        elif self.player_points_ace_1.get() == 21:
            self.info_msg.set("You won {} $!".format(int(self.bet_value.get()+self.bet_value.get()+self.bet_value.get()/2)))
            self.first_window.player_balance.set(int(self.first_window.player_balance.get()+(self.bet_value.get()+self.bet_value.get()+self.bet_value.get()/2)))
            self.wins.set(int(self.wins.get()+1))
            self.make_new_bet()

        elif self.player_points_ace_11.get() == 21:
            self.info_msg.set("You won {} $!".format(int(self.bet_value.get()+self.bet_value.get()+self.bet_value.get()/2)))
            self.first_window.player_balance.set(int(self.first_window.player_balance.get()+(self.bet_value.get()+self.bet_value.get()+self.bet_value.get()/2)))
            self.wins.set(int(self.wins.get()+1))
            self.make_new_bet()

    # Computer decisions method 
    def computer_move(self):
        self.decision_buttons_off()

        self.hidden_card.destroy()
        self.computer_cards[1].place(x=470, y=88)
        self.computer_cards[1].lift()
        self.first_computer_points_label.destroy()
        self.computer_points_label = tk.Label(self.game_frame, textvariable=self.computer_points_ace_1, font=("Titillium Web", 8), width=6)
        self.computer_points_label.config(fg="white", bg="#283753", anchor="center")
        self.computer_points_label.place(x=385, y=80)

        for check_times in range(1,10):

            if (self.computer_points_ace_1.get() or self.computer_points_ace_11.get()) >= 17:
                if (self.computer_points_ace_1.get() or self.computer_points_ace_11.get()) == 21:
                    self.info_msg.set("You lost {} $!".format(int(self.bet_value.get()*2)))
                    self.losses.set(int(self.losses.get()+1))
                    self.make_new_bet()
                    break

                elif self.computer_points_ace_1.get() == self.player_points_ace_1.get():
                    self.info_msg.set("You won {} $!".format(int(self.bet_value.get())))
                    self.wins.set(int(self.wins.get()+1))
                    self.make_new_bet()
                    break

                elif (self.player_points_ace_11.get() < 21 and (self.player_points_ace_11.get() > (self.computer_points_ace_1.get() or self.computer_points_ace_11.get()))):
                    self.info_msg.set("You won {} $!".format(int(self.bet_value.get())))
                    self.wins.set(int(self.wins.get()+1))
                    self.make_new_bet()
                    break

                elif (21 - self.computer_points_ace_1.get()) < (21 - self.player_points_ace_1.get()):
                    self.info_msg.set("You lost {} $!".format(int(self.bet_value.get())))
                    self.losses.set(int(self.losses.get()+1))
                    self.make_new_bet()
                    break

                elif (21 - self.computer_points_ace_1.get()) > (21 - self.player_points_ace_1.get()):
                    self.info_msg.set("You won {} $!".format(int(self.bet_value.get())))
                    self.wins.set(int(self.wins.get()+1))
                    self.make_new_bet()
                    break

            else:

                self.cc.set(self.cc.get()+1)
                self.cx += 20
                self.cy += 8
                comp_card = self.cards[random.randrange(1,len(self.cards))]

                if comp_card not in (self.player_cards and self.computer_cards):
                    self.computer_cards.append(comp_card)
                    self.computer_cards[self.cc.get()].place(x=self.cx, y=self.cy)
                    self.computer_cards[self.cc.get()].lift()

                    if (self.computer_cards[self.cc.get()] in self.point_1_or_11 and self.computer_points_ace_1.get() <= 10 and ((self.computer_cards[0] or self.computer_cards[1]) not in self.point_1_or_11)):
                        self.computer_points_label.destroy()
                        self.computer_points_label = tk.Label(self.game_frame, textvariable=self.computer_points_ace_1, font=("Titillium Web", 8), width=1)
                        self.computer_points_label.config(fg="white", bg="#283753", anchor="center")
                        self.computer_points_label.place(x=388, y=80)

                        self.computer_points_label_2 = tk.Label(self.game_frame, text=' /', font=("Titillium Web", 8), width=1)
                        self.computer_points_label_2.config(fg="white", bg="#283753", anchor="center")
                        self.computer_points_label_2.place(x=399, y=80)

                        self.computer_points_label_3 = tk.Label(self.game_frame, textvariable=self.computer_points_ace_11, font=("Titillium Web", 8), width=1)
                        self.computer_points_label_3.config(fg="white", bg="#283753", anchor="center")
                        self.computer_points_label_3.place(x=413, y=80)

                    if comp_card in self.point_1_or_11:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 1)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 11)
                    elif comp_card in self.point_10:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 10)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 10)
                    elif comp_card in self.point_9:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 9)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 9)
                    elif comp_card in self.point_8:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 8)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 8)
                    elif comp_card in self.point_7:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 7)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 7)
                    elif comp_card in self.point_6:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 6)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 6)
                    elif comp_card in self.point_5:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 5)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 5)
                    elif comp_card in self.point_4:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 4)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 4)
                    elif comp_card in self.point_3:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 3)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 3)
                    elif comp_card in self.point_2:
                        self.computer_points_ace_1.set(self.computer_points_ace_1.get() + 2)
                        self.computer_points_ace_11.set(self.computer_points_ace_11.get() + 2)

                    if (((self.computer_cards[0] in self.point_1_or_11 or self.computer_cards[1] in self.point_1_or_11) and self.computer_points_ace_11.get() > 21)):
                        self.computer_points_label.destroy()
                        self.computer_points_label_2.destroy()
                        self.computer_points_label_3.destroy()
                        self.computer_points_label = tk.Label(self.game_frame, textvariable=self.computer_points_ace_1, font=("Titillium Web", 8), width=6)
                        self.computer_points_label.config(fg="white", bg="#283753", anchor="center")
                        self.computer_points_label.place(x=385, y=80)
                        
                    if (self.computer_points_ace_1.get() or self.computer_points_ace_11.get()) >= 17:
                        if (self.computer_points_ace_1.get() or self.computer_points_ace_11.get()) == 21:
                            self.info_msg.set("You lost {} $!".format(int(self.bet_value.get()*2)))
                            self.losses.set(int(self.losses.get()+1))
                            self.make_new_bet()
                            break
                        
                        elif self.computer_points_ace_1.get() > 21:
                            self.info_msg.set("You won {} $!".format(int(self.bet_value.get()*2)))
                            self.wins.set(int(self.wins.get()+1))
                            self.make_new_bet()
                            break

                        elif self.computer_points_ace_1.get() == self.player_points_ace_1.get():
                            self.info_msg.set("You won {} $!".format(int(self.bet_value.get())))
                            self.wins.set(int(self.wins.get()+1))
                            self.make_new_bet()
                            break

                        elif (self.player_points_ace_11.get() < 21 and (self.player_points_ace_11.get() > (self.computer_points_ace_1.get() or self.computer_points_ace_11.get()))):
                            self.info_msg.set("You won {} $!".format(int(self.bet_value.get())))
                            self.wins.set(int(self.wins.get()+1))
                            self.make_new_bet()
                            break

                        elif (21 - self.computer_points_ace_1.get()) < (21 - self.player_points_ace_1.get()):
                            self.info_msg.set("You lost {} $!".format(int(self.bet_value.get())))
                            self.losses.set(int(self.losses.get()+1))
                            self.make_new_bet()
                            break

                        elif (21 - self.computer_points_ace_1.get()) > (21 - self.player_points_ace_1.get()):
                            self.info_msg.set("You won {} $!".format(int(self.bet_value.get())))
                            self.wins.set(int(self.wins.get()+1))
                            self.make_new_bet()
                            break

    def decision_buttons_off(self):
    # Method which make all the decision button (Hit, Stan, Split, Double) OFF

        # Destroying green one button and make it grey without functions
        self.hit_bttn.destroy()
        self.stand_bttn.destroy()
        self.double_bttn.destroy()

        self.hit_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/hit_off_img.png")
        self.hit_bttn = tk.Button(self.game_frame)
        self.hit_bttn.config(
            image=self.hit_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.hit_bttn.place(x=303, y=480)

        self.stand_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/stand_off_img.png")
        self.stand_bttn = tk.Button(self.game_frame)
        self.stand_bttn.config(
            image=self.stand_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.stand_bttn.place(x=441, y=480)

        self.double_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/double_off_img.png")
        self.double_bttn = tk.Button(self.game_frame)
        self.double_bttn.config(
            image=self.double_img,
            borderwidth=-10,
            bg="#1c2941",
            activebackground="#1c2941",
        )
        self.double_bttn.place(x=579, y=480)

    def make_new_bet(self):
        self.hit_bttn.destroy()
        self.stand_bttn.destroy()
        self.double_bttn.destroy()

        # Make new bet buttons
        if self.first_window.player_balance.get() > 0:
            self.new_bet_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/new_bet_img.png")
            new_bet_bttn = tk.Button(self.game_frame, command=self.new_bet)
            new_bet_bttn.config(
                image=self.new_bet_img,
                borderwidth=-10,
                bg="#1c2941",
                activebackground="#1c2941",
            )
            new_bet_bttn.place(x=303, y=480)
        else:
            self.new_bet_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/new_bet_off_img.png")
            new_bet_bttn = tk.Button(self.game_frame, command=self.new_bet)
            new_bet_bttn.config(
                image=self.new_bet_img,
                borderwidth=-10,
                bg="#1c2941",
                activebackground="#1c2941",
            )
            new_bet_bttn.place(x=303, y=480)

        if self.first_window.player_balance.get() >= self.bet_value.get():
            self.rebet_bet_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/rebet_img.png")
            rebet_bttn = tk.Button(self.game_frame, command=self.rebet)
            rebet_bttn.config(
                image=self.rebet_bet_img,
                borderwidth=-10,
                bg="#1c2941",
                activebackground="#1c2941",
            )
            rebet_bttn.place(x=441, y=480)
        else:
            self.rebet_bet_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/rebet_off_img.png")
            rebet_bttn = tk.Button(self.game_frame, command=self.rebet)
            rebet_bttn.config(
                image=self.rebet_bet_img,
                borderwidth=-10,
                bg="#1c2941",
                activebackground="#1c2941",
            )
            rebet_bttn.place(x=441, y=480)

        if self.first_window.player_balance.get() >= self.bet_value.get()*2:
            self.double_bet_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/double_img.png")
            double_bet_bttn = tk.Button(self.game_frame, command=self.double_bet)
            double_bet_bttn.config(
                image=self.double_bet_img,
                borderwidth=-10,
                bg="#1c2941",
                activebackground="#1c2941",
            )
            double_bet_bttn.place(x=579, y=480)
        else:
            self.double_bet_img = tk.PhotoImage(file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/double_off_img.png")
            double_bet_bttn = tk.Button(self.game_frame, command=self.double_bet)
            double_bet_bttn.config(
                image=self.double_bet_img,
                borderwidth=-10,
                bg="#1c2941",
                activebackground="#1c2941",
            )
            double_bet_bttn.place(x=579, y=480)

    # A new bet button method
    def new_bet(self):
        if self.first_window.player_balance.get() > 0:
            self.bets.set(int(self.bets.get()+1))
            self.game_frame.destroy()
            self.bottom_frame.destroy()
            self.make_bet_frame()
            self.make_bottom_frame()
            self.bet_value.set(0)
            self.info_msg.set("Please make a bet.")
        else:
            self.info_msg.set("You do not have enough money.")

    # A rebet button method
    def rebet(self):
        if self.first_window.player_balance.get() >= self.bet_value.get():
            self.bets.set(int(self.bets.get()+1))
            self.game_frame.destroy()
            self.bottom_frame.destroy()
            self.info_msg.set("")
            self.make_game_frame()
            self.first_window.player_balance.set(int(self.first_window.player_balance.get()-self.bet_value.get()))
            self.bet_value.set(self.bet_value.get())
        else:
            self.info_msg.set("You do not have enough money.")

    # A double button method
    def double_bet(self):
        if self.first_window.player_balance.get() >= self.bet_value.get()*2:
            self.bets.set(int(self.bets.get()+1))
            self.game_frame.destroy()
            self.bottom_frame.destroy()
            self.info_msg.set("")
            self.make_game_frame()
            self.first_window.player_balance.set(int(self.first_window.player_balance.get()-self.bet_value.get()*2))
            self.bet_value.set(self.bet_value.get()*2)
        else:
            self.info_msg.set("You do not have enough money.")

    # Opening first window as a Toplevel
    def new_window(self):
        self.first_window = FirstWindow()


class FirstWindow(tk.Toplevel):
    """First window class.
    Contains player name and balance entry, labels, Start/Quit buttons
    """
    def __init__(self):
        super().__init__()

        # Defining variables
        self.player_name = tk.StringVar()
        self.player_balance = tk.IntVar()

        # Adjusting the window
        width_of_window = 980
        height_of_window = 604
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width_of_window / 2))
        y_coordinate = int((screen_height / 2) - (height_of_window / 2) - 30)
        self.geometry(
            f"{width_of_window}x{height_of_window}+{x_coordinate}+{y_coordinate}"
        )
        self.resizable(width=False, height=False)  # Resizable of a window

        # Adding a background picture
        self.background_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/first_background_img.png"
        )
        first_win_bg_label = tk.Label(self, image=self.background_img)
        first_win_bg_label.place(x=0, y=0)

        # Player name Entry widged
        self.vcmd1 = self.register(self.callback_name)
        player_name_entry = tk.Entry(
            self,
            textvariable=self.player_name,
            font=("Titillium Web", 12),
            width=15,
            validate="all",
            validatecommand=(self.vcmd1, "%P"),
        )
        player_name_entry.place(x=700, y=230)
        player_name_entry.focus()

        # Player's balance Entry widget
        self.vcmd2 = self.register(self.callback_balance)
        player_balance_entry = tk.Entry(
            self,
            textvariable=self.player_balance,
            font=("Titillium Web", 12),
            width=15,
            validate="all",
            validatecommand=(self.vcmd2, "%P")
        )
        player_balance_entry.place(x=700, y=270)

        # Player name Label widget
        player_name_label = tk.Label(self, text="Player name:", font=("Titillium Web", 14))
        player_name_label.config(fg="white", bg="black")
        player_name_label.place(x=540, y=225)

        # Player balance Label widget
        player_balance_label = tk.Label(self, text="Balance:", font=("Titillium Web", 14))
        player_balance_label.config(fg="white", bg="black")
        player_balance_label.place(x=540, y=265)

        # Information about min/max balance Label widget
        self.min_max_label = tk.Label(
            self,
            text="The balance should be between 20 and 5000 $.",
            font=("Titillium Web", 10),
        )
        self.min_max_label.config(fg="white", bg="black")
        self.min_max_label.place(x=540, y=310)

        # Start game button widget
        self.start_button_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/start_button_img.png"
        )
        start_button = tk.Button(self, command=self.start_button_func)
        start_button.config(
            image=self.start_button_img,
            borderwidth=-10,
            bg="black",
            activebackground="black",
        )
        start_button.place(x=630, y=500)

        # Quit game button widget
        self.quit_button_img = tk.PhotoImage(
            file="C:/Users/rjg5by/Scripts/venv/blackjack/pictures/quit_button_img.png"
        )
        quit_button = tk.Button(self, command=self.quit_button_func)
        quit_button.config(
            image=self.quit_button_img, borderwidth=-10, bg="black", activebackground="black"
        )
        quit_button.place(x=800, y=500)

    # Method which validate if entered str is digit in Balance Entry
    def callback_balance(self, P):
        if len(P) <= 4 and (str.isdigit(P) or P == ""):
            return True
        else:
            return False

    # Method which validate if entered str is not longer than 15 characters in Player name Entry
    def callback_name(self, P):
        if len(P) <= 15:
            return True
        else:
            return False

    # This method checks if player typed a name, than checks if balance is 20-5000. If all statement are ok, move to main play game window
    def start_button_func(self):
        if self.player_name.get() == "":
            self.min_max_label.config(
                fg="red", bg="black", text="Please type your name."
            )
        elif self.player_balance.get() < 20:
            self.min_max_label.config(
                fg="red",
                bg="black",
                text="Please correct your balance value. It should be at least 20 $.",
            )
        elif self.player_balance.get() > 5000:
            self.min_max_label.config(
                fg="red",
                bg="black",
                text="Please correct your balance value. Maximum is 5000 $.",
            )
        else:
            self.master.deiconify()  # Main game play windows appears
            self.destroy()  # Exit of first window

    # Quiting whole game button
    def quit_button_func(self):
        self.master.destroy()


if __name__ == "__main__":
    MainApplication().mainloop()
