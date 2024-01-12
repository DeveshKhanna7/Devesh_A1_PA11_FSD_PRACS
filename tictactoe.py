import tkinter as tk
from tkinter import messagebox
import random
class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x500")
        self.window.configure(bg='#2C3E50')
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        title_label = tk.Label(self.window, text="Tic Tac Toe", font=('Helvetica', 24, 'bold'), bg='#2C3E50', fg='#ECF0F1')
        title_label.pack(pady=10)
        frame = tk.Frame(self.window, bg='#2C3E50')
        frame.pack()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(frame, text='', font=('Helvetica', 18, 'bold'), width=6, height=2,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j].configure(bg='#3498DB', fg='#ECF0F1')
        restart_button = tk.Button(self.window, text='Restart', font=('Helvetica', 14), width=10, height=2,
                                   command=self.restart_game)
        restart_button.pack(pady=10)
        restart_button.configure(bg='#E74C3C', fg='#ECF0F1')
        self.window.eval('tk::PlaceWindow %s center' % self.window.winfo_toplevel())
        self.window.mainloop()
    def on_click(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED, bg='#2ECC71')
            if self.check_winner(row, col):
                messagebox.showinfo("Congratulations!", f"Player {self.current_player} wins!")
                self.restart_game()
            elif self.is_board_full():
                messagebox.showinfo("Tied!", "The game is a draw.")
                self.restart_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self, row, col):
        if all(self.board[row][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][col] == self.current_player for i in range(3)):
            return True
        if row == col and all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False
    def is_board_full(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    def restart_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='', state=tk.NORMAL, bg='#3498DB')
        self.current_player = 'X'
if __name__ == "__main__":
    TicTacToe()