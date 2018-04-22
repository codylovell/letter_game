import random
import os

words = ["python",
		 "jumble",
		  "easy",
		  "difficult",
		  "answer",
		  "xylophone"]

def clear_screen():
	os.system('clear')

while True:
	start = input("Press enter to begin, or 'q' to exit, press 'c' to cheat.")
	if start.lower() == 'q':
		break
	if start.lower() == 'c':
		print(words)

	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []


	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):

		for letter in secret_word:
			if letter in good_guesses:
				print(letter, end='')
			else:
				print('_', end='')
		print('')
		print('Strikes: {}/7'.format(len(bad_guesses)))
		print('')


		guess = input('Guess: ').lower()

		if len(guess) != 1:
			clear_screen()
			print('You can only guess a single letter!')
			continue
		elif guess in bad_guesses or guess in good_guesses:
			clear_screen()
			print('You already guessed that letter!')
			continue
		elif not guess.isalpha():
			clear_screen()
			print('You can only guess letters!')
			continue


		if guess in secret_word:
			good_guesses.append(guess)
			clear_screen()
			if len(good_guesses) == len(list(secret_word)):
				print('You win.')
				break
		else:
			bad_guesses.append(guess)
			clear_screen()

	else:
		print("You didnt guess it my secret_word was: {}".format(secret_word))

