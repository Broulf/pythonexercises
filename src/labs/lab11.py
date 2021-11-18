# Author:         Anthony Segura
# ULID/Section:   C00441031 - 002
# lab11.py 
 
import math

def AreaCircle(radius):
    area = math.pi * radius ** 2
    return area 

def VolumeSphere(radius):
    volume = 4/3 * math.pi * radius ** 3
    return volume

def SurfaceAreaCube(length):
    surfaceArea = 6 * length ** 2
    return surfaceArea

def SurfaceAreaSphere(radius):
    surfaceArea = 4 * math.pi * radius ** 2
    return surfaceArea

def main():

    infile = open("lab11_input.txt","r")

    input_type = infile.readline().strip()
    dimension = eval(infile.readline().strip())

    while input_type != "###": 

        if input_type == "AC":
            circle_area = AreaCircle(dimension)
            print(format("Area of a Circle","30s"),format(circle_area,"15.2f"))
        elif input_type == "VS":
            sphere_volume = VolumeSphere(dimension)
            print(format("Volume of a Sphere","30s"),format(sphere_volume,"15.2f"))
        elif input_type == "SAC":
            cube_surface = SurfaceAreaCube(dimension)
            print(format("Surface Area of a Cube","30s"),format(cube_surface,"15.2f"))
        elif input_type == "SAS":
            sphere_surface = SurfaceAreaSphere(dimension)
            print(format("Surface Area of a Sphere","30s"),format(sphere_surface,"15.2f"))

        input_type = infile.readline().strip()
        dimension = eval(infile.readline().strip())

    infile.close()
    
main() 
