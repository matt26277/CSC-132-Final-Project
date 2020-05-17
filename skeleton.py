##############################################################################################################################################
## Name: Andrew LeBlanc
## Date: 
## Description: 
##############################################################################################################################################

from Tkinter import *
from time import sleep
import tkFont

class MainGUI (Frame):
    
    def __init__ (self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes ("-fullscreen", True)
        self.setupGUI()

    def setupGUI (self):

        self.display = Label (self, text ="", anchor = E,\
        bg = "white", height = 1, font = ("TexGyreAdventor",20))
        self.display.grid (row = 2, rowspan = 3, column = 0, columnspan = 2, \
                        sticky = E + W + N + S)
        
        for row in range (6):
            Grid.rowconfigure (self, row, weight =1)
        for col in range (10):
            Grid.columnconfigure (self, col, weight = 1)


        img = PhotoImage (file = "undo1.gif")
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "green", command = lambda:\
                        self.process ("undo"))
        
        
        button.image = img
        button.grid (row = 0, column = 9, sticky = N+S+E+W)
        
##        button = Button (self, bg = "white", text = "CLOTHES", \
##                        borderwidth = 1, highlightthickness = 0,\
##                        activebackground = "green", command = lambda:\
##                        self.process ("Clothes"))
##        
##        
##        button.grid (row = 2, column = 9, sticky = N+S+E+W)
##
##                         
##        button = Button (self, bg = "white", text = "ELECTRONICS", \
##                        borderwidth = 1, highlightthickness = 0,\
##                        activebackground = "green", command = lambda:\
##                         self.process ("Electronics"))
##        
##        
##        button.grid (row = 3, column = 9, sticky = N+S+E+W)
##
##
##        
##        button = Button (self, bg = "white", text = "VEHICLES", \
##                        borderwidth = 1, highlightthickness = 0,\
##                        activebackground = "green", command = lambda:\
##                         self.process ("Vehicle"))
##        
##        
##        button.grid (row = 4, column = 9, sticky = N+S+E+W)



                         
        img = PhotoImage (file = "xmark.gif")
        
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 10, width = 10,  command = lambda:\
                         self.process ("passed item"))
        
        button.image = img
        
        button.grid (row = 5, column = 4, sticky = N+S+E+W)


        img = PhotoImage (file = "checkmark.gif")

        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 10, width = 10, command = lambda:\
                         self.process ("added to cart"))
        
        button.image = img
       
        button.grid (row = 5, column = 5, sticky = N+S+E+W)

        img = PhotoImage (file = "cart2.gif")
        
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 10, width = 10, command = lambda:\
                         self.process ("cart"))
        
        button.image = img
        
        button.grid (row = 0, column = 0, sticky = N+S+E+W)


        n = len(item_list) - 1
        x = item_list [n]
            
        img = PhotoImage (file = x.image)
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 100, width = 100, command = lambda:\
                         self.process ("item"))
        button.image = img
        button.grid (row = 0, rowspan = 5, column = 3, columnspan = 4, sticky = N+S+E+W)



        self.pack (fill = BOTH, expand = 1)

        
    ############## use variable as parameter to create while loop for images, that way no pop is necessary
    def process (self, button):            

            
        if (button == "added to cart"):

##            if (len (item_list) <= 0):
##                self.display ["text"] = "NO MORE ITEMS"
                
            
##            elif (len (item_list) > 0):
##                m = len(item_list) -1
##                y = item_list [m]
##                cart_list.append (y)
##                print m
##                
##                item_list.pop()

                
                



            if (len(item_list) <= 1):
                 self.display ["text"] = "NO MORE ITEMS"
               

            else:
                self.display ["text"] = "Added to Cart"

                m = len(item_list) -1
                y = item_list [m]
                cart_list.append (y)
                cart_price.append (y.price)
    
                item_list.pop()
                n = len(item_list) - 1
                x = item_list [n]

                img = PhotoImage (file = x.image)
                button = Button (self, bg = "white", image = img, \
                                borderwidth = 0, highlightthickness = 0,\
                                activebackground = "white", height = 100, width = 100, command = lambda:\
                                 self.process ("item"))
                button.image = img
                button.grid (row = 0, rowspan = 5, column = 3, columnspan = 4, sticky = N+S+E+W)
                    
##                n = len(item_list) - 1
##                x = item_list [n]

        

                
##                img = PhotoImage (file = x.image)
##                button = Button (self, bg = "white", image = img, \
##                                borderwidth = 0, highlightthickness = 0,\
##                                activebackground = "white", height = 100, width = 100, command = lambda:\
##                                 self.process ("item"))
##                button.image = img
##                button.grid (row = 0, rowspan = 5, column = 3, columnspan = 4, sticky = N+S+E+W)


        elif (button == "passed item"):
            if (len(item_list) <=1):
                self.display ["text"] = "NO MORE ITEMS"

            else:
                self.display ["text"] = "Item Passed"
                m = len(item_list) -1
                y = item_list [m]
    
                item_list.pop()
                n = len(item_list) - 1
                x = item_list [n]

                img = PhotoImage (file = x.image)
                button = Button (self, bg = "white", image = img, \
                                borderwidth = 0, highlightthickness = 0,\
                                activebackground = "white", height = 100, width = 100, command = lambda:\
                                 self.process ("item"))
                button.image = img
                button.grid (row = 0, rowspan = 5, column = 3, columnspan = 4, sticky = N+S+E+W)
            
##                item_list.pop()
##                self.display ["text"] = "Item passed"
##                n = len(item_list) - 1
##                x = item_list [n]
##                
##                
##                img = PhotoImage (file = x.image)
##                button = Button (self, bg = "white", image = img, \
##                                borderwidth = 0, highlightthickness = 0,\
##                                activebackground = "white", height = 100, width = 100, command = lambda:\
##                                 self.process ("item"))
##                button.image = img
##                button.grid (row = 2, rowspan = 3, column = 4, columnspan = 2, sticky = N+S+E+W)

            



        elif (button == "cart"):
            g = 0

            while g < len (cart_list):
                f = cart_list[g]
                cart_items.append(f.name)
        
                g += 1

            self.display ["text"] = cart_items

            button = Button (self, bg = "white", text = "Proceed to Checkout", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", height = 10, width = 10, command = lambda:\
                         self.process ("checkout"))
        
        
            button.grid (row = 0, column = 1, sticky = N+S+E+W)

        elif (button == "checkout"):
            myFont = tkFont.Font (size = 20)
            button = Button (self, bg = "white", text = cart_items, \
                            borderwidth = 0, highlightthickness = 0,\
                            activebackground = "white", height = 1, width = 1, command = lambda:\
                             self.process ("item"))
            button ["font"] = myFont
            button.grid (row = 0, rowspan = 5, column = 3, columnspan = 4, sticky = N+S+E+W)
            
            self.display ["text"] = "Total Price: $" + str (sum(cart_price))

            button = Button (self, bg = "gold", text = "BUY ITEMS", \
                            borderwidth = 1, highlightthickness = 0,\
                            activebackground = "green", command = lambda:\
                            self.process ("purchase"))
        
        
            button.grid (row = 2, column = 8, columnspan = 2, sticky = N+S+E+W)

        elif (button == "purchase"):
            myFont = tkFont.Font (size = 90)
            button = Button (self, bg = "gold", text = "THANK YOU FOR SHOPPING \n WITH US!", \
                            borderwidth = 1, highlightthickness = 0,\
                            activebackground = "green", command = lambda:\
                            self.process ("FINISHED"))
            button ["font"] = myFont
        
            button.grid (row = 0, rowspan = 6, column = 0, columnspan = 10, sticky = N+S+E+W)
            
            
##            h = len(cart_list) - 1
##            j = cart_list [h]
##            self.display ["text"] = "Total Price: \n ${}" .format(j.price)

            

            
##            img = PhotoImage (file = j.image)
##            button = Button (self, bg = "white", image = img, \
##                                borderwidth = 0, highlightthickness = 0,\
##                                activebackground = "white", height = 100, width = 100)
##            button.image = img
##            button.grid (row = 2, rowspan = 3, column = 4, columnspan = 2, sticky = N+S+E+W)
##
##
##            k = cart_list [h-1]
##            img = PhotoImage (file = k.image)
##            button = Button (self, bg = "white", image = img, \
##                                borderwidth = 0, highlightthickness = 0,\
##                                activebackground = "white", height = 100, width = 100)
##            button.image = img
##            button.grid (row = 2, rowspan = 3, column = 7, columnspan = 2, sticky = N+S+E+W)
##
##            self.display ["text"] = "Total Price: \n ${}" .format(j.price + k.price)
##
##
##
##
##
##            button = Button (self, bg = "white", text = "Checkout All Items", \
##                        borderwidth = 0, highlightthickness = 0,\
##                        activebackground = "white", height = 10, width = 10)
##
##            button.grid (row = 5, column = 5, sticky = N+S+E+W)
##
##            button = Button (self, bg = "white", text = "Clear Cart", \
##                        borderwidth = 0, highlightthickness = 0,\
##                        activebackground = "white", height = 10, width = 10)
##
##            button.grid (row = 5, column = 4, sticky = N+S+E+W)

        elif (button == "undo" and len(cart_list) >= 1):
            cart_list.pop()
            self.display ["text"] = "LAST ITEM REOMVED FROM CART"



        elif (button == "item"):
            y = len(item_list) - 1
            x = item_list [y]
            self.display ["text"] = x
            
            
            
        

        
########################################################################################################

class Item (object):
    def __init__ (self, price, seller, location, weight, condition, brand, color, description, type, image, name):
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
        self.name = name

    def __str__ (self):
        return "Type: {} \n Price: ${} \n Seller: {} \n Location: {} \n Condition: {} \n Brand: {} \n Color: {} \n Description: {} \n Weight: {} lbs " \
               .format (self.type, self.price, self.seller, self.location, self.condition, self.brand, self.color, self.description, self.weight)

class Clothes (Item):
    def __init__ (self, price, size, seller, location, weight, condition, brand, color, description, type, image, name):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type, image, name)
        self.size = size

    def __str__ (self):
        return "Type: {} \n Size: {} \n Price: ${} \n Seller: {} \n Location: {} \n Condition: {} \n Brand: {} \n Color: {} \n Description: {} \n Weight: {} lbs" \
               .format (self.type, self.size, self.price, self.seller, self.location, self.condition, self.brand, self.color, self.description, self.weight)

class Electronics (Item):
    def __init__ (self, price, seller, location, weight, condition, brand, color, description, type, image, name):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type, image, name)
        
class Vehicle (Item):
    def __init__ (self, year, model, price, seller, location, weight, condition, brand, color, description, type, image, name):
        Item.__init__ (self, price, seller, location, weight, condition, brand, color, description, type, image, name)
        self.year = year
        self.model = model

    def __str__ (self):
        return "Type: {} \n Year: {}  \n Make: {} \n Model: {} \n Price: ${} \n Seller: {} \n Location: {} \n Condition: {} \n Color: {} \n Description: {} \n Weight: {} lbs" \
               .format (self.type, self.year, self.brand, self.model, self.price, self.seller, self.location, self.condition, self.color, self.description, self.weight)

        
cyber = Vehicle (2020, "Cyber Truck", 100000, "Elon", "CA", 12000, "New", "Tesla", "Grey", "Zoom Zoom", "Truck", "truck.gif", "Cyber Truck")

hat = Clothes (20, "OSFA", "Phrank", "NY", 0.5, "Used", "Supreme", "Black", "Says Bronx", "Hat", "hat.gif", "Bronx Hat")

shoes = Clothes (20, 8, "Steve", "FL", 1, "used", "Gucci", "White", "Gucci McQueen", "Speedy Shoes", "shoe.gif", "Speedy Shoes")

final = Item (0, "No one", "Nowhere", "0", "Nonexistent", "Nothing", "None", "No more items", "Nothing", "done.gif", "")

pants = Clothes (11, "XXXL", "Wally", "NJ", 5, "New", "LuLu Lemon", "Turquoise", "Fashionable", "Pants", "pants.gif", "LuLu Lemon Leggings")

atruck = Vehicle (1999, "Silverado", 1500, "Andrew", "LA", 5001, "Used", "Chevy", "Pewter", "Dents Everywhere", "Truck", "atruck.gif", "Old Chevy")

mtruck = Vehicle (2000, "Tacoma", 20000, "Matt", "LA", 3000, "Slightly Used", "Toyota", "Black", "Minor scratch on front bumper", "Truck", "mtruck.gif", "Scratched Tacoma")

struck = Vehicle (2016, "F-150", 10, "Seth", "LA", 4500, "Used", "Ford", "White", "Subwoofers go Boom Boom", "Truck", "struck.gif", "F-150")


item_list = [final, cyber, hat, shoes, pants, atruck, mtruck, struck]

cart_list = []

cart_price = []

clothes_list = [hat]

vehicle_list = [cyber]

electronics_list = []

cart_items = []

# create the window
window = Tk ()

# set the window title
window.title ("The Shopper")

#generate the GUI
p = MainGUI (window)

#display the GUI and wait for user interaction
window.mainloop ()









        
        





        
