users={
    "1001":{
        "name": "mani",
        "pin":"1234",
        "balance": 10000
    },
    "1002":{
        "name":"ramu",
        "pin":"4321",
        "balance":20000,
    }
}
def login():
    account_number =input ("enter account_number:")
    pin= input("enter pin:")

    if account_number in users:
        if users[account_number]["pin"]==pin:
            print("\nlogin sucessfull")
            print("welcome",users[account_number]["name"])
            return account_number
        else:
             print("wrong pin")
    else:
           print("account not found")
           return None
def check_balance(account_number):
    print("your balance is: $ ",users[account_number]["balance"])
def deposit(account_number):
    amount=float(input("enter deposit amount:"))
    if amount > 0:
       users[account_number]["balance"]+= amount
       print("amount deposited sucessfully")
       print("new balance: ",users[account_number]["balance"])
    else:
        print ("invalid amount: ")
def withdrawl (account_number):
    amount=float(input("enter withdrawl amount :"))
    if amount<=0:
       print("invalid amount")
    elif amount>users[account_number]["balance"]:
         print("insufficient balance")
    else:
        users[account_number]["balance"]-=amount
        print("pelase collect your cash")
        print("Reaming balance:",users[account_number]["balance"])
def atm_menu(account_number):
    while True:
        print("\n =======ATM MENU=========")
        print("1.check balance")
        print("2.deposit cash")
        print("3.withdraw cash")
        print("4.exit")
        print("============================")
        choice=input("enter number:")
        if choice=="1":
            check_balance(account_number)
        elif choice=="2":
            deposit(account_number)
        elif choice=="3":
            withdrawl(account_number)
        elif choice=="4":
            print("thank you using hdfc bank")
            break
        else:
            print("invalid choice pls try agaian")

account_number = login()

if account_number:
    atm_menu(account_number)
