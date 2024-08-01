import pandas as pd

def score_differential(df, game_id):
    filtered_df = df[(df["type_text"] == "End Period") & (df["period_number"] == 4) & (df["game_id"] == game_id)]
    return filtered_df.iloc[0]["home_score"] - filtered_df.iloc[0]["away_score"]

def end_of_game_data(df, game_id, all_team_id_dict):
    filtered_df = df[(df["type_text"] == "End Period") & (df["period_number"] == 4) & (df["game_id"] == game_id)]
    one_row_str = str(game_id) + ","
    #print(filtered_df.iloc[0]["home_team_id"])
    for key, value in all_team_id_dict.items():
        if int(key) == int(filtered_df.iloc[0]["home_team_id"]):
            one_row_str = one_row_str + "1, "
        elif int(key) == int(filtered_df.iloc[0]["away_team_id"]):
            one_row_str = one_row_str + "-1, "
        else:
            one_row_str = one_row_str + "0, "
    one_row_str = one_row_str + str(filtered_df.iloc[0]["home_score"] - filtered_df.iloc[0]["away_score"])
    return one_row_str



def wnba_team_data():
    df = pd.read_csv("play_by_play_2024.csv")
    pd.set_option("display.max_columns", None)
    game_data = df.groupby("game_id")
    game_data_list = list(game_data)
    all_team_id_dict = {3: "Dallas", 5: "Indiana", 6: "Los Angeles", 8: "Minnesota", 9: "NewYork", 11: "Phoenix", 14: "Seattle", 16: "Washington", 17: "Las Vegas", 18: "Connecticut", 19: "Chicago", 20: "Atlanta"}
    #print(game_data_list[0][0])
    #print(game_data_list[0][1])
    #print(fourth_period_data(df, game_data_list[0][0], all_team_id_dict))
    with open("bradleyterry_model_in_wnba.csv", "w") as f:
        f.write("GameID,Dallas,Indiana,LosAngeles,Minnesota,NewYork,Phoenix,Seattle,Washington,LasVegas,Connecticut,Chicago,Atlanta,ScoreDifferential\n")
        for game in game_data_list:
            if game[1].iloc[0]["home_team_id"] in all_team_id_dict or game[1].iloc[0]["home_team_id"] in all_team_id_dict:
                f.write(end_of_game_data(df, game[0], all_team_id_dict) + "\n")






if __name__=="__main__":
    wnba_team_data()