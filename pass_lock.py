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

    check_user = Details.check_user(fname,password)
    return check_user

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
                    print("cc-Create your Credential \n dc-Display Credentila \n cp-Copy Password \n ex-Exit")
                    options = input().lower().strip()
                    print("*"*40)
                    if options == "ex":
                        print("*"*40)
                        print(f"Thank you! {username}")
                        break


                    elif options == "ex":
                        print("Enter your Details")



        


if __name__ == '__main__':
    main()   

