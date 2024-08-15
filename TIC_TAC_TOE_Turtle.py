import turtle

HIGH = 225
MID_1 = 75
MID_2 = -75
LOW = -225

def main():

    changeCursorToPen() #Change the cursor to look like a pen.
    turtle.speed(0) # Set turtle speed to maximum
    drawBoard() # Draw the game board

    matrix =[['0','0','0'],['0','0','0'],['0','0','0']] # Initialize the game matrix

    game(matrix) # Start the game loop

    turtle.done() # Finish and close the turtle screen



def drawLine(start_x,end_x, start_y,end_y): #Draw line with coordinates
    turtle.penup()
    turtle.goto(start_x,start_y)
    turtle.pendown()
    turtle.goto(end_x, end_y)

def move(x,y):# Move turtle without drawing line

    turtle.penup()
    turtle.goto(x,y)

def drawBoard(): # Draw the TIC-TAC-TOE game board.

    turtle.pensize(5) #set the pen size

    drawLine(LOW, HIGH, MID_2, MID_2)
    move(HIGH, MID_1)
    drawLine(HIGH, LOW, MID_1, MID_1)
    move(MID_2, HIGH)
    drawLine(MID_2, MID_2, HIGH, LOW)
    move(MID_1, LOW)
    drawLine(MID_1, MID_1, LOW, HIGH)

def changeCursorToPen(): #Change the turtule cursor to look like a pen , to give a feeling that this is a real game.

    shape = ((0, 0), (6, 10), (25, 30), (30, 25), (10, 6))# the coordinates of each corner
    turtle.register_shape('pen', shape) # registering the new shap
    turtle.shape('pen')# changing the shape to 'pen'


def shapeMark(row, col, shape):  # Draw the shape (X or O) in the specified row and column.

    turtle.pensize(5)
    if shape == 'X':
        turtle.pencolor('blue')

    if shape == 'O':
        turtle.pencolor('red')

    # Determine the coordinates for drawing the shape based on row and col

    if row == 1:
        if col == 1:
            drawShape(shape, LOW, HIGH)
        if col == 2:
            drawShape(shape, MID_2, HIGH)
        if col == 3:
            drawShape(shape, MID_1, HIGH)

    if row == 2:
        if col == 1:
            drawShape(shape, LOW, MID_1)
        if col == 2:
            drawShape(shape, MID_2, MID_1)
        if col == 3:
            drawShape(shape, MID_1, MID_1)

    if row == 3:
        if col == 1:
            drawShape(shape, LOW, MID_2)
        if col == 2:
            drawShape(shape, MID_2, MID_2)
        if col == 3:
            drawShape(shape, MID_1, MID_2)

def drawShape(shape,x,y): #  Draw  X or O at the specified coordinates.

    if shape == 'X':
        drawX(x,y)

    if shape == 'O':
        drawO(x, y)

def drawX(x, y):# Draw X shape at specified coordinates

    #Draw first diagonal
    move(x + 20 , y -20)
    turtle.pendown()
    turtle.setheading(-45)
    turtle.forward(155)

    #Draw second diagonal
    turtle.setheading(90)
    turtle.penup()
    turtle.forward(110)
    turtle.setheading(225)
    turtle.pendown()
    turtle.forward(155)


def drawO(x,y): # draw a circle in a specific coordination

    turtle.penup()
    turtle.goto(x+75,y-130)
    turtle.setheading(365)
    turtle.pendown()
    turtle.circle(55)

def getRowCol(shape): # Ask from user in which row & col to place the shape.

    row = int(turtle.textinput('Row Needed','Enter the row location'))
    col = int(turtle.textinput('Col Needed','Enter the col location'))

   ## row = int(input(shape + ' turn,please enter the row: '))
   ## col = int(input(shape + ' turn,please enter the col: '))

    return row , col

def statCheck(matrix , shape): #check if some of the players won the game

    #check the horizontal and verticl shape location
    for i in range(len(matrix)):
        countHorizontal = 0 #Check for horizontal sequence
        countVertical = 0 #Check for vertical sequence
        for j in range(len(matrix[i])):
            if(matrix[i][j] == shape): #Horizontal
                countHorizontal = countHorizontal + 1
                if countHorizontal == 3: #If this is a 3 shapes sequence
                    drawWinLine(i,j,'H')
                    return False
            if(matrix[j][i] == shape):#Vertical
                countVertical = countVertical + 1
                if countVertical == 3: #If this is a 3 shapes sequence
                    drawWinLine(j, i, 'V')
                    return False

    countDiagonalL = 0
    countDiagonalR = 0
    j = 2
    # check the diagonal shapes location
    for i in range(len(matrix)):
        if(matrix[i][i] == shape): #Top left diagonal
            countDiagonalL = countDiagonalL + 1
            if countDiagonalL == 3: #If this is a 3 shapes sequence
                drawWinLine(i,j,'DL')
                return False
        if(matrix[i][j] == shape): #Top right diagonal
            countDiagonalR = countDiagonalR + 1
            j = j - 1
            if countDiagonalR == 3: #If this is a 3 shapes sequence
                drawWinLine(i, i, 'DR')
                return False

    return True

def drawWinLine(i,j,direction): #Draw a line through the winning cells.

    turtle.pensize(10)
    turtle.pencolor('purple')

    if direction == 'H':#Horizontal
        if i == 0:
            drawLine(LOW,HIGH,150,150)
        if i == 1:
            drawLine(LOW,HIGH,0,0)
        if i == 2:
            drawLine(LOW,HIGH,-150,-150)

    if direction == 'V':#Vertical
        if j == 0:
            drawLine(-150, -150, HIGH, LOW)
        if j == 1:
            drawLine(0, 0, HIGH, LOW)
        if j == 2:
            drawLine(150, 150, HIGH, LOW)

    if direction == 'DL':#Diagonal from top left board
        drawLine(LOW, HIGH, HIGH, LOW)

    if direction == 'DR':#Diagonal from top right board
        drawLine(HIGH,LOW,HIGH,LOW)




def fillAndCheck(shape,matrix): #Fill the cell with the player's shape and check for win/tie.
    row, col = getRowCol(shape)
    shapeMark(row, col, shape)
    matrix[row - 1][col - 1] = shape

    flag = statCheck(matrix, shape) # Check if the current player wins
    if flag == False:
        print(shape + " is the winner!")
        turtle.write(shape + " is the winner!")
    return flag


def game(matrix):  #Control the flow of the game.
    i = 0
    flag = True

    while (i < 9 and flag == True):

        i,flag = turn(i,flag,'X',matrix)

        i,flag = turn(i,flag,'O',matrix)

        if i == 9 and flag == True:
            print("It is a tie! Nobody win!")


def turn(i,flag,shape,matrix): # Represent the turn of the players and check for winning or tie.
    if flag == True and i < 9:
        flag = fillAndCheck(shape, matrix)
        i = i + 1

    return i, flag

main()

