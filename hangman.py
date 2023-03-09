#Hangman
# Import random word library
from random_word import RandomWords

def update_hidden_word(positions, ran_word): # this function will disclose correct positions in hidden_word and hide not guessed letter
    #print('*****----',guess) #checking if any guess is passed into this function
    result = []
    # This is going to be positions will equal 0 and 2. Ran word is CAT
    for i, char in enumerate(ran_word): 
        if i not in positions: 
        	# 1 is not in positions therefore we can expose index 1 (which is A)
        	result.append(char)        	            
        else:
        	# 0 and 2 are not in positions therefore we must return * to keep them hidden
        	result.append('*')        	
    return ''.join(result) # '**e'
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
	# while len(guess) != 1 and not guess.isalpha():
		guess = input('Guess a letter: ') #check if only receiving 1 character	
	return guess

	# create guessed_letters, if guess not in guessed_letter - append to guessed_letter, else print already guessed

def update_hidden_positions(positions, correct_positions):
    for position in correct_positions:
    	positions.remove(position)
    return positions

def main():
	
	r = RandomWords()
	# Return a single random word
	ran_word = r.get_random_word()
	print(ran_word)
	#hide the word
	hidden_ran_word = '*' * len(ran_word)
	print(hidden_ran_word)
	print(f'The word has {len(ran_word)} letters ')	

	#list of digits - how many digits all characters of the word 
	#to be hidden as positions
	hidden_positions = list(range(len(hidden_ran_word)))
	print(hidden_positions)

	game_over = False
	while not game_over:
		guess = get_letter() # check if letter is in word
		if guess in ran_word:
			 
			 hidden_positions = update_hidden_positions(hidden_positions, get_correct_positions(ran_word, guess))
			 if hidden_positions == []:
			 	print('Congratulations')
			 	game_over = True
			 print(update_hidden_word(hidden_positions, ran_word))
		else:
			print('Guess again, this is the info', hidden_ran_word)
    
 
if __name__ == '__main__':
    main()
    





