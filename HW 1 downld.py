#Python Program calculator
import math

#Asking what type of operation
while True:
    print("Is your operation Basic, Engineering, or Business")
    operation_type = input()

#If operation_type is basic arithmetic...
    if operation_type == "Basic" or operation_type == "basic":
        print("Is it +, -, /, or *?")
        operation_basic = input()
        if operation_basic == "+":
            print("Whats your first number?")
            num1 = input()
            print("Whats your second number?")
            num2 = input()
            print("Kabooyeah, check the response")
            answer = int(num1) + int(num2)
            print(answer)

        elif operation_basic == "-":
            print("Whats your first number?")
            num1 = input()
            print("Whats your second number?")
            num2 = input()
            print("Heyooo, BOOM?")
            answer = int(num1) - int(num2)
            print(answer)

        elif operation_basic == "*" or operation_basic == "x" or operation_basic == "X":
            print("Whats your first number?")
            num1 = input()
            print("Whats your second number?")
            num2 = input()
            print("The wife took the kids, anyways heres your answer")
            answer = int(num1) * int(num2)
            print(answer)

        elif operation_basic == "/":
            print("Whats your first number?")
            num1 = input()
            print("Whats your second number?")
            num2 = input()
            try:
                solution = int(num1)/int(num2)
                print(solution)
            except ZeroDivisionError:
                print("cannot divide by 0")

        else:
            print("Not one of the choices...")

#If operation_type is engineering (shape volume or area)...
    if operation_type == "Engineering" or operation_type == "engineering":
        print("Geometric or Conversions?")
        operation_type_2 = input()
        
        #Split between Geometric and Conversions, starts with Geometric
        def triangle_area(t_base, t_height):
            return 0.5 * t_base * t_height
        def rectangle_area(r_length, r_width):
            return r_length * r_width
        def circle_area(c_radius):
            return math.pi * c_radius**2
        def cube_volume(side):
            return side*side*side
        def cylinder_vol(cyl_height, cyl_radius):
            return cyl_height * math.pi * cyl_radius**2
        def cone_vol(cone_h, cone_r):
            return (cone_h * cone_r**2 * math.pi)/3
        if operation_type_2 == "Geometric" or operation_type_2 == "geometric":
            print("Is it triangle, rectangle, circle, cube, cylinder, or cone?")
            shape_type = input()
            if shape_type == "triangle" or shape_type == "Triangle":
                print("What is base?")
                t_base = int(input())
                print("What is height?")
                t_height = int(input())
                t_area = triangle_area(t_base, t_height)
                print(t_area)
            elif shape_type == "Rectangle" or shape_type == "rectangle":
                print("What is the rectangle's length?")
                r_length = int(input())
                print("What is it's width?")
                r_width = int(input())
                r_area = rectangle_area(r_length, r_width)
                print(r_area)
            elif shape_type == "Circle" or shape_type == "circle":
                print("What is the circle's radius?")
                c_radius = int(input())
                c_area = circle_area(c_radius)
                print(c_area)
            elif shape_type == "cube" or shape_type == "Cube":
                print("What is the cube's side length?")
                side=int(input())
                c_area = cube_volume(side)
                print(c_area)
            elif shape_type == "cylinder" or shape_type == "Cylinder":
                print("What is the cylinder's height")
                cyl_height = int(input())
                print("What is the cylinder's radius")
                cyl_radius = int(input())
                cyl_volume = cylinder_vol(cyl_height, cyl_radius)
                print("The volume is " + str(cyl_volume))
            elif shape_type == "Cone" or shape_type == "cone":
                print("What is the cone's height?")
                cone_h = int(input())
                print("What is the cone's base radius?")
                cone_r = int(input())
                cone_volume = cone_vol(cone_h, cone_r)
                print("Heres the beautiful cone volume you ordered " + str(cone_volume))
            else:
                print("Not an option, retype...")

        #If user is asking for conversions...                
        if operation_type_2 == "Conversions" or operation_type_2 == "conversions":
            print("Which Conversion? (please type out desired conversion exactly as presented below)")
            print("meters to feet")
            print("feet to meters")
            print("kgs to lbs")
            print("lbs to kgs")
            answer_2 = input()
            if answer_2 == "meters to feet":
                print("How many meters?")
                meters_1 = input()
                conversion = int(meters_1) * 3.28084
                print("That is " + str(conversion) + " ft.")
            elif answer_2 == "feet to meters":
                print("How many feet?")
                feet_1 = input()
                conversion = int(feet_1) * 0.3048
                print("That is " + str(conversion) + " m.")
            elif answer_2 == "kgs to lbs":
                print("How many kgs?")
                kgs_1 = input()
                conversion = int(kgs_1) * 2.20462
                print("That is " + str(conversion) + " lbs.")
            elif answer_2 == "lbs to kgs":
                print("How many lbs?")
                lbs_1 = input()
                conversion = int(lbs_1) * 0.453592
                print("That is " + str(conversion) + " kgs.")
            else:
                print("Not a choice, retype...")

#If the operaton_type is Business
    if operation_type == "Business" or operation_type == "business":
        print("What would you like to calculate? Please type exactly as portrayed below...")
        print("Compound Interest")
        print("Break-Even Value")
        answer = input()
        if answer == "Compound Interest" or answer == "compound interest":
            print("What is the principal?")
            principal = input()
            print("What is the annual interest rate (please input as decimal)?")
            i = input()
            print("How many periods?")
            p = input()
            compound_interest = (int(principal) * ((1 + float(i))**int(p))) - int(principal)
            print("The compounded interest is " + str(compound_interest) + "!")
        if answer == "Break-Even Value" or answer == "break-even value":
            print("What are the fixed costs?")
            fixed_costs = input()
            print("What is the sales price per unit?")
            sales_price = input()
            print("What are the variable costs per unit?")
            variable_price = input()
            try:
                break_even = int(fixed_costs)/(int(sales_price) - int(variable_price))
                print("Break-Even Value is " + str(break_even) + "!")
            except ZeroDivisionError:
                print("Error: Invalid Argument")
                

                                               
                                               

            

            

            
                  
           

            
                


 
  




    
