import random
the_number = random.randint(1, 100)
guess = int(input("Player1 Guess a number between 1 and 100: "))
player_counter = 1
score1 = 0
score2 = 0
while True:
    if player_counter%2 == 1:
        if guess > the_number:
            print(guess, "was too high. Try again.")
        elif guess < the_number:
            print(guess, "was too low. Try again.")
        else:
            score1 = score1 + 1
            print("Player1 wins this turn")
            print("he's score is",score1)
            if score1 > 1:
                break
            the_number = random.randint(1, 100)
    else:
        if guess > the_number:
            print(guess, "was too high. Try again.")
        elif guess < the_number:
            print(guess, "was too low. Try again.")
        else:
            score2 = score2 + 1
            print("Player2 wins this turn")
            print("he's score is",score2)
            if score2 > 1:
                break
            the_number = random.randint(1, 100)
    print('\n',"It's player",player_counter+1,"'s turn:")
    player_counter = player_counter + 1
    if player_counter > 1:
        player_counter = 0
    
    guess = int(input("Guess: "))
if score1 > score2:
    print("player1 wins!")
else:
    print("player2 wins!")
