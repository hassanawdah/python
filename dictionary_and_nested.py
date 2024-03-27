travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visit": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visit": 5,
    },
}

for key in travel_log:
    print(f"The key is {key}, and the value for this key is {travel_log[key]}")
    if type(travel_log[key]) == dict:
        for nestedKey in travel_log[key]:
            print(travel_log[key][nestedKey])

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])