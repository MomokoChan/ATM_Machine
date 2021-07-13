"""

Simple ATM program
Using exception handling code blocks such as try/ except / else / finally (NB: the more the better, but try to use at least two key words e.g. try/except) write a program that simulates and ATM machine to withdraw money.
Tasks:
1. Prompt user for a pin code
2. If the pin code is correct then proceed to the next step, otherwise ask a user to type in a password again. You can give a user a maximum of 3 attempts and then exit a program.
3. Set account balance to 100.
4. Now we need to simulate cash withdrawal
5. Accept the withdrawal amount
6. Subtract the amount from the account balance and display the remaining balance (NOTE! The balance cannot be negative!)
7. However, when a user asks to ‘withdraw’ more money than they have on their account, then you need to raise an error an exit the program.

"""


"""

The function atm_machine_pin takes a parameter that would be the user's pin
the argument passed is pin states on top
the function starts asking for the pin number
the function checks if the input is what it's expected to be (numbers)
the function returns true when the pin is right
if it's wrong it gives two more times to get the pin right
a while with a variable counter check the times the counter incremented inside the loop (flag)
it states how many attempts the user has left the while loop helps the program restarting from top if
pin digit is wrong or in case of ValueError. The ways to end the loop are in case of right digit pin or 3 attempts made.

"""

pin = 1234
def atm_machine_pin(pin):

    counter = 1
    balance = 100
    while counter <= 3:
        try:
            pin_input = int(input("Please digit your pin: "))
        except ValueError:
            print("You must digit a number, please try again.")
        else:
            if pin_input == pin:
                print("Access granted!")
                return True
            elif pin_input != pin:
                try:
                    if counter < 3:
                        print(f"Your pin is wrong please digit your ping again")

                    elif counter == 3:
                        raise TypeError

                except TypeError:
                    print("You have no more attempts left.")
                    print("Your account has been disabled, please contact your bank for further instructions")
                    return False

                else:
                    print(f"Warning: {3 - counter} attempt/s left")
                    counter = counter + 1

"""
the variable access stores the boolean value returned from the function atm_machine_pin
the function atm_machine_withdraw takes access as argument and checks if it's True in order to start
(digit pin inserted was right)

input to confirm user's choice to withdraw and while loop to flag his choice.
there is a valueError to check the data inserted is consistent
the last "if" checks that the amount requested is less or equal of the balance in order to not have a negative 
balance result

"""
account_balance = 100.00
access = atm_machine_pin(pin)
def atm_machine_withdraw(access):

    if access:  # true if the pin was right
        print()
        print(f" ------------------------------------- \n"
              f"|       Welcome to your balance       | "
              f"\n ------------------------------------- "
              f"\nYour balance is: £ {account_balance}")


        machine_active = True
        while machine_active:
            response = input("Would you like to withdraw? Please confirm y/n: ")
            if response == "y":
                try:
                    withdraw = float(input("Digit the amount: "))

                except ValueError:
                    print("You must digit a number, please try again.")
                    continue  # starts from beginning
                else:
                    break
            elif response == "n":
                print("Bye!")
                machine_active = False

            elif response != "y" or response != "n":
                print("Please digit y for yes or n for no.")
                continue


        if machine_active:
            try:
                if withdraw <= account_balance:
                    new_balance = account_balance - withdraw
                    print(f"Successfully completed \nHere is your new balance: \n£ {new_balance}")

                else:
                    raise TypeError
            except TypeError:
                print("I like your confidence but your balance doesn't have enough money for that \nBye!")



atm_machine_withdraw(access)


