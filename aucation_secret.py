bidder = {}
continue_or_stop = False


def find_highest_bidder(bid_records):
    highest_bidder = 0
    winner = ""
    for key in bid_records:
        if bid_records[key] > highest_bidder:
            highest_bidder = bidder[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bidder}")


while not continue_or_stop:
    print("Welcome to the secret auction program.")
    name = input("What is you name?: ")
    bid = float(input("What's your bid?:$ "))
    continue_or_stop = input("Are there any other bidders? Type 'yes' or 'no' .\n")
    bidder[name] = bid

    if continue_or_stop == "yes":
        continue_or_stop = False
    else:
        continue_or_stop = True
        find_highest_bidder(bidder)
