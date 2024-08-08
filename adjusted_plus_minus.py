import pandas as pd


def starter_names(team_id, game_id):
    df = pd.read_csv("player_box_2024.csv")
    pd.set_option("display.max_columns", None)
    filtered_df = df[(df["game_id"] == game_id) & (df["team_id"] == team_id)]
    #print(filtered_df)
    rows = filtered_df.shape[0]
    team_dict = {}
    for i in range(rows):
        #print(filtered_df.iloc[i]["athlete_id"])
        #print(filtered_df.iloc[i]["starter"])
        team_dict[filtered_df.iloc[i]["athlete_id"]] = filtered_df.iloc[i]["starter"]
    return team_dict


def substitution_record(game_df, game_id):
    filtered_df = game_df[(game_df["type_text"] == "Substitution")]
    #print(filtered_df.iloc[0]['home_team_id'])
    #print(filtered_df.iloc[0]['away_team_id'])
    home_team_active = starter_names(filtered_df.iloc[0]['home_team_id'], game_id)
    away_team_active = starter_names(filtered_df.iloc[0]['away_team_id'], game_id)
    #print(home_team_active)
    #print(away_team_active)
    rows = filtered_df.shape[0]

    stint_list = []

    last_substitution_clock_display_value = ""
    is_new_stint = True
    allPlayers = open('PlayersNames.csv', 'r')
    Lines = allPlayers.readlines()

    for i in range(rows):
        if filtered_df.iloc[i]['clock_display_value'] == last_substitution_clock_display_value:
            is_new_stint = False
        else:
            is_new_stint = True
        if is_new_stint:
            #print(filtered_df.iloc[i]['clock_display_value'])
            #print(filtered_df.iloc[i]["home_score"] - filtered_df.iloc[i]["away_score"])
            stint_number = str(game_id) + ","
            for line in Lines:
                player_id_and_name = line.split(",")
                #print(player_id_and_name[0])
                player_id = int(player_id_and_name[0])
                if player_id in home_team_active and home_team_active[player_id]:
                    stint_number = stint_number + "1" + ","
                elif player_id in away_team_active and away_team_active[player_id]:
                    stint_number = stint_number + "-1" + ","
                else:
                    stint_number = stint_number + "0" + ","

            #print(home_team_active)
            stint_number = stint_number + str(filtered_df.iloc[i]["home_score"] - filtered_df.iloc[i]["away_score"])
            #print(stint_number)
            #f.writelines(stint_number + "\n")
            stint_list.append(stint_number + "\n")
        last_substitution_clock_display_value = filtered_df.iloc[i]['clock_display_value']
        #in a substitution, players enter or left the game creates a new stint
        if filtered_df.iloc[i]['team_id'] == filtered_df.iloc[i]['home_team_id']:
            home_team_active[filtered_df.iloc[i]['athlete_id_1']] = True
            home_team_active[filtered_df.iloc[i]['athlete_id_2']] = False
        else:
            away_team_active[filtered_df.iloc[i]['athlete_id_1']] = True
            away_team_active[filtered_df.iloc[i]['athlete_id_2']] = False
    end_of_game_filtered_df = game_df[(game_df["type_text"] == "End Period") & (game_df["period_number"] == 4) & (game_df["game_id"] == game_id)]
    #print(end_of_game_filtered_df.iloc[0])
    end_of_game_stint = str(game_id) + ","
    for line in Lines:
        player_id_and_name = line.split(",")
        player_id = int(player_id_and_name[0])
        if player_id in home_team_active and home_team_active[player_id]:
            end_of_game_stint = end_of_game_stint + "1" + ","
        elif player_id in away_team_active and away_team_active[player_id]:
            end_of_game_stint = end_of_game_stint + "-1" + ","
        else:
            end_of_game_stint = end_of_game_stint + "0" + ","
    end_of_game_stint = end_of_game_stint + str(end_of_game_filtered_df.iloc[0]["home_score"] - end_of_game_filtered_df.iloc[0]["away_score"])
    #print(end_of_game_stint)
    stint_list.append(end_of_game_stint+ "\n")

    return stint_list

def each_game_data():
    df = pd.read_csv("play_by_play_2024.csv")
    pd.set_option("display.max_columns", None)
    game_data = df.groupby("game_id")
    game_data_lists = list(game_data)
    #print(game_data_lists[0][0])
    #print(game_data_lists[0][1])
    all_stint_list = []
    for game in game_data_lists:
        game_stint_list = substitution_record(game[1], game[0])
        all_stint_list.extend(game_stint_list)


    print(len(all_stint_list))
    allPlayers = open('PlayersNames.csv', 'r')
    Lines = allPlayers.readlines()

    with open('adjusted_plus_minus.csv', 'w') as f:
        all_ids = ""
        for line in Lines:
            player_id_and_name = line.split(",")
            #print(player_id_and_name[0])
            all_ids = all_ids + player_id_and_name[0] + ","
        #print(all_ids)
        f.writelines("GameID, " + all_ids + "ScoreDifferential" + "\n")

        for stint in all_stint_list:
            f.writelines(stint)
            #print(stint)







if __name__=="__main__":
    each_game_data()
