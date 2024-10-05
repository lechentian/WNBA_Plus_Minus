import pandas as pd


def different_stats(filtered_df):
    rows = filtered_df.shape[0]
    #print(rows)
    total_rebounds = 0
    total_minutes = 0
    total_assists = 0
    total_steals = 0
    total_points = 0
    for i in range(rows):
        total_minutes = total_minutes + filtered_df.iloc[i]["minutes"]
        total_rebounds = total_rebounds + filtered_df.iloc[i]["rebounds"]
        #print(filtered_df.iloc[i]['rebounds'])
        total_assists = total_assists + filtered_df.iloc[i]["assists"]
        total_steals = total_steals + filtered_df.iloc[i]["steals"]
        total_points = total_points + filtered_df.iloc[i]["points"]
    #print(total_rebounds, total_minutes)
    average_rebounds = format(total_rebounds / (total_minutes / 40), '.2f')
    average_assists = format(total_assists / (total_minutes / 40), '.2f')
    average_steals = format(total_steals / (total_minutes / 40), '.2f')
    average_points = format(total_points / (total_minutes / 40), '.2f')
    return average_rebounds, average_assists, average_steals, average_points, total_minutes

def all_players_data():
    df = pd.read_csv("player_box_2024_removed_USA.csv")
    pd.set_option("display.max_columns", None)
    allPlayers = open('PlayersNames.csv', 'r')
    Lines = allPlayers.readlines()
    with open("all_player_bpm_stats.csv", "w") as f:
        f.write("PlayerID, PlayerName, AverageRebounds, AverageAssists, AverageSteals, AveragePoints, TotalMinutes \n")
        for line in Lines:
            user_id_with_name = line.split(",")
            player_id = int(user_id_with_name[0].strip())
            filtered_df = df[(df["athlete_id"] == player_id)]
            x = different_stats(filtered_df)
            #print(x[1])
            line = str(player_id) + "," + str(user_id_with_name[1]).strip() + "," + str(x[0]) + "," + str(x[1]) + "," + str(x[2]) + "," + str(x[3]) + "," + str(x[4])
            print(line)
            f.write(line + "\n")

if __name__=="__main__":
    all_players_data()