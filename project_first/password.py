''' those function just for test a password '''
def is_acceptable_password(password:str)->bool:
    '''this function is acceptable_password returns false/true
if the password is bigest than 6 and contain a char and it's not number'''
    if(len(password)>6 and
       any(char.isdigit() for char in password) and
       password.isdigit() is False):
        return True
    if len(password) > 9:
        return True
    return False
def print_password(password: str)->bool:
    '''this function print password return true/false if the password biggest than 5'''
    if len(password)>5:
        print(password)
        return True
    print("small password ")
    return False
