import pandas as pd
import os

csv_file = input("Enter file name with .csv extension to analyze (example: filename.csv): ")
df = pd.read_csv(csv_file)

down_events = df[df["Event"] == "down"].copy()
#print(down_events)

up_events = df[df["Event"] == "up"].copy()
#print(up_events)

analyzed_df = pd.DataFrame()
analyzed_df["User"] = down_events["User"].values
analyzed_df["Key"] = down_events["Key"].values
analyzed_df["TimeDown"] = down_events["TimeInMillis"].values
analyzed_df["TimeUp"] = up_events["TimeInMillis"].values
analyzed_df["H"] = up_events["TimeInMillis"].values - down_events["TimeInMillis"].values
analyzed_df["DD"] = down_events["TimeInMillis"].diff().values
analyzed_df["UU"] = up_events["TimeInMillis"].diff().values
analyzed_df["UD"] = analyzed_df["UU"].values - analyzed_df["H"].values

analyzed_df.to_csv("analyzed_results.csv", index=False)

processed_df = pd.DataFrame(columns=["H", "DD", "UD", "key_stroke_average", "back_space_count", "shift_left_favored", "used_caps", "label"])

start_time = analyzed_df["TimeDown"].iloc[0]
end_time = analyzed_df["TimeUp"].iloc[-1]
username = analyzed_df.iloc[0]["User"]

total_time = end_time - start_time

processed_df.loc[0, "H"] = analyzed_df["H"].mean()
processed_df.loc[0, "DD"] = analyzed_df["DD"].mean()
processed_df.loc[0, "UD"] = analyzed_df["UD"].mean()
processed_df.loc[0, "key_stroke_average"] = (len(analyzed_df)/total_time)*500 #number of keys pressed in 500 ms(half a second)
processed_df.loc[0, "back_space_count"] = (analyzed_df["Key"].value_counts().get("BACK_SPACE", 0)/total_time)*500 #number of BACK_SPACE pressed in 500 ms(half a second)

shift_left_count = analyzed_df["Key"].value_counts().get("SHIFT_LEFT", 0)
shift_right_count = analyzed_df["Key"].value_counts().get("SHIFT_RIGHT", 0)

if shift_left_count < shift_right_count:
    shift_left_favored = 0
else:
    shift_left_favored = 1

processed_df.loc[0, "shift_left_favored"] = shift_left_favored

if "CAPS_LOCK" in analyzed_df["Key"].values:
    used_caps = 1
else:
    used_caps = 0

processed_df.loc[0, "used_caps"] = used_caps
processed_df.loc[0, "label"] = username

file_path = "key_stroke_data.csv"

if os.path.exists(file_path):
    include_header = False
else:
    include_header = True

processed_df.to_csv(file_path, header=include_header, index=False, mode='a')