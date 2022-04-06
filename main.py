#!/usr/bin/env python3
'''https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter#:~:text=One%20way%20to%20switch%20frames,use%20any%20generic%20Frame%20class.'''

from asyncio import ALL_COMPLETED
import webbrowser
import data
import random
import time
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
        # Clear screen
        for widgets in self.menu_frame.winfo_children():
            widgets.destroy()
        self.menu_frame.destroy()
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
        self.master.bind('<Return>', self.check)

    def check(self, event=None):
        font = ('Arial',14)
        Application.current_guess = self.guess_entry.get().lower()
        if len(Application.current_guess) == 5 and Application.guess_count < 5:
            self.guess_entry.delete(0, 'end')
            if Application.current_guess == self.wordle_word:
                for index, item in enumerate(Application.letter_grid[Application.guess_count]):
                    item.place(x=(37+(index*65)), y=100+(Application.guess_count*75), width=50, height=50)
                    item.config(text=Application.current_guess[index].upper(), font=('Arial', 36))
                    item.config(bg='green')
                self.notifications.config(text='Congradulations, you won!', font=font)
                self.menu_btn = tk.Button(self.game_frame, text='Menu', font=font, command=self.menu_from_game)
                self.menu_btn.place(x=163, y=510, width=75, height=25)
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
            Application.guess_count += 1
        elif len(Application.current_guess) != 5:
            self.notifications.config(text='Please only use 5 letter words', font=font)
        if Application.guess_count == 5:
            self.notifications.config(text=f'Sorry, the word was {self.wordle_word}', font=font)
            
    def menu_from_game(self):
        for widgets in self.game_frame.winfo_children():
            widgets.destroy()
        self.game_frame.destroy()
        self.menu()
    
    def menu_from_about(self):
        for widgets in self.about_frame.winfo_children():
            widgets.destroy()
        self.about_frame.destroy()
        self.menu()

    def close(self):
        self.master.destroy()

    def about(self):
        font = ('Arial',14)
        for widgets in self.menu_frame.winfo_children():
            widgets.destroy()
        self.menu_frame.destroy()
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
        webbrowser.open_new_tab(url)

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x550')
    root.title('WorldePy')
    app = Application(master=root)
    app.mainloop()