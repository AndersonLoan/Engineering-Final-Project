

import random
#create the deck
deck = ["A","K","Q","J","10","9","8","7","6","5","4","3","2","1","A","K","Q","J","10","9","8","7","6","5","4","3","2","1","A","K","Q","J","10","9","8","7","6","5","4","3","2","1","A","K","Q","J","10","9","8","7","6","5","4","3","2","1",]
player = []
dealer = []
PT = 0
DT = 0
y = 0





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
                y += 11
            elif(i != "A"):
                y += 10
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
    
def blackjack():
    Game_playing = True
    PlayerTurn = True
    DealerTurn = True
    print("Your goal is to get your points as close to 21 without going over and beating the dealers points.")
    print("You will do this by after you get dealt 2 cards you will press \'h\' if you want another card and \'g\' if you want to stay")
    print("If you and the dealer have the same total it will be a push and you will tie")
    print()
    a = input("Press s to start the game! Or q to go back to main menu ")  
    while(True):
        if(a == "q"):
            break
        if(a == "s"):
        #if(key.is_pressed("s")):
            while(Game_playing):
                    Pdeal()
                    Ddeal()
                    Pdeal()
                    Ddeal()
                    print(f'Player\'s cards {player}')
                    PT = cal(player,0)
                    print(f'Player\'s total {PT}')
                    print()
                    while(PlayerTurn == True and PT < 21):
                        print()
                        #if(key.is_pressed("h")):
                        b = input("Press h if you want another card or press g if you want to stay with the cards you have! ")
                        
                        while(b == "h" and PT < 21 and b != "h"):
                            Pdeal()
                            PT = cal(player,0)
                            print(f'Player\'s cards {player}')
                            print(f'Player\'s total {PT}')   
                            if(PT > 21):
                                print()
                                print("You went over 21 you lose")
                                break
                            print()
                            if(PT < 21):
                                b = input("Press g if you want to stay with your current cards or press h again for another card ")
                                print(b)
                                if(b == "g"):
                                    break
                        if(b == 'g'):
                            break 
                    if(PT>21):
                        break
                        
                        DT = cal(dealer,0)
                        print()
                        print(f'Dealer\'s cards {dealer}')
                        print(f'Dealer\'s total {DT}')
                    
                    while(DealerTurn == True):
                        if(DT < 17):
                            Ddeal()
                            DT = cal(dealer,0)
                            print()
                            print(f'Dealer\'s cards {dealer}')
                            print(f'Dealer\'s total {DT}')
                            if(DT > 21):
                                print()
                                print("The dealer went over 21 you Win")
                                break
                            if(DT > 16):
                                DealerTurn = False
                                if(DT > 21):
                                    Game_playing = False
                                    break
                                print()
                    if(DT>21):
                        break
                         
                    if(DT < 21 and PT < 21):
                        if(DT > PT):
                            print(f'Dealer\'s total {DT}')
                            print(f'Player\'s total {PT}') 
                            print()
                            print("The dealer has a higher value than you, you lose :(")
                            Game_playing = False
                        elif(PT > DT):
                            print(f'Dealer\'s total {DT}')
                            print(f'Player\'s total {PT}') 
                            print()
                            print("The dealer has a lower value than you, you win!!")  
                            Game_playing = False
                        elif(PT == DT):
                            print(f'Dealer\'s total {DT}')
                            print(f'Player\'s total {PT}') 
                            print()
                            print("You and the dealer had the same value it is a push!")
                            Game_playing = False
            break

    

        
