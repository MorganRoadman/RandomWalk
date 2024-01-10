import random
import turtle

def main():
    #Welcome banner
    print("Welcome to the Random Walk Model!")
    print("Random Walk is a process that simulates the succession of random steps\n")

    #User input of mathematical plot
    acceptablePlots = ["1d","1D","2d","2D"]
    plot = input("Would you like a 1D plot of 2D plot? ")

    #Error checking for user plot input
    while plot not in acceptablePlots:
        plot = input("Not a valid response. Please try again: ")

    #User input for number of steps to iterate through
    numberOfSteps = input("How many steps would you like? (Max of 1000) ")
    numberOfSteps = int(numberOfSteps)

    #Making sure the user does not kill the program
    while (numberOfSteps > 1000 or numberOfSteps < 0):
        numberOfSteps = input("Invalid response. Please try again: ")
        numberOfSteps = int(numberOfSteps)

    xMovement = []  #Creates a list for the x-axis movement of the turtle
    xPosition = 0   #Tracks the current x-axis position

    for i in range(numberOfSteps):  #Iterates through the number of steps
        #The turtle's movement can either be negative or positive
        xMovement.append(random.choice([-1,1]))  
        xPosition += xMovement[i]
        i += 1

    yMovement = []   #Creates a list for the y-axis movement of the turtle
    yPosition = 0    #Tracks the current y-axis position

    for i in range(numberOfSteps):  #Iterates through the number of steps
        #The turtle's movement can either be negative or positive
        yMovement.append(random.choice([-1,1]))
        yPosition += yMovement[i]
        i += 1


    #Outputs the correct graph
    if plot == "1d" or plot == "1D":
        oneDimensional(numberOfSteps,xMovement,xPosition)
    elif plot == "2d" or plot == "2D":
        twoDimensional(numberOfSteps,xMovement,xPosition,yMovement,yPosition)



def oneDimensional(steps, xMovement, xPosition):
    #Grid setup (do not need as much y-axis space as 2D plot)
    grid = turtle.getscreen()
    grid.setup(700,350)
    turtle.title("Random Walk 1D")

    #Turtle display text works strangely. In order to have text on the grid, you have to
    #create a turtle that will write text at its position

    #Turtle to write the text "X movement: " in the upper right corner
    xPos = turtle.Turtle()   
    xPos.hideturtle()     #Hides the visible turtle
    xPos.penup()          #Does not draw a line to "goto" position
    xPos.goto(175,125)    #Goes to this coordinate position
    xPos.write("X movement: ", font = ("Comic Sans",12,"normal"))  #Writes the text

    #Turtle to write the x-axis movement in the upper right corner
    #This text will be cleared and updated through each item in the xMovement list
    xText = turtle.Turtle()  
    xText.hideturtle()
    xText.penup()
    xText.goto(300,125)

    #Turtle to write the text "/ {steps}" in the lower right corner
    stepDisplay = turtle.Turtle()
    stepDisplay.hideturtle()
    stepDisplay.penup()
    stepDisplay.goto(260,-125)
    stepDisplay.write("/ " + str(steps), font = ("Comic Sans",12,"normal"))

    #Turtle to write the current step in the lower right corner
    #This text will be cleared and updated through each item in the xMovement list
    progress = turtle.Turtle()
    progress.hideturtle()
    progress.penup()
    progress.goto(225,-125)
    #Tracks current step since xMovement.index[item] will not work in this scenario
    currentIndex = 1  

    #Turtle to write the text "Origin" at the center of the screen
    #It is possible to have the moving turtle write the text before it starts moving,
    #but that text is not perfectly centered
    origin = turtle.Turtle()
    origin.hideturtle()
    origin.penup()
    origin.goto(-18,0)
    origin.write("Origin")

    turtle.lt(90) #faces original moving turtle up
    #Allows for the turtle to move in either direction for the first step

    for item in xMovement:  #Iterates through each item in xMovement
        #turtle.delay(50)  #Slows down turtle

        #Updates text (progress is current step, xText is x-axis movement)
        progress.write(currentIndex, font = ("Comic Sans",12,"normal"))  
        xText.write(item, font = ("Comic Sans",12,"normal"))  

        #Turtle movement
        if (item == 1):     #If the current movement is positive
            turtle.rt(90)   #Faces turtle right
            turtle.fd(20)   #Moves it forward
            turtle.lt(90)   #Faces turtle back up, making it ready for next movement
        elif (item == -1):  #If the current movement is negative
            turtle.lt(90)   #Faces turtle left
            turtle.fd(20)   #Moves it forward
            turtle.rt(90)   #Faces turtle back up, making it ready for next movement

        #Clearing text that needs updated each iteration, and updating current step
        xText.clear()
        progress.clear()
        currentIndex += 1

    #Text that displays when the turtle is done moving
    xPos.clear()
    stepDisplay.clear()
    xPos.write("Final x postion: " + str(xPosition), font = ("Comic Sans",12,"normal"))

    turtle.done()



def twoDimensional(steps,xMovement,xPosition,yMovement,yPosition):
    #Grid setup 
    grid = turtle.getscreen()
    grid.setup(700,700)
    turtle.title("Random Walk 2D")

    #Turtle to write the text "Y movement: " in the upper right corner
    yPos = turtle.Turtle()   
    yPos.hideturtle()     #Hides the visible turtle
    yPos.penup()          #Does not draw a line to "goto" position
    yPos.goto(175,275)    #Goes to this coordinate position
    yPos.write("Y movement: ", font = ("Comic Sans",12,"normal"))  #Writes the text

    #Turtle to write the y-axis movement in the upper right corner
    yText = turtle.Turtle()  
    yText.hideturtle()
    yText.penup()
    yText.goto(300,275)

    #Turtle to write the text "X movement: " in the upper right corner
    xPos = turtle.Turtle()   
    xPos.hideturtle()    
    xPos.penup()          
    xPos.goto(175,300)    
    xPos.write("X movement: ", font = ("Comic Sans",12,"normal")) 

    #Turtle to write the x-axis movement in the upper right corner
    xText = turtle.Turtle()  
    xText.hideturtle()
    xText.penup()
    xText.goto(300,300)

    #Turtle to write the text "/ {steps}" in the lower right corner
    stepDisplay = turtle.Turtle()
    stepDisplay.hideturtle()
    stepDisplay.penup()
    stepDisplay.goto(260,-300)
    stepDisplay.write("/ " + str(steps), font = ("Comic Sans",12,"normal"))

    #Turtle to write the current step in the lower right corner
    progress = turtle.Turtle()
    progress.hideturtle()
    progress.penup()
    progress.goto(225,-300)
    #Tracks current index for steps and for yMovement
    currentIndex = 0 

    #Turtle to write the text "Origin" at the center of the screen
    origin = turtle.Turtle()
    origin.hideturtle()
    origin.penup()
    origin.goto(-18,0)
    origin.write("Origin")

    turtle.lt(90) #faces original moving turtle up
    #Allows for the turtle to move in either direction for the first step

    for item in xMovement:  #Iterates through each item in xMovement
        #turtle.delay(30)  #Slows down turtle

        #Updates text for each iteration
        progress.write((currentIndex+1), font = ("Comic Sans",12,"normal"))  
        xText.write(item, font = ("Comic Sans",12,"normal"))
        yText.write(yMovement[currentIndex], font = ("Comic Sans",12,"normal"))

        #Turtle movement
        if (item == 1):     #If the current x-axis movement is positive
            turtle.rt(90)   #Faces turtle right
            turtle.fd(20)   #Moves it forward
            turtle.lt(90)   #Faces turtle back up, making it ready for next movement
            if (yMovement[currentIndex] == 1):    #If y-axis movement is positive
                turtle.fd(20)  #Moves it forward
            elif (yMovement[currentIndex] == -1): #If y-axis movement is negative
                turtle.rt(90)  #Faces turtle right
                turtle.rt(90)  #Faces turtle right again (now down)
                turtle.fd(20)  #Moves it forward
                turtle.lt(90)  #Faces turtle left
                turtle.lt(90)  #Faces turtle left (now up)

        elif (item == -1):  #If the current movement is negative
            turtle.lt(90)   
            turtle.fd(20)   
            turtle.rt(90)   #Faces turtle back up, making it ready for next movement
            if (yMovement[currentIndex] == 1):    #If y-axis movement is positive
                turtle.fd(20)  
            elif (yMovement[currentIndex] == -1): #If y-axis movement is negative
                turtle.rt(90) 
                turtle.rt(90) 
                turtle.fd(20) 
                turtle.lt(90)  
                turtle.lt(90)  

        #Clearing text that needs updated each iteration, and updating current index
        xText.clear()
        yText.clear()
        progress.clear()
        currentIndex += 1

    #Text that displays when the turtle is done moving
    xPos.clear()
    yPos.clear()
    stepDisplay.clear()
    xPos.write("Final x postion: " + str(xPosition), font = ("Comic Sans",12,"normal"))
    yPos.write("Final y postion: " + str(yPosition), font = ("Comic Sans",12,"normal"))


    turtle.done()

main()
