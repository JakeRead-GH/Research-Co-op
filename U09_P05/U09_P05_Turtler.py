"""/////////////////////////////////////////////////////////////////////////////

   Turtler
   
   Jake Read
   Created: January 22, 2020
   File Name: U09_P05_Turtler.py

   This program allows the user to play a game like Frogger, where you have
   to move a turtle up the screen to reach safe spots while avoiding cars
   and water in order to reach the next level. There are 4 levels and each
   one has a new feature. At the end of the game your time to complete will
   be displayed. The program is set up to allow for easy testing for each
   level. Simply change the level variable at the start of the main program
   to choose a level from 1 - 4, or 5 for the closing screen.

   Variable List:
   level-              The current level, ends program when it reaches 5
   testing-            A boolean that checks if the user is testing different
                       levels in order to load required items            
   not_hit-            A boolean that checks if the turtle has taken a hit
   win-                A boolean that means the game has ended with a win
   left_pad_taken-     A boolean that shows the left lily pad is taken
   central_pad_taken-  A boolean that shows the central lily pad is taken
   right_pad_taken-    A boolean that shows the right lily pad is taken
   lives-              How many lives the user has left
   delay-              Allows the logs to move less frequently than the cars
                       by counting down
   sink_countdown-     A countdown that activates the sinking lily pads
   start-              The time at the start of the game
   end-                The time at the end of the program

   Documented Errors:
   - I couldn't get the water to kill the turtle properly as when the log
     moves it dissapears briefly, which will cause the turtle to touch
     the water. The code I had to make the water dangerous is commented out
     if you want to look at it. I spent about an hour trying to fix this but
     I didn't even get close. Logically it should be working it just doesn't
     and I've checked every variable in the section for discrepencies and
     found nothing. It's frustrating because it's a pretty important part
     of the game.

   - I couldn't find any other errors, if your trying to find more just use
     the testing feature, it makes it way easier.
   
/////////////////////////////////////////////////////////////////////////////"""

import turtle, random, time    

"""/////////////////////////////////////////////////////////////////////////////
turtle_module_set_up sets up the turtle module for use in the rest of the
program

Variable List:
screen-         The screen used for the program
main-           The turtle that draws the main screen of each level
lives_display-  The turtle that shows the user how many lives they have left
/////////////////////////////////////////////////////////////////////////////"""
def turtle_module_set_up():
    global screen, main, lives_display
    
    screen = turtle.Screen()
    screen.setup(648, 420)

    main = turtle.Turtle()
    main.speed(0)
    main.hideturtle()

    lives_display = turtle.Turtle()
    lives_display.speed(0)
    lives_display.hideturtle()
    lives_display.penup()

"""/////////////////////////////////////////////////////////////////////////////
title_screen creates the title screen for the program. The cars in the
background still move in this section to make it animated.

Variable List:
space_not_pressed-  A boolean that checks if space has been pressed
/////////////////////////////////////////////////////////////////////////////"""
def title_screen():
    global space_not_pressed

    turtle.speed(0)
    turtle.fillcolor("lightGrey")
    turtle.hideturtle()
    
    turtle.penup()    
    turtle.goto(-150, -50)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(150, -50)
    turtle.goto(150, 100)
    turtle.goto(-150, 100)
    turtle.goto(-150, -50)
    turtle.end_fill()
    turtle.penup()    

    turtle.fillcolor("black")
    turtle.goto(0, 10)
    turtle.write("Turtler", True, align = "center", font = ("Arial", 50, "underline") )
    turtle.goto(0, -30)
    turtle.write("Press [Space] to Continue", True, align = "center", font = ("Arial", 18, "normal") )

    space_not_pressed = True

    screen.onkey(stop_screen, "space")
    screen.listen()
    
    while space_not_pressed:
        move_cars()


"""/////////////////////////////////////////////////////////////////////////////
instructions_screen creates the instructions screen for the program. This
screen also has the car's animations in the background.
/////////////////////////////////////////////////////////////////////////////"""
def instructions_screen():
    global space_not_pressed

    turtle.speed(0)
    turtle.fillcolor("lightGrey")
    turtle.hideturtle()
    
    turtle.penup()    
    turtle.goto(-290, -160)
    turtle.pendown()
    turtle.begin_fill()
    turtle.goto(290, -160)
    turtle.goto(290, 195)
    turtle.goto(-290, 195)
    turtle.goto(-290, -160)
    turtle.end_fill()
    turtle.penup()    

    turtle.fillcolor("black")
    turtle.goto(0, 120)
    turtle.write("Instructions", True, align = "center", font = ("Arial", 50, "underline") )
    turtle.goto(-275, 90)
    turtle.write("- Use the WASD keys to move.", font = ("Arial", 18, "normal") )
    turtle.goto(-275, 60)
    turtle.write("- Avoid cars and water as you move up the screen.", font = ("Arial", 18, "normal") )
    turtle.goto(-275, 30)
    turtle.write("- If you're hit you'll lose a life. You have 3", font = ("Arial", 18, "normal") )
    turtle.goto(-275, 5)
    turtle.write("  lives for each level.", font = ("Arial", 18, "normal") )
    turtle.goto(-275, -25)
    turtle.write("- When all three turtles have made it to the safe", font = ("Arial", 18, "normal") )
    turtle.goto(-275, -50)
    turtle.write("  zone, the next level will begin. There are 4 levels.", font = ("Arial", 18, "normal") )
    turtle.goto(-275, -80)
    turtle.write("- In later levels there are logs you have to use to", font = ("Arial", 18, "normal") )
    turtle.goto(-275, -105)
    turtle.write("  cross a river and lily pads that occasionally sink.", font = ("Arial", 18, "normal") )
    turtle.goto(0, -150)
    turtle.write("Press [Space] to Begin", True, align = "center", font = ("Arial", 18, "normal") )
    
    space_not_pressed = True

    screen.onkey(stop_screen, "space")
    screen.listen()
    
    while space_not_pressed:
        move_cars()


"""/////////////////////////////////////////////////////////////////////////////
stop_screen is the function that's called when space is pressed. It ends
both the title and instructions screens.
/////////////////////////////////////////////////////////////////////////////"""
def stop_screen():
    global space_not_pressed

    turtle.clear()
    space_not_pressed = False
        

"""/////////////////////////////////////////////////////////////////////////////
main_screen creates the playable screen for the program. A different layout
will be created depending on the current level.

Variable List:
y_pos-  A changing y position to create the different strips of colour
x_pos-  A changing x position to creat the 3 ending lily pads
/////////////////////////////////////////////////////////////////////////////"""
def main_screen():
    global main, level

    y_pos = -210

    for a in range(7):
        if level == 1:
            if a == 0 or a == 3:
                main.fillcolor("green")

            elif a == 6:
                main.fillcolor("lightBlue")

            else:
                main.fillcolor("grey")

        else:
            if a == 0 or a == 3:
                main.fillcolor("green")

            elif a == 1 or a == 2:
                main.fillcolor("grey")

            else:
                main.fillcolor("lightBlue")
            
            
        main.penup()
        main.goto(-324, y_pos)
        main.pendown()
        
        main.begin_fill()
        main.penup()
        main.goto(324, y_pos)
        main.pendown()
        main.goto(324, y_pos + 60)
        
        if a == 1 or (a == 4 and level == 1):
            main.pencolor("yellow")
            main.setheading(180)
            
            for b in range(22):
                main.forward(20)
                main.penup()
                main.forward(10)
                main.pendown()

            main.pencolor("black")

        else:
            main.penup()
            main.goto(-324, y_pos + 60)
            main.pendown()

        main.goto(-324, y_pos)
        main.end_fill()

        y_pos = y_pos + 60

    main.fillcolor("green")

    x_pos = -207

    main.penup()
    for c in range(3):
        main.goto(x_pos, 150)
        main.begin_fill()
        main.goto(x_pos + 60, 150)
        main.goto(x_pos + 60, 210)
        main.goto(x_pos, 210)
        main.goto(x_pos, 150)
        main.end_fill()

        x_pos = x_pos + 177


"""/////////////////////////////////////////////////////////////////////////////
initialize_turtle sets up the turtle's shape, size, speed, and random
starting position.

Variable List:
move_speed-  The distance the turtle moves with each key press
turtle_x-    The x position of the turtle
turtle_y-    The y position of the turtle
/////////////////////////////////////////////////////////////////////////////"""
def initialize_turtle():
    global move_speed, turtle_x, turtle_y

    turtle.hideturtle()
    turtle.shape("turtle")
    turtle.shapesize(2,2)
    turtle.setheading(90)

    move_speed = 29.5
    turtle_x = 0
    turtle_y = -183 
  
    turtle.penup()
    turtle.speed(0)
    turtle.goto(turtle_x, turtle_y)
    turtle.showturtle()


"""/////////////////////////////////////////////////////////////////////////////
initialize_cars sets up the features for all of the cars and puts them
into parallel lists. The positions of the cars differ depending on level.

Variable List:
cars-   A list that contains all of the cars
image-  The picture of each car to be placed on a turtle
xpos-   A list containing the x positions of the cars
ypos-   A list containing the y positions of the cars
speed-  A list containing the speeds of the cars
/////////////////////////////////////////////////////////////////////////////"""
def initialize_cars():
    global cars, xpos, ypos, speed, level

    cars = []
        
    image = "greenbugcar.gif"
    screen.register_shape(image)
    cars.append(turtle.Turtle(shape=image) )

    image = "redcar2.gif"
    screen.register_shape(image)
    cars.append(turtle.Turtle(shape=image) )

    image = "grey_car2.gif"
    screen.register_shape(image)
    cars.append(turtle.Turtle(shape=image) )

    image = "yellow_car2.gif"
    screen.register_shape(image)
    cars.append(turtle.Turtle(shape=image) )

    image = "blue_van2.gif"
    screen.register_shape(image)
    cars.append(turtle.Turtle(shape=image) )

    image = "red_lorry2.gif"
    screen.register_shape(image)
    cars.append(turtle.Turtle(shape=image) )

    for a in range(6):
        cars[a].speed(0)
        cars[a].penup()

    xpos = []
    ypos = [0, 0, 0, 0, 0, 0]
    speed = []

    if level == 1:
        ypos[0] = -120
        ypos[1] = 60
        ypos[2] = -60
        ypos[3] = 120
        ypos[4] = -60
        ypos[5] = 120

    else:
        ypos[0] = -60
        ypos[1] = -60
        ypos[2] = -1000
        ypos[3] = -1000
        ypos[4] = -120
        ypos[5] = -120
        

    #Green Car
    xpos.append(-50)  
    speed.append(25)
    cars[0].goto(xpos[0], ypos[0])

    #Red Car
    xpos.append(-200)
    speed.append(25)
    cars[1].goto(xpos[1], ypos[1])

    #Grey Car
    xpos.append(-180)
    speed.append(15)
    cars[2].goto(xpos[2], ypos[2])

    #Yellow Car
    xpos.append(180)
    speed.append(15)
    cars[3].goto(xpos[3], ypos[3])

    #Blue Van
    xpos.append(180)
    speed.append(15)
    cars[4].goto(xpos[4], ypos[4])

    #Red Lorry
    xpos.append(-180)
    speed.append(15)
    cars[5].goto(xpos[5], ypos[5])


"""/////////////////////////////////////////////////////////////////////////////
initialize_logs creates all of the logs and places them on the screen in
a preset position.

Variable List:
logs-   A list containing all of the logs 
image-  The picture of each car to be placed on a turtle
logx-   A list containing the x positions of all the logs
logy-   A list containing the y positions of all the logs
/////////////////////////////////////////////////////////////////////////////"""
def initialize_logs():
    global logs, logx, logy, logs_left, logs_right

    logs = []
    
    image = "log2.gif"
    screen.register_shape(image)
    logs.append(turtle.Turtle(shape=image) )

    image = "log3.gif"
    screen.register_shape(image)
    logs.append(turtle.Turtle(shape=image) )

    image = "log4.gif"
    screen.register_shape(image)
    logs.append(turtle.Turtle(shape=image) )

    image = "log5.gif"
    screen.register_shape(image)
    logs.append(turtle.Turtle(shape=image) )

    logx = []
    logy = [0, 0, 0, 0]

    logx.append(-200)
    logx.append(150)
    logx.append(-150)
    logx.append(180)

    if level == 2:      
        logy[0] = 60
        logy[1] = 120
        logy[2] = 120
        logy[3] = 60

    else:
        logy[0] = 60
        logy[1] = -1000
        logy[2] = -1000
        logy[3] = 60


    for a in range(4):
        logs[a].speed(0)
        logs[a].penup()
    
        logs[a].goto(logx[a], logy[a])


"""/////////////////////////////////////////////////////////////////////////////
initialize_lily_pads creates all of the lily pads and places them on the
screen in a preset position.

Variable List:
lily_pads-  A list containing all of the lily pads
image-      The picture of each car to be placed on a turtle
padsx-      A list containing the x positions of all the lily pads
/////////////////////////////////////////////////////////////////////////////"""
def initialize_lily_pads():
    global lily_pads
    
    lily_pads = []
    image = "lily_pad2.gif"
    screen.register_shape(image)

    for a in range(6):
        lily_pads.append(turtle.Turtle(shape=image) )

    padsx = []

    padsx.append(-206.5)
    padsx.append(-147.5)
    padsx.append(-29.5)
    padsx.append(29.5)
    padsx.append(147.5)
    padsx.append(206.5)

    for b in range(6):
        lily_pads[b].speed(0)
        lily_pads[b].penup()
        lily_pads[b].goto(padsx[b], 120)


"""/////////////////////////////////////////////////////////////////////////////
left allows the turtle to move left when [a] is pressed. It can't move off
the screen
/////////////////////////////////////////////////////////////////////////////"""
def left():
    global turtle_x, move_speed
  
    turtle_x = turtle_x - move_speed


"""/////////////////////////////////////////////////////////////////////////////
right allows the turtle to move right when [d] is pressed. It can't move off
the screen
/////////////////////////////////////////////////////////////////////////////"""
def right():
    global turtle_x, move_speed
  
    turtle_x = turtle_x + move_speed


"""/////////////////////////////////////////////////////////////////////////////
up allows the turtle to move up when [w] is pressed. It can't move off
the screen
/////////////////////////////////////////////////////////////////////////////"""
def up():
    global turtle_y, move_speed

    turtle_y = turtle_y + move_speed


"""/////////////////////////////////////////////////////////////////////////////
down allows the turtle to move down when [s] is pressed. It can't move off
the screen
/////////////////////////////////////////////////////////////////////////////"""
def down():
    global turtle_y, move_speed

    turtle_y = turtle_y - move_speed


"""/////////////////////////////////////////////////////////////////////////////
move_turtle moves the turtle to a new position based on movement
instructions from the user. It also checks to see if a lily pad has been
filled

Variable List:
turtle_x-  The new x corrdinate of the turtle
turtle_y-  The new y coordinate of the turtle
/////////////////////////////////////////////////////////////////////////////"""
def move_turtle():
    global turtle_x, turtle_y, turtle, left_pad_taken, central_pad_taken, right_pad_taken
    
    turtle.goto(turtle_x, turtle_y)

    if turtle.xcor() == -177 and turtle.ycor() == 171 and left_pad_taken == False:
        turtle.stamp()
        turtle_x = 0
        turtle_y = -183
        turtle.goto(turtle_x, turtle_y)
        left_pad_taken = True

    elif turtle.xcor() == 0 and turtle.ycor() == 171 and central_pad_taken == False:
        turtle.stamp()
        turtle_y = -183
        turtle.goto(turtle_x, turtle_y)
        central_pad_taken = True

    elif turtle.xcor() == 177 and turtle.ycor() == 171 and right_pad_taken == False:
        turtle.stamp()
        turtle_x = 0
        turtle_y = -183
        turtle.goto(turtle_x, turtle_y)
        right_pad_taken = True


"""/////////////////////////////////////////////////////////////////////////////
move_car moves the cars to the right or left. If they goes off the side of the
screen they teleport back to the other side.
/////////////////////////////////////////////////////////////////////////////"""
def move_cars():
    global car, xpos, ypos, speed

    for a in range(6):
        if a == 0 or a == 1:
            xpos[a] = xpos[a] + speed[a]
            
            if xpos[a] > 300:
                xpos[a] = -300

        else:
            xpos[a] = xpos[a] - speed[a]
            
            if xpos[a] < -300:
                xpos[a] = 300

        cars[a].goto(xpos[a], ypos[a])


"""/////////////////////////////////////////////////////////////////////////////
move_logs moves the logs once for every 5 times the cars move. This allows
them to move at the same speed as the turtle so they can cary it. If the
turtle is on a log it will be pulled along. If the turtle's hitbox leaves
the logs hit box while over water it will die, or at least it should anyway
but that sections turned off because the logs kill the turtle when they move.
If the logs leave the screen they reappear on the opposite side.

Variable List:
logs_left-   The left hitboxes of the logs
logs_right-  the right hitboxes of the logs
/////////////////////////////////////////////////////////////////////////////"""
def move_logs():
    global logs, logx, logy, delay, logs_left, logs_right, turtle_x, turtle_y, not_hit

    delay = delay - 1

    if delay == 0:
        logs_left = []
        logs_right = []

        logs_left.append(logs[0].xcor() - 75)
        logs_right.append(logs[0].xcor() + 75)
        logs_left.append(logs[1].xcor() - 115)
        logs_right.append(logs[1].xcor() + 115)
        logs_left.append(logs[2].xcor() - 38)
        logs_right.append(logs[2].xcor() + 38)
        logs_left.append(logs[3].xcor() - 75)
        logs_right.append(logs[3].xcor() + 75)

        for a in range(4):        
            if turtle.ycor() > (logs[a].ycor() - 30) and turtle.ycor() < (logs[a].ycor() + 30):
                if turtle.xcor() > logs_left[a] and turtle.xcor() < logs_right[a]:
                    if a == 0 or a == 3:
                        turtle_x = turtle_x + 29.5

                    else:
                        turtle_x = turtle_x - 29.5

                #else:
                    #not_hit = False

            if a == 0 or a == 3:            
                logx[a] = logx[a] + 29.5

                if logx[a] > 350:
                    logx[a] = -350 

            else:
                logx[a] = logx[a] - 29.5

                if logx[a] < -350:
                    logx[a] = 350 

            logs[a].goto(logx[a], logy[a])
            turtle.goto(turtle_x, turtle_y)
            
        delay = 5


"""/////////////////////////////////////////////////////////////////////////////
sink_lily_pads causes the lily pads to flash a few times and then sink.
one of the 3 sets of lily pads sink at random every few seconds. I didn't
until now that the original lily pads move, so mine are stationary.

Variable List:
sinking-  The randomly selected set of lily pads that sinks
/////////////////////////////////////////////////////////////////////////////"""
def sink_lily_pads():
    global lily_pads, sink_countdown, sinking

    if sink_countdown == 30:
        sinking = random.randint(1, 3)

    if sink_countdown == 20:
        for a in range(6):
            lily_pads[a].showturtle()

    
    sink_countdown = sink_countdown - 1

    if sink_countdown <= 15 and sink_countdown % 2 == 0 and sink_countdown > 1:
        if sinking == 1:
            lily_pads[0].hideturtle()
            lily_pads[1].hideturtle()

        elif sinking == 2:
            lily_pads[2].hideturtle()
            lily_pads[3].hideturtle()

        else:
            lily_pads[4].hideturtle()
            lily_pads[5].hideturtle()
            
    elif sink_countdown <= 15 and sink_countdown % 2 == 1 and sink_countdown > 1:
        if sinking == 1:
            lily_pads[0].showturtle()
            lily_pads[1].showturtle()

        elif sinking == 2:
            lily_pads[2].showturtle()
            lily_pads[3].showturtle()

        else:
            lily_pads[4].showturtle()
            lily_pads[5].showturtle()

    if sink_countdown == 0:
        sink_countdown = 30
        
    

"""/////////////////////////////////////////////////////////////////////////////
check_hit creates the hitboxes of the cars andthe turtle and updates
not_hit when the hitboxes overlap.

Variable List:
cars_left-        A list containing the left hit box of every car
cars_right-       A list containing the right hit box of every car
cars_top-         A list containing the top hit box of every car
cars_bottom-      A list containing the bottom hit box of every car
turtle_left_x-    The turtle's left hitbox
turtle_right_x-   The turtle's right hitbox
turtle_top_y-     The turtle's top hitbox
turtle_bottom_y-  The turtle's bottom hitbox
/////////////////////////////////////////////////////////////////////////////"""
def check_hit():
    global turtle_x, turtle_y, turtle, not_hit, lives, cars, turtle_left_x
    global turtle_right_x, turtle_top_y, turtle_bottom_y, lives_display

    turtle_left_x = turtle.xcor()- 20
    turtle_right_x = turtle.xcor() + 20
    turtle_top_y = turtle.ycor() + 25
    turtle_bottom_y = turtle.ycor() - 20

    #Cars
    cars_left = []
    cars_right = []
    cars_top = []
    cars_bottom = []

    cars_left.append(cars[0].xcor() - 15)
    cars_right.append(cars[0].xcor() + 20)
    cars_top.append(cars[0].ycor() + 10)
    cars_bottom.append(cars[0].ycor() - 10)

    cars_left.append(cars[1].xcor() - 30)
    cars_right.append(cars[1].xcor() + 40)
    cars_top.append(cars[1].ycor() + 10)
    cars_bottom.append(cars[1].ycor() - 15)

    cars_left.append(cars[2].xcor() - 40)
    cars_right.append(cars[2].xcor() + 30)
    cars_top.append(cars[2].ycor() + 10)
    cars_bottom.append(cars[2].ycor() - 10)

    cars_left.append(cars[3].xcor() - 40)
    cars_right.append(cars[3].xcor() + 30)
    cars_top.append(cars[3].ycor() + 10)
    cars_bottom.append(cars[3].ycor() - 15)

    cars_left.append(cars[4].xcor() - 50)
    cars_right.append(cars[4].xcor() + 40)
    cars_top.append(cars[4].ycor() + 23)
    cars_bottom.append(cars[4].ycor() - 22)

    cars_left.append(cars[5].xcor() - 70)
    cars_right.append(cars[5].xcor() + 55)
    cars_top.append(cars[5].ycor() + 25)
    cars_bottom.append(cars[5].ycor() - 25)

    for a in range(6):
        if turtle_right_x > cars_left[a] and turtle_left_x < cars_right[a] and turtle_top_y > cars_bottom[a] and turtle_bottom_y < cars_top[a]:
            not_hit = False


    #Water at the top of the screen (This water actually will kill you)
    if turtle.xcor() < -207 and turtle.ycor() == 171:
        not_hit = False

    elif turtle.xcor() > -147 and turtle.xcor() < -30 and turtle.ycor() == 171:
        not_hit = False

    elif turtle.xcor() > 30 and turtle.xcor() < 147 and turtle.ycor() == 171:
        not_hit = False

    elif turtle.xcor() > 207 and turtle.ycor() == 171:
        not_hit = False
        

    if not_hit == False:
        screen.onkey(None, "a")
        screen.onkey(None, "d")
        screen.onkey(None, "w")
        screen.onkey(None, "s")

        lives = lives - 1
        not_hit = True
        turtle_x = 0
        turtle_y = -183
        time.sleep(1)
        turtle.goto(turtle_x, turtle_y)

        screen.onkey(left, "a")
        screen.onkey(right, "d")
        screen.onkey(up, "w")
        screen.onkey(down, "s")

        lives_display.clear()
        lives_display.goto(-300, 170)
        lives_display.write("Lives: " + str(lives), font = ("Arial", 16, "normal") )


"""/////////////////////////////////////////////////////////////////////////////
check_off_screen checks the turtle coordinates to make sure it hasnt gone
off the screen. If it has it loses a life.
/////////////////////////////////////////////////////////////////////////////"""
def check_off_screen():
    global turtle_x, turtle_y, not_hit
    
    if turtle_x > 300 or turtle_x < -300 or turtle_y < -210 or turtle_y > 210:
        not_hit = False


"""/////////////////////////////////////////////////////////////////////////////
check_best_time calculates the time it took the user to complete the game
using the start and end values taken previously. It then compares this time to
the current best time stored in a file. If the user was faster than the best
time then the best time is updated to be the users time. The time is then
split into minutes and seconds for a nicer display later in the program.
If you're using the test option a preset time will be used to keep the top
time fair.

Variable List:
file-             The file that contains the fastest completion of the game
completion_time-  The time it took the user to complete the game
minutes-          The minutes in the completion time
seconds-          The additional seconds of the completion time
best_time-        The fastest the game has been completed
best_minutes-     The minutes in the best time
best_seconds-     The additional seconds of the best time

/////////////////////////////////////////////////////////////////////////////"""
def check_best_time():
    global start, end, minutes, best_minutes, seconds, best_seconds, completion_time

    if testing != True:
        completion_time = round(end - start, 2)
    
    file = open("best_time.txt")
    best_time = float(file.readline().strip() )
    file.close()

    if completion_time < best_time:
        best_time = completion_time

        file = open("best_time.txt", 'w')
        file.write(str(best_time) )
        file.close()

    seconds = completion_time % 60
    minutes = (completion_time - seconds) / 60

    best_seconds = best_time % 60
    best_minutes = (best_time - best_seconds) / 60


"""/////////////////////////////////////////////////////////////////////////////
closing_screen creates the final screen of the program. Depending on wether
the user won or lost, they'll get an appropriate screen. In addiition the
users completion time and the best time are displayed. The turtle will move
across the screen under the information when the screen first loads.

Variable List:
message-  A parameter that determines if the user won or lost
/////////////////////////////////////////////////////////////////////////////"""
def closing_screen(message):
    global turtle_x, completion_time, best_time, seconds, best_seconds, minutes, best_minutes
    
    screen.clear()
    initialize_turtle()
    
    screen.bgcolor("lightBlue")
    main.goto(0, 80)
    
    if message == "win":
        main.write("You Win!", True, align = "center", font = ("Arial", 40, "normal") )
        main.goto(0, -45)
        main.write("Completion Time: " + str(int(minutes) ) + " min  " + str(int(seconds) ) + "s", True, align = "center", font = ("Arial", 20, "normal") )
        main.goto(0, -80)
        main.write("Best Time: " + str(int(best_minutes) ) + " min  " + str(int(best_seconds) ) + "s", True, align = "center", font = ("Arial", 20, "normal") )

    else:
        main.write("You Ran Out of Lives!", True, align = "center", font = ("Arial", 40, "normal") )
        
    main.goto(0, 5)
    main.write("Thanks for Playing!", True, align = "center", font = ("Arial", 40, "normal") )
    turtle_x = -400
    turtle.goto(turtle_x, -110)
    turtle.setheading(0)

    for a in range(25):
        turtle_x = turtle_x + 30
        turtle.goto(turtle_x, -110)
        time.sleep(0.1)

## Main Program
turtle_module_set_up()

level = 1

if level > 1:
    testing = True

else:
    testing = False
    
main_screen()
initialize_cars()
title_screen()
instructions_screen()
initialize_turtle()

screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.listen()

playing = True
not_hit = True
win = False
left_pad_taken = False
central_pad_taken = False
right_pad_taken = False

lives = 3
lives_display.goto(-300, 170)
lives_display.write("Lives: " + str(lives), font = ("Arial", 16, "normal") )
delay = 5
sink_countdown = 30

if testing:
    if level > 1:
        initialize_logs()

    if level > 2:
        initialize_lily_pads()

    if level == 5:
        completion_time = 165
        win = True

else:
    start = time.time()

while lives != 0 and level != 5:
    move_turtle()
    move_cars()

    if level > 1:
        move_logs()

    if level == 4:
        sink_lily_pads()
        
    check_hit()
    check_off_screen()

    if left_pad_taken and central_pad_taken and right_pad_taken and level:
        level = level + 1

        if level < 5:
            left_pad_taken = False
            central_pad_taken = False
            right_pad_taken = False
            lives = 3
            main_screen()
            lives_display.clear()
            lives_display.goto(-300, 170)
            lives_display.write("Lives: " + str(lives), font = ("Arial", 16, "normal") )
            initialize_cars()
            initialize_logs()

            if level > 2:
                initialize_lily_pads()

        else:
            win = True       

screen.onkey(None, "a")
screen.onkey(None, "d")
screen.onkey(None, "w")
screen.onkey(None, "s")

if win:
    end = time.time()
    check_best_time()
    closing_screen("win")

else:
    closing_screen("lose")

screen.exitonclick()
