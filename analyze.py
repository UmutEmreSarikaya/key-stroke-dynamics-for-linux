import pandas as pd
import csv

df = pd.read_csv("output.csv")

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
                
print(result_df)
result_df.to_csv("analyzed_results.csv", index=False)