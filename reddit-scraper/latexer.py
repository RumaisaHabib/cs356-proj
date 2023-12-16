import pandas as pd
import os

files = sorted(os.listdir())

for file in files:
    if file[-3:] =="csv":
        topic = file.split(".")[0]
        assigned = ", ".join([x.title() for x in list(pd.read_csv(file)["Topic Name"])])
        assigned = assigned.replace("&","\&")
        print(f"{topic.capitalize()} & {assigned} \\\\")