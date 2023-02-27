#Hangman
# Import random word library
from random_word import RandomWords
r = RandomWords()
# Return a single random word
ran_word = r.get_random_word()
print(ran_word)
#hide the word
hidden_ran_word = '*' * len(ran_word)
print(hidden_ran_word)

#ask player to guess a letter

while True:
	guess = str(input('Guess a letter: '))
	global guess
	if guess.isalpha(): #possibly call the is_in_ran_word function?
		print('Thank you')
		break
	else:
		print('Only enter letters please! ')
#Convert random word to list
hidden_ran_word = list(hidden_ran_word)

#check if letter in secret word
def is_letter_in_ran_word():
	if guess in ran_word:
		print(f'The letter {guess} is in the guessed word')
is_letter_in_ran_word()
	


        








 	
 	
# else:
	# print('No such letter in this word')
	# print( part of hangman)


