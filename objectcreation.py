import classcreation as cc

deck = cc.Deck()
dealer = cc.Dealer("Dealer")
numplayers = None
while not numplayers:
  numplayers_string = input("How many players?: ")
  try:
    numplayers = int(numplayers_string)
  except:
    print("Error")
playerslist = []
for i in range(numplayers):
  playerslist.append(cc.Players(input("Input name: ")))

game = cc.Game(dealer, playerslist, deck)