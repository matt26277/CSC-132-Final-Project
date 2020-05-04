from Tkinter import *
from random import *

class Item (object):
    def __init__ (self, price, seller, location, weight, condition, brand, color, description, type):
        self.price = price
        self.seller = seller
        self.location = location
        self.weight = weight
        self.condition = condition
        self.brand = brand
        self.color = color
        self.description = description
        self.type = type

class Clothes (Item):
    def __init__ (self, size):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)
        self.size = size

class Electronics (Item):
    def __init__ (self, memory, model):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)
        self.memory = memory
        self.model = model

class Vehicle (Item):
    def __init__ (self, year, model, mileage, engine, transmission, drivetrain):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)
        self.year = year
        self.model = model
        self.mileage = mileage
        self.engine = engine
        self.trans= transmisson
        self.drive = drivetrain
        
class Accessories (Item):
    def __init__ (self):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)

class Entertainment (Item):
    def __init__ (self, year, title):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)
        self.year = year
        self.title = title
        
class Furniture (Item):
    def __init__ (self, dimensions, material):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)
        self.dimensions = dimentsions
        self.material = material

        
class Sports_Outdoors (Item):
    def __init__ (self, material):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)
        self.material = material

class Tools (Item):
    def __init__ (self):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)

class Pet (Item):
    def __init__ (self, species):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)
        self.species = species

class Misc (Item):
    def __init__ (self):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type)



class MainGUI (Frame):
    # the constructor
    def __init__ (self, parent):
        Frame.__init__(self, parent, bg="red")
        parent.attributes ("-fullscreen", True)
        self.setupGUI()

    # sets up the GUI
    def setupGUI (self):
        # the calculator uses the TexGyreAdventor font (see
        # on most Linux system, simply double-click the font
        #  files and install them
        # on the RPi, copy them to /usr/local/share/fonts (with sudo):
        #  sudo cp tex*.otf /usr/local/share/fonts
        # then reboot the display
        # right-align text in the display; and set its
        #  background to white, its height to 2 characters, and
        #  its font to 50 point TexGyreAdventor
        self.display = Label (self, text ="", anchor = E,\
        bg = "white", height = 1, font = ("TexGyreAdventor",45))
        # put it in the top row, spanning across all four
        #  columns; and expand it on all four sides
        self.display.grid (row = 0, column = 0, columnspan = 4, \
                        sticky = E + W + N + S)
        # the button layout
        #  (   )   AC  **
        #  7   8   9   /
        #  4   5   6   *
        #  1   2   3   -
        #  0   .   =   + 
        # configure the rows and columns of the Frame to adjust
        #  to the window
        # there are 6 rows (0 through 5)
        for row in range (6):
            Grid.rowconfigure (self, row, weight =1)
        # there are 4 columns, 0 through 3
        for col in range (4):
            Grid.columnconfigure (self, col, weight = 1)

        #################### the first row ####################
        # (
        # first, fetch and store the image
        # to work best on the RPi, images should be 115x115
        #  pixels
        # otherwise, may need to add .subsample(n)
        img = PhotoImage (file = "xmark.gif")
        # next, create the button
        button = Button (self, bg = "black", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "black", command = lambda:\
                        self.process ("("))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 0, sticky = N+S+E+W)

window = Tk()
window = MainGUI(window)
window.mainloop()


