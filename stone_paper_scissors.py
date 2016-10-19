import getpass
import sys
def player_name(game_flag = False):
    global player1 
    global player2
    global high_score
    player1 = raw_input("Enter player 1 name: ")
    player2 = raw_input("Enter player 2 name: ")
    high_score = int(raw_input("Enter the score limit: "))
    
    new_game()

def menu():
    string = '''STONE PAPER SCISSORS\n
                1. New Game\n
		2. Change Player Names\n
		3. Instructions\n
		4. Quit\n'''
    print string
    choice = input("Enter your choice: ")

    if choice == 1 or choice == 2:
        player_name(game_flag = True)
    elif choice == 3:
        display_instructions()
    else:
        sys.exit('Invalid choice or quit chosen')

def new_game():
    allowed = ['s', 'p', 'r']
    choice_flag = False
    p1score = 0
    p2score = 0
    score_check = 0
    while score_check < high_score:
        while not choice_flag:
            p1choice = getpass.getpass("Player 1 turn: ")
            if p1choice.lower() not in allowed:
	        print "invalid choice try again\n"
            else:
                choice_flag = True
    
        choice_flag = False
        while not choice_flag:
	    p2choice = getpass.getpass("Player 2 turn: ")
	    if p2choice.lower() not in allowed:
	        print "invalid choice try again\n"
	    else:
                choice_flag = True
        choice_flag = False	
	if p1choice == p2choice:
	    continue
        elif p1choice == 'r' and p2choice == 's':
	    p1score += 1
	elif p1choice == 's' and p2choice == 'p':
	    p1score += 1
	elif p2choice == 'p' and p2choice == 'r':
	    p1score += 1
	else:
	    p2score += 1
	score_check = max(p1score,p2score)
    
    if p1score > p2score:
	print "%s wins\n"%player1
    else:
	print "%s wins\n"%player2

    menu()

def display_instructions():
    print ''' INSTRUCTIONS:\n
              1. Allowed inputs are:\n
	             STONE = r\n
		     PAPER = p\n
		     SCISSORS = s\n
	      2. Stone beats Scissors\n
	         Paper beats Stone\n
		 Scissors beats Paper\n
              3. The first player to reach high score wins\n'''
    menu()	 

if __name__ == '__main__': 
    menu()
