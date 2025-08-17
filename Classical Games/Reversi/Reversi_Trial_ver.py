# The following Python file demostrates a game of Reversi

import random, time

# define starting position
black_pos=[(4,4),(5,5)]
white_pos=[(4,5),(5,4)]
empty_pos=[]
for i in range(8):
    for j in range(8):
        empty_pos += [(i+1,j+1)]
for x in black_pos:
    empty_pos.remove(x)
for x in white_pos:
    empty_pos.remove(x)
chess_board=[]
for i in range(8):
    for j in range(8):
        chess_board += [(i+1,j+1)]

Black_Turn = True
White_Turn = False
Win = False

# compute the outcomes if valid, count score for algorithm (not yet due to my poor coding skills)
def valid_pos(black_pos,white_pos,empty_pos,new_pos,new_pos_x,new_pos_y,Black_Turn,White_Turn):
    t=0
    if Black_Turn == True:
        for i in range(-1,2):
            for j in range(-1,2):
                if (i,j) != (0,0):
                    if (new_pos_x+i,new_pos_y+j) in white_pos:
                        for count in range(1,9):
                            check_pos=(new_pos_x+i*count,new_pos_y+j*count)
                            if check_pos in black_pos:
                                for c in range(1,count):
                                    check_pos=(new_pos_x+i*c,new_pos_y+j*c)
                                    black_pos.append(check_pos)
                                    white_pos.remove(check_pos)
                                t += count - 1
                                break
                            if check_pos in empty_pos:
                                break
    if White_Turn == True:
        for i in range(-1,2):
            for j in range(-1,2):
                if (i,j) != (0,0):
                    if (new_pos_x+i,new_pos_y+j) in black_pos:
                        for count in range(1,9):
                            check_pos=(new_pos_x+i*count,new_pos_y+j*count)
                            if check_pos in white_pos:
                                for c in range(1,count):
                                    check_pos=(new_pos_x+i*c,new_pos_y+j*c)
                                    white_pos.append(check_pos)
                                    black_pos.remove(check_pos)
                                t += count - 1
                                break
                            if check_pos in empty_pos:
                                break
    return t

# check whether valid move exists
def Validity(black_pos,white_pos,empty_pos,Black_Turn,White_Turn):
    Valid_List=[]
    for place in empty_pos:
        x = int(place[0])
        y = int(place[1])
        if Black_Turn == True:
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i,j) != (0,0):
                        if (x+i,y+j) in white_pos:
                            for count in range(1,9):
                                check_pos=(x+i*count,y+j*count)
                                if check_pos in black_pos and place not in Valid_List:
                                    Valid_List.append(place)
                                    break
                                if check_pos in empty_pos:
                                    break                           
        if White_Turn == True:
            for i in range(-1,2):
                for j in range(-1,2):
                    if (i,j) != (0,0):
                        if (x+i,y+j) in black_pos:
                            for count in range(1,9):
                                check_pos=(x+i*count,y+j*count)
                                if check_pos in white_pos and place not in Valid_List:
                                    Valid_List.append(place)
                                    break
                                if check_pos in empty_pos:
                                    break
    return Valid_List

# Print current position
def print_board(black_pos,white_pos,empty_pos):
    for i in range(1,9):
        line=''
        for j in range(1,9):
            if (i,j) in black_pos:
                line += ' X'
            elif (i,j) in white_pos:
                line += ' O'
            else: line += ' _'
        print(line)

# Place a new piece (pvp)
def pvp(black_pos,white_pos,empty_pos,Win,Black_Turn,White_Turn):
    while Win == False:
        print_board(black_pos,white_pos,empty_pos)
        if Black_Turn == True:
            print("Black's turn")
        elif White_Turn == True: 
            print("White's turn")
        exist = Validity(black_pos,white_pos,empty_pos,Black_Turn,White_Turn)
        print('The valid positions are', exist)
        while True:
            if Black_Turn == True and exist == []:
                print("There is no valid position for Black. White's turn.")
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif White_Turn == True and exist == []:
                print("There is no valid position for White. Black's turn.")
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            else: new_pos_x = int(input('Please enter x-coordinate (1-8):'))
            new_pos_y = int(input('Please enter y-coordinate (1-8):'))
            new_pos = (new_pos_x,new_pos_y)
            if new_pos in exist:
                empty_pos.remove(new_pos)
                if Black_Turn == True:
                    black_pos.append(new_pos)
                if White_Turn == True:
                    white_pos.append(new_pos)
                valid_pos(black_pos,white_pos,empty_pos,new_pos,new_pos_x,new_pos_y,Black_Turn,White_Turn)
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif new_pos not in empty_pos:
                print('Please place on an empty spot.')
            else: print('This is not a valid position.')
        if black_pos == [] or white_pos == [] or empty_pos == []:
            Win = True
    return Win

# Place a new piece (pvc)
def pvc(black_pos,white_pos,empty_pos,Win,Black_Turn,White_Turn):
    while Win == False:
        print_board(black_pos,white_pos,empty_pos)
        if Black_Turn == True:
            print("Black's turn")
        else: print("White's turn")
        exist = Validity(black_pos,white_pos,empty_pos,Black_Turn,White_Turn)
        print('The valid positions are', exist)
        while True:
            if Black_Turn == True and exist == []:
                print("There is no valid position for Black. White's turn.")
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif White_Turn == True and exist == []:
                print("There is no valid position for White. Black's turn.")
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif Black_Turn == True: 
                new_pos_x = int(input('Please enter x-coordinate (1-8):'))
                new_pos_y = int(input('Please enter y-coordinate (1-8):'))
                new_pos = (new_pos_x,new_pos_y)
            elif White_Turn == True: 
                new_pos = random.choice(exist)
                print('White placed on', new_pos,'.')
                new_pos_x = int(new_pos[0])
                new_pos_y = int(new_pos[1])
            if new_pos in exist:
                empty_pos.remove(new_pos)
                if Black_Turn == True:
                    black_pos.append(new_pos)
                if White_Turn == True:
                    white_pos.append(new_pos)
                valid_pos(black_pos,white_pos,empty_pos,new_pos,new_pos_x,new_pos_y,Black_Turn,White_Turn)
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif new_pos not in empty_pos:
                print('Please place on an empty spot.')
            else: print('This is not a valid position.')
        if black_pos == [] or white_pos == [] or empty_pos == []:
            Win = True
    return Win

# Place a new piece (auto)
def auto(black_pos,white_pos,empty_pos,Win,Black_Turn,White_Turn):
    while Win == False:
        time.sleep(0.5)
        print_board(black_pos,white_pos,empty_pos)
        if Black_Turn == True:
            print("Black's turn")
        else: print("White's turn")
        exist = Validity(black_pos,white_pos,empty_pos,Black_Turn,White_Turn)
        print('The valid positions are', exist)
        while True:
            if Black_Turn == True and exist == []:
                print("There is no valid position for Black. White's turn.")
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif White_Turn == True and exist == []:
                print("There is no valid position for White. Black's turn.")
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif Black_Turn == True: 
                new_pos = random.choice(exist)
                print('Black placed on', new_pos,'.')
                new_pos_x = int(new_pos[0])
                new_pos_y = int(new_pos[1])
            elif White_Turn == True: 
                new_pos = random.choice(exist)
                print('White placed on', new_pos,'.')
                new_pos_x = int(new_pos[0])
                new_pos_y = int(new_pos[1])
            if new_pos in exist:
                empty_pos.remove(new_pos)
                if Black_Turn == True:
                    black_pos.append(new_pos)
                if White_Turn == True:
                    white_pos.append(new_pos)
                valid_pos(black_pos,white_pos,empty_pos,new_pos,new_pos_x,new_pos_y,Black_Turn,White_Turn)
                Black_Turn = not Black_Turn
                White_Turn = not White_Turn
                break
            elif new_pos not in empty_pos:
                print('Please place on an empty spot.')
            else: print('This is not a valid position.')
        if black_pos == [] or white_pos == [] or empty_pos == []:
            Win = True
    return True

# Select Game Mode
Mode_Selected = False
while Mode_Selected = False:
    Mode = int(input('Please select game mode: 1. pvp; 2. pvc (default: Black), 3. auto. Type the number:'))
    if Mode == 1:
        Win = pvp(black_pos,white_pos,empty_pos,Win,Black_Turn,White_Turn)
        Mode_Selected = True
    elif Mode == 2:
        Win = pvc(black_pos,white_pos,empty_pos,Win,Black_Turn,White_Turn)
        Mode_Selected = True
    elif Mode == 3: 
        Win = auto(black_pos,white_pos,empty_pos,Win,Black_Turn,White_Turn)
        Mode_Selected = True
    else: print('Please select a number among 1, 2 and 3.')

# display victory
if Win == True:
    print_board(black_pos,white_pos,empty_pos)
    if len(black_pos)>len(white_pos):
        print('Black wins by', len(black_pos) - len(white_pos),'!')
    elif len(black_pos)<len(white_pos):
        print('White wins by', -len(black_pos) + len(white_pos),'!')
    else: print('Tie!')

