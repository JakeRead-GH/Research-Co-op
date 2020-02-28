import turtle
import time
import random
import tkinter


def turtle_setup():
    global machine, spin_one, spin_two, spin_three, info, handle, screen
    
    screen = turtle.Screen()
    screen.setup(800, 800, 400, 100)

    machine = turtle.Turtle()
    spin_one = turtle.Turtle()
    spin_two = turtle.Turtle()
    spin_three = turtle.Turtle()
    handle = turtle.Turtle()
    info = turtle.Turtle()

    machine.speed(0)
    spin_one.speed(0)
    spin_two.speed(0)
    spin_three.speed(0)
    info.speed(0)
    handle.speed(0)

    turtle.hideturtle()
    machine.hideturtle()
    spin_one.hideturtle()
    spin_two.hideturtle()
    spin_three.hideturtle()
    info.hideturtle()
    handle.hideturtle()

 

def title_screen():
    global image
    
    image = "background.gif"
    screen.bgpic(image)

    info.color("white")
    info.penup()
    info.goto(0, 100)
    info.write("Virtual Slot Machine", True, align = "center", font = ("Arial", 60, "underline") )
    info.goto(0, 0)
    info.write("By Jake Read", True, align = "center", font = ("Arial", 35, "underline") )
    info.goto(-350, -350)
    info.write("Beta v.1.4", font = ("Arial", 18, "normal") )


def instructions():
    turtle.hideturtle()
    
    info.clear()
    screen.bgcolor("white")
    info.color("black")
    info.penup()
    info.goto(0, 325)
    info.write("Instructions", True, align = "center", font = ("Arial", 35, "underline") )
    info.goto(-350, 275)
    info.write("- Press [s] to start spinning and [space] to stop.", font = ("Arial", 18, "normal") )
    info.goto(-350, 230)
    info.write("- When you start spinning you will be prompted for a bet. You", font = ("Arial", 18, "normal") )
    info.goto(-340, 200)
    info.write("start with $200 and can increase this by placing bets and winning.", font = ("Arial", 18, "normal") )


    ##Table

    #Table Info
    info.goto(0, 140)
    info.write("Payoff Table", True, align = "center", font = ("Arial", 18, "bold") )
    info.goto(-230, 100)
    info.write("Description           Examples        Payoff", font = ("Arial", 18, "bold") )
    info.goto(-275, 60)
    info.write("Three of a Kind                 4 4 4           10 x bet", font = ("Arial", 18, "normal") )
    info.goto(-275, 20)
    info.write("Outside Match                  4 5 4             3 x bet", font = ("Arial", 18, "normal") )
    info.goto(-275, -20)
    info.write("Side by Side Match           4 4 6             2 x bet", font = ("Arial", 18, "normal") )
    info.goto(9, -60)
    info.write("4 5 5", font = ("Arial", 18, "normal") )
    info.goto(-275, -100)
    info.write("Straight in Sequence        4 5 6             5 x bet", font = ("Arial", 18, "normal") )
    info.goto(9, -140)
    info.write("1 2 3", font = ("Arial", 18, "normal") )

    #Border
    info.goto(-290, 170)
    info.pendown()
    info.goto(-290, -145)
    info.goto(260, -145)
    info.goto(260, 170)
    info.goto(-290, 170)

    #Rows
    info.goto(-290, 135)
    info.goto(260, 135)
    info.goto(260, 95)
    info.goto(-290, 95)
    info.goto(-290, 55)
    info.goto(260, 55)
    info.goto(260, 15)
    info.goto(-290, 15)
    info.goto(-290, -65)
    info.goto(260, -65)

    #Columns
    info.penup()
    info.goto(-40, 135)
    info.pendown()
    info.goto(-40, -145)
    info.goto(110, -145)
    info.goto(110, 135)


    info.penup()
    info.goto(-350, -200)
    info.write("- You can quit at any time by entering 'quit' as a bet.", font = ("Arial", 18, "normal") )
    info.goto(-350, -240)
    info.write("- You can save your game by entering 'save' as a bet.", font = ("Arial", 18, "normal") )
    info.goto(0, -300)
    info.write("Press [space] to continue.", True, align = "center", font = ("Arial", 18, "bold") )


def load_save():
    global money
    
    load = tkinter.messagebox.askyesno("Load Game", "Do you want to load a previously saved game?")

    if load:
        not_valid = True

        while not_valid:
            file_name = tkinter.simpledialog.askstring("Load File", "Enter the name of your save file")
        
            try:
                load_file = open(file_name)    
                not_valid = False
                line = load_file.readline()
                money = float(line)
                load_file.close()
                
            except:
                print("hello")
                go_back = tkinter.messagebox.askyesno("Invalid File Name", "That file does not exist. Do you want to go back and start a new game?")
                
                if go_back:
                    not_valid = False

    screen.listen()
                    

def skip_instructions():
    global displaying

    displaying = False


def main_screen():
    global machine, info, handle, money

    info.clear()

    #Body
    machine.fillcolor("red3")
    machine.begin_fill()
    machine.penup()
    machine.goto(-250, -300)
    machine.pendown()
    machine.goto(-250, 250)
    machine.setheading(270)
    machine.circle(50, -90)
    machine.goto(200, 300)
    machine.setheading(180)
    machine.circle(50, -90)
    machine.goto(250, -300)
    machine.goto(-250, -300)
    machine.end_fill()

    machine.fillcolor("silver")
    machine.penup()
    machine.goto(-270, -300)
    machine.pendown()
    machine.begin_fill()
    machine.goto(270, -300)
    machine.goto(270, -350)
    machine.goto(-270, -350)
    machine.goto(-270, -300)
    machine.end_fill()

    #Number Area
    machine.fillcolor("black")
    machine.penup()
    machine.goto(-200, 200)
    machine.pendown()
    machine.begin_fill()
    machine.goto(200, 200)
    machine.goto(200, 0)
    machine.goto(-200, 0)
    machine.goto(-200, 200)
    machine.end_fill()

    machine.fillcolor("white")

    for a in range(-180, 180, 130):
        machine.penup()
        machine.goto(a, 180)
        machine.pendown()
        machine.begin_fill()
        machine.goto(a, 20)
        machine.goto(a + 100, 20)
        machine.goto(a + 100, 180)
        machine.goto(a, 180)
        machine.end_fill()

    #Decoration Strips
    machine.fillcolor("red")
    machine.penup()

    for b in range(-50, -250, -50):
        machine.goto(-180, b)
        machine.begin_fill()
        machine.goto(180, b)
        machine.goto(180, b - 30)
        machine.goto(-180, b - 30)
        machine.goto(-180, b)
        machine.end_fill()

    #Starting Numbers
    spin_one.goto(-148, 60)
    spin_one.write("7", font = ("Arial", 60, "normal") )
    spin_two.goto(-20, 60)
    spin_two.write("7", font = ("Arial", 60, "normal") )
    spin_three.goto(110, 60)
    spin_three.write("7", font = ("Arial", 60, "normal") )

    #Other Info
    info.penup()
    info.goto(-200, 350)
    info.write("Bank: ", font = ("Arial", 20, "normal") )
    info.goto(-200, 320)
    info.write("$" + '{0:.2f}'.format(money), font = ("Arial", 20, "normal") )

    info.goto(120, 350)
    info.write("Bet:", font = ("Arial", 20, "normal") )
    info.goto(120, 320)
    info.write("$0.00", font = ("Arial", 20, "normal") )
    
    

def draw_handle(orientation):
    global handle
    
    if orientation == "up":
        mult = 1

    elif orientation == "down":
        mult = -1

    handle.clear()

    handle.fillcolor("silver")
    handle.penup()
    handle.goto(250, 0)
    handle.pendown()
    handle.begin_fill()
    handle.goto(280, 0)
    handle.goto(280, 200 * mult)
    handle.goto(310, 200 * mult)
    handle.goto(310, -30 * mult)
    handle.goto(250, -30 * mult)
    handle.goto(250, 0)
    handle.end_fill()

    handle.fillcolor("black")
    handle.penup()
    handle.goto(295, 180 * mult)
    handle.pendown()

    if orientation == "down":
        handle.setheading(180)

    handle.begin_fill()
    handle.circle(30)
    handle.end_fill()
    handle.setheading(0)


def read_leaderboard():
    global names, top_ten
    
    names = []
    top_ten = []

    file = open("leaderboard.txt", "r")

    for a in range(10):
        line = file.readline()
        names.append(str(line.strip() ) )
        line = file.readline()
        top_ten.append(float(line.strip() ) )

    file.close()


def get_bet():
    global bet, money, not_done, saving
    
    not_valid = True

    while not_valid:
        bet = tkinter.simpledialog.askstring("Bet", "Please enter the amount you want to bet, 'Save' to save, or 'Quit' to exit:")

        try:
            bet = float(bet)
            
            if len(str(round(bet, 2) - bet) ) > 3:
                tkinter.messagebox.showerror("Invalid Input", "Please enter the bet size in basic format." + '\n' + "Ex. 22.43")

            elif bet <= 0:
                tkinter.messagebox.showerror("Invalid Input", "Please enter a value greater than 0.")

            elif money - bet < 0:
                tkinter.messagebox.showerror("Invalid Input", "Bet cannot be higher than current bank.")
            
            else:
                not_valid = False
                
        except:
            try:
                bet = bet.upper()

                if bet == "QUIT":
                    not_valid = False
                    not_done = False

                elif bet == "SAVE":
                    not_valid = False
                    saving = True

                else:
                    tkinter.messagebox.showerror("Invalid Input", "Please enter a number, 'Save', or 'Quit'.")

            except:            
                tkinter.messagebox.showerror("Invalid Input", "Please Enter a Value.")
            
        
    if bet != "QUIT" and bet != "SAVE":
        money = money - bet

        info.clear()
        
        info.goto(-200, 350)
        info.write("Bank: ", font = ("Arial", 20, "normal") )
        info.goto(-200, 320)
        info.write("$" + '{0:.2f}'.format(money), font = ("Arial", 20, "normal") )

        info.goto(120, 350)
        info.write("Bet:", font = ("Arial", 20, "normal") )
        info.goto(120, 320)
        info.write("$" + '{0:.2f}'.format(bet), font = ("Arial", 20, "normal") )
    

def spin_machine():
    global spin_one, spin_two, spin_three, space_pressed, slot_one, slot_two, slot_three, still_spinning

    slot_one = random.randint(1, 10)
    slot_two = random.randint(1, 10)
    slot_three = random.randint(1, 10)

    one_not_done = True
    two_not_done = True
    three_not_done = True
    
    spin_one.penup()
    spin_two.penup()
    spin_three.penup()

    a = 1
    b = 3
    c = 7
    
    still_spinning = True
    space_pressed = False

    screen.onkey(stop_spin, "space")
    screen.listen()

    while still_spinning:
        a = a + 1
        b = b + 1
        c = c + 1

        if a > 10:
            a = 1

        elif b > 10:
            b = 1

        elif c > 10:
            c = 1

        if two_not_done:
            spin_two.clear()

        if three_not_done:
            spin_three.clear()
            
        if one_not_done:
            spin_one.clear()
            spin_one.goto(-148, 60)

            if a == 10:
                spin_one.goto(-175, 60)
                spin_one.write("10", font = ("Arial", 60, "normal") )

            else:
                spin_one.write(str(a), font = ("Arial", 60, "normal") )

        if two_not_done:
            spin_two.goto(-20, 60)
            
            if b == 10:
                spin_two.goto(-45, 60)
                spin_two.write("10", font = ("Arial", 60, "normal") )

            else:
                spin_two.write(str(b), font = ("Arial", 60, "normal") )

        if three_not_done:
            spin_three.goto(110, 60)
            
            if c == 10:
               spin_three.goto(85, 60)
               spin_three.write("10", font = ("Arial", 60, "normal") )

            else:
                spin_three.write(str(c), font = ("Arial", 60, "normal") )
    
        if a == slot_one and space_pressed:
            one_not_done = False

        if b == slot_two and space_pressed:
            two_not_done = False

        if c == slot_three and space_pressed:
            three_not_done = False

        if one_not_done == False and two_not_done == False and three_not_done == False:
            still_spinning = False

        if space_pressed:
            time.sleep(0.2)

        else:
            time.sleep(0.1)
        

def stop_spin():
    global space_pressed

    space_pressed = True


def calc_winnings():
    global slot_one, slot_two, slot_three, bet, money, bankrupt, not_done, winnings

    if slot_one == slot_two == slot_three:
        winnings = bet * 10
        reason = "Three of a Kind!"

    elif slot_three - slot_two == 1 and slot_two - slot_one == 1:
        winnings = bet * 5
        reason = "Straight in Sequence!"

    elif slot_one == slot_three:
        winnings = bet * 3
        reason = "Outside Match!"

    elif slot_one == slot_two or slot_two == slot_three:
        winnings = bet * 2
        reason = "Side by Side Match!"

    else:
        winnings = 0
        tkinter.messagebox.showinfo("You Lost", "You didn't win anything this time.")

    money = money + winnings

    info.clear()
    
    info.goto(-200, 350)
    info.write("Bank: ", font = ("Arial", 20, "normal") )
    info.goto(-200, 320)
    info.write("$" + '{0:.2f}'.format(money), font = ("Arial", 20, "normal") )

    info.goto(120, 350)
    info.write("Bet:", font = ("Arial", 20, "normal") )
    info.goto(120, 320)
    info.write("$0.00", font = ("Arial", 20, "normal") )

    if winnings != 0:
        tkinter.messagebox.showinfo("You Won!", reason + '\n' + "Your Winnings: $" + '{0:.2f}'.format(winnings) )

    elif money <= 0:
        bankrupt = True
        not_done = False


def update_leaderboard():
    global winnings, names, top_ten

    if winnings > top_ten[9]:
        not_valid = True
        
        while not_valid:
            name = tkinter.simpledialog.askstring("You're on the Leaderboard!", "Please Enter Your Name in xxx format:")
            
            if len(name) != 3:
                tkinter.messagebox.showerror("Invalid Input", "Please use xxx format.")

            else:
                name = name.upper()
                not_valid = False
            
        top_ten[9] = winnings
        names[9] = name

        for b in range(9):
            for c in range(9):
                if top_ten[c] < top_ten[c + 1]:
                    temp = top_ten[c]
                    top_ten[c] = top_ten[c + 1]
                    top_ten[c + 1] = temp

                    temp = names[c]
                    names[c] = names[c + 1]
                    names[c + 1] = temp

    file = open("leaderboard.txt", "w")

    for d in range(10):
        file.write(names[d] + '\n')
        file.write(str(top_ten[d]) + '\n')

    file.close()

    screen.listen()
    

def start():
    global waiting

    waiting = False


def ask_play_again():
    global not_done, money, bankrupt
    
    ask_continue = tkinter.messagebox.askyesno("YOU ARE BANKRUPT!", "Do you want to play again?")

    if ask_continue:
        bankrupt = False
        not_done = True
        money = 200

        info.clear()
    
        info.goto(-200, 350)
        info.write("Bank: ", font = ("Arial", 20, "normal") )
        info.goto(-200, 320)
        info.write("$" + '{0:.2f}'.format(money), font = ("Arial", 20, "normal") )

        info.goto(120, 350)
        info.write("Bet:", font = ("Arial", 20, "normal") )
        info.goto(120, 320)
        info.write("$0.00", font = ("Arial", 20, "normal") )


def save_game():
    global money, saving
    
    not_valid = True

    while not_valid:
        file_name = tkinter.simpledialog.askstring("Save File Creation", "Enter the name of your save file:")

        if file_name != "leaderboard" and file_name != "leaderboard.txt":
            not_valid = False

        else:
            tkinter.messagebox.showinfo("Invalid File Name", "Wow, you found the rarest error message. Leaderboard is the only option that doesn't work.")

    save_file = open(file_name, 'w')
    save_file.write(str(money) )
    save_file.close()

    saving = False
    

def closing_screen():
    global image, names, top_ten
    
    machine.clear()
    handle.clear()
    spin_one.clear()
    spin_two.clear()
    spin_three.clear()
    info.clear()
    
    screen.bgpic(image)
    info.color("white")

    #Messages
    info.goto(0, 250)
    info.write("Thanks for Playing!", True, align = "center", font = ("Arial", 36, "bold", "underline") )

    info.goto(0, -260)
    info.write("Click to Exit", True, align = "center", font = ("Arial", 20, "underline") )
    

    ##Table

    #Table info
    info.goto(0, 160)
    info.write("Top Ten Winners", True, align = "center", font = ("Arial", 24, "bold") )
    info.goto(-125, 125)
    info.write("Name" , font = ("Arial", 20, "bold") )
    info.goto(35, 125)
    info.write("Winnings" , font = ("Arial", 20, "bold") )

    y_pos = 90

    for a in range(10):
        info.goto(-125, y_pos)
        info.write(names[a], font = ("Arial", 18, "normal") )
        info.goto(50, y_pos)
        info.write("$" + '{0:.2f}'.format(top_ten[a]), font = ("Arial", 18, "normal") )
        y_pos = y_pos - 30

    #Table Structure
    info.goto(-180, 200)
    info.pendown()
    info.goto(-180, -180)
    info.goto(190, -180)
    info.goto(190, 200)
    info.goto(-180, 200)

    info.goto(-180, 160)
    info.goto(190, 160)
    info.goto(190, 125)
    info.goto(-180, 125)
    info.penup()
    info.goto(0, -180)
    info.pendown()
    info.goto(0, 160)
        

## Main Program
turtle_setup()

money = 200
bet = 0
bankrupt = False
saving = False
still_spinning = True
waiting = True
not_done = True
displaying = True

title_screen()
time.sleep(3)

screen.clear()
instructions()

screen.onkey(skip_instructions, "space")
screen.onkey(start, "s")
screen.listen()

while displaying:
    turtle.goto(0, 0)

load_save()
main_screen()
draw_handle("up")

while not_done:
    while waiting:
        turtle.goto(0, 0)

    read_leaderboard()
    get_bet()
    
    if bet != "QUIT" and bet != "SAVE":
        draw_handle("down")
        time.sleep(1)
        draw_handle("up")
        spin_machine()
        calc_winnings()
        update_leaderboard()

        waiting = True

    if bankrupt:
        ask_play_again()

    if saving:
        save_game()

closing_screen()
turtle.exitonclick()
