import random

# The top eight of the 2023 AFL finals, you can change the teams and skill points if you want
teams = {
    'Collingwood': 30,
    'Brisbane': 28,
    'Melbourne': 26,
    'Port Adelaide': 24,
    'Carlton': 22,
    'St Kilda': 20,
    'GWS Giants': 18,
    'Sydney': 16
}

# Play game is random with + 80 points to make the scores more realistic for an AFL game 
# The team with more skill points will have a slight advantage
def play_game(team1, team2):
    team1_score = random.randint(0, teams[team1]) + 80
    team2_score = random.randint(0, teams[team2]) + 80
    print(f'{team1}: {team1_score}, {team2}: {team2_score}')
    if team1_score > team2_score:
        return team1, team2
    else:
        return team2, team1
# Round 1 the losers of the top 4 will play the winners in the bottom 4 and the losers in bottom 4 are knocked out
print("Round 1 Lineup:")
print("Collingwood vs Melbourne")
print("Carlton vs Sydney")
print("St Kilda vs GWS Giants")
print("Brisbane vs Port Adelaide")
input("Press Enter to start Round 1...")

round_1_game_1_winner, round_1_game_1_loser = play_game('Collingwood', 'Melbourne')
round_1_game_2_winner, round_1_game_2_loser = play_game('Carlton', 'Sydney')
round_1_game_3_winner, round_1_game_3_loser = play_game('St Kilda', 'GWS Giants')
round_1_game_4_winner, round_1_game_4_loser = play_game('Brisbane', 'Port Adelaide')

# The winner of the bottom 4 will play the losers of the top 4, the losers in the games are knocked out.

print("\nRound 2 Lineup:")
print(f"{round_1_game_2_winner} vs {round_1_game_1_loser}")
print(f"{round_1_game_3_winner} vs {round_1_game_4_loser}")
input("Press Enter to start Round 2...")

round_2_game_1_winner, round_2_game_1_loser = play_game(round_1_game_2_winner, round_1_game_1_loser)
round_2_game_2_winner, round_2_game_2_loser = play_game(round_1_game_3_winner, round_1_game_4_loser)

# Preliminary finals are the winners of round 2 play the winners of the top 4, losers in the games are knocked out
# And the winners go on to the finals.

print("\nPreliminary Finals Lineup:")
print(f"{round_2_game_1_winner} vs {round_1_game_4_winner}")
print(f"{round_2_game_2_winner} vs {round_1_game_1_winner}")
input("Press Enter to start Preliminary Finals...")

prelim_finals_winner, prelim_finals_loser = play_game(round_2_game_1_winner, round_1_game_4_winner)
prelim_finals2_winner, prelim_finals2_loser = play_game(round_2_game_2_winner, round_1_game_1_winner)

# AFL grand finals

print("\nFinals Lineup:")
print(f"{prelim_finals_winner} vs {prelim_finals2_winner}")
input("Press Enter to start Finals...")

finals_winner, finals_loser = play_game(prelim_finals_winner, prelim_finals2_winner)

print(' |-------------------------------------------------------------|')
print(' |*************************************************************|')
print(' |#############################################################|')
print(f'  The winner of the 2023 AFL Grand Finals is: {finals_winner}  ')
print(' |#############################################################|')
print(' |*************************************************************|')
print(' |-------------------------------------------------------------|')

# Please feel free to let me know how to modify and make the code better
