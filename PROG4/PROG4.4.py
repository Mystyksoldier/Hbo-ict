oldpassword = input("Enter your old password: ")
newpassword = input("Enter your new password: ")

def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        return True
    else:
        return False
    
print(new_password(oldpassword, newpassword))