
# Authentication decorator. Build a password authenticator.

import getpass

print('Create your account here! \n')

user_name = input('Enter your Username: ')
pass_word = getpass.getpass('Enter your Password: ')

print('done!! \n')
pass_count = len(pass_word)
pass_block = int(pass_count) * '*'

print(f'Your username is: {user_name}\nYour password is: {pass_block}\n')

print('Login Here \n')

username = input('Enter Username: ')
password = getpass.getpass('Enter Password: ')


def authenticated(func):
    def wrapper(*args, **kwargs):
        # password = getpass.getpass("Verify password: ")
        if password == pass_word:
            result = func(*args, **kwargs)
            return result
        else:
            print("Authentication failed.")
            print('incorrect username or password!!')

    return wrapper


@authenticated
def protected_function():
    print("Access granted. You're authenticated!")


# Test the decorated function
protected_function()