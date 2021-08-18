import json
import sys
from datetime import timedelta
from datetime import date

original_stdout = sys.stdout
today = date.today()
yesterday = yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
print(yesterday)

with open("C:\\FilePath\\Systems.json", "r") as f1:
    data = json.load(f1)
    for system in data:
        if system["CreatedOn"][0:10] == yesterday:
            with open("C:\\FilePath\\Systems-Report-%s.txt" % (yesterday), "a+") as f2:
                sys.stdout = f2
                print("Inspector: ", system["Inspector"]["Alias"])
                print("Environment: ", system["Environment"]["Name"])
                print("Alias: " , system["Launchpoint"]["Alias"])
                print("Name: ", system["Name"])
                print("Created On: ", system["CreatedOn"])
                print()
                sys.stdout = original_stdout