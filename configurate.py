import customtkinter as ctk
class ConfiguratorApp():
    
    def select_button(self, entry, game, label) -> None:
        number = entry.get().lower()
        if number.isdigit():
            entry.delete(0, ctk.END)
            number = int(number)
            game.player_number(number, label)
        elif number != '':
            print("введте корренкое число")