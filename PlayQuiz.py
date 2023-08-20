import random
from QSN_Management import *
from tkinter import *




global quiztype

def saveuserchoice(OptionA,OptionB,OptionC,OptionD,questionno,userans):

    if chosen.get() == 'A':
        OptionB.deselect()
        OptionC.deselect()
        OptionD.deselect()
        OptionA.select()
        chosen.set('A')
        userans.update({qnolist[questionno.get()-1]:chosen.get()})

    if chosen.get() == 'B':
        OptionC.deselect()
        OptionA.deselect()
        OptionD.deselect()
        OptionB.select()
        chosen.set('B')
        userans.update({qnolist[questionno.get() - 1]: chosen.get()})

    if chosen.get() == 'C':
        OptionD.deselect()
        OptionA.deselect()
        OptionB.deselect()
        OptionC.select()
        chosen.set('C')
        userans.update({qnolist[questionno.get() - 1]: chosen.get()})


    if chosen.get() == 'D':
        OptionA.deselect()
        OptionB.deselect()
        OptionC.deselect()
        OptionD.select()
        chosen.set('D')
        userans.update({qnolist[questionno.get() - 1]: chosen.get()})

def startplay(gkframe,pzframe,quiztype):
    global mincount, qnolist, heading, questionno, questiondes, OptionA, OptionB, OptionC, OptionD, userans, anskey
    global beginbtn, chosen, nxtbtn, bckbtn, savebtn, playframe, qtype, qnoL2, heading, questiondes, questionno
    heading = StringVar()
    questiondes = StringVar()
    questionno = IntVar()
    chosen = StringVar()
    qtype = StringVar()
    userans = {}
    anskey = {}

    questiondes.set('')
    questionno.set(0)
    qnolist = []



    q1 = "select distinct qno from questions where subject = '{}'".format(quiztype)
    mycur.execute(q1)
    myrange = mycur.fetchall()
    # fetch list of questions from db
    for i in myrange:
        qnolist.append(i[0])

    # shuffle the question numbers
    random.shuffle(qnolist)

    # dictionary is stored with user answer values
    for i in range(len(qnolist)):
        userans[qnolist[i]] = 'X'


    if quiztype == 'gk':
        heading.set('GK ROUND')
        questionno.set(0)
        questiondes.set('')
        qtype.set('gk')

        buildplayingframe(gkframe,heading,questiondes,questionno)
        #print(gkframe)

    if quiztype == 'puzzle':
        heading.set('PUZZLE ROUND')
        qtype.set('puzzle')
        questionno.set(0)
        questiondes.set('')

        buildplayingframe(pzframe,heading,questiondes,questionno)
        #print(pzframe)



def buildplayingframe(playframe,heading,questiondes,questionno):

    if playframe is not None:
        playframe.pack()
        playframe.place()
        playframe.tkraise()

    qnoL1 = Label(playframe, text="Question No: ", bg='#0E2B41', fg='white',font=("ExoBlack",16))
    qnoL1.pack(side=LEFT)
    qnoL1.place(x=50, y=50)

    qnoL2 = Label(playframe, text='', textvariable=questionno,bg='#0E2B41', fg='white',font=("ExoBlack",16))
    qnoL2.pack(side=LEFT)
    qnoL2.place(x=170, y=50)

    qdesL2 = Label(playframe, textvariable=questiondes, bg='#0E2B41', fg='white',font=("ExoBlack",16),wraplength=700)
    qdesL2.pack(side=LEFT)
    qdesL2.place(x=50, y=100)

    OptionA = Radiobutton(playframe, text='', variable=chosen, value='A',bg='#0E2B41',fg='white',borderwidth=4,selectcolor='#0E2B41',command=lambda:saveuserchoice(OptionA,OptionB,OptionC,OptionD,questionno,userans),font=("ExoBlack",16))
    OptionA.pack(anchor=W)
    OptionA.place(x=90, y=200)

    OptionB = Radiobutton(playframe, text='', variable=chosen, value='B',bg='#0E2B41', fg='white',selectcolor='#0E2B41', command=lambda:saveuserchoice(OptionA,OptionB,OptionC,OptionD,questionno,userans),font=("ExoBlack",16))
    OptionB.pack(anchor=W)
    OptionB.place(x=90, y=250)

    OptionC = Radiobutton(playframe, text='', variable=chosen, value='C',bg='#0E2B41', fg='white', selectcolor='#0E2B41',command=lambda:saveuserchoice(OptionA,OptionB,OptionC,OptionD,questionno,userans),font=("ExoBlack",16))
    OptionC.pack(anchor=W)
    OptionC.place(x=90, y=300)

    OptionD = Radiobutton(playframe, text='', variable=chosen, value='D',bg='#0E2B41', fg='white', selectcolor='#0E2B41',command=lambda:saveuserchoice(OptionA,OptionB,OptionC,OptionD,questionno,userans),font=("ExoBlack",16))
    OptionD.pack(anchor=W)
    OptionD.place(x=90, y=350)

    OptionA.configure(text='')
    OptionB.configure(text='')
    OptionC.configure(text='')
    OptionD.configure(text='')


    nxtbtn = Button(playframe, text="Next", fg='blue', bg='yellow', height="1", width='10',font=("ExoBlack",16),command=lambda:viewnextquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,nxtbtn,bckbtn,beginbtn))
    nxtbtn.pack()
    nxtbtn.place(x=600, y=450)

    bckbtn = Button(playframe, text="Back", fg='blue', bg='yellow', height="1", width='10',font=("ExoBlack",16),command=lambda:viewprequestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,bckbtn,nxtbtn,beginbtn))
    bckbtn.pack()
    bckbtn.place(x=10, y=450)

    savebtn = Button(playframe, text="Save", fg='blue', bg='yellow', height="1", width='10',font=("ExoBlack",16),command=lambda:saveuseranswer())
    savebtn.pack()
    savebtn.place(x=300, y=450)



    exitbtn = Button(playframe,text="Exit", fg='blue', bg='yellow', height="1", width=10,font=("ExoBlack",16),command=lambda:exitproc3(playframe))
    exitbtn.pack()
    exitbtn.place(x=650, y=0)


    beginbtn = Button(playframe, text=heading.get(), fg='blue', bg='yellow', height="25", width='65',font=("ExoBlack",16),command=lambda:viewquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,beginbtn,bckbtn,nxtbtn))
    beginbtn.pack(anchor=CENTER)
    beginbtn.place(x=0, y=0)

def exitproc3(playframe):
    playframe.pack_forget()
    playframe.place_forget()

def viewnextquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,nxtbtn,bckbtn,beginbtn):
    beginbtn.place()


    if questionno.get() < len(qnolist):
        questionno.set(questionno.get() + 1)


    if questionno.get() >= 0 and questionno.get() <= len(qnolist):

        q1 = "select * from questions where qno={} and subject= '{}'".format(qnolist[questionno.get()-1], qtype.get())
        mycur.execute(q1)
        mydata = mycur.fetchone()
        questiondes.set('')
        questiondes.set(mydata[1])
        OptionA.configure(text=mydata[2], bg='#0E2B41', fg='white')
        OptionB.configure(text=mydata[3], bg='#0E2B41', fg='white')
        OptionC.configure(text=mydata[4], bg='#0E2B41', fg='white')
        OptionD.configure(text=mydata[5], bg='#0E2B41', fg='white')
        bckbtn.configure(text='Back')
        nxtbtn.configure(text='Next')

        chosen.set(userans.get(qnolist[questionno.get() - 1]))
        #print(userans.get(qnolist[questionno.get() - 1]))

    if questionno.get() == len(qnolist):
        nxtbtn.configure(text='Over')
        bckbtn.configure(text='Back')

def viewprequestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,bckbtn,nxtbtn,beginbtn):
    beginbtn.place()


    if questionno.get() > 1:
        questionno.set(questionno.get() - 1)


    if questionno.get() >= 0 and questionno.get() <= len(qnolist):

        q1 = "select * from questions where qno={} and subject= '{}'".format(qnolist[questionno.get()-1], qtype.get())
        mycur.execute(q1)
        mydata = mycur.fetchone()

        questiondes.set('')
        questiondes.set(mydata[1])
        OptionA.configure(text=mydata[2], bg='#0E2B41', fg='white')
        OptionB.configure(text=mydata[3], bg='#0E2B41', fg='white')
        OptionC.configure(text=mydata[4], bg='#0E2B41', fg='white')
        OptionD.configure(text=mydata[5], bg='#0E2B41', fg='white')
        bckbtn.configure(text='Back')
        nxtbtn.configure(text='Next')

        chosen.set(userans.get(qnolist[questionno.get() - 1]))
        #print(userans.get(qnolist[questionno.get() - 1]))

    if questionno.get() == 1:
        bckbtn.configure(text='Begin')
        nxtbtn.configure(text='Next')

def viewquestions(qnolist,questionno,questiondes,OptionA,OptionB,OptionC,OptionD,beginbtn,bckbtn,nxtbtn):
    questionno.set(1)
    beginbtn.place()
    beginbtn.configure(text=heading.get(), height="1", width='55')


    if questionno.get() >= 0 and questionno.get() <= len(qnolist):
        q1 = "select * from questions where qno={} and subject= '{}'".format(qnolist[questionno.get()-1],qtype.get())

        mycur.execute(q1)
        mydata = mycur.fetchone()

        questiondes.set('')
        questiondes.set(mydata[1])
        OptionA.configure(text=mydata[2],bg='#0E2B41', fg='white')
        OptionB.configure(text=mydata[3],bg='#0E2B41', fg='white')
        OptionC.configure(text=mydata[4],bg='#0E2B41', fg='white')
        OptionD.configure(text=mydata[5],bg='#0E2B41', fg='white')

        chosen.set(userans.get(qnolist[questionno.get() - 1]))
        #print(userans.get(qnolist[questionno.get() - 1]))

        bckbtn.configure(text='Back')
        nxtbtn.configure(text='Next')




def saveuseranswer():
    global writeline
    import pickle

# get the answer key from db
    for i in range(len(qnolist)):

        q2 = "select distinct qno,answerkey from questions where  qno = {}".format(qnolist[i])
        mycur.execute(q2)
        myrange2 = mycur.fetchone()
        # fetch list of answers from db
        anskey[myrange2[0]] = myrange2[1]

#anskey dictionary hold answers and userans dictionary holds user anwers. now compare and write the output to a file
    writetofile = []
    f = open("username.dat", "wb")

    for idx in range(len(userans)):

        if userans[qnolist[idx]] == anskey[qnolist[idx]]:
            writeline = [idx + 1, userans[qnolist[idx]], anskey[qnolist[idx]], 1]
        else:
            writeline = [idx + 1, userans[qnolist[idx]], anskey[qnolist[idx]], 0]

        writetofile.append(writeline)
    pickle.dump(writetofile, f)
    f.close()





