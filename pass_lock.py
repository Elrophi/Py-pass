import pyperclip
from user_details import User, Details


def new_user(fname,lname,password):
    '''
    create new user
    '''
    n_user = User(fname,lname,password)
    return n_user

def save_user(user):
    '''
    save new user account
    '''
    User.save_user_details(user)

def verify_user(fname,password):
    '''
    verify if there is already a user before adding details
    '''

    checking_user = Details.check_user(fname,password)
    return checking_user

def new_password():
    '''
    automatic random password generator
    '''
    passcode = Details.new_password()
    return passcode

def create_detail(username,site,account,password):
    '''
    create new user details
    '''
    new_details=Details(username,site,account,password)
    return new_details

def save_details(details):
    '''
    save newly created detail
    '''
    Details.save_details(details)

def display_details(username):
    '''
    display saved user details
    '''
    return Details.display_details(username)

def copy_details(site):
    '''
    copy all details to clipboard
    '''
    return Details.copy_details(site) 


def main():
    print("Welcome to PY-Password-Locker")
    while True:
        print('*'*40)
        print("Select task to execute\n ca-Create Account \n li-Log In\n ex-Exit")
        print("*"*40)
        # strip() removes spaces at the begining and end of the input the user is providing
        options = input().lower().strip()
        if options == 'ca':
            print("*"*40+"\n")
            print("Fill in your details")
            f_name = input('Enter your first name - ').strip()
            l_name = input('Enter your last name - ').strip()
            password = input('Enter your password - ').strip()

            save_user(new_user(f_name,l_name,password))
            print(" ")
            print(f"New Account Created for: {f_name} {l_name} and password: {password}")

        elif options == 'ex':
            print("*"*40)
            print("Goodbye!")
            break

        elif options == 'li':
            print("*"*40)
            print("To login, enter your account details")
            username = input("Enter your first name - ").strip()
            password = str(input("Enter your password - "))

            user_exists = verify_user(username,password)
            if user_exists == username:
                print(f"welcome {username} feel free to continue and select an option ")
                while True:
                    print("*"*40)
                    print("Select your option\n cc-Create your Credential \n dc-Display Credentila \n cp-Copy Password \n ex-Exit")
                    options = input().lower().strip()
                    print("*"*40)
                    if options == "ex":
                        print("*"*40)
                        print(f"Thank you! {username}")
                        break


                    elif options == "cc":
                        print("Enter your Details")
                        site = input('Enter the site\'s name - ').strip()
                        account = input("Enter your account\'s name - ").strip()
                        while True:
                            # print("*"*40)
                            print("Select your prefered password choice\n up-User Password\n gp-Generated Password\n ex-Exit")
                            pwd = input().lower().strip()
                            if pwd == 'up':
                                print("*"*40)
                                password = input("Enter your password- ").strip()
                                break
                            elif pwd == 'gp':
                               print("*"*40)
                               password = new_password()
                               break
                            elif pwd == 'ex':
                                print("Exited!")
                                break
                            else:
                                print("Wrong input! Try again")

                        save_details(create_detail(username,site,account,password))
                        print("*"*40)
                        print(f"Credentials given below:\n site- {site}\n account- {account}\n password- {password}")

                    elif options == "dc":
                        print("*"*40)
                        if display_details(username):
                            print("Your Credentials:")
                            print("*"*40)
                            for details in display_details(username):
                                print(f"These are your credentials\n site - {details.site}\n account - {details.account}\n password - {details.password}")
                                print("*"*40)
                        else:
                            print("*"*40)
                            print("You dont seem to have any credential saved yet, you can create a new one")
                            print("*"*40)
                    
                    elif options == "cp":
                        print("*"*40)
                        pick_site = input("Enter site name - ")
                        print("")
                        copy_details(pick_site)
                        print("*"*40 +"\n Password copied")
                    else:
                        print("Wrong input! Try again")

            else:
                print("*"*40)
                print("Wrong input! Try again")

        else:
            print("*"*40)
            print("Wrong input! Try again")

                        


if __name__ == '__main__':
    main()   

