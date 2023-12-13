import pandas as pd
import os

df = pd.read_csv("analyzed_results.csv")

processed_df = pd.DataFrame(columns=["H", "DD", "UU", "UD", "Key_stroke_average", "Label"])

start_time = df["TimeDown"].iloc[0]
end_time = df["TimeUp"].iloc[-1]
username = df.iloc[0]["User"]

total_time = end_time - start_time

processed_df.loc[0, "H"] = df["H"].mean()
processed_df.loc[0, "DD"] = df["DD"].mean()
processed_df.loc[0, "UU"] = df["UU"].mean()
processed_df.loc[0, "UD"] = df["UD"].mean()
processed_df.loc[0, "Key_stroke_average"] = (len(df)/total_time)*500 #number of keys pressed in 500 ms(half a second)
processed_df.loc[0, "Label"] = username

file_path = "key_stroke_data.csv"

if os.path.exists(file_path):
    include_header = False
else:
    include_header = True

processed_df.to_csv(file_path, header=include_header, index=False, mode='a')