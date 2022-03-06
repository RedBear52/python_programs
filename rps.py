#!/usr/bin/env python3
import random
from itertools import cycle

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ["rock", "paper", "scissors"]
cycle_moves = cycle(moves)


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        pass

    def move(self):
        return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        random_move = random.choice(moves)
        return random_move


class HumanPlayer(Player):
    def move(self):
        response = validate_mv_choice(
            "Rock, paper or scissors?", "rock", "paper", "scissors")
        print(f"\nYou chose: {response}\n")
        return response


def validate_round_choice(prompt):
    # validate input as integer + learn how many rounds user would like to play
    while True:
        try:
            response = int(input(prompt))
            if response <= 0:
                print("Please enter a numeral with a value greater than zero!")
                continue
            break
        except ValueError:
            print("Please type a numeral.")
    return response


def validate_mv_choice(hp_choice, ch1, ch2, ch3):
    response = input(hp_choice).lower()
    while True:
        if response == ch1:
            break
        elif response == ch2:
            break
        elif response == ch3:
            break
        else:
            response = validate_mv_choice(
                "Rock, paper or scissors?", "rock", "paper", "scissors")
    return response


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = None
        self.first_move = random.choice(moves)

    def move(self):
        if self.their_move is None:
            return self.first_move
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        return next(cycle_moves)


def decide_victor(one, two):
    if (one == "rock" and two == "scissors") or\
      (one == "scissors" and two == "paper") or\
      (one == "paper" and two == "rock"):
        return "p1 wins"
    elif (two == 'rock' and one == 'scissors') or\
        (two == 'scissors' and one == 'paper') or\
            (two == 'paper' and one == 'rock'):
        return "p2 wins"
    else:
        return "p1 & p2 tie"


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1score = 0
        self.p2score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        report_results = decide_victor(move1, move2)
        if report_results == "p1 wins":
            print("Player One wins the round!\n")
            self.p1score += 1
        elif report_results == "p2 wins":
            print("Player Two wins the round!\n")
            self.p2score += 1
        else:
            print("The round ended in a draw...\n")
        print("-CURRENT SCORE-")
        print(f"Player One: {self.p1score}")
        print(f"Player Two: {self.p2score}\n")

    def play_game(self):
        round_num = (1)
        print("**********************************************************")
        print(f"Let's play {round_num} round of Rock Paper Scissors...")
        print("\nGame start!\n")
        self.play_round()
        self.game_over(round_num)

    def play_match(self):
        round_num = 0
        print("**********************************************************")
        print(f"\nLet's play a multi-round match of Rock Paper Scissors.\n")
        response = validate_round_choice("How many rounds would\
 you like to play?")
        round_num += int(response)
        print(f"\nAlrighty then. We're playing a {round_num} game series.")
        print("\nThis will be fun!\n")
        print("\nGame start!\n")
        for round in range(round_num):
            print(f"Round {round+ 1}:")
            self.play_round()
        self.game_over(round_num)

    def game_over(self, round_num):
        print("\n-GAME OVER-\n")
        print("-GRAND TOTAL-")
        print(f"""Player One's Total Wins: {self.p1score}
Player Two's Total Wins: {self.p2score} """)
        if self.p1score > self.p2score:
            print(f"Player One is the winner of this {round_num} game\
 series!\n")
        elif self.p2score > self.p1score:
            print(f"Player Two is the winner of this {round_num} game\
 series!\n")
        else:
            print(f"Player One and Player Two tied in this {round_num} game\
 series...\n")
        print("**********************************************************")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_match()
