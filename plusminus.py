import pandas as pd
def get_court_time(enter, left):
    in_time_array = enter.split(":")
    in_time_array = [float(i) for i in in_time_array]
    out_time_array = left.split(":")
    out_time_array = [float(i) for i in out_time_array]
    on_court_time = in_time_array[1]+60-out_time_array[1]
    on_court_time = on_court_time+(in_time_array[0]-out_time_array[0]-1)*60
    return on_court_time

def last_period_score(df, game_id, period_number):
    if period_number == 1:
        return 0,0
    period_number = period_number - 1
    filtered_df = df[(df["type_text"] == "End Period") & (df["period_number"] == period_number) & (df["game_id"] == game_id)]
    return filtered_df.iloc[0]["home_score"], filtered_df.iloc[0]["away_score"]

def current_period_score(df, game_id, period_number):
    filtered_df = df[(df["type_text"] == "End Period") & (df["period_number"] == period_number) & (df["game_id"] == game_id)]
    return filtered_df.iloc[0]["home_score"], filtered_df.iloc[0]["away_score"]

def cal_data_for_each_period(full_df, player_df, player_id, period_id, game_id):
    filtered_df = player_df[(player_df['type_text'] == 'Substitution') & (player_df['period_number'] == period_id)]
    rows = filtered_df.shape[0]
    period_total = 0
    self_team_score_total = 0
    opposing_team_score_total = 0
    if rows == 0:
        active_df = player_df[(player_df['period_number'] == period_id)]
        if active_df.shape[0] > 0:
            if active_df.iloc[0]['home_team_id'] == active_df.iloc[0]['team_id']:
                self_team_score_total = self_team_score_total + current_period_score(full_df, game_id, period_id)[0] - last_period_score(full_df, game_id, period_id)[0]
                opposing_team_score_total = opposing_team_score_total + current_period_score(full_df, game_id, period_id)[1] - last_period_score(full_df, game_id, period_id)[0]
            else:
                self_team_score_total = self_team_score_total + current_period_score(full_df, game_id, period_id)[1] - last_period_score(full_df, game_id, period_id)[0]
                opposing_team_score_total = opposing_team_score_total + current_period_score(full_df, game_id, period_id)[0] - last_period_score(full_df, game_id, period_id)[0]
            return 600, self_team_score_total - opposing_team_score_total
        else:
            return 0,0
    else:
        #print(filtered_df)
        need_skip_next = False
        #current_period_total = 0
        for i in range(rows):
            if need_skip_next:
                need_skip_next = False
                continue
            #print("==============="+str(i))
            if player_id == filtered_df.iloc[i]['athlete_id_1'] :  # join court
                # print("join court")
                # print(filtered_df.iloc[i]['clock_display_value'])
                # print(filtered_df.iloc[i + 1]['clock_display_value'])
                if (i + 1) < rows:
                    period_total = period_total + get_court_time(filtered_df.iloc[i]['clock_display_value'], filtered_df.iloc[i + 1]['clock_display_value'])
                    need_skip_next = True
                    if filtered_df.iloc[i]['home_team_id'] == filtered_df.iloc[i]['team_id']:
                        self_team_score_total = self_team_score_total + filtered_df.iloc[i + 1]['home_score'] - filtered_df.iloc[i]['home_score']
                        opposing_team_score_total = opposing_team_score_total + filtered_df.iloc[i + 1]['away_score'] - filtered_df.iloc[i]['away_score']
                    else:
                        self_team_score_total = self_team_score_total + filtered_df.iloc[i + 1]['away_score'] - filtered_df.iloc[i]['away_score']
                        opposing_team_score_total = opposing_team_score_total + filtered_df.iloc[i + 1]['home_score'] - filtered_df.iloc[i]['home_score']
                else:
                    period_total = period_total + get_court_time(filtered_df.iloc[i]['clock_display_value'], "0:00")
                    if filtered_df.iloc[i]['home_team_id'] == filtered_df.iloc[i]['team_id']:
                        self_team_score_total = self_team_score_total + current_period_score(full_df, game_id, period_id)[0]- filtered_df.iloc[i]['home_score']
                        opposing_team_score_total =  opposing_team_score_total + current_period_score(full_df, game_id, period_id)[1] - filtered_df.iloc[i]['away_score']
                    else:
                        self_team_score_total = self_team_score_total + current_period_score(full_df, game_id, period_id)[1] - filtered_df.iloc[i]['away_score']
                        opposing_team_score_total = opposing_team_score_total + current_period_score(full_df, game_id, period_id)[0] - filtered_df.iloc[i]['home_score']
            else: # off court
                # print("off court")
                # print(filtered_df.iloc[i]['clock_display_value'])
                # print(filtered_df.iloc[i+1]['clock_display_value'])
                period_total = period_total + get_court_time("10:00", filtered_df.iloc[i]['clock_display_value'])
                if filtered_df.iloc[i]['home_team_id'] == filtered_df.iloc[i]['team_id']:
                    self_team_score_total = self_team_score_total + filtered_df.iloc[i]['home_score'] - last_period_score(full_df, game_id, period_id)[0]
                    opposing_team_score_total = opposing_team_score_total + filtered_df.iloc[i]['away_score'] - last_period_score(full_df, game_id, period_id)[1]
                else:
                    self_team_score_total = self_team_score_total + filtered_df.iloc[i]['away_score'] - last_period_score(full_df, game_id, period_id)[1]
                    opposing_team_score_total = opposing_team_score_total + filtered_df.iloc[i]['home_score'] - last_period_score(full_df, game_id, period_id)[0]
        #print("===============" + str(current_period_total))
        #print(self_team_score_total, opposing_team_score_total)
        return period_total, self_team_score_total - opposing_team_score_total

def each_game_data(full_df, game_id, player_df, player_id):
    each_game_on_court_time = 0
    game_plus_minus = 0
    for i in range(1,5,1):
        x = cal_data_for_each_period(full_df, player_df, player_id, i, game_id)
        each_game_on_court_time = each_game_on_court_time + x[0]
        game_plus_minus = game_plus_minus + x[1]
    return each_game_on_court_time, game_plus_minus
    #print(" player : " + str(player_id)+ " in game : " +str(game_id)+   " play "+ str(total_on_court_time) + " , and the total plus minus is " + str(total_plus_minus))

def all_players_data():
    df = pd.read_csv("play_by_play_2024.csv")
    pd.set_option("display.max_columns", None)
    allPlayers = open('PlayersNames.csv', 'r')
    Lines = allPlayers.readlines()
    with open("plusminusdataset.csv", "w") as f:
        f.write("PlayerID, PlayerName, TotalOnCourtTime, TotalPlusMinus, AveragePlusMinus \n")
        for line in Lines:
            user_id_with_name = line.split(",")
            player_id = int(user_id_with_name[0].strip())
            filtered_df = df[(df["athlete_id_1"] == player_id) | (df["athlete_id_2"] == player_id)]
            game_data = filtered_df.groupby("game_id")
            game_data_lists = list(game_data)
            #print(game_data_lists[0][0])
            #print(game_data_lists[0][1])
            print("The player "+ str(player_id) + " taken " + str(len(game_data_lists)) + " games")
            total_on_court_time = 0
            total_plus_minus = 0
            #each_game_data(df, game_data_lists[0][0], game_data_lists[0][1], player_id)
            for game in game_data_lists:
                y = each_game_data(df, game[0], game[1], player_id)
                total_on_court_time = total_on_court_time + y[0]
                total_plus_minus = total_plus_minus + y[1]
            if total_on_court_time != 0:
                average_plus_minus = format(total_plus_minus/(total_on_court_time/2400), '.2f')
            else:
                average_plus_minus = "/"
            line = str(player_id) + "," + str(user_id_with_name[1]).strip() + "," + str(total_on_court_time) + "," + str(total_plus_minus) + "," + str(average_plus_minus)
            #print(line)
            f.write(line + "\n")

def player_name_list():
    df = pd.read_csv('player_box_2024.csv')
    pd.set_option('display.max_columns', None)
    user_groups = df.groupby("athlete_id")
    all_user_lists = list(user_groups)
    with open('PlayersNames.csv', 'w') as f:
        for i in range(len(all_user_lists)):
            #print(all_user_lists[i][0])
            text_with_player_name = all_user_lists[i][1].iloc[0]["athlete_display_name"]
            #print(text_with_player_name)
            f.writelines(str(all_user_lists[i][0]) + "," + text_with_player_name + "\n")

if __name__=="__main__":
    player_name_list()
    all_players_data()

