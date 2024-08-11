import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


#https://aiplanet.com/blog/a-beginners-guide-to-linear-regression-in-python-with-scikit-learn/
data = pd.read_csv("adjusted_plus_minus_2.csv")

#print(data.shape)

allPlayers = open('PlayersNames.csv', 'r')
Lines = allPlayers.readlines()
all_user_ids = []
all_user_name = []
for line in Lines:
    player_id_and_name = line.split(",")
    #all_ids = all_ids + player_id_and_name[0] + ","
    #if player_id_and_name[0] != "585":
    all_user_ids.append(player_id_and_name[0])
    all_user_name.append(player_id_and_name[1])

all_user_ids.pop()
coefficient = ","
#print(all_ids)


x = data[all_user_ids].values
y = data['ScoreDifferential'].values
y_wight_sting_time = data['StintTime'].values
#print(x)
print(y_wight_sting_time)
print(type(y_wight_sting_time))
y_list = np.ndarray.tolist(y_wight_sting_time)
# print(y_list)
# for i in y_list:
#     if i <0:
#         print(i)


model = LinearRegression()
model.fit(x, y, sample_weight=y_wight_sting_time)
r2_score = model.score(x, y)
#print(model.coef_)
#print(model.intercept_)
#print(f"R-squared value: {r2_score}")
List_result = np.ndarray.tolist(model.coef_)
List_result.append(-1.223758894)
print(List_result)
print(len(List_result))
all_user_ids.append(5209660)


data = pd.read_csv("plusminus_data_set.csv")
cc = data['Plus_min'].values
print(len(cc))


print(len(all_user_ids))

with open('graph.csv', 'w') as f:
    f.writelines("UserId,UserName,Plus_min,Adjust_plus_min" +"\n")
    for i in range(len(all_user_ids)):
        f.writelines(str(all_user_ids[i])+","+all_user_name[i].strip()+","+str(cc[i])+","+str(List_result[i])+"\n")
        #player_id_and_name = line.split(",")
        #print(player_id_and_name[0])
        #all_ids = all_ids + player_id_and_name[0] + ","
    #print(all_ids)
    #f.writelines(all_ids + "\n")
    #coefficient = ","
    #for line in List_result:
        #coefficient = coefficient + str(line) + ","
    #f.writelines(coefficient + "\n")

#'585','869','887','918','924','981','1004','1054','1068','2284331','2490553','2490794','2491205','2491214','2529047','2529122','2529130','2529137','2529140','2529183','2529205','2529458','2529622','2566081','2566106','2566110','2566186','2566453','2569044','2590093','2593770','2955898','2984741','2987869','2987891','2988756','2998927','2998928','2998938','2999035','2999101','3054590','3056672','3056730','3058892','3058893','3058895','3058901','3058902','3058908','3065570','3099025','3099736','3102133','3142010','3142055','3142086','3142191','3142250','3142255','3142327','3142948','3143510','3146151','3149391','3156318','3904576','3904577','3906753','3906972','3907781','3913881','3913903','3916514','3917450','3917453','3922628','3934218','4038390','4065759','4065760','4065820','4065870','4066527','4066533','4066548','4066553','4066585','4068042','4068159','4068161','4257500','4280850','4280892','4281183','4281190','4281253','4281929','4282168','4282173','4398567','4398591','4398674','4398726','4398729','4398751','4398752','4398764','4398768','4398776','4398779','4398829','4398899','4398907','4398911','4398915','4398935','4398938','4398966','4399114','4399415','4420318','4422426','4432830','4432831','4432832','4432834','4432841','4432864','4432865','4433293','4433386','4433402','4433403','4433404','4433405','4433408','4433468','4433630','4433633','4433635','4433661','4594527','4595236','4595910','4683006','5017721','5017726','5105752','5106150','5130672','5209660',