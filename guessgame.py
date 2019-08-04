import random
secret = random.randint(1,100)
guess = secret + 1
while guess!=secret:
	guess = int(input("Guess the number(from 1 to 100): "))
	if guess<=0:
		print("Sorry! better luck next time")
		break
	if guess>secret:
		print("Number two large! Try again")
	elif guess<secret:
		print("Number two Small! Try again")
else:
	print("Congratulation! you Guessed it Right")