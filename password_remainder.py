name = "Tarık"
password = "tc5584"

nickname = input("Enter your name :").title().strip()

if nickname == name :
    print(f"Hello, {name}! The password is : {password}")
else :
    print(f"Hello, {nickname}! See you later.")