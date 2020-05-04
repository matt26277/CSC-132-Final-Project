##############################################################################################################################################
## Name: Andrew LeBlanc
## Date: 2-12-20
## Description: This will create a working calculator
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
        for col in range (9):
            Grid.columnconfigure (self, col, weight = 1)

        #################### the first row ####################
        # (
        # first, fetch and store the image
        # to work best on the RPi, images should be 115x115
        #  pixels
        # otherwise, may need to add .subsample(n)
        img = PhotoImage (file = "xmark.gif")
        # next, create the button
        button = Button (self, bg = "white", text = "CLOTHES", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                        self.process ("("))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 0, sticky = N+S+E+W)

                         
        img = PhotoImage (file = "rpr.gif")
        # next, create thenext button
        button = Button (self, bg = "white", text = "ELECTRONICS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process (")"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 1, sticky = N+S+E+W)


        img = PhotoImage (file = "clr.gif")
        # next, create the button
        button = Button (self, bg = "white", text = "VEHICLES", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("AC"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 2, sticky = N+S+E+W)



        img = PhotoImage (file = "bak.gif")
        # next, create the button
        button = Button (self, bg = "white", text = "ACCESSORIES", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 3, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "ENTERTAINMENT", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 4, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "FURNITURE", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 5, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "SPORTS AND OUTDOORS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 6, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "TOOLS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 7, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "PETS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 8, sticky = N+S+E+W)

        button = Button (self, bg = "white", text = "MISCELLANEOUS", \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("bak"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 1, column = 9, sticky = N+S+E+W)

        ###################### second row #########################

##        img = PhotoImage (file = "cart.gif")
##        # next, create the button
##        button = Button (self, bg = "white", image = img, \
##                        borderwidth = 0, highlightthickness = 0,\
##                        activebackground = "white", command = lambda:\
##                         self.process ("7"))
##        # set the button's image
##        button.image = img
##        # put the button in the proper row and column
##        button.grid (row = 0, column = 9, sticky = N+S+E+W


                         
        img = PhotoImage (file = "xmark.gif")
        # next, create thenext button
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("2"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 4, column = 3, sticky = N+S+E+W)


        img = PhotoImage (file = "checkmark.gif")
        # next, create the button
        button = Button (self, bg = "white", image = img, \
                        borderwidth = 0, highlightthickness = 0,\
                        activebackground = "white", command = lambda:\
                         self.process ("3"))
        # set the button's image
        button.image = img
        # put the button in the proper row and column
        button.grid (row = 4, column = 5, sticky = N+S+E+W)


        self.pack (fill = BOTH, expand = 1)

        #process button presses 
    def process (self, button):
        
        #AC clears the display
        if (button == "AC"):
            self.display ["text"] = ""
        # = starts an evaluation of whats on the display
        elif (button == "="):
            expr = self.display ["text"]

            #the evaluation might return an error
            try:
                result = eval (expr)
                self.display ["text"] =str(result)
            except:

                #note the error display
                self.display ["text"] = "ERROR"

        elif (button == "bak"):
            back = self.display ["text"]
            self.display ["text"] = str(back[:-1])
            
            
        else:
            self.display ["text"] += button

        
      
# create the window
window = Tk ()

# set the window title
window.title ("The Reckoner")

#generate the GUI
p = MainGUI (window)

#display the GUI and wait for user interaction
window.mainloop ()










        
        





        
