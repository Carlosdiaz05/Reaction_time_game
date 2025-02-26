import tkinter as tk
import random
import time


class ReactionGame:
    def __init__(self, root, rounds):
        self.root = root
        self.root.title("Reaction Time Game")
        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.colors = {'r': 'red', 'g': 'green', 'b': 'blue', 'y': 'yellow', 'o': 'orange'}
        self.current_color = None
        self.start_time = None
        self.reaction_times = []
        self.rounds = rounds
        self.current_round = 0

        self.root.bind("<KeyPress>", self.check_reaction)
        self.start_game()

    def start_game(self):
        self.next_flash()

    def next_flash(self):
        if self.current_round >= self.rounds:
            self.end_game()
            return

        self.current_round += 1
        delay = random.uniform(0.5, 2)  # Random delay between 0.5-2 seconds
        self.root.after(int(delay * 1000), self.flash)

    def flash(self):
        self.current_color = random.choice(list(self.colors.keys()))
        self.canvas.configure(bg=self.colors[self.current_color])
        self.start_time = time.time()

    def check_reaction(self, event):
        if event.char == self.current_color:
            reaction_time = time.time() - self.start_time
            self.reaction_times.append(reaction_time)
            self.canvas.configure(bg='white')
            self.next_flash()

    def end_game(self):
        avg_time = sum(self.reaction_times) / len(self.reaction_times)
        self.canvas.create_text(200, 200, text=f"Avg Reaction Time: {avg_time:.3f} sec", font=("Arial", 16))
        self.root.unbind("<KeyPress>")


def rexecute():
    rounds = int(input("Enter the number of rounds (Recommended: 10-30): "))
    root = tk.Tk()
    game = ReactionGame(root, rounds)
    root.mainloop()


if __name__ == "__main__":
    rexecute()
