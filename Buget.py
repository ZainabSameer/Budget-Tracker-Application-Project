import csv
from datetime import datetime

def add_new_entry():
    Title = input("enter title")
    Type = input("enter “I” for Income or “E” for Expense").strip().upper()
    while Type not in ['I', 'E']:
        Type = input("Invalid input. Type (I for Income, E for Expense) ").strip().upper()
    Amount = float(input("Enter amount"))
    date = input ("enter date (MM-DD-YYYY)")
    while not validate_date(date):
        date = input("Invalid date. Enter date (MM-DD-YYYY) ")
    categories = ["Office Supplies", "Salary", "Rent", "Travel"]
    print("Available categories")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")
    
    category_choice = int(input("Choose a category by number ")) - 1
    selected_category = categories[category_choice] if 0 <= category_choice < len(categories) else None

    if selected_category is None:
        print("Invalid category choice")
        return

    accounts = ["Business Account", "Personal Account"]
    print("Available accounts")
    for i, account in enumerate(accounts, 1):
        print(f"{i}. {account}")
    
    account_choice = int(input("Choose an account by number")) - 1
    account = accounts[account_choice] if 0 <= account_choice < len(accounts) else None

    if account is None:
        print("Invalid account choice")
        return
    
    with open('budget.csv',mode='a') as file:
        writer =csv.writer(file)
        writer.writerow([Title,Type,Amount,date])
    print("entery added")    

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%m-%d-%Y")
        return True
    except ValueError:
        return False

def Display_Account_Balance():
    choice_account = input("Enter account name to view balance or 'all' for total balance")
    total_income = 0
    total_expense = 0
    with open('entries.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if (choice_account == 'all' or row[5] == choice_account):
                if row[1] == 'I':
                    total_income += float(row[2])
                elif row[1] == 'E':
                    total_expense += float(row[2])
    net_balance = total_income - total_expense
    print(f"Net Balance for {choice_account}: ${net_balance:.2f}")

with open('entries.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Type", "Amount", "Date", "Category", "Account"])
    
#def main_menu ():
    #print(f"1. Add a New Entry:")
    #print(f"2. Display Account Balance:")
    #print(f"3. View All Entries: ")
    #print(f"4. Search Entries:")
    #print(f"5. Generate Reports:")
    #print(f"6. Manage Accounts and Categories: ")
    #print(f"7. exit")


#main_menu ()

while(True):
        choice = input ("Choice opation 1. To Add a New Entry , 2. To Display Account Balance , 3. To View All Entries , 4. To Search for Entries , 5.  To Generate Reports , 6.  To Manage Accounts and Categories 7. exit" )
        if choice == '1':
            add_new_entry()
        elif choice == '2':
            Display_Account_Balance()
        elif choice == '3':
            View_Entries()
        elif choice == '4':
            Search_Entries()
        elif choice == '5':
            Generate_Reports()
        elif choice == '6':
            Manage()
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again")