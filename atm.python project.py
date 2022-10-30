from ast import  boolop
from pickle import TRUE
import time

print("========== WELCOME TO ATM MACHINE ===========")

print("please insert your card")
print("=============================================")
print("=============================================")

time.sleep(3)

password = 141703

print("WELCOME TO INDIAN OVERSEAS BANK ATM")
print("=============================================")
print("=============================================")

pin=int(input("enter your atm pin number")) 
print("=============================================")
print("=============================================")

balance = 10000

if pin==password:
    while TRUE:

        print("""
            1==balance
            2==withdraw amount
            3==deposite amount
            4==exit
            """
            )

        try:
            option=int(input("please enter your choise"))
        except:
            print("please enter valid option")

        if option==1:
            print(f"your current balance is {balance}")

            print("=============================================")
            print("=============================================")
            print("=============================================")

        if option==2:
        
            withdraw_amount=int(input("please enter withdraw_amount"))

            print("=============================================")
            print("=============================================")
            print("=============================================")

            balance=balance-withdraw_amount 

            print(f"{withdraw_amount} is dabited from your account")
            print("=============================================")
            print("=============================================")

            print(f"your updated balanceis {balance}")
            print("=============================================")
            print("=============================================")

        if option==3:

            deposit_amount=int(input("please enter  deposit_amount"))

            print("=============================================")
            print("=============================================")
            print("=============================================")

            balance=balance+deposit_amount 

            print(f"{ deposit_amount} is craedited to your account")
            print("=============================================")
            print("=============================================")

            print(f"your updated balanceis {balance}")
            print("=============================================")
            print("=============================================")

        if option==4:

         break

        print("thank you for using our bank atm ")
        print("===================================================")
        print("===================================================")

        print("please visit again")
        
else:
     print("wrong pin please try again")