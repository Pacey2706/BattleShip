# art from https://ascii.co.uk/ and https://asciiart.website/
print(r"""   
 _           _   _   _           _     _  
| |         | | | | | |         | |   (_)      
| |__   __ _| |_| |_| | ___  ___| |__  _ _ __  
| '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
|_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
                                        | |    
                                        |_|       
             )_)  )_)  )_)
            )___))___))___)\
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------""")
# Start game from user input yes or no
start_game = input("Would you like to play battleships? (yes/no)")
while start_game == "yes" or "no":
    if start_game == "yes":
        main()
    elif start_game == "no":
        quit()
    else: 
        start_game = input("please choose either (yes/no)")

PLAYER_BOARD = [ ] #set boards as 5/5
COMPUTER_BOARD =[ ]

def print_board():
    pass

def create_computerships():
    pass

def computers_turn():
    pass

def players_turn():
    pass

def main():
    pass

