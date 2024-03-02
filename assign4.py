import math
print("Welcome to Right Triangle Solver App")
#getting input from user
side_1=float(input("what is the first leg of the triangle:"))
side_2=float(input("what is the second leg of the triangle:"))

#calculations
side_3=math.sqrt(side_1 ** 2 +side_2** 2)
side_3=round(side_3, 3)
area=0.5*side_1*side_2
area=round(area,3)

print(f" For a triangle with legs of {side_1} and {side_2} the hypotenuse is {side_3}")
print(f" For a triangle with legs of {side_1} and {side_2} the area is {area}")
