# button.py
# for lab 10 on writing classes

from graphics import *

class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, image, center):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        #w,h = width/2.0, height/2.0
        #x,y = center.getX(), center.getY()
        ## you should comment these variables...
        #self.xmax, self.xmin = x+w, x-w 
        #self.ymax, self.ymin = y+h, y-h
        #p1 = Point(self.xmin, self.ymin)
        #p2 = Point(self.xmax, self.ymax)
        #self.rect = Rectangle(p1,p2)
        #self.rect.setFill('lightgray')
        #self.rect.draw(win)
        #self.label = Text(center, label)
        #self.label.draw(win)
        #self.activate() # Start off all buttons as active. This is how to call another method in this class
        center=self.center

    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') # color the text "black"
        self.rect.setWidth(2)       # set the outline to look bolder
        self.active = True          # set the boolean instance variable that tracks "active"-ness to True

    ## check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill("darkgray") ## color the text "darkgray"
        self.rect.setWidth(1) ## set the outline to look finer/thinner
        self.active=False ## set the boolean instance variable that tracks "active"-ness to False

    ## check 4.  complete the isClicked() method
    def isClicked(self, pt):
        """Returns true if button is active and Point pt is inside"""
        return self.xmax >= pt.getX() >= self.xmin and self.ymax >= pt.getY() >= self.ymin

    
def main():
    
    ## check 1. create a graphical window in which to test the Button class
    win=GraphWin("Button Test",600,600)
    
    ## check 2. test the Button constructor method ...
    ## - create two Button objects, one named "Roll Dice" and the other "Quit"
    ## - activate the Roll button
    b1=Button(win,Point(300,300),100,50,"Roll Dice")
    b2=Button(win,Point(300,400),100,50,"Quit")

    ## check 3. now test the deactivate() method ...
    ## - deactivate the "Quit" button

    b2.deactivate()

    pt = win.getMouse()
    ## check 4. test the .isClicked() method using an if statement
    ## - (remove (comment out) this test code before moving onto the next check)
    ##if b2.isClicked(pt):
    ##    b2.activate()

    ## check 5: 
    ## - loop until the "Quit" button is clicked...
        ## if the roll button is clicked
            ## activate the quit button
        ## take the next mouse click

    while not b2.isClicked(pt):
        if b1.isClicked(pt):
            b2.activate()
        pt=win.getMouse()
            
        
    # we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__": 
    main()
