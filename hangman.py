from random_word import RandomWords

def update_hidden_word(positions, ran_word): # this function will disclose correct positions in hidden_word and hide not guessed letter
	
	result = []
	# This is going to be positions will equal 0 and 2. Ran word is CAT
	for i, char in enumerate(ran_word): 
		if i not in positions: 
			# 1 is not in positions therefore we can expose index 1 (which is A)
			result.append(char)        	            
		else:
			# 0 and 2 are not in positions therefore we must return * to keep them hidden
			result.append('_')        	
	return ' '.join(result) # '**e'
			# print(guess, i, '. position')
  #NOW NEED TO CHECK IF THE GUESSED RESULT MATCHES HIDDEN POSITIONS AND REMOVE THOSE IN HIDDEN POSITIONS

def get_correct_positions(ran_word, guess):	#getting correct positions in the random word which we then use to update what stays hidden and what gets disclosed
	result = []
	for i, char in enumerate(ran_word):
		if guess == char:
			result.append(i)
	return result
		
   
def get_letter(): # get a letter from user
	guess = ''
	while not (len(guess) == 1 and guess.isalpha()):
		guess = input('Guess a letter: ') #check if only receiving 1 character and if it is a letter
	return guess

	# create guessed_letters, if guess not in guessed_letter - append to guessed_letter, else print already guessed

def update_hidden_positions(keep_hidden, remove_guessed_positions):
	for position in remove_guessed_positions:
		keep_hidden.remove(position)
		#print(position)
	return keep_hidden

def update_guessed_leters (guess, guessed_letters): #function will update the list with already guessed letters and return updated list
	guessed_letters.append(guess)
	guessed_letters_set = set(guessed_letters)
	print(guessed_letters_set)
	return list(guessed_letters_set)

def get_hidden_string(positions, ran_word):
	result = []
	# cat 0, 2 
	# *a*
	for i, char in enumerate(ran_word):
		if i in positions: # positions are what has yet not been guessed correctly
			result.append('_')
		else:
			result.append(char)
	return ' '.join(result)

	return result

def get_body_parts(number_of_wrong_guesses):
	body_parts = ['head', 'neck', 'torso', 'right arm', 'left arm', 'right leg', 'left leg']
	# return body_parts[0:3] 
	return '\n'.join(body_parts[0:number_of_wrong_guesses])


def main():

	hangmanpics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
		
	r = RandomWords()
	# Return a single random word
	ran_word = r.get_random_word()
	print(ran_word)
	#hide the word
	hidden_ran_word = '_ ' * len(ran_word)
	print(hidden_ran_word)
	print(f'The word has {len(ran_word)} letters ')	

	#list of digits - how many digits all characters of the word 
	#to be hidden as positions
	hidden_positions = list(range(len(ran_word)))
	# print(hidden_positions)

	guessed_letters = []
	bad_guesses = 0
	game_over = False
	while not game_over:
		guess = get_letter() # check if letter is in word
		

		if guess in guessed_letters:
			print('You already guessed that letter')
		else:
			guessed_letters = update_guessed_leters(guess, guessed_letters)

			if guess in ran_word:
				 
				hidden_positions = update_hidden_positions(hidden_positions, get_correct_positions(ran_word, guess))
				if hidden_positions == []:
					print('Congratulations, you have guessed the word.')
					game_over = True
				print(update_hidden_word(hidden_positions, ran_word))
			else:
				# bad_guesses = bad_guesses + 1 (same as the next line)
				bad_guesses += 1
				print(hangmanpics[bad_guesses-1])
				if  bad_guesses > 6:
					print("You have lost. Game over.")
					game_over = True
				else:
					print('Guess again, this is the info', get_hidden_string(hidden_positions, ran_word))
			
		
if __name__ == '__main__':
	main()





