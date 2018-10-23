import tkinter
import random
import math
import time
import timeit
from tkinter import *
from tkinter import ttk
from pygame import mixer  # Load the required libraries

root = Tk()
mixer.init()
mixer.music.load('sss.mp3')
mixer.music.play()
root.title("LEARN THAT NUMBER by Зламана Кабіна ")
root.geometry("740x440")
root.configure(background='green')


def preintro():
    """
    Creates starting screen with the chosen specifications.
    e.g.740x440 extension, team logo, etc.
    """
    root.geometry("740x370")
    intfr = Frame(root, bg="black")
    intfr.pack()
    photo = PhotoImage(file="rrr.gif")
    w = Label(root, image=photo, bg="green")
    w.photo = photo
    w.pack()

    def intro():
        """
        Creates starting buttons with the chosen specifications.
        e.g. "Start!" button, "How to play" button, etc.
        """
        start = Button(
            intfr,
            width=91,
            height=3,
            text="Start!",
            bg="yellow",
            command=lambda: [
                intfr.pack_forget(),
                w.pack_forget(),
                mainbody()])
        start.grid(columnspan=4, row=0)
        rules = Button(
            intfr,
            width=45,
            bg="green",
            text="How to play",
            command=rulesf)
        rules.grid(column=0, columnspan=2, row=1)
        help = Button(
            intfr,
            width=45,
            bg="green",
            text="Help with numbers",
            command=intro_help)
        help.grid(column=2, columnspan=2, row=1)

        docum = Text(intfr, width="73", height="5")
        docum.grid(columnspan=4, row=4)
        docum.insert(
            END, "Welcome! 'Зламана кабіна Entertainment' presents \nthe\
 new revolutionary game 'Learn That Number' for number learning. \nEnjoy your\
 game and do not cheat.")

    def intro_help():
        """
        Creates four buttons on the second screen
        e.g. "Ulam numbers" button, "DO NOT PRESS THIS!" button, etc.
        """
        ulhe = Button(
            intfr,
            width=22,
            bg="white",
            text="Ulam numbers",
            command=ulhelp)
        luhe = Button(
            intfr,
            width=21,
            bg="white",
            text="Happy numbers",
            command=luhelp)
        prim = Button(
            intfr,
            width=21,
            bg="white",
            text="Prime numbers",
            command=prhelp)
        easter_egg = Button(
            intfr,
            width=22,
            bg="white",
            text="DO NOT PRESS THIS!",
            fg="red",
            command=lambda: [
                intfr.pack_forget(),
                easter(),
                w.pack_forget()])
        ulhe.grid(column=0, row=3)
        luhe.grid(column=1, row=3)
        prim.grid(column=2, row=3)
        easter_egg.grid(column=3, row=3)
        docum = Text(intfr, width="73", height="5")
        docum.grid(columnspan=4, row=4)
        docum.insert(
            END, "Choose the type of number to get an explanation.\n \n \n\
Just do not press that forbidden button!")

    def luhelp():
        """
        Creates documentation page which helps with happy numbers
        """
        docum = Text(intfr, width="73", height="5")
        docum.grid(columnspan=4, row=4)
        docum.insert(
            END, "A happy number is defined by the following process: \
Starting with any\npositive integer, replace the number by the sum of the \
squares of its\ndigits in base-ten, and repeat the process until the number \
either\nequals 1 (where it will stay), or it loops endlessly in a cycle\
\nthat does not include 1. Ex: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49.")

    def prhelp():
        """
        Creates documentation page which helps with prime numbers
        """
        docum = Text(intfr, width="73", height="5")
        docum.grid(columnspan=4, row=4)
        docum.insert(END, "When a number has only two factors it is\
 called a prime number. \nHere are the first few prime numbers: 2, 3, 5, 7,\
 11, 13, 17, 19, 23,\n29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,\
 89, 97.")

    def ulhelp():
        """
        Creates documentation page which helps with Ulam's numbers
        """
        docum = Text(intfr, width="73", height="5")
        docum.grid(columnspan=4, row=4)
        docum.insert(
            END, "Ulam sequence starts with  1 and 2. Then it is defined\
to be the\nsmallest integer that is the sum of two distinct earlier\
terms in\nexactly one way and larger than all earlier terms. 3 is an Ulam \
number\n(1+2); and 4 is an Ulam number (1+3). Ex: 1, 2, 3, 4, 6, 8, 11, 13, \
16,\n18, 26, 28, 36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102.")

    def rulesf():
        """
        Creates general documentation page which helps you start the game
        """
        docum = Text(intfr, width="73", height="5")
        docum.grid(columnspan=4, row=4)
        docum.insert(END,
                     "When you click the `start` button, the game will start\n\
The game lasts 60 seconds. If you beat the previous record, then it \
will be erased and the new record will be set.\n\
Try to guess as many numbers as you can. \
Each failure costs some points, so be careful!")

    def easter():
        """
        Creates the screen-size photo, which appears after pressing the
        "DO NOT PRESS THIS!" button
        """
        mixer.music.stop()
        root.attributes('-fullscreen', True)
        photo = PhotoImage(file="www.gif")
        w = Label(root, image=photo, bg="green")
        w.photo = photo
        w.pack()
    intro()


def mainbody():
    """
    Main function that runs when player starts the game with numbers.
    Sets time limit to 60 seconds.
    Starts counting shots, misses, intargets, points.
    Includes 3 functions-generators.
    Makes buttons needed to return to the menu,
    to start again and to choose numbers,
    according to what number the game asks to find.
    """
    Starttime = time.time()
    shots = [0]
    miss = [0]
    intarget = [0]
    poi = [0]
    curt = [1]
    import math
    from math import sqrt

    def generator_of_numbers():
        """
        General function that contains 3 functions-generators.

        Returns three lists - happy, prime and Ulam numbers
        with maximum number ~100

        (None) -> (list, list, list)
        """
        def generate_ulams():
            """
            Returns Ulam numbers limited by 100

            (None) -> list
            """
            ulams = [1, 2]
            limit = 100
            sums = [0 for i in range(2*limit)]
            newUlam = 2
            sumIndex = 1

            while(newUlam < limit):
                for i in ulams:
                    if (i < newUlam):
                        sums[i + newUlam] += 1
                while(sums[sumIndex] != 1):
                    sumIndex += 1
                newUlam = sumIndex
                sumIndex += 1
                ulams.append(newUlam)

            return ulams

        def ishappy(n):
            """
            Checks whether n is a happy number or no

            (number) -> bool

            >>> ishappy(1)
            True
            >>> ishappy(7)
            True
            >>> ishappy(5)
            False
            """
            cache = []
            while n != 1:
                n = sum(int(i)**2 for i in str(n))
                if n in cache:
                    return False
                cache.append(n)
            return True

        def isprime(n):
            """
            Checks whether n is prime number or no

            (number) -> bool

            >>> isprime(2)
            True
            >>> isprime(5)
            True
            >>> isprime(4)
            False
            """
            if n == 2 or n == 1:
                return True
            elif n < 2 or n % 2 == 0:
                return False
            else:
                for i in range(3, int(sqrt(n)+1), 2):
                    if n % i == 0:
                        return False
                return True

        happies = []
        primes = []
        ulams = generate_ulams()

        for i in range(1, 101):
            if ishappy(i):
                happies.append(i)

        for i in range(1, 106):
            if isprime(i):
                primes.append(i)

        return happies, primes, ulams

    ulam = generator_of_numbers()[2]
    lucky = generator_of_numbers()[0]
    prime = generator_of_numbers()[1]
    hum = []
    for q in ulam:
        hum.append(q)
    for w in lucky:
        hum.append(w)
    for e in prime:
        hum.append(e)
    root.geometry("800x327")
    Forehead = Frame(
        root,
        bg="green",
        highlightbackground="black",
        highlightcolor="black",
        width=500,
        height=100)
    Forehead.pack(expand=NO, fill=BOTH)
    Bottomf = Frame(
        root,
        bg="green",
        highlightbackground="green",
        highlightcolor="green",
        width=500,
        height=300)
    Bottomf.pack(expand=YES, fill=BOTH)
    photo = PhotoImage(file="rrr.gif")
    w = Label(Bottomf, image=photo, bg="green")
    w.photo = photo
    w.grid(row=1, columnspan=8)
    Timer = Button(
        Forehead,
        text="Try again",
        width=12,
        bg="yellow",
        fg="black",
        command=lambda: [
            tryagain(),
            mainbody()])
    Task = Label(
        Forehead,
        text="Prime number",
        width=20,
        foreground="black",
        bg="gray",
        bd="3",
        highlightbackground="black",
        highlightthickness="10",
        highlightcolor="black")
    Points = Label(
        Forehead,
        text=(
            "Points:",
            0),
        highlightbackground="black",
        width=15,
        bg="black",
        fg="white")
    Shots = Label(
        Forehead,
        text=(
            "Shots:",
            shots[0]),
        highlightbackground="black",
        width=15,
        bg="black",
        fg="white")
    Intarget = Label(
        Forehead,
        text=(
            "Intarget:",
            intarget[0]),
        highlightbackground="black",
        width=15,
        bg="black",
        fg="white")
    Misses = Label(
        Forehead,
        text=(
            "Misses:",
            miss[0]),
        highlightbackground="black",
        width=10,
        bg="black",
        fg="white")
    Tomenu = Button(
        Forehead,
        text="Back to menu",
        width=12,
        bg="yellow",
        fg="black",
        command=lambda: [
            tryagain(),
            preintro()])

    def simprand():
        """
        Ends game when player reached 60 secs.
        Generates random number's name among three that player has to find.
        Adds points accordingly to what number was guessed and subtracts points
        if the number guessed was wrong.
        Chooses random number from three lists
        of numbers (Happies, Primes, Ulams).
        """
        if time.time() > Starttime + 60:
            endofgame()
        else:
            a = int(random.randrange(0, 3))
            sum = 0
            if a == 1:
                Task['text'] = "Prime number"
                curt.clear()
                curt.append(1)
            elif a == 2:
                Task['text'] = "Ulam number"
                curt.clear()
                curt.append(0)
            else:
                Task['text'] = "Happy number"
                curt.clear()
                curt.append(2)

            b1['text'] = int(random.randrange(1, 101))
            if b1['text'] in ulam:
                sum += 1
            b2['text'] = int(random.randrange(1, 101))
            if b2['text'] in hum:
                sum += 1
            b3['text'] = int(random.randrange(1, 101))
            if b3['text'] in ulam:
                sum += 1
            b4['text'] = int(random.randrange(1, 101))
            if b4['text'] in lucky:
                sum += 1
            b5['text'] = int(random.randrange(1, 101))
            if b5['text'] in prime:
                sum += 1
            b6['text'] = int(random.randrange(1, 101))
            if b6['text'] in hum:
                sum += 1
            b7['text'] = int(random.randrange(1, 101))
            if b7['text']in prime:
                sum += 1
            b8['text'] = int(random.randrange(1, 101))
            if b8['text'] in hum:
                sum += 1
            if sum < 3:
                simprand()

    def but(text):
        """
        Counts points, checks whether the chosen number is right for the task.
        """
        p = -1
        u = -1
        l = -1
        text = int(text)
        if text in prime:
            p = 1
        if text in ulam:
            u = 0
        if text in lucky:
            l = 2
        if p == curt[0] or u == curt[0] or l == curt[0]:
            shots[0] = shots[0] + 1
            poi[0] = round(poi[0] + (1 * 1 + abs((poi[0] / shots[0]))), 2)
            Points['text'] = ("Points:", int(poi[0] * 100))
            Shots['text'] = ("Shots:", shots[0])
            intarget[0] = intarget[0] + 1
            Intarget['text'] = ("Intarget:", intarget[0])
        else:
            shots[0] = shots[0] + 1
            poi[0] = round(poi[0] - (1 * 1 - abs((poi[0] / shots[0]))), 2)
            Points['text'] = ("Points:", int(poi[0] * 100))
            Shots['text'] = ("Shots:", shots[0])
            miss[0] = miss[0] + 1
            Misses['text'] = ("Misses:", miss[0])
        simprand()

    def tryagain():
        """
        Allows player to discard his current points and start the game again.
        """
        Forehead.pack_forget()
        Bottomf.pack_forget()

    b1 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b1['text'])])
    b1.grid(column=0, row=0)
    b2 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b2['text'])])
    b2.grid(column=1, row=0)
    b3 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b3['text'])])
    b3.grid(column=2, row=0)
    b4 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b4['text'])])
    b4.grid(column=3, row=0)
    b5 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b5['text'])])
    b5.grid(column=4, row=0)
    b6 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b6['text'])])
    b6.grid(column=5, row=0)
    b7 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b7['text'])])
    b7.grid(column=6, row=0)
    b8 = Button(Bottomf, width=10, text=int(
        random.randrange(0, 101)), command=lambda: [but(b8['text'])])
    b8.grid(column=7, row=0)
    Task.grid(column=0, row=0)
    Timer.grid(column=1, row=0)
    Tomenu.grid(column=2, row=0)
    Points.grid(column=3, row=0)
    Shots.grid(column=4, row=0)
    Intarget.grid(column=5, row=0)
    Misses.grid(column=6, row=0)

    def endofgame():
        """
        Collects player's data about highscores
        """
        tryagain()
        res = round(poi[0] * 100, 0)
        p = ""
        f = open('records.txt', 'r')
        for u in f:
            p += u
        f = open('records.txt', 'r+')
        if float(res) > float(p):
            f.write(str(res))
            f.close()
        f = open('records.txt', 'r')
        p = ""
        for u in f:
            p += u
        f.close()
        p = int(float(p))

        Endl = Frame(root, bg="green")
        Endl.pack()

        photo = PhotoImage(file="rrr.gif")
        w = Label(Endl, image=photo, bg="yellow")
        w.photo = photo
        Result = Label(Endl, width=93, text=("Your", "points:", int(res)))
        Record = Label(Endl, width=93, text=("Record:", p))
        Backtomenu = Button(
            Endl,
            width=93,
            text="Back to menu",
            bg="yellow",
            command=lambda: [
                btm()])
        Result.pack()
        Record.pack()
        Backtomenu.pack()
        w.pack()

        def btm():
            """
            Returns player to the starting screen.
            """
            root.geometry("740x370")
            Endl.pack_forget()
            preintro()


preintro()   # starts the game window

root.mainloop()   # starts main functions of the game

