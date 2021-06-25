tweet = input("Enter tweet:\n")

abbreviations = {
    "LOL": "laughing out loud",
    "BFN": "bye for now",
    "FTW": "for the win",
    "IRL": "in real life",
    "IANAL": "I am not a lawyer",
    "ROFL": "rolling on floor laughing",
    "LMAO": "laughing my ass off"
}

for key in abbreviations:
    if key in tweet:
        print(key)
        print(abbreviations[key])
else: 
    print("search completed")