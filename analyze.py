import pandas as pd

df = pd.read_csv("keylogger_results.csv")

# result_df = pd.DataFrame(columns=["User", "Key", "TimeDown", "TimeUp", "H"])
# last_down = {}

# for index, row in df.iterrows():
#     user = row["User"]
#     key = row["Key"]
#     event = row["Event"]
#     time = row["TimeInMillis"]
#     if event == "down":
#         last_down[(user, key)] = time
#     elif event == "up" and (user, key) in last_down:
#         down_time = last_down[(user, key)]
#         hold_time = time - down_time
#         new_row = {
#             "User": user,
#             "Key": key,
#             "TimeDown": down_time,
#             "TimeUp": time,
#             "H": hold_time
#         }
#         result_df = pd.concat([result_df, pd.DataFrame([new_row])], ignore_index=True)
#         del last_down[(user, key)]

down_events = df[df["Event"] == "down"].copy()
print(down_events)

up_events = df[df["Event"] == "up"].copy()
print(up_events)

result_df = pd.DataFrame()
result_df["User"] = down_events["User"].values
result_df["Key"] = down_events["Key"].values
result_df["TimeDown"] = down_events["TimeInMillis"].values
result_df["TimeUp"] = up_events["TimeInMillis"].values
result_df["H"] = up_events["TimeInMillis"].values - down_events["TimeInMillis"].values

result_df["DD"] = down_events["TimeInMillis"].diff().values
result_df["UU"] = up_events["TimeInMillis"].diff().values
result_df["UD"] = result_df["UU"].values - result_df["H"].values

def fillNaValues(columnName):
    average = result_df[columnName].mean()
    result_df[columnName] = result_df[columnName].fillna(average)

fillNaValues("DD")
fillNaValues("UU")
fillNaValues("UD")

pd.set_option('display.max_columns', None)
print(result_df)
result_df.to_csv("analyzed_results.csv", index=False)