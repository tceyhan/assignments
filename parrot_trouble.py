def parrot_trouble(talking, hour):
    if talking and (hour < 6 or hour > 21): 
        return True 
    else: 
        return False 
print(parrot_trouble(False, 22))