from Game import Game
from configurate import ConfiguratorApp
import customtkinter as ctk

app = ctk.CTk()
game = Game()
conf_app = ConfiguratorApp()

class main():
    def __init__(self) -> None:
        app.title(" guess the number")
        app.geometry("500x175")

        label = ctk.CTkLabel(master= app, text=game.start_game())
        entry_frame = ctk.CTkFrame(master=app)
        entry = ctk.CTkEntry(master=entry_frame, placeholder_text="Enter the number", width=200)
        submit_button = ctk.CTkButton(master=entry_frame, text="Enter", command=lambda: conf_app.select_button(entry, game, label), width=100)
        
        label.pack()
        entry_frame.pack(pady=20)
        entry.pack(side="left", padx=5)
        submit_button.pack(side="left", padx=5)

init = main()
app.mainloop()