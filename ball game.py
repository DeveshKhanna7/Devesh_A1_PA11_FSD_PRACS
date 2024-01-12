import tkinter as tk
from tkinter import messagebox
import random
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 700
BALL_RADIUS = 30
BALL_COLORS = ["red", "green", "blue", "orange", "purple"]
BALL_SPEED = 3
NEW_BALL_INTERVAL = 500  
GAME_DURATION = 10  
class CatchTheBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Catch the Ball")
        self.canvas = tk.Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        self.score = 0
        self.game_over = False
        self.balls = []
        self.root.after(NEW_BALL_INTERVAL, self.create_ball)
        self.info_label = tk.Label(self.root, text="Score: 0 | Time: 60 seconds", font=("Helvetica", 14))
        self.info_label.pack()
        self.canvas.bind("<Button-1>", self.catch_ball)
        self.timer = GAME_DURATION
        self.update_timer()
    def create_ball(self):
        if not self.game_over:
            x = random.randint(BALL_RADIUS, CANVAS_WIDTH - BALL_RADIUS)
            y = -BALL_RADIUS
            color = random.choice(BALL_COLORS)
            ball = self.canvas.create_oval(x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS, fill=color)
            self.balls.append(ball)
            self.move_ball(ball)
            self.root.after(NEW_BALL_INTERVAL, self.create_ball)
    def move_ball(self, ball):
        if not self.game_over and ball in self.balls:
            self.canvas.move(ball, 0, BALL_SPEED)
            x1, y1, x2, y2 = self.canvas.coords(ball)
            if y2 > CANVAS_HEIGHT:
                self.remove_ball(ball)
                self.decrement_score()
            self.root.after(10, self.move_ball, ball)
    def remove_ball(self, ball):
        if ball in self.balls:
            self.balls.remove(ball)
            self.canvas.delete(ball)
    def catch_ball(self, event):
        if not self.game_over:
            x, y = event.x, event.y
            for ball in self.balls:
                x1, y1, x2, y2 = self.canvas.coords(ball)
                if x1 < x < x2 and y1 < y < y2:
                    self.remove_ball(ball)
                    self.increment_score()
    def increment_score(self):
        if not self.game_over:
            self.score += 1
            self.info_label.config(text=f"Score: {self.score} | Time: {self.timer} seconds")
    def decrement_score(self):
        if not self.game_over and self.score > 0:
            self.score -= 1
            self.info_label.config(text=f"Score: {self.score} | Time: {self.timer} seconds")
    def update_timer(self):
        if not self.game_over:
            self.timer -= 1
            self.info_label.config(text=f"Score: {self.score} | Time: {self.timer} seconds")
            if self.timer == 0:
                self.end_game()
            else:
                self.root.after(1000, self.update_timer)
    def end_game(self):
        self.game_over = True
        self.info_label.config(text=f"Game Over | Final Score: {self.score}")
        messagebox.showinfo("Game Over", f"Your Final Score: {self.score}")
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.restart_game()
    def restart_game(self):
        self.score = 0
        self.game_over = False
        self.balls = []
        self.timer = GAME_DURATION
        self.info_label.config(text=f"Score: {self.score} | Time: {self.timer} seconds")
        for ball in self.balls:
            self.canvas.delete(ball)
        self.balls = []
        self.root.after(NEW_BALL_INTERVAL, self.create_ball)
        self.update_timer()
if __name__ == "__main__":
    root = tk.Tk()
    game = CatchTheBallGame(root)
    root.mainloop()