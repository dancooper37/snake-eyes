# Snake Eyes - By Daniel Cooper 13/9/19

import random
import time
from tkinter import *
from tkinter import messagebox

turnText = [" Player 1's turn.", "Player 2's turn."] 
turn = 0
accumulated = 0
bank = [0, 0]

def won(player):
    global turn
    print("Player",turn + 1,"has won")
    wonWindow = Toplevel()
    wonWindow.geometry("300x200")
    wonWindow.title("Winner")
    Button(wonWindow, text = "New Game", command = newGame).pack()
    wonWindow.destroy()
    turn = 0
    accumulated = 0
    bank = [0, 0]
           
    
# Menu functions
def newGame(): # Resets variablesfor a new game, and update tkinter widgets.
    if messagebox.askyesno("New Game", "Are you sure you want to start a new game?") == True:
        rollButton.config(state = ACTIVE) 
        accumulated = 0
        bank = [0, 0] 
        turn = 0 
        labelPlayerOne.config(bg="black", fg="white") 
        labelPlayerTwo.config(bg="#F0F0F0", fg="black")
        labelInstruct.config(text=turnText[turn])
        scoreButton.config(text="Accumulated score: " + str(accumulated))
        labelBankOne.config(text="Points = " + str(bank[0]))
        labelBankTwo.config(text="Points = " + str(bank[1]))
    else:
        quitGame()

# Rules window
def rules():
    rulesWindow = Toplevel()
    rulesWindow.title('Rules')
    rulesWindow.wm_iconbitmap("icon.ico")
    rulesWindow.geometry("200x200")
    message = "Snake eyes is a turn-based game,\nwhere two dice are rolled each turn.\nblah\nblah\nblah"
    Label(rulesWindow, text=message).pack(expand=True, fill=BOTH)
    Button(rulesWindow, text='Understood', command=rulesWindow.destroy).place(x=185, y=185, anchor="se")

def special():
    colours = ["red", "green", "blue", "yellow", "orange"]
    for i in range(50):
        magic = random.randint(0,4)
        specialColour = colours[random.randint(0,4)]
        specialWindow = Toplevel()
        specialWindow.wm_iconbitmap("icon.ico")
        specialWindow.config(bg = specialColour)
        if magic == 0:
            specialWindow.geometry("100x100")
        elif magic == 1:
            specialWindow.geometry("100x200")

# Options window
def gameOptions():
    optionsWindow = Toplevel()
    optionsWindow.title("Options")
    optionsWindow.wm_iconbitmap("icon.ico")
    optionsWindow.geometry("400x400")
    optionsLabelOne = Label(optionsWindow, text = "Nothing's here yet").pack()
    specialButton = Button(optionsWindow, text = "Special Button", command = special).pack()
    print("Options")

    

# Quit messagebox and action
def quitGame():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?") == True:
        quit()

# Simulates the rolling of the dice
def rollDice():
    diceRolled = []
    for i in range(2):
        diceValue = random.randint(1,6)
        diceRolled.append(diceValue)
    print("The player rolled a %d and a %d" % (diceRolled[0], diceRolled[1]))
    for i in range(15):
        imgWidgetLeft.config(image = diceImages[random.randint(0, 5)])
        imgWidgetRight.config(image = diceImages[random.randint(0, 5)])
        root.after(10)
        continue
    imageNumberOne = diceRolled[0]
    imgWidgetLeft.config(image = diceImages[imageNumberOne - 1])
    imageNumberTwo = diceRolled[1]
    imgWidgetRight.config(image = diceImages[imageNumberTwo - 1])
    moveOptions = 0   #Any move possible
    moveOptions = diceRolled.count(1)
    
    if moveOptions == 0:
        bankButton.config(state = ACTIVE)
        global accumulated
        accumulated = accumulated + diceRolled[0] + diceRolled[1]
        scoreButton.config(text = "Accumulated score: " + str(accumulated))
        labelInstruct.config(text = "Roll again or bank.")
    elif moveOptions == 1:
        bankButton.config(state = DISABLED)
        accumulated = 0
        scoreButton.config(text = "Accumulated score: " + str(accumulated))
        nextTurn()
    else:
        bankButton.config(state=DISABLED)
        accumulated = 0
        scoreButton.config(text="Accumulated score: " + str(accumulated))
        bank[turn] = 0
        if turn == 0:
            labelBankOne.config(text="Points = " + str(bank[0]))
        else:
            labelBankTwo.config(text="Points = " + str(bank[1]))
        nextTurn()

# Moves on to the next turn, changes window text
def nextTurn():
    global turn
    #print(turn)
    if turn == 1:
        turn = 0
        labelPlayerOne.config(bg = "black", fg = "white")
        labelPlayerTwo.config(bg = "#F0F0F0", fg = "black")
    else:
        turn = 1
        labelPlayerTwo.config(bg = "black", fg = "white")
        labelPlayerOne.config(bg = "#F0F0F0", fg = "black")
    labelInstruct.config(text = turnText[turn])

# Internally and visually banks points
def bankPoints():
    global accumulated
    bankButton.config(state = DISABLED)
    bank[turn] = bank[turn] + accumulated
    accumulated = 0
    scoreButton.config(text="Accumulated score: " + str(accumulated))
    if turn == 0:
        labelBankOne.config(text = "Points = " + str(bank[0]))
    else:
        labelBankTwo.config(text = "Points = " + str(bank[1]))
    if bank[turn] >= 100:
        won(turn)
    nextTurn()

# Main window
root = Tk()
root.title("Snake Eyes") # Gives the main window a name
root.geometry("600x400") # Sets the size of the main window
root.wm_iconbitmap('icon.ico') # Changes the icon of the windows

# Images of dice
diceImages = []
diceImages.append(PhotoImage(file = "one.gif"))
diceImages.append(PhotoImage(file = "two.gif"))
diceImages.append(PhotoImage(file = "three.gif"))
diceImages.append(PhotoImage(file = "four.gif"))
diceImages.append(PhotoImage(file = "five.gif"))
diceImages.append(PhotoImage(file = "six.gif"))
imageNumberOne = 5
imageNumberTwo = 5

# Menu
mainMenu = Menu(root, tearoff = 0) #Defines the main menu inside the main window

#File menu
file = Menu(mainMenu, tearoff = 0) #Creates a sub-menu under the mainMenu called 'file', and disables tearoff
file.add_command(label = "New Game", command = newGame) #Adds the 'New Game' command
mainMenu.add_cascade(label = "File", menu = file) 

#Options menu
options = Menu(mainMenu, tearoff = 0) 
options.add_command(label = "Options", command = gameOptions)
mainMenu.add_cascade(label = "Options", menu = options)

#Rules
mainMenu.add_command(label = "Rules", command = rules)

#Quit
mainMenu.add_command(label = "Quit", command = quitGame)

#Header label
labelHeader = Label(root, text = "Snake Eyes", font = ("Arial Bold", 24))
labelHeader.place(x = 550, y = 30, anchor = "ne")
labelCreator = Label(root, text = "The Game", font = ("Arial Bold", 14)).place(x = 510, y = 85, anchor = "ne")

#Canvas containg header line
headerCanvas = Canvas(root)
headerCanvas.create_line(0, 10, 200, 10, width = 2)
headerCanvas.place(x = 360, y = 125, anchor = "nw")

#Canvas containing score line
scoreSeperator = Canvas(root)
scoreSeperator.create_line(0, 10, 200, 10, width = 2)
scoreSeperator.place(x = 360, y = 235, anchor = "nw")

#Canvas containing aline somewhere
seperatorCanvas = Canvas(root, width = 10, height = 325)
seperatorCanvas.create_line(6, 0, 6, 325, width = 2)
seperatorCanvas.place(x = 325, y = 25)

#Canvas for button backgrounds
buttonCanvas = Canvas(root, bg = "black", width = 280, height = 155)
buttonCanvas.place(x = 20, y = 165)

#Shows the two dice images
imgWidgetLeft = Label(root, image = diceImages[imageNumberOne]) #Creates a label widget
imgWidgetLeft.place(x = 25, y = 25) #Places the label widget within the window
imgWidgetRight = Label(root, image = diceImages[imageNumberTwo])
imgWidgetRight.place(x = 175, y = 25)

#Button for roll command
rollButton = Button(root, text = "Roll the dice", width = 20, height = 1, font = ("Arial Bold", 14), command = rollDice)
rollButton.place(x = 37, y = 180)

#Button for bank command
bankButton = Button(root, text = "Bank your points", width = 20, height = 1, font = ("Arial Bold", 14), command = bankPoints, state = DISABLED)
bankButton.place(x = 37, y = 225)

#Button showing accumulated score
scoreButton = Button(root, text = "Accumulated score: " + str(accumulated), width = 20, height = 1, font = ("Arial Bold", 14), fg = "black")
scoreButton.place(x = 37, y = 270)

#Labels showing players and points in the bank
labelPlayerOne = Label(root, text = "Player 1's Bank", bg = "black", fg = "white", font = ("Arial Bold", 14), width = 16)
labelPlayerOne.place(x = 362, y = 150)
labelPlayerTwo = Label(root, text = "Player 2's Bank", font = ("Arial Bold", 14), width = 16)
labelPlayerTwo.place(x = 362, y = 260)
labelBankOne = Label(root, text = "Points = " + str(bank[0]), font = ("Arial Bold", 14), width = 16, height = 1)
labelBankOne.place(x = 362, y = 200)
labelBankTwo = Label(root, text = "Points = " + str(bank[1]), font = ("Arial Bold", 14), width = 16, height = 2)
labelBankTwo.place(x = 362, y = 300)

#Label showing turn and move info
labelInstruct = Label(root, text = "Player 1's turn.", font = ("Arial Bold", 14), width = 24)
labelInstruct.place(x = 165, y = 350, anchor = "center")

#Configures the menu to the root window
root.config(menu = mainMenu)

#Creates the root window
root.mainloop()
