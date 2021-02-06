# For calculating area of circle


radius = eval(input("Enter the value of radius: "))
area=3.1415922653589793238*radius*radius
print("Area of circle having radius =", radius,"is", area)




# Getting extension of file

filename = input("Enter the filename:")
file_extension=filename.split(".")
print("The extension of file is" + repr(file_extension[-1]),":'python'" )

