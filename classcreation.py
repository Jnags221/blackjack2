import random


# This class creates the players and the dealer

class People():
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.cardsvalue = 0
        self.cardsvaluelist = []

    # This creates and deals two cards to the players and the dealer

    def initialcards(self, deck):
        card1, card1value = deck.getcard()
        card2, card2value = deck.getcard()
        self.cards.append(card1)
        self.cardsvalue += card1value
        self.cardsvaluelist.append(card1value)
        self.cards.append(card2)
        self.cardsvalue += card2value
        self.cardsvaluelist.append(card2value)

    # This creates the method which allows the players and the dealer to hit

    def hit(self, deck):
        card, cardvalue = deck.getcard()
        self.cards.append(card)
        self.cardsvalue += cardvalue
        self.cardsvaluelist.append(cardvalue)

    def Aces(self):
        count = 0
        for card in self.cardsvaluelist:
            if card == 11:
                count += 1
        while (self.cardsvalue > 21) and (count > 0):
            count -= 1
            self.cardsvalue -= 10

    def clearcards(self):
        self.cards = []
        self.cardsvalue = 0
        self.cardsvaluelist = []

    # This class creates the Dealer


class Dealer(People):

    def __init__(self, name):
        super(Dealer, self).__init__(name)


# This creates the Players

class Players(People):

    def __init__(self, name, balance=1000):
        super(Players, self).__init__(name)
        self.balance = balance
        self.bet = 0

    def placebet(self, amount):
        if amount <= self.balance:
            self.bet = 0
            self.balance -= amount
            self.bet += amount
        else:
            self.bet(int(input("{}, Out of your budget, Enter valid amount: ".format(self.name))))

    def double(self, deck):
        self.hit(deck)
        self.balance -= self.bet
        self.bet *= 2

    def win(self):
        if (self.cardsvaluelist[0] + self.cardsvaluelist[1]) == 21:
            self.balance += 2.5 * self.bet
        else:
            self.balance += 2 * self.bet


# This creates the Deck

class Deck():
    def __init__(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        # This creates the pack

        self.pack = []
        for suit in range(len(self.suits)):
            for value in range(len(self.values)):
                self.pack.append(self.values[value] + " of " + self.suits[suit])

        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4,
                       5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.packvalues = list(zip(self.pack, self.values))

        random.shuffle(self.packvalues)
        self.pack, self.values = zip(*self.packvalues)
        self.pack = list(self.pack)
        self.values = list(self.values)

    def getcard(self):
        return self.pack.pop(), self.values.pop()

    def reset(self):
        self.suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        # This creates the pack

        self.pack = []
        for suit in range(len(self.suits)):
            for value in range(len(self.values)):
                self.pack.append(self.values[value] + " of " + self.suits[suit])

        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4,
                       5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

        self.packvalues = list(zip(self.pack, self.values))

        random.shuffle(self.packvalues)
        self.pack, self.values = zip(*self.packvalues)
        self.pack = list(self.pack)
        self.values = list(self.values)


class Game():
    def __init__(self, dealer, players, deck):
        self.dealer = dealer
        self.players = players
        self.deck = deck

    def round(self):
        self.dealer.initialcards(self.deck)

        for playerbet in self.players:
            print("{},".format(playerbet.name), "Your balance is: {}".format(playerbet.balance))
            amount = float(input("{}, How much would you like to bet?: ".format(playerbet.name)))
            playerbet.placebet(amount)

        for playerdeal in self.players:
            playerdeal.initialcards(self.deck)
            print(playerdeal.cards)
        print(self.dealer.cards[0])
        for playerturn in self.players:
            playerturn.Aces()
            if playerturn.cardsvalue < 21:
                choice = input("{} would you like to Hit, Double or Stand?: ".format(playerturn.name))
            else:
                choice = "Stand"
            while choice == "Hit":
                playerturn.hit(self.deck)
                print(playerturn.cards)
                playerturn.Aces()
                if playerturn.cardsvalue < 21:
                    choice = input("Would you like to Hit or Stand?: ")
                else:
                    choice = "Stand"

            if choice == "Double":
                playerturn.double(self.deck)
                print(playerturn.cards)
        print(self.dealer.cards)
        while self.dealer.cardsvalue <= 16:
            self.dealer.hit(self.deck)
            self.dealer.Aces()
        print(self.dealer.cards)

        for playercheck in self.players:

            if (playercheck.cardsvalue <= 21) and (self.dealer.cardsvalue <= 21) and (
                    playercheck.cardsvalue > self.dealer.cardsvalue):
                playercheck.win()
                print("{}, You have won.".format(playercheck.name),
                      "Your balance is now {}".format(playercheck.balance))

            elif (playercheck.cardsvaluelist[0] + playercheck.cardsvaluelist[1] == 21) and (
                    self.dealer.cardsvalue == 21):
                playercheck.win()
                print("{}, You have won.".format(playercheck.name),
                      "Your balance is now {}".format(playercheck.balance))

            elif playercheck.cardsvalue == self.dealer.cardsvalue:
                playercheck.balance += playercheck.bet
                print("{}, You have tied.".format(playercheck.name),
                      "Your balance is now {}".format(playercheck.balance))

            else:
                print("{}, You have lost.".format(playercheck.name),
                      "Your balance is now {}".format(playercheck.balance))

        self.dealer.clearcards()
        for playerclear in self.players:
            playerclear.bet = 0
            playerclear.clearcards()

        self.deck.reset()
