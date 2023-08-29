import tkinter as tk #This gives the application a GUI


def classic(): #Start menu of the application
    game_window = tk.Toplevel(root)
    game_window.title("Classic")

    game_label = tk.Label(game_window, text="Welcome to the Game!")
    game_label.pack()


def daily_word():
    options_window = tk.Toplevel(root)
    options_window.title("daily word")

    options_label = tk.Label(options_window, text="Game Options:")
    options_label.pack()

def settings():
    options_window = tk.Toplevel(root)
    options_window.title("Game Settings:")

    options_label = tk.Label(options_window, text="Settings:")
    options_label.pack()

def exit_game():
    root.quit()


root = tk.Tk()
root.title("Game Menu")

title_label = tk.Label(root, text="Game Menu")
title_label.pack()

start_button = tk.Button(root, text="Classic", command=classic)
start_button.pack()

options_button = tk.Button(root, text="Daily word", command=daily_word)
options_button.pack()

settings_button = tk.Button(root, text="Game option", command=settings)
start_button.pack()

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack()

root.mainloop()