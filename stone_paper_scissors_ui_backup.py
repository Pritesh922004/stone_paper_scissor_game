import random
import tkinter as tk
from tkinter import messagebox


class StonePaperScissorsApp:
    WIN_RULES = {
        "Stone": "Scissors",
        "Paper": "Stone",
        "Scissors": "Paper",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Stone Paper Scissors")
        self.root.geometry("420x360")
        self.root.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0
        self.round_count = 0

        self.title_label = tk.Label(
            root,
            text="Stone Paper Scissors",
            font=("Arial", 20, "bold"),
            pady=10,
        )
        self.title_label.pack()

        self.info_label = tk.Label(
            root,
            text="Choose one option to play a round.",
            font=("Arial", 11),
        )
        self.info_label.pack(pady=5)

        self.score_label = tk.Label(
            root,
            text=self.get_score_text(),
            font=("Arial", 12, "bold"),
            fg="navy",
        )
        self.score_label.pack(pady=8)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=12)

        for choice in self.WIN_RULES:
            button = tk.Button(
                self.button_frame,
                text=choice,
                width=12,
                font=("Arial", 11),
                command=lambda selected=choice: self.play_round(selected),
            )
            button.pack(side=tk.LEFT, padx=6)

        self.result_label = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            justify="center",
            pady=10,
        )
        self.result_label.pack()

        self.history_label = tk.Label(
            root,
            text="No rounds played yet.",
            font=("Arial", 10),
            fg="dim gray",
            wraplength=360,
            justify="center",
        )
        self.history_label.pack(pady=5)

        self.control_frame = tk.Frame(root)
        self.control_frame.pack(pady=16)

        self.reset_button = tk.Button(
            self.control_frame,
            text="Reset Score",
            width=12,
            command=self.reset_game,
        )
        self.reset_button.pack(side=tk.LEFT, padx=6)

        self.exit_button = tk.Button(
            self.control_frame,
            text="Exit",
            width=12,
            command=root.destroy,
        )
        self.exit_button.pack(side=tk.LEFT, padx=6)

    def get_score_text(self):
        return (
            f"Player Score: {self.user_score}    "
            f"Computer Score: {self.computer_score}    "
            f"Rounds: {self.round_count}"
        )

    def decide_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "draw"
        if self.WIN_RULES[player_choice] == computer_choice:
            return "player"
        return "computer"

    def play_round(self, player_choice):
        computer_choice = random.choice(list(self.WIN_RULES.keys()))
        winner = self.decide_winner(player_choice, computer_choice)
        self.round_count += 1

        if winner == "player":
            self.user_score += 1
            result_text = "You win this round!"
            result_color = "green"
        elif winner == "computer":
            self.computer_score += 1
            result_text = "Computer wins this round!"
            result_color = "red"
        else:
            result_text = "This round is a draw!"
            result_color = "orange"

        self.score_label.config(text=self.get_score_text())
        self.result_label.config(
            text=(
                f"You chose: {player_choice}\n"
                f"Computer chose: {computer_choice}\n"
                f"{result_text}"
            ),
            fg=result_color,
        )
        self.history_label.config(
            text=f"Round {self.round_count} completed. Click another option to continue playing."
        )

    def reset_game(self):
        if messagebox.askyesno("Reset Game", "Do you want to reset the score?"):
            self.user_score = 0
            self.computer_score = 0
            self.round_count = 0
            self.score_label.config(text=self.get_score_text())
            self.result_label.config(text="", fg="black")
            self.history_label.config(text="Game reset successfully. Start a new round!")


def main():
    root = tk.Tk()
    app = StonePaperScissorsApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
