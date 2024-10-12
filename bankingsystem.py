def show_balance():
    pass

def deposit():
    pass

def withdraw():
    pass

 
balance = 0
is_running = True

while is_running:
    print("Banking Program")
    choice = input("Press 'd' to deposit, 'w' to withdraw, 'b' to show balace, 'q' to quit:")
    
    if choice == 'd':
        show_balance()
    elif choice == 'w':
        withdraw()
    elif choice == 'b':
        show_balance()
    elif choice == 'q':
        is_running = False
    else:
        print("Invalid choice. Please try again.")