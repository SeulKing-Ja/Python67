import random as rd

spots = {1 : 'o|', 2 : 'o|', 3 : 'o|', 4 : 'o|', 5 : 'o|', 6 : 'o|',\
        7 : 'o|', 8 : 'o|', 9 : 'o|', 10: 'o|', 11 : 'o|', 12 : 'o|', \
        13 : 'o|', 14 : 'o|', 15 : 'o|', 16 : 'o|', 17 : 'o|', 18 : 'o|', \
        19 : 'o|', 20 : 'o|', 21 : 'o|', 22 : 'o|', 23 : 'o|', 24 : 'o|', \
        25 : 'o|', 26 : 'o|', 27 : 'o|', 28 : 'o|', 29 : 'o|', 30 : 'o|', \
        31 : 'o|', 32 : 'o|', 33 : 'o|', 34 : 'o|', 35 : 'o|', 36 : 'o|'}

#FUNCTION
def create_board(spots):
    for i in spots:
        if i % 6 == 0:
            print(spots[i], end='')
            print()
        else:
            print(spots[i], end='')

def plays(spots, select, who):
    select = select + 30
    while True:
        if spots[select] == 'o|' and who:
            if who == 'Player':
                new = {select : 'P|'}
                spots.update(new)
                break
            elif who == 'Computer':
                new = {select : 'C|'}
                spots.update(new)
                break
        else:         
            select =select - 6        
    return spots

def win(player):
        for cols in range(1,6):
           if  spots[cols] == player and spots[cols+7] == player and spots[cols+14] == player or spots[cols] == player and spots[cols+1] == player and spots[cols+2] == player:
               return(True)
           elif spots[cols] == player and spots[cols+1] == player and spots[cols+2] == player:
               return(True)
           elif spots[cols] == player and spots[cols+6] == player and spots[cols+12] == player:
               return(True)

#MAIN
create_board(spots)
while True:
    if win('P|'):
        print('Player Win!!!')
        break
    elif win('C|'):
        print('Computer Win!!!')
        break
    #Player Turn
    Player = int(input('Enter Row:'))
    plays(spots, Player, 'Player')
    create_board(spots)

    #Computer Turn
    Computer = rd.randint(1, 6)
    print('Computer Select',Computer)
    plays(spots, Computer, 'Computer')
    create_board(spots)