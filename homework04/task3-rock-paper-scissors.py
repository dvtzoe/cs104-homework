import random

choices = ["rock", "paper", "scissors"]

draw_count = 0
player_win_count = 0
computer_win_count = 0

while (player_choice := input("rock, paper, scissors? ")) != "q":
    if player_choice not in choices:
        print("Invalid choice")
    else:
        computer_choice_index = random.randint(0, 2)
        print(f"Computer: {choices[computer_choice_index]}")

        player_choice_index = choices.index(player_choice)

        index_difference = (computer_choice_index - player_choice_index) % 3

        if index_difference == 0:
            print("Draw!")
            draw_count += 1
        elif index_difference == 1:
            print("Computer wins!")
            computer_win_count += 1
        else:
            print("You wins!")
            player_win_count += 1
print(
    f"You won {player_win_count}, the computer won {computer_win_count}, draws: {draw_count}"
)
