import random
def roll():
    dice1 = random.randrange(1,7)
    dice2 = random.randrange(1,7)
    return (dice1, dice2)

first_roll = roll() 
contnue = "NO"
if sum(first_roll) in (7, 11):
    print("WON, first time")
elif sum(first_roll) in (2,3,12):
    print( "CRAPS, LOST")
else:
    firsthand = sum(first_roll)
    contnue = "YES"

while ( contnue == "YES" ) :
    rolling = roll() 
    if sum(rolling) == first_roll:
        contnue = "NO"
        print( "WON, with same number" )
    elif sum(rolling) == 7:
        contnue = "NO"
        print("LOST, 7 came")
    else:
        print ("Continue with sum {}".format(sum(rolling)))
        contnue

