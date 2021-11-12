import tkinter as tk
#import Main as main


root = tk.Tk()


number_of_players = 1
def set_players(val):
    global number_of_players
    number_of_players = (int(val))


value_of_balance = 100


def set_balance(val):
    global value_of_balance
    value_of_balance = (int(val))


class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(fill=tk.BOTH)

        # Create menu buttons

        title_label = tk.Label(self, text='Nags Gaming')
        window_one_button = tk.Button(self, text='BlackJack', command=self.window_one)
        close_button = tk.Button(self, text='Close', command=self.master.destroy)

        # Attach to grid

        title_label.grid(row=0, column=0)
        window_one_button.grid(row=1, column=0)
        close_button.grid(row=0, column=0, sticky="nw")

        # Describe grid

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)

        root.geometry("500x300")

    def window_one(self):
        self.destroy()
        Window_One(self.master)

    def window_two(self):
        self.destroy()
        Menu(self.master)


class Window_One(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.parent = parent
        self.pack(fill=tk.BOTH)

        # Create menu buttons

        self.title_label = tk.Label(self, text='BlackJack')
        self.menu_button = tk.Button(self, text='Back To Menu', command=self.menu)
        self.balance_val = tk.Label(self, text='Set your starting balance')
        self.balance_val_slider = tk.Scale(self, from_=100, to=1000, orient=tk.HORIZONTAL, command=set_balance)
        self.num_players = tk.Label(self, text='How many players are there?')
        self.num_players_slider = tk.Scale(self, from_=1, to=5, orient=tk.HORIZONTAL, command=set_players)
        self.num_players_button = tk.Button(self, text='Press this Button to Play', command=self.window_two)

        # Attach to grid

        self.title_label.grid(row=0, column=0, sticky='ew')
        self.menu_button.grid(row=0, column=0, sticky="nw")
        self.balance_val.grid(row=1, column=0)
        self.balance_val_slider.grid(row=2, column=0)
        self.num_players.grid(row=3, column=0)
        self.num_players_slider.grid(row=4, column=0)
        self.num_players_button.grid(row=5, column=0)

        # Describe grid

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

    def window_two(self):
        self.destroy()
        Window_Two(self.master)

    def menu(self):
        self.destroy()
        Menu(self.master)


class Window_Two(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.configure(background="green")

        self.pack(fill=tk.BOTH)

        # Create a top and bottom frame

        bottom_frame = tk.Frame(self)
        middle_frame = tk.Frame(self)
        top_frame = tk.Frame(self)

        bottom_frame.grid(row=2, sticky="news")
        top_frame.grid(row=0, sticky='news')
        middle_frame.grid(row=1, sticky="news")

        bottom_frame.configure(background='green')
        middle_frame.configure(background='yellow')
        top_frame.configure(background='red')

        self.rowconfigure(0, minsize=280, weight=1)
        self.rowconfigure(1, minsize=280, weight=1)
        self.rowconfigure(2, minsize=280, weight=1)

        self.columnconfigure(0, weight=1)

        for i in range(number_of_players):
            if i == 0:
                position = i
                balance = value_of_balance
                player = 'Player 1: ' f'{balance}'
            else:
                position = (i + 1) * 2
                player_num = i + 1
                balance = value_of_balance
                player = f'Player {player_num}: ' f'{balance}'

            card1_image = tk.Label(middle_frame, text='Insert Image Card1', bg='blue', fg='white', font=('Times', 15))
            card2_image = tk.Label(middle_frame, text='Insert Image Card2', bg='blue', fg='white', font=('Times', 15))
            balance_box = tk.Label(bottom_frame, text=player, bg='blue', fg='white', font=('Times', 15))
            bet_size_box = tk.Label(bottom_frame, text='Insert your betsize', bg='blue', fg='white', font=('Times', 15))
            hit_button = tk.Button(bottom_frame, text='HIT', bg='blue', fg='black', font=('Times', 15))
            double_button = tk.Button(bottom_frame, text='DOUBLE', bg='blue', fg='black', font=('Times', 15))
            stand_button = tk.Button(bottom_frame, text='STAND', bg='blue', fg='black', font=('Times', 15))
            split_button = tk.Button(bottom_frame, text='SPLIT', bg='blue', fg='black', font=('Times', 15))

            card1_image.grid(row=0, column=position, rowspan=20, sticky='news', padx=10, pady=10)
            card2_image.grid(row=0, column=position + 1, rowspan=20, sticky='news', padx=10, pady=10)
            balance_box.grid(row=0, column=position, sticky='news', padx=10, pady=10)
            bet_size_box.grid(row=0, column=position + 1, sticky='news', padx=10, pady=10)
            hit_button.grid(row=1, column=position, sticky='news', padx=10, pady=10)
            double_button.grid(row=1, column=position + 1, sticky='news', padx=10, pady=10)
            stand_button.grid(row=2, column=position, sticky='news', padx=10, pady=10)
            split_button.grid(row=2, column=position + 1, sticky='news', padx=10, pady=10)

            bottom_frame.columnconfigure(position, weight=1)
            bottom_frame.columnconfigure(position + 1, weight=1)
            middle_frame.columnconfigure(position, weight=1)
            middle_frame.columnconfigure(position + 1, weight=1)

        bottom_frame.rowconfigure(0, weight=1)
        bottom_frame.rowconfigure(1, weight=1)
        bottom_frame.rowconfigure(2, weight=1)

        middle_frame.rowconfigure(0, weight=1)

        menu_button = tk.Button(top_frame, text='Back To Menu', command=self.menu)
        dealer_name = tk.Label(top_frame, text='Dealer', bg='blue', fg='white', font=('Times', 15))
        dealer_card1_image = tk.Label(top_frame, text='Insert Image Card1', bg='blue', fg='white', font=('Times', 15))
        dealer_card2_image = tk.Label(top_frame, text='Insert Image Card2', bg='blue', fg='white', font=('Times', 15))

        menu_button.grid(row=0, column=0, sticky="nw")
        dealer_name.grid(row=0, column=1, columnspan=2, sticky="news", padx=10, pady=10)
        dealer_card1_image.grid(row=1, column=1, rowspan=20, sticky='news', padx=10, pady=10)
        dealer_card2_image.grid(row=1, column=2, rowspan=20, sticky='news', padx=10, pady=10)

        top_frame.rowconfigure(0, weight=1)
        top_frame.rowconfigure(1, weight=1, minsize=210)

        top_frame.columnconfigure(0, weight=1, minsize=400)
        top_frame.columnconfigure(1, weight=1)
        top_frame.columnconfigure(2, weight=1)
        top_frame.columnconfigure(3, weight=1, minsize=400)

        root.geometry("1250x840")

    def menu(self):
        self.destroy()
        Menu(self.master)

    def window_one(self):
        self.destroy()
        Window_One(self.master)





root.geometry("500x300")
root.resizable(width=0, height=0)

menu = Menu(root)

root.mainloop()

