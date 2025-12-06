import random


def roll():
    min = 1
    max = 6
    roll = random.randint(min, max)

    return roll


while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 and 4 players.")
    else:
        print("Invalid, try again.")

max_score = 100
scores = [0] * players
current_player = 0
while True:
    print(f"\nPlayer {current_player + 1}'s turn:")
    turn_score = 0

    while True:
        choice = input("Roll or Hold? (r/h): ").lower()
        if choice == 'r':
            roll_result = roll()
            print(f"You rolled a {roll_result}.")
            if roll_result == 1:
                print("Turn over! No points earned this turn.")
                turn_score = 0
                break
            else:
                turn_score += roll_result
                print(f"Current turn score: {turn_score}")
        elif choice == 'h':
            scores[current_player] += turn_score
            print(
                f"Total score for Player {current_player + 1}: {scores[current_player]}")
            break
        else:
            print("Invalid choice, please enter 'r' to roll or 'h' to hold.")

    if scores[current_player] >= max_score:
        print(
            f"Player {current_player + 1} wins with a score of {scores[current_player]}!")
        break

    current_player = (current_player + 1) % players
    print(f"Scores: {', '.join(f'Player {i + 1}: {score}' for i,
          score in enumerate(scores))}")
