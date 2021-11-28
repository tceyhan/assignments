fibonacci = []
x,y = 1,1
while x <= 55:
    fibonacci.append(x)
    x, y =  y, x + y
    print(fibonacci)
    

