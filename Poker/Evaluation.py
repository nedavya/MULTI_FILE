import csv

ranking_table = []

# Function to load the ranking table from CSV
def load_ranking_table(filename):
    global ranking_table
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ranking_table.append(row)

# Load ranking table at the beginning of the script
load_ranking_table('Pre_Flop.csv')


rank_initials = {
    "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "T",
    "Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"
}

# Function to evaluate the hand based on the ranking table
def evaluate_hand(cards):
    # Convert cards to a format similar to the one in the ranking table for comparison
    cards_str = "".join([rank_initials[card[0]] for card in cards])
    # Check for pair
    for row in ranking_table:
        if (row['Hand'] == cards_str and row['Type'] == 'pair') or (
                row['Hand'] == cards_str[::-1] and row['Type'] == 'pair'):  # Check reversed order for pair
            return int(row['Rank']), row['Type'], row['Win']

    # Check for suited
    if cards[0][1] == cards[1][1]:  # Same suit
        for row in ranking_table:
            if ((row['Hand'][0] == rank_initials[cards[0][0]] and row['Hand'][1] == rank_initials[cards[1][0]] and row['Type'] == 'suited') or (row['Hand'][0] == rank_initials[cards[1][0]] and row['Hand'][1] == rank_initials[cards[0][0]] and row['Type'] == 'suited')):
                return int(row['Rank']), row['Type'], row['Win']

    # Check for other types (e.g., not suited)
    for row in ranking_table:
        if (row['Hand'] == cards_str and row['Type'] == 'not') or (
                row['Hand'] == cards_str[::-1] and row['Type'] == 'not'):
            return int(row['Rank']), row['Type'], row['Win']

    # If no match is found, return a default rank and type
    return -1, "Unknown", "0"

def display_hand_rank(cards):
    rank, hand_type, win_percentage = evaluate_hand(cards)
    if rank == -1:
        print("Rank not found")
    else:
        for row in ranking_table:
            if int(row['Rank']) == rank and row['Type'] == hand_type:
                print(f"Rank: {row['Rank']} | Type: {row['Type']} | Win %: {win_percentage}")
                break


