import csv
from datetime import datetime

def add_new_entry():
    Title = input("enter title ")
    Type = input("enter “I” for Income or “E” for Expense ").strip().upper()
    while Type not in ['I', 'E']:
        Type = input("Invalid input. Type (I for Income, E for Expense) ").strip().upper()
    Amount = float(input("Enter amount "))
    date = input ("enter date (MM-DD-YYYY) ")
    while not validate_date(date):
        date = input("Invalid date. Enter date (MM-DD-YYYY) ")
    categories = ["Office Supplies", "Salary", "Rent", "Travel"]
    print("Available categories ")
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
    
    with open('budget.csv',mode='a',newline='') as file:
        writer =csv.writer(file)
        writer.writerow([Title,Type,Amount,date,selected_category,account])
    print("entery added")    

def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%m-%d-%Y")
        return True
    except ValueError:
        return False

def Display_Account_Balance():
    choice_account = input("Enter account name to view balance or 'all' for total balance ")
    total_income = 0
    total_expense = 0
    try:
        with open('budget.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if len(row) < 6:
                    continue 
                print(f"Processing row: {row}")  
                if choice_account == 'all' or row[5] == choice_account:
                    if row[1] == 'I':
                        total_income += float(row[2])
                        print(f"Added to income: {row[2]}") 
                    elif row[1] == 'E':
                        total_expense += float(row[2])
                        print(f"Added to expense: {row[2]}") 
        net_balance = total_income - total_expense
        print(f"Net Balance for {choice_account}: ${net_balance:.2f}")
    except FileNotFoundError:
        print("Error: 'budget.csv' file not found.")

#with open('budget.csv', 'w') as file:
    #writer = csv.writer(file)
    #writer.writerow(["Title", "Type", "Amount", "Date", "Category", "Account"])


def View_Entries():
    with open('budget.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader, start=1):
            if len(row) < 6:
                continue
            try:
                amount = float(row[2]) 
                print(f"{i}. [{row[3]}] {row[0]}: {'-' if row[1] == 'E' else '+'}${amount:.2f} ({row[1]}) - Category: {row[4]} - Account: {row[5]}")
            except ValueError:
                print(f"Invalid amount format in row {i}: {row}")


def Search_Entries():
    search= input("Enter title or date or category or account type ").strip()
    with open('budget.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        found = False 
        for row in reader:
            if len(row) < 6:
                continue
            if (search in row[0] or search in row[3] or
                search in row[4] or search in row[5]):
                amount = float(row[2])
                sign = '-' if row[1] == 'E' else '+'
                print(f"Search Results for {row[0]}: [{row[3]}] {row[0]}: {sign}${amount:.2f} ({row[1]}) - Category: {row[4]} - Account: {row[5]}")
        if not found:
            print("No entries found")

def Generate_Reports():
    Reports = input("Generate report by 1.Date Range 2. Category 3.Account ")
    if Reports == '1':
        start_date = input('enter start sate (MM-DD-YYY) ')
        end_date = input('enter end date (MM-DD-YYYY) ')
        total_income = 0
        total_expense = 0
        with open('budget.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                if len(row) < 6:
                    continue     
                row_date = datetime.strptime(row[3], "%m-%d-%Y")
                if start_date <= row_date.strftime("%m-%d-%Y") <= end_date:
                    if row[1] == 'I':
                        total_income += float(row[2])
                    elif row[1] == 'E':
                        total_expense += float(row[2])
        net_balance = total_income - total_expense
        print(f"Report for Date Range ({start_date} to {end_date})")
        print(f"Total income  ${total_income:.2f}")
        print(f"Total expenses ${total_expense:.2f}")
        print(f"Net balance ${net_balance:.2f}")

    elif Reports == '2':
        category = input("enter category ")
        total_income, total_expenses = 0, 0

        with open('budget.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            
            for row in reader:
                if len(row) < 6 or row[4] != category:
                    continue
                
                if row[1] == 'I':
                    total_income += float(row[2])
                elif row[1] == 'E':
                    total_expenses += float(row[2])
        
        net_balance = total_income - total_expenses
        print(f"Report for Category '{category}':")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Net Balance: ${net_balance:.2f}")

    elif Reports == '3':
        account = input("Enter account (Personal Account) OR (Business Account) ")
        total_income, total_expenses = 0, 0

        with open('budget.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader) 
            
            for row in reader:
                if len(row) < 6 or row[5] != account:
                    continue
                
                if row[1] == 'I':
                    total_income += float(row[2])
                elif row[1] == 'E':
                    total_expenses += float(row[2])
        
        net_balance = total_income - total_expenses
        print(f"Report for Account '{account}':")
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Net Balance: ${net_balance:.2f}")

    else:
        print("Invalid choice. Please try again!!")


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
        choice = input ("Choice opation 1. To Add a New Entry , 2. To Display Account Balance , 3. To View All Entries , 4. To Search for Entries , 5.  To Generate Reports , 6.  To Manage Accounts and Categories 7. exit  " )
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