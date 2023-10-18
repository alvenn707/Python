import math

select = input("Enter Shape:\n")

if select == "triangle":
    x = float(input("Enter Length:\n"))
    y = float(input("Enter Width:\n"))
    answer = (x * y) / 2
    print(f"The area of the triangle is:\n {answer}")
elif select == "square":
    x = float(input("Enter Length:\n"))
    y = float(input("Enter Width:\n"))
    answer = x * y
    print(f"The area of the square is:\n {answer}")
elif select == "circle":
     x = float(input("Enter Radius:\n"))
     answer = x * math.pi
     print(f"The area of the circle is:\n{answer}")
else:
    print("Enter type of shape again:\n")
     


    
    

