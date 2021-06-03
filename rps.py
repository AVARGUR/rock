import random
while True:
	choices = ["rocks" , "papers" , "sissors"]

	pc = random.choice(choices)
	player = input("player")
	while player not in choices:
		player = input("player")
	print("player:",player)	

	if player == pc:
		print("tie")
	elif player == "rocks":
		if pc == "papers" :
			print("pc won")
		if pc == "sissors" :
			print("pc loose")
	elif player == "papers":
		if pc == "sissors" :
			print("pc won")
		if pc == "rocks" :
			print("pc loose")
	elif player == "sissors":
		if pc == "rocks" :
			print("pc won")
		if pc == "papers" :
			print("pc loose")	
	
	play_again = input("play again = yes/no ?")
	
	if play_again != "yes":
		break
print("bye")
