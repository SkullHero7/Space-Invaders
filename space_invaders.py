import turtle
import os
import math
import random

####################### Setting up the screen

wn = turtle.Screen()
#tells turle to set up a screen
wn.bgcolor("black")
#sets the background color to black
wn.title("Space Invaders")
#sets the title 
wn.bgpic("space_invaders_background.gif")

# register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


# Set up border 600x600 square pixel
border_pen = turtle.Turtle()
#tells turtle to make a pen
border_pen.speed(0)
# tells the pen how fast to go 'zero is fastest'
border_pen.color("white")
# tells the pen what color to be/use
border_pen.penup()
# the pen starts in the center. This command allows me to change the start position without it draging the ink to said point.
border_pen.setposition(-300,-300)
# tells the pen to where to start
border_pen.pendown()
# puts the pen down
border_pen.pensize(3)
# how thick the pen is
for side in range(4):
    # how many sides to draw
    border_pen.fd(600)
    # go foward 600 pixels
    border_pen.left(90)
    # make a 90 degree angle
border_pen.hideturtle()
# hides the pen


#Set up the score board
score = 0
# Draw the score board
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
 


#########################  
# Create the player

player = turtle.Turtle()
# tells the program turtle to make a object called player
player.color("blue")
# makes the player object blue
player.shape("player.gif")
# makes the player object a triangle
player.penup()
# prevents the object from tracing blue everywhere
player.speed(0)
# makes the setup of this process to 0(the fastest)
player.setposition(0, -250)
#  sets the starting position of the player at 0,-250
player.setheading(90)
# makes it so the players faces straight
playerspeed = 15
# sets the speed to 15 pixels


########### Controls

def move_left():
    x = player.xcor()
    # finds the current x cordinate of the player
    x -= playerspeed
     # takes the current value of x, finds the current player speed and subtracts them
    if x < -280:
        x = - 280
        # boundry check. If the player goes to x -280(the boundry for this screen) then player will be set to -280 thus preventing it from going further
    player.setx(x)
    #moves the player to the new x cordinate

def move_right():
    x = player.xcor()
    # finds the current x cordinate of the player
    x += playerspeed
    # takes the current value of x and adds the player speed
    if x > 280:
        x = 280
        # boundry check. If the player goes to x 280 then the player will be set to x 280 thus preventing the player from going any further.
    player.setx(x)
    # moves the player to  the new x cordinate

def fire_bullet():
    global bulletstate
    # makes it so the variable can be changed from any function
    if bulletstate == "ready":
        # if the variable is in the deafault form
        bulletstate = "fire"
        # change the state to fire
        x = player.xcor()
        # place the bullet at the x cord of player
        y = player.ycor() +10
        #  place the bullet at the y cord but 10 pixels up of the player
        bullet.setposition(x,y)
        # moves the bullet to this new position
        bullet.showturtle() 
        # shows the bullet
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    # uses a math formula to determin the distance betwen two variables
    if distance < 15:
        return True
        # if the distance is less tha n15 pixels then return true aka collision 
    else:
        return False
###### Creat keyboard bindings

turtle.listen()
# tells the turtle to listen for keyboard actions
turtle.onkey(move_left, "Left")
# when i push the left key I call the function move left
turtle.onkey(move_right, "Right")
# when i push the right key i call the function move right
turtle.onkey(fire_bullet, "space")

##############
# create the players weapon/bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 40

#Define bullet state
# ready - ready to fire
# fire - bullet is firing

bulletstate = "ready"
##################################
# Create the enemy and number of enemies

#Number of enemies
number_of_enemies = 7
enemies = []
# make an empty list
for i in range(number_of_enemies):
    # add 5 to list
    enemies.append(turtle.Turtle())
    # add to list

for enemy in enemies:
    # for each enemy add the below
    enemy.color("red")
    # makes the variable red
    enemy.shape("invader.gif")
    # makes the variable a circle
    enemy.penup()
    # prevents tracing
    enemy.speed(0)
    # creates this really fast
    x = random.randint(-200, 200)
    # sets the x cord 
    y = random.randint(100, 250)
    # sets the y cord
    enemy.setposition(x, y)
    # places them in the starting position 


enemyspeed = 5
# sets the movement speed at 2



############################ Main game loop
while True:
    for enemy in enemies:
    # puts eveything below to all the enemies

        # Move the enemy
        x = enemy.xcor()
        # locate the starting x value
        x += enemyspeed
        # adds the enemy speed to the value (in this case its 2 pixels)
        enemy.setx(x)
        # sets the new value at + 2 

        # Move ALL of the enemies back and down
        if enemy.xcor() > 280:
            for e in enemies:
                # if enemy reaches boundry
                y = e.ycor()
                # find the y cord
                y -= 50
                # subtract 40 pixels (move down 40 pixels)
                e.sety(y)
                # set the new y cord
            enemyspeed *= -1
                # change the direction. It is currently moving +2 pixels(to the right) by * -1 we make it -2(to the left) 
                
        if enemy.xcor() < -280:
            for e in enemies:
                # if enemy reaches boudnry
                y = e.ycor()
                # find the y cord
                y -= 50
                # subtract 40 pixels
                e.sety(y)
                # set the new y cord
            enemyspeed *= -1
                # change the direction. -2 * -1 = +2 thus its now moving to the right
       
        if isCollision(bullet, enemy): 
            # if the isCollision statement returns true
            bullet.hideturtle()
            # hide the bullet
            bullet.setposition(0, -400)
            # reset the bullet off screen
            bulletstate = "ready"
            # reset bullet state
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # reset enemy position
            score += 10
            # add 10  to the score if there is a collision
            scorestring = "Score: %s" %score
            # add that 10 to the score variable
            score_pen.clear()
            # clears the previous score 
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            #writes the new score    
 
    
        if isCollision(player, enemy):
            # if the isCollision statment returns true 
            player.hideturtle()
            # hide the enemy
            enemy.hideturtle()
            # hide the player
            print ("Game Over")
            # game over buddy
            break

    ######### move the bullet
    y = bullet.ycor()
    # find the current y cord of the bullet
    y += bulletspeed
    # adds the bullet speed to it (so 20 pixels up)
    bullet.sety(y)
    # sets the bullet in motion

    if bullet.ycor() > 275:
        # detects top border
        bullet.hideturtle()
        # if bullet reaches the top hid the bullet
        bulletstate = "ready"
        # reset the state of the bullet to 'ready'


delay = input("Press enter to finish")