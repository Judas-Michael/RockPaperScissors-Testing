import random

computerWin = "The computer"
humanWin = "The player"
tieWin = "tie"
#1 = Rock
#2 = Paper
#3 = Scissors

def computer_choose():
   
   	x = random.randint(1,3) #this assigns the computers choice
	
	return x

def human_choose():

   choice = input("Rock, Paper, Scissors?")
   return choice

def who_won(human, computer):

if choice == "Rock" and x == 2:
		winner = computer
	if choice == "Rock" and x == 1:
		winner= tieWin
	if choice == "Rock" and x == 3:
		winner = human
	if choice == "Scissors" and x == 2:
		winner = human
	if choice == "Scissors" and x == 1:
		winner = computer
	if choice == "Rock" and x == 3:
		winner= tieWin
	if choice == "Paper" and x == 2:
		winner = tieWin
	if choice == "Paper" and x == 1:
		winner = human
	if choice =="Paper" and x == 3:
		winner = computer
	return winner

def game():

   c = computer_choose()

   h = human_choose()

   winner = who_won(h, c)
   if winner != tieWin
		print(winner + "is the winner")
	else
		print("It's a tie!")

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
			answer = "Y" #entry validation
			print("That's not an answer!")
		
		
