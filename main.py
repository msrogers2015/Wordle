#!/usr/bin/env python3
import webbrowser, random, time
import data
import tkinter as tk

class Application(tk.Frame):
    guess_count = 0
    current_guess = ''
    letter_grid = [
        [],
        [],
        [],
        [],
        []
    ]

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.menu()

    def menu(self):
        '''Creation, display and control of main menu'''
        # Menu Frame
        self.menu_frame = tk.Frame(self.master)
        # Creating widges
        self.title_l = tk.Label(self.menu_frame, text='WordlePY', font=('Arial', 36), anchor=tk.CENTER)
        self.play_btn = tk.Button(self.menu_frame, text='Play', command=self.start_game,  font=('Arial', 20), anchor=tk.CENTER)
        self.about_btn = tk.Button(self.menu_frame, text='About',  command=self.about, font=('Arial', 20), anchor=tk.CENTER)
        self.quit_btn = tk.Button(self.menu_frame, text='Quit', command=self.close,  font=('Arial', 20), anchor=tk.CENTER)
        # Placing widgets
        self.menu_frame.pack(expand=True, fill='both')
        self.title_l.place(x=63, y=25, width=275, height=75)
        self.play_btn.place(x=100, y=150, width=200, height=50)
        self.about_btn.place(x=100, y=225, width=200, height=50)
        self.quit_btn.place(x=100, y=300, width=200, height=50)
    
    def start_game(self):
        '''Creation, display and control of main game'''
        self.wordle_word = random.choice(data.words).lower()
        # Clear screen
        for widgets in self.menu_frame.winfo_children():
            widgets.destroy()
        self.menu_frame.destroy()
        # Setting up game frame for widgets
        self.game_frame = tk.Frame(self.master)
        self.game_frame.pack(expand=True, fill='both')
        # Game objects
        self.guess_label = tk.Label(self.game_frame, text='Make a guess', font=('Arial', 18))
        self.guess_text = tk.StringVar()
        self.guess_entry = tk.Entry(self.game_frame)
        self.guess_btn = tk.Button(self.game_frame, text='Guess', command=self.check)
        self.notifications = tk.Label(self.game_frame)
        # Place widgets
        self.guess_label.place(x=113, y=25, width=175, height=25)
        self.guess_entry.place(x=75, y=60, width=125, height=25)
        self.guess_btn.place(x=225, y=60, width=50, height=25)
        self.notifications.place(x=50, y=460, width=300, height=30)
        # Create letter objects
        for row in range(5):
            for col in range(5):
                self.letter_label = tk.Label(self.game_frame)
                Application.letter_grid[row].append(self.letter_label)
        # Enabling enter key as an alternative for clicking the guess button
        self.master.bind('<Return>', self.check)

    def check(self, event=None):
        font = ('Arial',14)
        # Assigning class variable to value from entry box
        Application.current_guess = self.guess_entry.get().lower()
        # Ensuring word is 5 characters long
        if len(Application.current_guess) == 5 and Application.guess_count < 5:
            # Clear entry widget for next guess attempt
            self.guess_entry.delete(0, 'end')
            # If word is correctly guessed, display all gree boxes and alter player they they have won.
            # Also display menu buttons so they can play again
            if Application.current_guess == self.wordle_word:
                for index, item in enumerate(Application.letter_grid[Application.guess_count]):
                    item.place(x=(37+(index*65)), y=100+(Application.guess_count*75), width=50, height=50)
                    item.config(text=Application.current_guess[index].upper(), font=('Arial', 36))
                    item.config(bg='green')
                self.notifications.config(text='Congradulations, you won!', font=font)
                self.menu_btn = tk.Button(self.game_frame, text='Menu', font=font, command=self.menu_from_game)
                self.menu_btn.place(x=163, y=510, width=75, height=25)
            # Check each letter, updaing the background to display either correct placement, correct letter
            # but wrong placement or wrong letter altogether
            for index, item in enumerate(Application.letter_grid[Application.guess_count]):
                item.place(x=(37+(index*65)), y=100+(Application.guess_count*75), width=50, height=50)
                item.config(text=Application.current_guess[index].upper(), font=('Arial', 36))
                if Application.current_guess[index] == self.wordle_word[index]:
                    item.config(bg='green')
                    continue
                if Application.current_guess[index] in self.wordle_word:
                    item.config(bg='yellow')
                    continue
                item.config(bg='red')
            # Updating guess count to keep track of attempts for ending the game
            Application.guess_count += 1
        # If the input is not 5 characters long, display a error message and allow user to try again.
        # This won't count against their guesses
        elif len(Application.current_guess) != 5:
            self.notifications.config(text='Please only use 5 letter words', font=font)
        # If this is the fifth guess, signal the end of the game. 
        if Application.guess_count == 5:
            self.notifications.config(text=f'Sorry, the word was {self.wordle_word}', font=font)
            
    def menu_from_game(self):
        ''''Clear screen of game screen items and display the menu'''
        for widgets in self.game_frame.winfo_children():
            widgets.destroy()
        self.game_frame.destroy()
        self.menu()
    
    def menu_from_about(self):
        '''Clear screen of about screen items and display the menu'''
        for widgets in self.about_frame.winfo_children():
            widgets.destroy()
        self.about_frame.destroy()
        self.menu()

    def close(self):
        '''Close the application'''
        self.master.destroy()

    def about(self):
        font = ('Arial',14)
        # Clearing screen of the menu items
        for widgets in self.menu_frame.winfo_children():
            widgets.destroy()
        self.menu_frame.destroy()
        # Create a frame to hold the information for the about screen
        self.about_frame = tk.Frame(self.master)
        self.about_frame.pack(expand=True, fill='both')
        # Adding Widgets
        self.link_btn = tk.Button(self.about_frame)
        self.developer = tk.Label(self.about_frame, text='Created by Marquel Rogers', font=font)
        self.website = tk.Label(self.about_frame, text='https://www.marquel.xyz', font=font, cursor='hand2')
        self.menu_btn = tk.Button(self.about_frame, text='Menu', command=self.menu_from_about, font=('Arial',20))
        self.quit_btn = tk.Button(self.about_frame, text='Quit', command=self.quit, font=('Arial',20))
        #Placing widgets
        self.developer.place(x=25, y=25, width=350, height=35)
        self.website.place(x=25, y=60, width=350, height=35)
        self.menu_btn.place(x=75, y=300, width=100, height=50)
        self.quit_btn.place(x=225, y=300, width=100, height=50)
        # Portfolio Link
        self.website.bind('<Button-1>', lambda e: self.portfolio('https://www.marquel.xyz'))
        for widget in self.about_frame.winfo_children():
            print(widget)
    
    def portfolio(self, url):
    '''Opens a web browser and navigates to my portfolio'''
        webbrowser.open_new_tab(url)

if __name__ == '__main__':
    # Create application window, set the size and give it a name
    root = tk.Tk()
    root.geometry('400x550')
    root.title('WorldePy')
    # Create an instance of Application class for all the logic
    app = Application(master=root)
    # Loop through the code for displaying GUI
    app.mainloop()
