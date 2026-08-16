user_dict = {}
continue_bidding = True

while continue_bidding:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid value: $"))
    user_dict[name] = bid
    
    should_continue = input("Are there any other bidders? yes/no: ").lower()
    if should_continue == "no":
        continue_bidding = False

# Find the highest bidder
highest_bidder = max(user_dict, key=user_dict.get)
print(f"The winner is {highest_bidder} with a bid of ${user_dict[highest_bidder]}")
