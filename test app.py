import Tkinter as tk     
import tkFont as tkfont  

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Cart, Add, Clothes, Electronics, Vehicles, Shirt):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Shopping", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Cart",
                            command=lambda: controller.show_frame("Cart"))
        button2 = tk.Button(self, text="Add New Item",
                            command=lambda: controller.show_frame("Add"))
        clothes = tk.Button (self, text = "Clothes", command = lambda: controller.show_frame ("Clothes"))
        electronics = tk.Button (self, text = "Electronics", command = lambda: controller.show_frame ("Electronics"))
        vehicles = tk.Button (self, text = "Vehicles", command = lambda: controller.show_frame ("Vehicles"))
        
        button1.pack()
        button2.pack()
        clothes.pack ()
        electronics.pack ()
        vehicles.pack ()


class Cart(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Your Items:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Shopping page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()




class Add(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Add New Item", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Shopping page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Clothes (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Clothes: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Shopping page",
                           command=lambda: controller.show_frame("StartPage"))
        shirt = tk.Button (self, text = "Shirt", command = lambda: controller.show_frame ("Shirt"))
        button.pack()
        shirt.pack()

class Shirt(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Your Items:", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Shopping page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class Electronics (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Electronics: ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Shopping page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        
class Vehicles (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text= "Vehicles", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the Shopping page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()

    
#########################################################################
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


test_item = Item (10, "bob", "here", 100, "used", "nike", "brown", "my piece of shit car", "vehicle", "plus.gif")

print test_item.type
