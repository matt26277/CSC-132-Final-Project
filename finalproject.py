from Tkinter import *
from random import *

class Item (Object):
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











