
while(True):
    number = input("Enter your number") 
    if number.isdigit() and int(number) > 0:
        length = len(number)
        sum = 0
        for integer in number:
            integer = int(integer)
            sum += integer ** length
        if int(number) == sum:
            print("This is an armstrong number")  
        else:
            print("This is not an armstrong number")
        break
    else:
        print("Please enter a valid number")