import pandas as pd

df = pd.read_csv("keylogger_results.csv")

down_events = df[df["Event"] == "down"].copy()
#print(down_events)

up_events = df[df["Event"] == "up"].copy()
#print(up_events)

result_df = pd.DataFrame()
result_df["User"] = down_events["User"].values
result_df["Key"] = down_events["Key"].values
result_df["TimeDown"] = down_events["TimeInMillis"].values
result_df["TimeUp"] = up_events["TimeInMillis"].values
result_df["H"] = up_events["TimeInMillis"].values - down_events["TimeInMillis"].values

result_df["DD"] = down_events["TimeInMillis"].diff().values
result_df["UU"] = up_events["TimeInMillis"].diff().values
result_df["UD"] = result_df["UU"].values - result_df["H"].values

pd.set_option('display.max_columns', None)
#print(result_df)
result_df.to_csv("analyzed_results.csv", index=False)