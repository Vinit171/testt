import re

while(True):
    i = input("Enter the password\n")


    if (len(i)<= 6 or len(i) >16):
        print("Please enter a password which is not smaller than 6 character and not larger than 16 characters")

    elif not re.search("[a-z]",i):
        print("Please enter at least one small")

    elif not re.search("[A-Z]",i):
        print("please enter a capital letter")

    elif not re.search("[0-9]", i):
        print("Enter a number which contains at least one number digit")

    elif not re.search("[$,#,!,@,&,*]", i):
        print("Enter a number which contains special character like ($,#,!,@,&,*)")

    else:
        print("welcome!Password is valid")
        exit()



#-----------------------------------------------------------------------------------------------------------


