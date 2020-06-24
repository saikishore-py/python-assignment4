# program to find area of a regular polygon

from math import tan, pi

ns= int(input("enter the no of sides:"))

sl= float(input('enter the length of each side:'))


#area of regular polygon

ar= ns * (sl**2)/(4*tan(pi/ns))


print('the area of the polygon is:', ar)