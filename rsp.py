import random

moves = ['rock', 'paper', 'scissors']


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_turn, player_turn):
        pass


class RandomPlayer(Player):

    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)

    def learn(self, my_turn, player_turn):
        pass


class ReflectPlayer(Player):

    def __init__(self):
        self.move_temp = "rock"

    def move(self):
        return self.move_temp

    def learn(self, my_turn, player_turn):
        self.move_temp = player_turn


class CyclePlayer(Player):
    def __init__(self):
        self.move_temp = "rock"

    def move(self):
        if self.move_temp == "rock":
            return "paper"
        elif self.move_temp == "paper":
            return "scissors"
        elif self.move_temp == "scissors":
            return "rock"
        else:
            return "rock"

    def learn(self, my_turn, player_turn):
        self.move_temp = my_turn


class HumanPlayer(Player):

    def move(self):

        while True:

            string = input("rock, paper, scissors? ")
            if string.lower() not in moves:
                print("Please choose rock, paper or scissors.")
            else:
                break
        return string

    def learn(self, my_turn, player_turn):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.win = 0
        self.loss = 0
        self.tie = 0

    def play_round(self):
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"\nPlayer 1: {move1} Player 2: {move2}")
        if beats(move1, move2):
            self.win += 1
        elif beats(move2, move1):
            self.loss += 1
        else:
            self.tie += 1

        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

    def play_game(self):
        print("GAME START")
        for round in range(3):
            print(f"\033Round {round}")
            self.play_round()
        if self.win > self.loss:
            print("Game over "),
            print(f"Player 1 wins (player1: {self.win} player2: {self.loss})")
        elif self.win < self.loss:
            print("Game over"),
            print(f"Player 2 wins (player2: {self.loss} player1: {self.win})")
        else:
            print("game over "),
            print(f"It's a tie. (player1: {self.win} player2: {self.loss})")
        print(f"\n\n\n")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
