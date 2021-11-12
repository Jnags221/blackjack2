import objectcreation as oc

def round_creation():
    numrounds = None
    while not numrounds:
        numrounds_string = input("How many rounds would you like to play?: ")
        try:
            numrounds = int(numrounds_string)
        except:
            print("Error")

    for i in range(numrounds):
        oc.game.round()
