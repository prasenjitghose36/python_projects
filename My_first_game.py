from random import randint as randint

print("Hello Welcome to this rock, paper and scissors game")
print(".....Rock.....\n.....Paper.....\n.....Scissors.....\nBy Prasenjit Ghose")
print("BOOM ^_^")

player = input("Player Enter your choice: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer == "rock"
elif rand_num == 1:
	computer == "paper"
else:
	computer == "scissors"
print(f"Computer plays {computer}")	

if player == computer:
	print("It's a Tie")

elif player == "rock":
	if computer == "scissors":
		print("player wins !")
	elif computer == "paper":
		print("computer wins !")

elif player == "paper":
	if computer == "scissors":
		print("computer wins !")
	elif computer == "rock":
		print("player wins !")

elif player == "scissors":
	if computer == "rock":
		print("computer wins !")
	elif computer == "paper":
		print("player wins !")

else:
	print("Something went wrong")
