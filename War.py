import random
deck = ["A","K","Q","J","10","9","8","7","6","5","4","3","2","1","A","K","Q","J","10","9","8","7","6","5","4","3","2","1","A","K","Q","J","10","9","8","7","6","5","4","3","2","1","A","K","Q","J","10","9","8","7","6","5","4","3","2","1"]
player = []
p = []
dealer = []
d = []
tie = []
PT = 0
DT = 0







def cal(a,y):
    '''
    calculates the points of the player/ dealer
    
    Parameters
    ----------
    a : list
        it is the player or dealers deck.
    y : int
        it is the points of the player/dealer.

    Returns
    -------
    y : int
        is the points after calculation.

    '''
    for i in a:
        try:
            y += int(i)
        except:
            if(i == "A"):
                y += 14
            elif(i == "K"):
                y += 13
            elif(i == "Q"):
                y += 12
            elif(i == "J"):
                y += 11
    return y


def Pdeal():
    '''
    Deals to the players deck

    '''
    i = random.randint(0,len(deck)-1)
    player.append(deck[i]) 
    del deck[i]
        
        
def Ddeal():
    '''
    Deals to the Dealers deck

    '''
    i = random.randint(0,len(deck)-1)
    dealer.append(deck[i])    
    del deck[i]
    
    
for i in range(len(deck)//2):
    Pdeal()
    Ddeal()

def war():
    
    print("Your goal for War is to have a higher card than your opponent and be the last one left with cards!!")
    a = input("Press a if you want to place down a card or press g to end the game! ").lower()
    while(len(player) != 0 and len(dealer) != 0):
        if(a == "a"):
            p.append(player[0])
            del player[0]
            d.append(dealer[0])
            del dealer [0]
            PT = cal(p,0)
            DT = cal(d,0)
            print(f" Player 1\'s points {PT}")
            print(f" Player 2\'s points {DT}")
            if(PT > DT):
                print("Player 1 wins this round!")
                player.append(p[0])
                player.append(d[0])
                del p[0:]
                del d[0:]
            elif(DT > PT):
                print("Player 2 wins this round!")
                dealer.append(p[0])
                dealer.append(d[0])
                del p[0:]
                del d[0:]
            else:
                print("You tied nobody wins")
                player.append(p[0])
                dealer.append(d[0])
                del p[0:]
                del d[0:]
        elif(a == "g"):
            break
        a = input("Press a if you want to play a card or press g to end the game! ")
            
        
        
    if(len(player) < len(dealer)):
        print("Player 2 wins")
    if(len(dealer) < len(player)):
        print("PLayer 1 wins")
        
        
        
        
        
        
        
        
        
    