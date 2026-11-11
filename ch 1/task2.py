# price1= float(input("Enter the price of the first item: "))
# price2= float(input("Enter the price of the second item: "))
# price3= float(input("Enter the price of the third item: "))
# total_price = price1 + price2 + price3
# average_price = total_price / 3
# print(f"The total price of the three items is: {total_price}")
# print(f"The average price of the three items is: {average_price}")


#
#  part two

while True:
    name = input("Enter your name: ")
    if('S' in name):
        print("Your name contains the letter S.")
    elif('s' in name):
        print("Your name contains the letter s.")
    else:
        print("Your name does not contain the letter S or s.")