import random

computerWin = "The computer"
humanWin = "The player"
tieWin = "tie"
#1 = Rock
#2 = Paper
#3 = Scissors


def main():

	answer = "Y"

	while (answer != "N"):#asks to start game

		answer = input("Wanna play 'Rock Paper Scissors'? (Y or N) ")
		if answer == "Y":
			print("Cool!")
			game()
	
		if answer == "N":
			print("Oh.... ok")
		else:
			print("That's not an answer!")
			answer = "Y" #entry validation
		

def computer_choose():
	x = random.randint(1,3) #this assigns the computers choice
	return x

def human_choose():

   choice = input("Rock, Paper, Scissors?")
   return choice

def who_won(human, computer):

	if human == "Rock" and computer == 2:
		winner = computerWin
	if human == "Rock" and computer == 1:
		winner= tieWin
	if human == "Rock" and computer == 3:
		winner = humanWin
	if human == "Scissors" and computer == 2:
		winner = humanWin
	if human == "Scissors" and computer == 1:
		winner = computerWin
	if human == "Rock" and computer == 3:
		winner= tieWin
	if human == "Paper" and computer == 2:
		winner = tieWin
	if human == "Paper" and computer == 1:
		winner = humanWin
	if human =="Paper" and computer == 3:
		winner = computerWin
	return winner

def game():
	c = computer_choose()
	h = human_choose()
	winner = who_won(h, c)
	
	if winner == "tie":
		print("It's a tie!")
	else:
		print(winner + " is the winner")
		
if __name__ == "__main__": main()


		
