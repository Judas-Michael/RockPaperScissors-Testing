import Rock_Paper_Scissors
from unittest import TestCase

class testGame(TestCase):
	
	def test_winner(self):
	
		winner = Rock_Paper_Scissors.who_won('Rock', 2) #sends rock and 2 to who won, saves result
		self.assertEqual(winner, "The computer") #compares result to what the answer should be
		
		winner = Rock_Paper_Scissors.who_won('Scissors', 1) #sends scissors and 1 to who won, saves result
		self.assertEqual(winner, "The computer") #compares result to what the answer should be
		
		winner = Rock_Paper_Scissors.who_won('Rock', 1) #sends rock and 1 to who won, saves result
		self.assertEqual(winner, "tie") #compares result to what the answer should be
		
		winner = Rock_Paper_Scissors.who_won('Paper', 1) #sends Paper and 1 to who won, saves result
		self.assertEqual(winner, "The player") #compares result to what the answer should be
		self.assertIsNot(winner, "tie") #makes sure that the winner is not a tie
		
	def test_random_value(self):
	
		x = Rock_Paper_Scissors.computer_choose() #gets random value from computer chose
		self.assertNotEqual(x, 4) #random integer is not 4
		
	def test_saves_value(self):
		choice = Rock_Paper_Scissors.computer_choose() #gets integer from computer choice
		self.assertIsNotNone(choice) #makes sure there is a value saved
		
		
