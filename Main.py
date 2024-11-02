from Menu import *  #return menu
from Pick_items_and_price import * # return: num of items, list of item picked, sum price for item picked
from Delivery import * # return distance , delivery fee
from Currency_exchange import * #return list of exchange rate, chosen currency , total price in desie currency
from Account import *
import pyfiglet 

#Start
# python3 -m pip install --upgrade pip # pip install pyfiglet
# welcome customer
title = pyfiglet.figlet_format("BIL SHOP", font="5lineoblique") 
print(title) # Welcome customer
print(f"Here are the items you can buy today {menu()}") #print out menu 
menu_items=menu()

#choose items
num_of_product=num_item() # ask how many item does the customer want to buy
item_picked=[]
for i in range (0,int(num_of_product)): # ask them to pick the item for n times
   choose_item(menu_items,item_picked)  # create a list of items customer picked

#calculate price for all products
total_price=0 #calcualte the total price 
total_price=sum_price(menu_items,item_picked,total_price)

#find delivery distance
distance=delivery_location()

# Calcualte delivery fee
delivery_price=0
delivery_price=delivery_fee(distance)
total_price = total_price + delivery_price

#currency exchange if under 10 pounds or over 1000, can't convert
if total_price>=10 and total_price<=1000:
   chosen_currency=""
   print(f"Choose the currency you want to pay with {currency_dict()}") #choose currency
   chosen_currency=choose_currency(chosen_currency,currency_dict())

   exchange(chosen_currency,total_price,currency_dict()) #currency exchange

# Account
create_an_account(item_picked) #create account,login
print("Thank you for shopping in the BIL shop")
#end...





