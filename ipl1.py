import random

# Function to simulate a match between two teams
def simulate_match(team1, team2, teams):
    # Get the win percentages of both teams
    team1_win_prob = teams[team1]["win_percentage"]
    team2_win_prob = teams[team2]["win_percentage"]

    # Generate random numbers to simulate match outcome
    team1_chance = random.randint(1, 100)
    team2_chance = random.randint(1, 100)

    # Determine which team wins based on their win probabilities
    if team1_chance <= team1_win_prob:
        return team1
    elif team2_chance <= team2_win_prob:
        return team2
    else:
        # If both fail, choose randomly between the two
        return team1 if random.choice([True, False]) else team2

# Function to simulate the tournament
def simulate_tournament(teams):
    team_list = list(teams.keys())
    remaining_teams = team_list.copy()

    # Simulate rounds of matches
    while len(remaining_teams) > 1:
        next_round_teams = []
        
        # Pair teams for each match
        random.shuffle(remaining_teams)
        for i in range(0, len(remaining_teams), 2):
            team1 = remaining_teams[i]
            team2 = remaining_teams[i + 1]
            winner = simulate_match(team1, team2, teams)
            next_round_teams.append(winner)
            print(f"Match Result: {team1} vs {team2} -> Winner: {winner}")

        # Update remaining teams for next round
        remaining_teams = next_round_teams

    return remaining_teams[0]

# Function to get user input for teams and win percentages
def get_user_input():
    teams = {}
    print("Enter team details:")

    # Number of teams user wants to input
    num_teams = int(input("How many teams do you want to enter? "))
    
    # Get details for each team
    for i in range(num_teams):
        team_name = input(f"Enter the name of team {i+1}: ")
        win_percentage = int(input(f"Enter the win percentage for {team_name}: "))
        teams[team_name] = {"win_percentage": win_percentage}
    
    return teams

# Main function to run the program
def main():
    # Get teams and win percentages from user
    teams = get_user_input()

    # Run the tournament simulation
    print("\nStarting the IPL Tournament Simulation...\n")
    winning_team = simulate_tournament(teams)
    
    print(f"\nThe predicted IPL Winning Team is: {winning_team}")

# Run the main function
if __name__ == "__main__":
    main()
