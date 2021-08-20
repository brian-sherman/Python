import json
import sys

original_stdout = sys.stdout
technician = input("Enter the technician's email address: ")
technician = technician.lower()
count = 0

def inspector_printout():
    print("Inspector: ", inspector["Inspector"]["Alias"])
    print("Environment: ", inspector["Environment"]["Name"])
    print("Alias: " , inspector["Alias"])
    print("Created On: ", inspector["CreatedOn"])
    print()

with open("C:\\FilePath\\Inspectors.json", "r") as f1:
    data = json.load(f1)
    for inspector in data:
        with open("C:\\FilePath\\Inspectors-Technician-Report-%s.txt" % (technician), "a+") as f2:
            sys.stdout = f2
            if "UpdatedBy" in inspector.keys() and inspector["UpdatedBy"]["Username"] == technician:
                print("Updated By: ", inspector["UpdatedBy"]["Username"])
                inspector_printout()
                count += 1
            elif "CreatedBy" in inspector.keys() and inspector["CreatedBy"]["Username"] == technician:
                print("CreatedBy: ", inspector["CreatedBy"]["Username"])
                inspector_printout()
                count += 1
            sys.stdout = original_stdout

with open("C:\\FilePath\\Inspectors-Technician-Report-%s.txt" % (technician), "a+") as f2:
    sys.stdout = f2
    f2.write("\n")
    print("Total inspectors created and updated by %s = %d" % (technician, count))
    sys.stdout = original_stdout