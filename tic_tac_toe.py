def print_table(n):
    for i in range(n):
	print ' ---'*n
	print '|   '*int(n+1)
    print ' ---'*n

def tic_tac_toe_checker(game):

    for i in range(3):
	v = game[0][i]+game[1][i]+game[2][i]
        h = game[i][0]+game[i][1]+game[i][2]

        if v == 'xxx' or h == 'xxx':
	    return 1
        if v == 'ooo' or h == 'ooo':
	    return 2
    
    d = game[0][0]+game[1][1]+game[2][2]
    od = game[0][2]+game[1][1]+game[2][0]
    if d == 'xxx' or od == 'xxx':
        return 1
    if d == 'ooo' or od == 'ooo':
	return 2
    
    return-1

def print_game(game):
    for i in range(3):
	print game[i]

def modify_table(game):
    j = 0
    c = 0
    for i in range(3): 
	print ' ---'*3
        for j in range(3):
	    print '| %s'%game[i][j],
	print '|'
    print ' ---'*3

def validate_input(s):
    pass    

def new_game():
    game = [[' ', ' ', ' '],[' ', ' ', ' '], [' ', ' ', ' ']]
    s = -1
    count = 1
    list_co = []
    modify_table(game)
    while s < 0 :
	if count <= 9:
	    print "chance of player %d" %(count %2 if count%2 != 0 else 2)
	    sa = raw_input("Enter x and y: ").split()
	    if len(sa) != 2:
	        print "Invalid input" 
	        continue
	    x,y = map(int,sa)
	    if x > 3 or y > 3:
	        print "Invalid Input"
	        continue
	    tup = [x,y]
	    if tup in list_co:
                print "already occupied"
	        modify_table(game)
	        continue
	    count += 1
	    list_co.append(tup)
	    game[x-1][y-1] = 'x' if count % 2 != 0 else 'o'
            modify_table(game)
            s = tic_tac_toe_checker(game)
	else:
            break

    if s == 1:
	print "Player 1 wins"
    elif s == 2:
	print "Player 2 wins"
    else:
	print "Draw"

if __name__ == '__main__':
    new_game()
