
from PlayQuiz import *
from USERRESULT import *
global newWindow,usertype,QSNAWindow,QSNUWindow,playwindow,resframe
global menubar, playmenu, usermenu, questionmenu, Reportmenu, subjecttype



def show_Newscreen(window,usertype):
    # Toplevel object which will
    # be treated as a new window, 0E2B41

    newWindow = Toplevel(window)
    newWindow.config(background='#0E2B41', takefocus=True)
    window.iconify()

    # background_image = PhotoImage(file=".\\Photos\\introscreen2.gif")
    # img1 = background_image.subsample(2000, 2000)
    #
    # cv1 = Canvas(newWindow, width=40, height=25)
    # cv1.create_image(0, 0, image=img1, anchor='nw')
    # cv1.pack(side='top', fill='both', expand='yes')
    # cv1.place()


    QSNAWindow = Frame(newWindow, height=500, width=745,background='#0E2B41', takefocus=True)
    QSNAWindow.pack()
    QSNAWindow.place()
    QSNAWindow.pack_forget()
    QSNAWindow.place_forget()


    QSNUWindow = Frame(newWindow, height=500, width=745,background='#0E2B41', takefocus=True)
    QSNUWindow.pack()
    QSNUWindow.place()
    QSNUWindow.pack_forget()
    QSNUWindow.place_forget()


    gkframe = Frame(newWindow, height=500, width=745,background='#0E2B41', takefocus=True)
    gkframe.pack()
    gkframe.place()
    gkframe.pack_forget()
    gkframe.place_forget()


    pzframe = Frame(newWindow, height=500, width=745,background='#0E2B41', takefocus=True)
    pzframe.pack()
    pzframe.place()
    pzframe.pack_forget()
    pzframe.place_forget()

    resframe = Frame(newWindow, height=500, width=745,background='#0E2B41', takefocus=True)
    resframe.pack()
    resframe.place()
    resframe.pack_forget()
    resframe.place_forget()


    # sets the title of the
    # Toplevel widget
    newWindow.title("Menu options")
    # sets the geometry of toplevel
    newWindow.geometry('746x500+250+150')
    newWindow.positionfrom()
    newWindow.resizable(TRUE, TRUE)

    menubar = Menu(newWindow)
    newWindow.config(menu=menubar)
    playmenu = Menu(menubar)
    menubar.add_cascade(label='Start Playing', menu=playmenu)
    playmenu.add_radiobutton(label='General Knowledge',command=lambda:startplay(gkframe,pzframe,"gk"))
    playmenu.add_radiobutton(label='Puzzle',command=lambda:startplay(gkframe,pzframe,"puzzle"))
    playmenu.add_separator()
    playmenu.add_command(label='Exit', command=newWindow.quit)
    questionmenu = Menu(menubar)
    menubar.add_cascade(label='Question Management', menu=questionmenu)
    questionmenu.add_command(label='Add New Question',command=lambda:add_screen(QSNAWindow))
    questionmenu.add_command(label='Update Existing Questions',command=lambda:update_screen(QSNUWindow))
    questionmenu.add_separator()
    Reportmenu = Menu(menubar)
    menubar.add_cascade(label='Player Report', menu=Reportmenu)
    Reportmenu.add_command(label='Your Score',command=lambda:showuserresult(resframe))
    Reportmenu.add_separator()
    Reportmenu.add_command(label='Exit', command=newWindow.quit)

    questionmenu.add_command(label='Exit', command=newWindow.quit)
    abtmenu = Menu(menubar)
    menubar.add_cascade(label='About', menu=abtmenu)
    abtmenu.add_command(label='A simple dynamic database application to set the  question paper and students can take tests')

    if usertype == "All":
        menubar.entryconfig("Start Playing", state="normal")
        menubar.entryconfig("Question Management", state="normal")
        menubar.entryconfig("Player Report", state="normal")






