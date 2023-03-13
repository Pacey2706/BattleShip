# art from https://ascii.co.uk/ and https://asciiart.website/
# print(r"""   
#  _           _   _   _           _     _  
# | |         | | | | | |         | |   (_)      
# | |__   __ _| |_| |_| | ___  ___| |__  _ _ __  
# | '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \ 
# | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) |
# |_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/ 
#                                         | |    
#                                         |_|       
#              )_)  )_)  )_)
#             )___))___))___)\
#            )____)____)_____)\\
#          _____|____|____|____\\\__
# ---------\                   /---------""")
# # Start game from user input yes or no
# start_game = input("Would you like to play battleships? (yes/no)")
# while start_game == "yes" or "no":
#     if start_game == "yes":
#         main()
#     elif start_game == "no":
#         quit()
#     else: 
#         start_game = input("please choose either (yes/no)")


PLAYER_BOARD = []
for x in range(5):
    PLAYER_BOARD.append(["~"] * 5)

COMPUTER_BOARD = []
for x in range(5):
    COMPUTER_BOARD.append(["~"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))
print(print_board(COMPUTER_BOARD))

def create_computerships():
    pass

def computers_turn():
    pass

def players_turn():
    pass

def main():
    pass

