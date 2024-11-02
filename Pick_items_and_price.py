def num_item():           # Ask the customer how many item they want to buy + input validation
    while True:
        try:
            num_of_product=int(input("How many product do you want to buy: "))
        except ValueError:
            print("Please input number only! ")
        else:
            break
    return num_of_product



def choose_item(menu_items,item_picked):           # Ask the customer to choose the item+input validation
    while True:
        try:
            choose=str(input("Enter the name of product: ")).lower()
            if choose not in menu_items:
                raise TypeError
        except TypeError or ValueError:
            print("Please only type in the name of product from the menu")
        else:
            item_picked.append(choose)
            break
    return item_picked

def sum_price(menu_items,item_picked,total_price):         # Sum price for all items picked +validation 
    for i in range(0,len(item_picked)):
        Price_for_each_item=menu_items.get(item_picked[i])
        total_price+=Price_for_each_item
        
    return total_price
