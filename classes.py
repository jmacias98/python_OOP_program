'''This program takes 3 classes that inherit an Shape class. 
This program uses methods to find the area of 3 shapes, circle, cube, square,
 as well as class name and then display the results on the screen, a file, or GUI window, 
 depending on the users choice'''

import random
from tkinter import *
from abc import abstractmethod
from matplotlib import pyplot as plt

class Shape(object):
    def __init__(self, color = "Red"):
        self.__color = color

    def set_color(self, color):
        self.__color = color
              
    def get_color(self):
        return self.__color
    
    def display(self):
        print("Color Information:",self.__color)
        
    @abstractmethod
    def find_area(self):
        pass
    @abstractmethod
    def find_volume(self):
        pass
    @abstractmethod
    def __str__(self):
        pass

class Circle(Shape):
    def __init__(self, color, radius = 1):
        super().__init__(color=color)
        self.__radius = radius
        self.__area = self.find_area()

    def set_radius(self,radius):
        self.__radius = radius
    def get_radius(self):
        return self.__radius

    def find_area(self):
        pi = 3.14
        self.__area = pi*(self.__radius**2)
        return self.__area

    def display(self):
        name = Circle(Shape)
        self.find_area()
        print("Class:",name.__class__.__name__,"Area:", self.__area)
        return self.__area
    def __str__(self):
        name = Circle(Shape)
        self.find_area()
        return(self.__area)
        
class Square(Shape):
    def __init__(self, color, side = 2.3):
        super().__init__(color=color)
        self.__side = side
        self.__area = self.find_area()

    def set_side(self,side):
        self.__side = side

    def get_side(self):
        return self.__side
    
    def find_area(self):
        self.__area = (self.__side**2)
        return self.__area

    def display(self):
        name = Square(Shape)
        self.find_area()
        print("Class:",name.__class__.__name__,"Area:", format(self.__area,".2f"))
        return self.__area
    def __str__(self):
        name = Square(Shape)
        self.find_area()
        return(self.__area)

class Cube(Shape):
    def __init__(self, color, length = 3, width = 3, height = 3):
        super().__init__(color=color)
        self.__length = length
        self.__width = width
        self.__height = height 
        self.__volume = self.find_volume()

    def set_length(self, length):
        self.__length = length 
    def get_length(self):
        return self.__length

    def set_width(self, width):
        self.__width = width
    def get_width(self):
        return self.__width
    
    def set_height(self, height):
        self.__height = height
    def get_height(self):
        return self.__height

    def find_volume(self):
        self.__volume = (self.__length * self.__width * self.__height)
        return self.__volume

    def display(self):
        name = Cube(Shape)
        self.find_volume()
        print("Class:",name.__class__.__name__,"Volume:", self.__volume)
        return self.__volume
    def __str__(self):
        name = Cube(Shape)
        self.find_volume()
        return(self.__volume)

def main():
    shapes = []
    for i in range(15):
        randomSelection = random.randint(1,3)
        if randomSelection ==1:
            shapes.append(Circle(Shape))
        elif randomSelection ==2:
            shapes.append(Square(Shape))
        else:
            shapes.append(Cube(Shape))
    ans=True
    while ans:
        print("\t==============MENU==============")
        print ("""
        1.Display Results on Console
        2.Save Results Into a File
        3.Display Results in a GUI Window
        4.Exit
        """)
        ans= input("What would you like to do? ")
        if ans == "1":
            for shape in shapes:
                shape.display()
                                
        elif ans=="2":
            fileName = input("Enter a File Name: ")
            with open(fileName, "w") as outfile:
                for shape in shapes:
                    if isinstance(shape, Circle):
                        typeOfShape = "Circle"
                    elif isinstance(shape, Square):
                        typeOfShape = "Square"
                    else:
                        typeOfShape = "Cube"
                    outfile.write("{}: Area: {:.2f} \n".format(typeOfShape, shape.__str__()))

        elif ans=="3":
            window = Tk()
            window.title("Shape Program")
            window.geometry("450x650")
            window.configure(background="light green")
            details = Label(window, text="This window displays the Shape Program Results")
            details.pack()
            for shape in shapes:
                if isinstance(shape, Circle):
                    typeOfShape = "Circle:"
                elif isinstance(shape, Square):
                    typeOfShape = "Square:"
                else:
                    typeOfShape = "Cube:"
                whichShape = Label(window,text=typeOfShape)
                whichShape.pack()
                area = Label(window, text=shape.__str__())
                area.pack()
            window.mainloop()

        elif ans == "4":
            print("Goodbye!")
            return False           
        else:
            print("\n Not Valid Choice Try again")
main()
'''        ==============MENU==============

        1.Display Results on Console
        2.Save Results Into a File
        3.Display Results in a GUI Window
        4.Exit

What would you like to do? 1
Class: Cube Volume: 27
Class: Circle Area: 3.14
Class: Cube Volume: 27
Class: Cube Volume: 27
Class: Cube Volume: 27
Class: Square Area: 5.29
Class: Circle Area: 3.14
Class: Circle Area: 3.14
Class: Square Area: 5.29
Class: Square Area: 5.29
Class: Cube Volume: 27
Class: Circle Area: 3.14
Class: Cube Volume: 27
Class: Circle Area: 3.14
Class: Square Area: 5.29
       ==============MENU==============

        1.Display Results on Console
        2.Save Results Into a File
        3.Display Results in a GUI Window
        4.Exit

What would you like to do? 2
Enter a File Name: textFileResults.txts
        ==============MENU==============

        1.Display Results on Console
        2.Save Results Into a File
        3.Display Results in a GUI Window
        4.Exit

What would you like to do? 4
Goodbye!
'''
