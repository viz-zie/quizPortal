import random
import time
from QSN_Management import *
from tkinter import *


playwindow = Toplevel
global quiztype

def saveuserchoice():
    global choice

    choice = chosen.get()
    print(choice)

    if choice == 'A':
        OptionA.select()
        chosen.set('A')
        # OptionA.configure(selectcolor="RED")
        OptionB.deselect()
        OptionC.deselect()
        OptionD.deselect()



    if choice == 'B':
        OptionB.select()
        chosen.set('B')
        # OptionB.configure(selectcolor="RED")
        OptionC.deselect()
        OptionA.deselect()
        OptionD.deselect()


    if choice == 'C':
        OptionC.select()
        chosen.set('C')
        # OptionC.configure(selectcolor="RED")
        OptionD.deselect()
        OptionA.deselect()
        OptionB.deselect()


    if choice == 'D':
        OptionD.select()
        chosen.set('D')
        # OptionD.configure(selectcolor="RED")
        OptionA.deselect()
        OptionB.deselect()
        OptionC.deselect()



def startplay(playwindow,quiztype):
    global mincount, qnolist, heading, questionno, questiondes, OptionA, OptionB, OptionC, OptionD
    global beginbtn, chosen,nxtbtn,bckbtn,savebtn,playframe,qtype
    heading = StringVar()
    questiondes = StringVar()
    questionno = IntVar()
    chosen = StringVar()
    qtype = StringVar()

    questiondes.set('')
    questionno.set(0)

    qnolist = []

    # OptionA.place_forget()
    # OptionB.place_forget()
    # OptionC.place_forget()
    # OptionD.place_forget()

    q1 = "select distinct qno subject from questions where subject = '{}'".format(quiztype)
    print(q1)
    mycur.execute(q1)
    myrange = mycur.fetchall()

    for i in myrange:
        print(i[0])
        qnolist.append(i[0])

    random.shuffle(qnolist)

    if quiztype == 'gk':
        heading.set('GK ROUND')
        qtype.set('gk')
        gkframe = Frame(playwindow, height=500, width=745)
        gkframe.pack()
        gkframe.config(background='#0E2B41', takefocus=True)
        questionno.set(0)
        buildplayingframe(gkframe)

    if quiztype == 'puzzle':
        heading.set('PUZZLE ROUND')
        qtype.set('puzzle')
        pzframe = Frame(playwindow, height=500, width=745)
        pzframe.pack()
        pzframe.config(background='#0E2B41', takefocus=True)
        questionno.set(0)
        buildplayingframe(pzframe)



def buildplayingframe(playframe):

    HeadL = Label(playframe, textvariable=heading, bg='#0E2B41', fg='white')
    HeadL.config(font=("ExoBlack", 24))
    HeadL.pack(side=LEFT)
    HeadL.place(x=250, y=50)

    qnoL1 = Label(playframe, text="Question No: ", bg='#0E2B41', fg='white',font=("ExoBlack",16))
    qnoL1.pack(side=LEFT)
    qnoL1.place(x=50, y=100)

    qnoL2 = Label(playframe, textvariable=questionno, bg='#0E2B41', fg='white',font=("ExoBlack",16))
    qnoL2.pack(side=LEFT)
    qnoL2.place(x=170, y=100)

    qdesL2 = Label(playframe, textvariable=questiondes, bg='#0E2B41', fg='white',font=("ExoBlack",16))
    qdesL2.pack(side=LEFT)
    qdesL2.place(x=50, y=150)

    OptionA = Radiobutton(playframe, text='', variable=chosen, value='A',command=lambda:saveuserchoice(),font=("ExoBlack",16))
    OptionA.pack(anchor=W)
    OptionA.place(x=90, y=200)

    OptionB = Radiobutton(playframe, text='', variable=chosen, value='B', command=lambda:saveuserchoice(),font=("ExoBlack",16))
    OptionB.pack(anchor=W)
    OptionB.place(x=90, y=250)

    OptionC = Radiobutton(playframe, text='', variable=chosen, value='C', command=lambda:saveuserchoice(),font=("ExoBlack",16))
    OptionC.pack(anchor=W)
    OptionC.place(x=90, y=300)

    OptionD = Radiobutton(playframe, text='', variable=chosen, value='D', command=lambda:saveuserchoice(),font=("ExoBlack",16))
    OptionD.pack(anchor=W)
    OptionD.place(x=90, y=350)

    OptionA.configure(text='')
    OptionB.configure(text='')
    OptionC.configure(text='')
    OptionD.configure(text='')


    nxtbtn = Button(playframe, text="Next", fg='blue', bg='yellow', height="1", width='10',font=("ExoBlack",16),command=lambda:viewnextquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,nxtbtn,bckbtn))
    nxtbtn.pack()
    nxtbtn.place(x=600, y=450)

    bckbtn = Button(playframe, text="Back", fg='blue', bg='yellow', height="1", width='10',font=("ExoBlack",16),command=lambda:viewprequestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,bckbtn,nxtbtn))
    bckbtn.pack()
    bckbtn.place(x=10, y=450)

    savebtn = Button(playframe, text="Save", fg='blue', bg='yellow', height="1", width='10',font=("ExoBlack",16),command=lambda:saveuseranswer(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,savebtn))
    savebtn.pack()
    savebtn.place(x=300, y=450)

    beginbtn = Button(playframe, text="Begin", fg='blue', bg='yellow', height="1", width='18',font=("ExoBlack",16),command=lambda:viewquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,beginbtn,bckbtn,nxtbtn))
    beginbtn.pack()
    beginbtn.place(x=0, y=100)

def viewnextquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,nxtbtn,bckbtn):
    if questionno.get() != len(qnolist):
        questionno.set(questionno.get() + 1)

    if questionno.get() >= 0 and questionno.get() < len(qnolist):
        print('hi')
        q1 = "select * from questions where qno={} and subject= '{}'".format(qnolist[questionno.get()], qtype.get())
        print(q1)
        mycur.execute(q1)
        mydata = mycur.fetchone()

        questiondes.set(mydata[1])
        OptionA.configure(text=mydata[2], bg='#0E2B41', fg='white')
        OptionB.configure(text=mydata[3], bg='#0E2B41', fg='white')
        OptionC.configure(text=mydata[4], bg='#0E2B41', fg='white')
        OptionD.configure(text=mydata[5], bg='#0E2B41', fg='white')
        bckbtn.configure(text='Back')
        nxtbtn.configure(text='Next')

    if questionno.get() == len(qnolist):
        print('end of questions')
        nxtbtn.configure(text='Over')
        bckbtn.configure(text='Back')

def viewprequestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,bckbtn,nxtbtn):
    if questionno.get() != 0:
        questionno.set(questionno.get() - 1)

    if questionno.get() >= 0 and questionno.get() < len(qnolist):
        print('hi')
        q1 = "select * from questions where qno={} and subject= '{}'".format(qnolist[questionno.get()], qtype.get())
        print(q1)
        mycur.execute(q1)
        mydata = mycur.fetchone()

        questiondes.set(mydata[1])
        OptionA.configure(text=mydata[2], bg='#0E2B41', fg='white')
        OptionB.configure(text=mydata[3], bg='#0E2B41', fg='white')
        OptionC.configure(text=mydata[4], bg='#0E2B41', fg='white')
        OptionD.configure(text=mydata[5], bg='#0E2B41', fg='white')
        bckbtn.configure(text='Back')
        nxtbtn.configure(text='Next')

    if questionno.get() == 0:
        print('begin questions')
        bckbtn.configure(text='Begin')
        nxtbtn.configure(text='Next')

def viewquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,beginbtn,bckbtn,nxtbtn):
    print('begin')
    print(questionno.get())
    questionno.set(0)
    if questionno.get() >= 0 and questionno.get() < len(qnolist):
        q1 = "select * from questions where qno={} and subject= '{}'".format(qnolist[questionno.get()],qtype.get())
        print(q1)
        mycur.execute(q1)
        mydata = mycur.fetchone()
        print(mydata)
        questiondes.set(mydata[1])
        OptionA.configure(text=mydata[2],bg='#0E2B41', fg='white')
        OptionB.configure(text=mydata[3],bg='#0E2B41', fg='white')
        OptionC.configure(text=mydata[4],bg='#0E2B41', fg='white')
        OptionD.configure(text=mydata[5],bg='#0E2B41', fg='white')
        beginbtn.place_forget()
        bckbtn.configure(text='Back')
        nxtbtn.configure(text='Next')

def saveuseranswer(qnolist, questionno, questiondes, OptionA, OptionB, OptionC, OptionD, savebtn):
    pass


    # Timercnt = Label(Playwindow, text=mincount)
    # Timercnt.pack(side=TOP, anchor='nw')
    # Timercnt.place(x=470, y=100)
    #
    # for i in range(5, 0, -1):
    #     mincount = i
    #     time.sleep(1)

