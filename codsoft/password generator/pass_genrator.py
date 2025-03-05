import random

#while True:
def genrat_pass(l):
        charter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqristuvwxyz!@#$%^&*-+1234567890"

        password = " "
        for i in range(l):
                password = password + random.choice(charter)

        return password

        lenght = int(input("enter password lenght:"))
        if lenght.isdigit():
            print("your password is :", genrat_pass(lenght))
        #else:
            #brake()

