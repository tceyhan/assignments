age = input("Are you a cigarette addict older than 75 years old? (yes or no) : ").lower()
chronic = input("Do you have a severe chronic disease? (yes or no) :").lower()
immune = input("Is your immune system too weak? (yes or no) : ").lower()

risk = age == "yes" and chronic == "yes" and immune == "yes"

if  risk :
    print("You are in risky group")
else :
     print("You are not risky group")