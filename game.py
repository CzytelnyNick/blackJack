import random
import time
import sys
def playGame():
    x = 0 
    y = 0 
    
    cardsArr = {"as":11, "dwojka": 2, "trojka": 3, "czworka": 4, "piatka": 5, "szostka": 6, "siodemka": 7, "osemka": 8, "dziewiatka": 9, "dziesiatka": 10, "walet": 10, "dama": 10, "krol": 10}
    tab = []
    
    botCardSum = 0
    tab2= []
    def get_key(val):
        for key, value in cardsArr.items():
            if val == value:
                return key
    card1 = random.choice(list(cardsArr.values()))
    card2 = random.choice(list(cardsArr.values()))
    cardSum = card1 + card2
    j=1
    # botCard1 = random.choice(list(cardsArr.values())) 
    botCard1 = 11
    botCard2 = random.choice(list(cardsArr.values()))
    botCardSum = botCard1 + botCard2
    tab2.append(get_key(botCard1))
    tab2.append(get_key(botCard2))
    
    print ("Wylosowałeś: " + get_key(card1) + " i " + get_key(card2) + " co oznacza, że masz " + str(cardSum) + " punktów") 
    print("Bot wylosował " + get_key(botCard1) + " i  * ")
    if cardSum == 21:
                    print("CZARNYJACEK WYGRAŁEŚ")
                    answer="n"
                    sys.exit()
    while(True):
        try:
                
            answer = input("Czy chcesz dobrać kartę? (y/n): ")  
            if answer == "y":
                if card1 == 11 or card2 == 11:
                    cardSum -= 10
                cardsArr["as"] = 1
                
                card3 = random.choice(list(cardsArr.values()))
                # card3 = cardsArr["as"]
                cardSum += card3
                print ("Wylosowałeś: " + get_key(card3) + " co oznacza, że masz " + str(cardSum) + " punktów")
                if cardSum > 21:
                    print("Przegrałeś!")
                    answer="n"
                    j=0
                if cardSum == 21:
                    print("CZARNYJACEK WYGRAŁEŚ")
                    answer="n"
                    
                    j=0

            if answer == "n":
                cardsArr["as"] = 11
                
                if j == 0:
                    break
                while(True):
                        
                        
                        if(botCardSum >= 17):
                            value=0
                        else:
                            value = random.randint(0,1)
                            
                        
                        if value == 0:
                           
                            break
                        elif value == 1: 
                            
                                if card1 == 11 or card2 == 11:
                                    cardSum -= 10
                                cardsArr["as"] = 1
                                # botCard3 = random.choice(list(cardsArr.values()))
                                botCard3 = 11
                                
                                botCardSum += botCard3
                                tab2.append(get_key(botCard3))
                                print("Bot dobrał " + get_key(botCard3) + " i ma " + str(botCardSum) + " pkt")
                            
                    
                
                print("Bot wylosował: ", tab2, end="")
                print(" i ma " + str(botCardSum) + " pkt")
                
                if botCardSum > 21:
                    print("Wygrałeś!")
                    break
                
                elif botCardSum == 21:
                    print("CZARNYJACEK PRZEGRAŁEŚ")
                    break
                elif cardSum == botCardSum:
                    print("Remis!")
                    break
                elif cardSum < botCardSum:
                    print("Przegrałeś")
                    break
                elif cardSum > botCardSum:
                    print("Wygrałeś")
                    break
            
            # print(get_key(11))
            # input(card1)
        except ValueError:
            print(ValueError)
playGame()