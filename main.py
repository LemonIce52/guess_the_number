import random

class Game():
    def __init__(self) -> None:
        self.number = random.randint(1, 40)
        self.is_game = True
        self.attempts = 0
    
    def player_number(self, player_numb) -> None:
        if player_numb == 0:
            print("It was nice to play, I'll wait for you again :)")
            self.is_game = False
        elif player_numb > self.number:
            print("Your number is higher than what I guessed :)")
            self.attempts += 1
        elif player_numb < self.number:
            print("Your number is less than what I guessed :)")
            self.attempts += 1
        elif player_numb == self.number:
            print("You guessed :)")
            print("I have thought of a new number, try to guess it.")
            self.attempts = 0
            self.number = random.randint(1, 40)
        
        self.clue()
        
    def clue(self) -> None:
        if self.attempts >= 5:
            print(f"My number is between {self.number - random.randint(7, 13)} and {self.number + random.randint(7, 13)}")
            self.attempts = 0

game = Game()
print("""
      Welcome to the game guess the number, I guess a number from 1 to 40 and you try to guess it.
      If you want to leave the game, write the number 0.
      If anything, I have already guessed the number :)
      """)

while game.is_game:
    player_numb = int(input("Enter number --> "))
    print("")
    game.player_number(player_numb)