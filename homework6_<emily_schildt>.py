web_users = ["violet", "daphne", "anthony", "eloise", "simon"]
new_users = ["eloise", "simon", "sophie", "benedict", "kate"]
for user in new_users:
    if user in web_users:
        print(f"{user}: This user name is already in use. Please choose a different user name.")
    else:
        print(f"{user}: This user name is available.")


cities = {
    "Seattle": {
        "country": "United States",
        "population": "780995",
        "fact": "Known as the Emerald City"
    },
    "Positano": {
        "country": "Italy",
        "population": "3678",
        "fact": "Cliffside town on the Amalfi Coast"
    },
    "Luxembourg City": {
        "country": "Luxembourg",
        "population": "136208",
        "fact": "There are three official languages"
    }
}
for city, info in cities.items():
    print(f"City: {city} Country: {info['country']} Population: {info['population']} Fact: {info['fact']}")