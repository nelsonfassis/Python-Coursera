#Check the password length#

def change_passwd():
    while True:
        passwd = raw_input("Enter a password with at least 8 characters: ")
        if len(passwd) < 8:
            continue
        else:
            while True:
                check_passwd = raw_input("Re-enter your password: ")
                if passwd != check_passwd:
                    print "Passwords doesn't match"
                    continue
                else: break
                
            break
    print "Password changed"            
change_passwd()