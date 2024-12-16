import art
print(art.logo)

def finding_highest_number(name):
    number = 0
    winner = ""
    for key in name:
        bidder_amount = name[key] #the value of the key
        if bidder_amount > number: #Check which one is the highest

            #This seperate the key and value into seperate variable
            number = bidder_amount
            winner = key #putting the key in here just in case
    print(f"The higest bidder is {winner} with ${number}")


list_bidder = {}
game = True

while game:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    yes_or_no = input("Is there any other bid(yes or no): ")
    list_bidder[name] = bid #Adding new information inside dict
    print("\n" * 20)

    if yes_or_no == "no":
        game = False
        finding_highest_number(list_bidder)



#print(list_bidder)