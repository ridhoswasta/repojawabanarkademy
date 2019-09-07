import re

def is_username_valid(x):
    if re.match(r'[a-z]{5,9}$', x):
        return True
    else:
        return False

def is_password_valid(x):
    if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", x):
        return True
    else:
        return False

print(is_username_valid('siska'))
print(is_password_valid('codeYourFuture!123'))
