import pandas as pd
import csv

df = pd.read_csv("output.csv")
# userList = data.User.unique()
# keyList = data.Key.unique()

# print(userList)

# df = pd.DataFrame(columns=['Subject','Key','H','UD','DD'])
# for i in range(0, len(userList)):
#     for j in range(0,len(keyList)):
#         queryData = data.query("User == '" + userList[i] + "' and Key == '" + keyList[j] + "'")
#         queryLen = len(queryData)
#         print(queryData)
#         finalData = {}
#         if queryLen > 0:
#             if(queryLen > 2):
#                 for k in range(0,queryLen,2):
#                     finalData['Subject'] = userList[i]
#                     finalData['Key'] = keyList[j]
#                     finalData['H'] = queryData.iloc[k+1].TimeInMillis - queryData.iloc[k].TimeInMillis
#                     keyUpIndex = queryData.iloc[k+1].name
#                     if(data.iloc[keyUpIndex + 1].User == userList[i]):
#                         finalData['UD'] = data.iloc[keyUpIndex+1].TimeInMillis - queryData.iloc[k+1].TimeInMillis
#                         finalData['DD'] = data.iloc[keyUpIndex+1].TimeInMillis - queryData.iloc[k].TimeInMillis
#                     else:
#                         finalData['UD'] =  finalData['H']
#                         finalData['DD'] = finalData['H']
#                     df.loc[len(df)] = finalData
#             else:
#                 finalData['Subject'] = userList[i]
#                 finalData['Key'] = keyList[j]
#                 finalData['H']= queryData.query("Event=='up'").TimeInMillis - queryData.query("Event=='down'").TimeInMillis
#                 keyUpIndex = queryData.query("Event=='up'").index[0]
#                 if(data.iloc[keyUpIndex + 1].User == userList[i]):
#                         finalData['UD'] = data.iloc[keyUpIndex+1].TimeInMillis - queryData.query("Event=='up'").TimeInMillis
#                         finalData['DD'] = data.iloc[keyUpIndex+1].TimeInMillis - queryData.query("Event=='down'").TimeInMillis
#                 else:
#                     finalData['UD'] =  finalData['H']
#                     finalData['DD'] =  finalData['H']
#                 df.loc[len(df)] = finalData
            
           
                
# f = open("distance.csv", 'w',newline='\n')
# writer = csv.writer(f)
# writer.writerow(['Subject','Key','H','UD','DD'])
# for row in df.iterrows():
#     #print(row[1])
#     writer.writerow(row[1])
    
# f.close()

result_df = pd.DataFrame(columns=["User", "Key", "TimeDown", "TimeUp", "TimePassed"])

last_down = {}

for index, row in df.iterrows():
    user = row["User"]
    key = row["Key"]
    event = row["Event"]
    time = row["TimeInMillis"]
    if event == "down":
        last_down[(user, key)] = time
    elif event == "up" and (user, key) in last_down:
        down_time = last_down[(user, key)]
        time_passed = time - down_time
        new_row = {
            "User": user,
            "Key": key,
            "TimeDown": down_time,
            "TimeUp": time,
            "TimePassed": time_passed
        }
        result_df = pd.concat([result_df, pd.DataFrame([new_row])], ignore_index=True)
        del last_down[(user, key)]


    # if row["Event"] == "down":
    #     current_user = row["User"]
    #     current_key = row["Key"]
    #     down_time = row["TimeInMillis"]
    # elif row["Event"] == "up" and row["User"] == current_user and row["Key"] == current_key:
    #     up_time = row["TimeInMillis"]
    #     time_passed = up_time - down_time

    #     new_row = {
    #         "User": current_user,
    #         "Key": current_key,
    #         "TimeDown": down_time,
    #         "TimeUp": up_time,
    #         "TimePassed": time_passed
    #     }

    #     result_df = pd.concat([result_df, pd.DataFrame([new_row])], ignore_index=True)
                
print(result_df)
result_df.to_csv("analyzed_results.csv", index=False)