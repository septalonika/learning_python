welcome_message = "Welcome to Cugud Store"

user_selection = 1

print("=========================================")
print(f"====== {welcome_message} =======")
print("=========================================")
print(" ")
print(" ")

while user_selection != 0:
    print("=========================================")
    print("Anything we can help?")
    print("[1] Buy")
    print("[2] Check Stock")
    print("[0] Exit")
    print("=========================================")
    
    print(" ")
    user_selection = int(input("Please select an option: "))
    
    if user_selection == 1:
        print(" ")
        print(" ")
        print("=========================================")
        print("What do you want to buy?")
        print("[1] T-Shirt")
        print("[2] Pants")
        print("[3] Shoes")
        print("[4] cancel")
    elif user_selection == 2:
        print(" ")
        print(" ")
        print("=========================================")
        print("What do you want to buy?")
        print("[1] T-Shirt")
        print("[2] Pants")
        print("[3] Shoes")
        print("[4] cancel")
        
    elif user_selection == 0:
        print(" ")
        print(" ")
        print("=========================================")
        print("Goodbye")
        print("=========================================")

        