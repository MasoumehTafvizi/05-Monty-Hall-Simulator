import streamlit as st
import time
from src.monty_hall import simulate_game

st.image("./images/monty_hall.png", width=700)

st.title(":red_car: Monty Hall Simulator :goat: ")
num_games = st.number_input(
    "Enter number of games to simulate:", 
    min_value=1, 
    max_value=100000, 
    value=100
)

col1, col2 = st.columns(2)
col1.subheader("Win percentage without switching:")
col2.subheader("Win percentage with switching:")

chart1 = col1.line_chart(x = None, y = None, height=400)
chart2 = col2.line_chart(x = None, y = None, height=400)

num_wins_without_switching = 0
num_wins_with_switching = 0

for i in range(num_games):
    win_no_switch, win_with_switch = simulate_game(1)
    num_wins_without_switching += win_no_switch
    num_wins_with_switching += win_with_switch
    
    chart1.add_rows([num_wins_without_switching/(i + 1)])
    chart2.add_rows([num_wins_with_switching/(i + 1)])
    
    time.sleep(0.01)
    