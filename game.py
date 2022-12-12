import random
import time

def playGame():
    x = 0 
    y = 0 
    cardsArr = {"as":11, "dwojka": 2, "trojka": 3, "czworka": 4, "piatka": 5, "szostka": 6, "siodemka": 7, "osemka": 8, "dziewiatka": 9, "dziesiatka": 10, "walet": 10, "dama": 10, "krol": 10}
    tab = [];
    
    def chance(): 
         
    def get_key(val):
        for key, value in cardsArr.items():
            if val == value:
                return key
    while(True):
        try:
            
            if x == 0:
                card1 = random.choice(list(cardsArr.values()))
                card2 = random.choice(list(cardsArr.values()))
                botCard1 = random.choice(list(cardsArr.values()))
                botCard2 = random.choice(list(cardsArr.values()))
            
            # rand = random.randint(1, 13)
                cardSum = card1 + card2
                botCardSum = botCard1 + botCard2

                if (botCardSum < 17):
                    botCard1 = random.choice(list(cardsArr.values()))
                    botCard2 = random.choice(list(cardsArr.values()))
                    botCardSum = botCard1 + botCard2
                
                if card1 + card2 < 21:
                    print ("Wylosowałeś: " + get_key(card1) + " i " + get_key(card2) + " co oznacza, że masz " + str(cardSum) + " punktów")
                    print ("Przeciwnik wylosował: " + get_key(botCard1) + " i " + " KARTE " + " co oznacza, że ma " + str(botCardSum) + " punktów")
                    y = 1
                    if botCardSum == 21:
                        print("Przegrałeś, przeciwnik ma blackjacka!")
                        break
                tab.append(card1)
                tab.append(card2)

            else:
                cardsArr["as"] = 1
                # print(cardsArr["as"])
                tab.append(card1)
                tab.append(card2)
                print(tab)
                continue
                
                
            answer = input("Czy chcesz dobrać kartę? (y/n): ")  
            if answer == "y":
                
                if y == 1:
                    
                    cardsArr["as"] = 1
                    if card1 == 11 or card2 == 11:
                        cardSum - 10 
                    print(cardSum)
                card3 = random.choice(list(cardsArr.values()))
                cardSum = cardSum + card3
                print ("Wylosowałeś: " + get_key(card3) + " co oznacza, że masz " + str(cardSum) + " punktów")
                if cardSum > 21:
                    print("Przegrałeś!")
                    break
                elif cardSum == 21:
                    print("BLACKJACK!")
                    break
                else: 
                    x = 1
            elif answer == "n":
                if cardSum > botCardSum:
                    print("Wygrałeś!")
                    break
                elif cardSum < botCardSum:
                    print("Przegrałeś!")
                    break
                elif cardSum == botCardSum:
                    print("Remis!")
                    break
            
           
            # print(get_key(11))
            # input(card1)
        except ValueError:
            print(ValueError)
playGame()