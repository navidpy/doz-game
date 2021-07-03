from tkinter import *
import tkinter.messagebox
#=========================================
window=Tk()
window.geometry("325x560")
window.title("dozzzzz")
window.resizable(False,False)
#========================================
x=[0,0,0,0,0,0,0,0]
o=[0,0,0,0,0,0,0,0]
playerOne=0
playerTwo=0
XO=["X","O","X","O","X","O","X","O","X","O","X"]
indexs=-1
number_play=0
#===============================================================================================
def won():
    global indexs, x, o, playerOne, playerTwo, number_play
    if 3 in x:
        x=[0,0,0,0,0,0,0,0]
        o=[0,0,0,0,0,0,0,0]
        indexs=-1
        playerOne+=1
        number_play = 0
        emtiaz()
        tkinter.messagebox.showinfo("X won !", f"{name1.get()} player won !!!!")
        game()
    elif 3 in o:
        x=[0,0,0,0,0,0,0,0]
        o=[0,0,0,0,0,0,0,0]
        indexs=0
        playerTwo+=1
        number_play = 0
        emtiaz()
        tkinter.messagebox.showinfo("O won !", f"{name2.get()} player won !!!!")
        game()
    elif number_play==9:
        x=[0,0,0,0,0,0,0,0]
        o=[0,0,0,0,0,0,0,0]
        indexs=-1
        number_play=0
        game()
def nobat():
    lblred1=Label(window,text="       " , fg="white" , bg="white" , font = ('tahoma' , 48 , "bold"))
    lblred1.place(x=170 ,y=25)
    if XO[indexs]=="X":
        nobat=Label(window,text=name2.get()[:6] , fg="white" , bg="red" , font = ('tahoma' , 25 , "bold"))
        nobat.place(x=170 ,y=44)
    elif XO[indexs]=="O":
        nobat=Label(window,text=name1.get()[:6] , fg="white" , bg="blue" , font = ('tahoma' , 25 , "bold"))
        nobat.place(x=170 ,y=44)
    lblyellow=Label(window,text="  " , fg="white" , bg="dark red" , font = ('tahoma' , 48 , "bold"))
    lblyellow.place(x=307 ,y=25)
def emtiaz():
    lblredname1=Label(window,text=name1.get()[:7]+" : "+str(playerOne), fg="white" , bg="blue" , font = ('tahoma' , 15 , "bold"))
    lblredname1.place(x=26 ,y=35)
    lblredname2=Label(window,text=name2.get()[:7]+" : "+str(playerTwo), fg="white" , bg="red" , font = ('tahoma' , 15 , "bold"))
    lblredname2.place(x=26 ,y=68)
def types(location):
    global indexs , x , o , playerOne , playerTwo,number_play
    indexs+=1
    number_play+=1
    if location=="1":
        if XO[indexs] == "X":
            x[0]+=1
            x[3]+=1
            x[6]+=1
        else:
            o[0]+=1
            o[3]+=1
            o[6]+=1
    elif location=="2":
        if XO[indexs] == "X":
            x[4]+=1
            x[0]+=1
        else:
            o[0]+=1
            o[4]+=1
    elif location=="3":
        if XO[indexs] == "X":
            x[0]+=1
            x[5]+=1
            x[7]+=1
        else:
            o[0]+=1
            o[5]+=1
            o[7]+=1
    elif location=="4":
        if XO[indexs] == "X":
            x[1]+=1
            x[3]+=1
        else:
            o[1]+=1
            o[3]+=1
    elif location=="5":
        if XO[indexs] == "X":
            x[4]+=1
            x[1]+=1
            x[6]+=1
            x[7]+=1
        else:
            o[4]+=1
            o[1]+=1
            o[6]+=1
            o[7]+=1
    elif location=="6":
        if XO[indexs] == "X":
            x[1]+=1
            x[5]+=1
        else:
            o[1]+=1
            o[5]+=1
    elif location=="7":
        if XO[indexs] == "X":
            x[3]+=1
            x[2]+=1
            x[7]+=1
        else:
            o[2]+=1
            o[3]+=1
            o[7]+=1
    elif location=="8":
        if XO[indexs] == "X":
            x[4]+=1
            x[2]+=1
        else:
            o[4]+=1
            o[2]+=1
    elif location=="9":
        if XO[indexs] == "X":
            x[2]+=1
            x[5]+=1
            x[6]+=1
        else:
            o[2]+=1
            o[5]+=1
            o[6]+=1
    #====================
    if 3 not in x and 3 not in o and number_play !=9:
        nobat()
    return XO[indexs]
def color(item):
    if item=="X":
        return "blue"
    else:
        return "red"
def heder():
    global playerOne,playerTwo,x,o,indexs,number_play
    playerTwo=0
    playerOne=0
    x=[0,0,0,0,0,0,0,0]
    o=[0,0,0,0,0,0,0,0]
    number_play = 0
    indexs=-1
    lblredwhite=Label(window,text="               " , fg="white" , bg="white" , font = ('tahoma' , 48 , "bold"))
    lblredwhite.place(x=18 ,y=25)
    nobat=Label(window,text=name1.get()[:6] , fg="white" , bg="blue" , font = ('tahoma' , 25 , "bold"))
    nobat.place(x=170 ,y=44)
    lblyellow=Label(window,text="  " , fg="white" , bg="dark red" , font = ('tahoma' , 48 , "bold"))
    lblyellow.place(x=307 ,y=25)
    start.destroy()
    game()
def  game():
    global l1 , l2,l3,l4 ,l5 ,l6 ,l7, l8 ,l9 ,again
    def l1():
        typ=types("1")
        lb1=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb1.place(x=43 ,y=155)
        won()
    def l2():
        typ=types("3")
        lb2=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb2.place(x=215 ,y=155)
        won()
    def l3():
        typ=types("2")
        lb3=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb3.place(x=128 ,y=155)
        won()
    def l4():
        typ=types("7")
        lb4=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb4.place(x=37 ,y=380)
        won()
    def l5():
        typ=types("9")
        lb5=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb5.place(x=215 ,y=380)
        won()
    def l6():
        typ=types("8")
        lb6=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb6.place(x=127 ,y=380)
        won()
    def l7():
        typ=types("4")
        lb7=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb7.place(x=39 ,y=267)
        won()
    def l8():
        typ=types("6")
        lb8=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb8.place(x=215 ,y=267)
        won()
    def l9():
        typ=types("5")
        lb9=Label(window,text=typ , fg=color(typ) , bg="yellow" , font = ('tahoma' , 56 , "bold"))
        lb9.place(x=128 ,y=267)
        won()

    lblyellow = Label(window, text="    ", fg="black", bg="black", font=('tahoma', 196, "bold"))
    lblyellow.place(x=37, y=155)
    lblyellow = Label(window, text="    ", fg="yellow", bg="yellow", font=('tahoma', 198, "bold"))
    lblyellow.place(x=279, y=155)
    lblreddark = Label(window, text=" ", fg="dark red", bg="dark red", font=('tahoma', 230, "bold"))
    lblreddark.place(x=305, y=130)

    emtiaz()
    #======================================================================================
    l1 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l1 , cursor='hand2' ,bg="yellow", bd=0)
    l1.place(x=37 , y=155)

    l2 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l2 , cursor='hand2' ,bg="yellow", bd=0)
    l2.place(x=210 , y=155)

    l3 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l3 , cursor='hand2' ,bg="yellow", bd=0)
    l3.place(x=123 , y=155)
    #===========================================================================
    l4 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l4 , cursor='hand2' ,bg="yellow", bd=0)
    l4.place(x=37 , y=380)

    l5 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l5 , cursor='hand2' ,bg="yellow", bd=0)
    l5.place(x=210 , y=380)

    l6 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l6 , cursor='hand2' ,bg="yellow", bd=0)
    l6.place(x=123 , y=380)
    #===========================================================================
    l7 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l7 , cursor='hand2' ,bg="yellow", bd=0)
    l7.place(x=37 , y=267)

    l8 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l8 , cursor='hand2' ,bg="yellow", bd=0)
    l8.place(x=210 , y=267)

    l9 = Button(window , text = "  " ,font = ('tahoma' , 35 , "bold") , fg= 'white'
    , command = l9 , cursor='hand2' ,bg="yellow", bd=0)
    l9.place(x=123 , y=267)
#======================================================================================================#
lblred=Label(window,text="   " , fg="red" , bg="dark red" , font = ('tahoma' , 345 , "bold"))
lblred.place(x=0 ,y=0)
lblyellow=Label(window,text="    " , fg="yellow" , bg="yellow" , font = ('tahoma' , 230 , "bold"))
lblyellow.place(x=18 ,y=130)
lblred1=Label(window,text=" " , fg="red" , bg="dark red" , font = ('tahoma' , 230 , "bold"))
lblred1.place(x=305 ,y=130)
lblred2=Label(window,text="               " , fg="black" , bg="black" , font = ('tahoma' , 48 , "bold"))
lblred2.place(x=18 ,y=25)
#================================================================
L1 = Label(window, text="player one : " ,font = ('tahoma' , 12 , "bold"),bg="blue",fg="white")
L1.place(x=23 , y=35)
name1=Entry(window , fg= 'blue', bd=4,font = ('tahoma' , 9 , "bold") )
name1.place(x=129, y=35)
L1 = Label(window, text="player two : " ,font = ('tahoma' , 12 , "bold"),bg="red",fg="white")
L1.place(x=23 , y=70)
name2=Entry(window , fg= 'red', bd=4,font = ('tahoma' , 9 , "bold") )
name2.place(x=129, y=70)
#==================================================================
again = Button(window , text = "  Again  " ,font = ('tahoma' , 12 , "bold")
    , command =heder  , cursor='hand2' ,bg="green", bd=6)
again.place(x=213 , y=513)
start = Button(window , text = "   Start   " ,font = ('tahoma' , 12 , "bold")
    , command = heder , cursor='hand2' ,bg="green", bd=6)
start.place(x=213 , y=513)

exit = Button(window , text = "    Exit    " ,font = ('tahoma' , 12 , "bold")
    , command = lambda:window.destroy() , cursor='hand2' ,bg="gray", bd=6)
exit.place(x=18 , y=513)
#===================================================================
window.mainloop()