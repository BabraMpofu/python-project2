#A program that  calculate the volume of a geometric shapes.
from math import *

#information needed to calculate the volume of a helix
radius=float(input("enter the radius of the helix in (cm): "))#ask the user to input the radius
height=float(input("enter the height of the helix in (cm): "))#input the height
r=radius
h=height
#this is the formular for the volume of the helix
volume_helix = pi * r**2 * h
#information needeed to calculate the volume of the elipse
site_a =float(input("enter the value of site a: "))
site_b =float(input("enter the value of site b: "))
site_c =float(input("enter the value of site c: "))
a=site_a
b=site_b
c=site_c
#this is the formular for the volume of the elipse
volume_elipse = (4/3)* pi * a * b *c
#Allow the user to decide when the program should stop performing
while True:
    shape=input("enter the name of the shape (helix,elipse): ")
    if shape == "helix":
        print("the volume of the helix is",volume_helix,"cm cubed")
    elif shape == "elipse":
        print("the volume of the elipse is",volume_elipse,"cm cubed")
    else:
        print("invalid name shape.please try again")
    choice=input("do you want to calculate the volume of another shape?(yes/no): ")
    if choice =="no":
            break
                  



