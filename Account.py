import csv

def save_to_database(username, password, item_picked):
    import csv
    with open("users.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, ";".join(item_picked)])
    print(f"Account for {username} created and order saved.")

# Function to log in and retrieve a user’s previous orders.
def view_orders(username, password):
    import csv
    with open("users.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 3:  # Ensure row has enough data
                continue
            if row[0] == username and row[1] == password:
                orders = row[2].split(";")  # Convert the saved order string back to a list
                print(f"Welcome back, {username}. Your previous orders: {orders}")
                return orders
    print("Invalid username or password.")
    return None


def create_an_account(item_picked):
    
    username = input("Create a new username: ")
    password = input("Create a new password: ")
    

    
    save_to_database(username, password, item_picked)

    
    print("\nNow, please log in to your account.")
    login_username = input("Username: ")
    login_password = input("Password: ")

    
    view_orders(login_username, login_password)


