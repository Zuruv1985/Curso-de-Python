import random


def choose_options():
    opciones= ("piedra","papel","tijera")
    user_option= input("Escribe piedra, papel o tijera ==>  " ).lower()
            
    if not user_option in opciones:
        print(" Ingrese una opción valida")
        return None, None
    computer_option = random.choice (opciones)
    print("-"*30)
    print ("Has elegido ", user_option)  
    print ("La computadora ha elegido " + computer_option)
    return user_option, computer_option
    
def check_rules(user_option, computer_option, user_wins , computer_wins):
    if user_option==computer_option:
        print ("Has empatado con la computadora")

    elif user_option== "piedra":
        if computer_option=="tijera":
            print ("Felicidades, has ganado")
            user_wins += 1
        elif computer_option == "papel":
            print ("Lo siento. Has perdido esta ronda")
            computer_wins += 1
    elif user_option == "papel":    
        if computer_option == "piedra":
            print ("Felicidades, has ganado")
            user_wins += 1
        elif computer_option == "tijera":
            print ("Lo siento. Has perdido esta ronda")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print ("Felicidades, has ganado")
            user_wins += 1

        elif computer_option == "piedra":
            print ("Lo siento. Has perdido esta ronda")
            computer_wins += 1
    return user_wins, computer_wins


def run_game():
    rounds=1
    computer_wins = 0
    user_wins = 0

    while True:
        print()
        print ("*" *30)
        print ("RONDA # => ", rounds)
        print ("Ganes de la computadora => ", computer_wins)
        print("Ganes del Usuario => ", user_wins)
        print ("*" * 30)
        print()
        rounds += 1

        user_option, computer_option= choose_options() 
        user_wins, computer_wins= check_rules(user_option, computer_option, user_wins, computer_wins)  
        
        if computer_wins == 2:
            print ("LA COMPUTADORA HA GANADO LA PARTIDA")
            exit()
        if user_wins == 2:
            print ("EN HORA BUENA, LE HAS GANADO LA PARTIDA A LA COMPUTADORA")
            exit()    
run_game()
            

