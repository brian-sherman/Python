import json
import sys
from datetime import timedelta
from datetime import date

original_stdout = sys.stdout
today = date.today()
yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime('%Y-%m-%d')
print(yesterday)

with open("C:\\Filepath\\Systems.json", "r") as f1:
    data = json.load(f1)

with open("C:\\Filepath\\Inspectors.json", "r") as f2:
    data2 = json.load(f2)

for system in data:
    if system["CreatedOn"][0:10] == yesterday:
        with open("C:\\Filepath\\Systems-Report-%s.txt" % (yesterday), "a+") as f3:
            sys.stdout = f3
            system_environment_name = system["Environment"]["Name"]
            system_launchpoint_alias = system["Launchpoint"]["Alias"]
            print("Inspector: ", system["Inspector"]["Alias"])
            print("Environment: ", system_environment_name)
            print("Alias: " , system_launchpoint_alias)
            print("Name: ", system["Name"])
            print("Created On: ", system["CreatedOn"])
            for inspector in data2:
                try:
                    if system_environment_name == inspector["Environment"]["Name"] and system_launchpoint_alias == inspector["Alias"]:
                        if "UpdatedBy" in inspector.keys():
                            print("Updated By: ", inspector["UpdatedBy"]["Username"])
                        elif "CreatedBy" in inspector.keys():
                            print("CreatedBy: ", inspector["CreatedBy"]["Username"])
                        else:
                            print("Unable to identify user. Please check CW Manage.")
                except TypeError:
                    continue     
            print()
            sys.stdout = original_stdout