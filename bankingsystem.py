def show_balance():   
    print(f"Your balance: RM{balance:.2f}")
  

def deposit():
    dep = float(input("Please enter you amount:RM"))
    
    if dep < 0:
        print("Invalid amount")
        return 0
    else: 
        return dep

def withdraw():
    wd = float(input("Please enter you amount:RM"))
    
    if wd <= 0:
        print("Invalid amount")
        return 0
    elif wd > balance: 
        print("Insufficient balance!")
        return 0
    else:
        return wd

dep = 0
balance = 0
is_running = True

while is_running:
    print("------------------------")
    print("Banking Program")
    print("------------------------")
    choice = input("Press 'd' to deposit, 'w' to withdraw, 'b' to show balace, 'q' to quit:")
    
    if choice == 'd':
        balance += deposit()
        
    elif choice == 'w':
        balance -= withdraw()
        
    elif choice == 'b':
        show_balance()
        
    elif choice == 'q':
        is_running = False
    else:
        print("Invalid choice. Please try again.")
           
print("Thank you!")