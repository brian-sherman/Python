import json
import sys
from datetime import timedelta
from datetime import date

original_stdout = sys.stdout
today = date.today()
yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
print(yesterday)

with open("C:\\FilePath\\Inspectors.json", "r") as f1:
    data = json.load(f1)
    for inspector in data:
        if inspector["CreatedOn"][0:10] == yesterday:
            with open("C:\\FilePath\\Inspectors-Report-%s.txt" % (yesterday), "a+") as f2:
                sys.stdout = f2
                print("Inspector: ", inspector["Inspector"]["Alias"])
                print("Environment: ", inspector["Environment"]["Name"])
                print("Alias: " , inspector["Alias"])
                print("Created On: ", inspector["CreatedOn"])
                if "UpdatedBy" in inspector.keys():
                    print("Updated By: ", inspector["UpdatedBy"]["Username"])
                elif "CreatedBy" in inspector.keys():
                    print("CreatedBy: ", inspector["CreatedBy"]["Username"])
                print()
                sys.stdout = original_stdout

