##############################################################################################################################################
## Name: Andrew LeBlanc
## Date: 
## Description: 
##############################################################################################################################################

from Tkinter import *

# the main GUI
class MainGUI (Frame):
    # the constructor
    def __init__ (self, parent):
        Frame.__init__(self, parent, bg="white")
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
        bg = "white", height = 1, font = ("TexGyreAdventor",20))
        # put it in the top row, spanning across all four
        #  columns; and expand it on all four sides
        self.display.grid (row = 3, column = 0, columnspan = 2, \
                        sticky = E + W + N + S)
                # there are 6 rows (0 through 5)
        for row in range (6):
            Grid.rowconfigure (self, row, weight =1)
        # there are 4 columns, 0 through 3
        for col in range (10):
            Grid.columnconfigure (self, col, weight = 1)

        #################### the first row ####################
        # (
        # first, fetch and store the image
        # to work best on the RPi, images should be 115x115
        #  pixels
        # otherwise, may need to add .subsample(n)
        # next, create the button
        button = Button (self, bg = "white", text = "CLOTHES", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                        self.process ("("))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 0, sticky = N+S+E+W)

                         
        # next, create thenext button
        button = Button (self, bg = "white", text = "ELECTRONICS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process (")"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 1, sticky = N+S+E+W)


        # next, create the button
        button = Button (self, bg = "white", text = "VEHICLES", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("AC"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 2, sticky = N+S+E+W)



        # next, create the button
        button = Button (self, bg = "white", text = "ACCESSORIES", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 3, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "ENTERTAINMENT", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 4, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "FURNITURE", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 5, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "SPORTS AND OUTDOORS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 6, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "TOOLS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 7, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "PETS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 8, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "MISCELLANEOUS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        # put the button in the proper row and column
        button.grid (row = 1, column = 9, sticky = N+S+E+W)


                         
        img = PhotoImage (file = "xmark.gif")
        # next, create thenext button
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 10, width = 10,  command = lambda:\
                         self.process ("passed item"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 5, column = 4, sticky = N+S+E+W)


        img = PhotoImage (file = "checkmark.gif")
        # next, create the button
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 10, width = 10, command = lambda:\
                         self.process ("added to cart"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 5, column = 5, sticky = N+S+E+W)

        img = PhotoImage (file = "plus.gif")
        # next, create the button
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 1, width = 1, command = lambda:\
                         self.process ("+"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 0, column = 0, sticky = N+S+E+W)


        img = PhotoImage (file = item1.image)
        # next, create the button
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 100, width = 100, command = lambda:\
                         self.process ("item"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 2, rowspan = 3, column = 4, columnspan = 2, sticky = N+S+E+W)


        self.pack (fill = BOTH, expand = 1)

        #process button presses 
    def process (self, button):
        cart_list = []
        
        if (button == "added to cart"):
            self.display ["text"] = ""
            cart_list.append (item1)

        elif (button == "+"):
            self.display ["text"] = cart_list

        elif (button == "item"):
            self.display ["text"] = item1
##            back = self.display ["text"]
##            self.display ["text"] = str(back[:-1])
            
            
        else:
            self.display ["text"] += button
########################################################################################################

class Item (object):
    def __init__ (self, price, seller, location, weight, condition, brand, color, description, type, image):
        self.price = price
        self.seller = seller
        self.location = location
        self.weight = weight
        self.condition = condition
        self.brand = brand
        self.color = color
        self.description = description
        self.type = type
        self.image = image

    def __str__ (self):
        return "Price: ${}" .format (self.price)

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
        
item1 = Item (100, "andrew", "ruston", 12, "used", "nike", "red", "boring", "ball", "truck.gif")

print item1.seller

# create the window
window = Tk ()

# set the window title
window.title ("The Shopper")

#generate the GUI
p = MainGUI (window)

#display the GUI and wait for user interaction
window.mainloop ()









        
        





        
