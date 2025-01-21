import csv

def main_menu ():
    print(f"1. Add a New Entry:")
    print(f"2. Display Account Balance:")
    print(f"3. View All Entries: ")
    print(f"4. Search Entries:")
    print(f"5. Generate Reports:")
    print(f"6. Manage Accounts and Categories: ")
    print(f"7. exit")

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

