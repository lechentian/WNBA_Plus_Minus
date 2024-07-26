import pandas as pd

df = pd.read_csv('play_by_play_2024.csv')
pd.set_option('display.max_columns', None)
user_groups= df.groupby("athlete_id_1")
all_user_lists = list(user_groups)
print(all_user_lists[0][1])
print(all_user_lists[0][1].iloc[0]["text"])
#text_with_player_name = all_user_lists[0][1].iloc[0]["text"]
#player_name_list = text_with_player_name.split(" ")
#new_list = [x for x in player_name_list if x[0].isupper()]
#user_name = " ".join(new_list)
#print(user_name)
#print(type(all_user_lists[0][1]))
with open('allPlayers.csv', 'w') as f:
    for i in range(len(all_user_lists)):
        print(all_user_lists[i][0])
        text_with_player_name = all_user_lists[i][1].iloc[0]["text"]
        player_name_list = text_with_player_name.split(" ")
        new_list = [x for x in player_name_list if x[0].isupper()]
        user_name = " ".join(new_list[0:2])
        print(user_name)
        f.writelines(str(int(all_user_lists[i][0])) + "," + user_name + "\n")