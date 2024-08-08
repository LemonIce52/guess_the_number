import random

class Game():
    
    def __init__(self) -> None:
        self.number = random.randint(1, 40)
        self.attempts = 0
    
    def start_game(self) -> str:
        lable = """
        Welcome to the game guess the number, 
        I guess a number from 1 to 40 and you try to guess it.
        If you want to leave the game, write the number 0.
        If anything, I have already guessed the number :)
                """
        return lable
    
    def player_number(self, player_numb, label) -> None:
        if player_numb > self.number:
            label.configure(text = "Your number is higher than what I guessed :)")
            self.attempts += 1
        elif player_numb < self.number:
            label.configure(text = "Your number is less than what I guessed :)")
            self.attempts += 1
        elif player_numb == self.number:
            label.configure(text = "You guessed :)\nI have thought of a new number, try to guess it.")
            self.attempts = 0
            self.number = random.randint(1, 40)
        
        self.clue(label)
        
    def clue(self, label) -> None:
        if self.attempts >= 5:
            label.configure(text = f"My number is between {self.number - random.randint(7, 13)} and {self.number + random.randint(7, 13)}")
            self.attempts = 0