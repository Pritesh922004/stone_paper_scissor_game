import random

import streamlit as st


WIN_RULES = {
    "Stone": "Scissors",
    "Paper": "Stone",
    "Scissors": "Paper",
}


def initialize_state():
    if "player_score" not in st.session_state:
        st.session_state.player_score = 0
        st.session_state.computer_score = 0
        st.session_state.round_count = 0
        st.session_state.last_result = "Choose an option to start playing."
        st.session_state.last_type = "info"
        st.session_state.player_choice = None
        st.session_state.computer_choice = None


def decide_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "draw"
    if WIN_RULES[player_choice] == computer_choice:
        return "player"
    return "computer"


def play_round(player_choice):
    computer_choice = random.choice(list(WIN_RULES.keys()))
    winner = decide_winner(player_choice, computer_choice)

    st.session_state.round_count += 1
    st.session_state.player_choice = player_choice
    st.session_state.computer_choice = computer_choice

    if winner == "player":
        st.session_state.player_score += 1
        st.session_state.last_result = "You win this round!"
        st.session_state.last_type = "success"
    elif winner == "computer":
        st.session_state.computer_score += 1
        st.session_state.last_result = "Computer wins this round!"
        st.session_state.last_type = "error"
    else:
        st.session_state.last_result = "This round is a draw!"
        st.session_state.last_type = "warning"


def reset_game():
    st.session_state.player_score = 0
    st.session_state.computer_score = 0
    st.session_state.round_count = 0
    st.session_state.last_result = "Game reset successfully. Start a new round!"
    st.session_state.last_type = "info"
    st.session_state.player_choice = None
    st.session_state.computer_choice = None


def show_result():
    getattr(st, st.session_state.last_type)(st.session_state.last_result)
    if st.session_state.player_choice and st.session_state.computer_choice:
        st.write(f"You chose: **{st.session_state.player_choice}**")
        st.write(f"Computer chose: **{st.session_state.computer_choice}**")


def main():
    st.set_page_config(page_title="Stone Paper Scissors UI", page_icon="✊")
    initialize_state()

    st.title("✊ Stone Paper Scissors UI")
    st.write("Play against the computer and try to get the highest score.")

    score_col1, score_col2, score_col3 = st.columns(3)
    score_col1.metric("Player Score", st.session_state.player_score)
    score_col2.metric("Computer Score", st.session_state.computer_score)
    score_col3.metric("Rounds", st.session_state.round_count)

    button_col1, button_col2, button_col3 = st.columns(3)
    with button_col1:
        if st.button("Stone", use_container_width=True):
            play_round("Stone")
    with button_col2:
        if st.button("Paper", use_container_width=True):
            play_round("Paper")
    with button_col3:
        if st.button("Scissors", use_container_width=True):
            play_round("Scissors")

    if st.button("Reset Score", use_container_width=True):
        reset_game()

    show_result()


if __name__ == "__main__":
    main()
