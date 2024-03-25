import random
import math
import sys
import time

def play_rps():
    moves = ['r', 'p', 's']
    tries = 3

    while True:
        user = input("\t\tEnter your choice: 'r' for rock, 'p' for paper, or 's' for scissors: ")
        user = user.lower()

        if user not in moves:
            tries -= 1
            print("\t Please enter either:'r','p',or 's'. You have {} attempts left. \n".format(tries))
        else:
            computer = random.choice(moves)

            if user == computer:
                return (0, user, computer)

            if if_win(user, computer):
                return (1, user, computer)

            return (-1, user, computer)

def if_win(person, online):
    return (
        (person == 'r' and online == 's') or
        (person == 's' and online == 'p') or
        (person == 'p' and online == 'r'))

def play_best_of(n):
    player_wins = 0
    computer_wins = 0
    wins_necessary = math.ceil(n / 2)
    while player_wins < wins_necessary and computer_wins < wins_necessary:
        result, user, computer = play_rps()

        if result == 0:
            print("\t It's a tie! You and the computer have both chosen {}.".format(computer))
        elif result == 1:
            player_wins += 1
            print("\t You won!. You've chosen {} and the computer chose {}. Your score is {} ".format(user, computer,player_wins))
        elif result == -1:
            computer_wins += 1
            print("\t You lost. 😞. You've chosen {} and the computer chose {}. The computer's score is {}".format(user, computer,computer_wins))
        print('\n')

    if player_wins > computer_wins:
        print('You have won the best of {} games! Good job.'.format(n))
    else:
        print('Sorry, the computer won the best of {} games! :('.format(n))

def main():
    print("Welcome to Rock Paper & Scissors!\n")
    player_name = input("Enter your name: ")
    print("\nHi {}, shall we begin?\n".format(player_name))

    rounds = int(input("\tEnter the number of rounds you would like to play: "))
    play_best_of(rounds)

if __name__ == "__main__":
    main()