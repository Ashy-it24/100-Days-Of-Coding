logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def fhighest_bidder(data_bid):
    highest_price = 0
    winner = ""
    for i in data_bid:

        price=data_bid[i]

        if price>highest_price:
            highest_price=price
            winner=i
    print("highest bidder is ",winner,"with $",highest_price)
data_dictionary={}
should_continue=True
while should_continue:
    print(logo)

    name=input("Whats your name:\n")
    bid=int(input("Enter your bid $"))

# TODO-2: Save data into dictionary {name: price}

    data_dictionary[name]=bid
    option = input("Is there anyone else bidding yes/no\n")



    if option=="no":
        should_continue=False
        fhighest_bidder(data_bid=data_dictionary)
    else:
        print("\n"*100)
