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
print(f'The word has {len(ran_word)} letters ')

# check if letter is in the word and how many times and on which positions			
def is_letter_in_ran_word():
    if guess in ran_word:
	    count_guess = ran_word.count(guess)	   
	    print(f'The letter {guess} is in the guessed word {count_guess} times')
	    guess_position()
	    guess_letter()
    else:
		    print('No such letter in this word!')
	
def guess_position():
	#if guess in ran_word:
		for idx, val in enumerate(ran_word, start = 1):
			if guess == val:
				print(val, idx,'. position')

#ask player to guess a letter
def guess_letter():
	while True:
		global guess
		guess = str(input('Guess a letter: '))	
		if guess.isalpha(): #possibly call the is_in_ran_word function?
			print(is_letter_in_ran_word())
			print(guess_position())
			break
		else:
			print('Only enter letters please! ')
guess_letter()
#Convert random word to list
hidden_ran_word = list(hidden_ran_word)

	


        








 	
 	
# else:
	# print('No such letter in this word')
	# print( part of hangman)


