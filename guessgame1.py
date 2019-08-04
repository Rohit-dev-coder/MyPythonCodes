from random import randint
num = randint(1,100)
while True:
	guess = int(input("Guess the number(from1 to 100):"))
	if num == guess:
		print("Congratulation! you guess it right")
		break
	if guess>num:
		print("Number is too large! Try again")
	elif guess<num and guess>0:
		print("Number is too small! try again")
	else:
		print("Sorry! better luck next time")