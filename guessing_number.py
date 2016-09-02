from random import ramdint

def main():
	print "Welcome to our number guessing game!"
	number = ranint(1,10)
	num = 5
	while num:
		num = num - 1
		guess = raw_input("Guess a number between 1 and ten: ")
		if guess == number:
			print "You got it"
			break
		elif guess > number:
			print "Sorry,that's too high! Guess again!"
		elif guess < number:
			print "Sorry,that's too low! Guess again!"
if __name__ == "main":
	main()