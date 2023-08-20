from tkinter import *
import mysql.connector as ms

# QSNAWindow = Toplevel
# QSNUWindow = Toplevel

mycon=ms.connect(host="localhost",user="root",password="Psbbkkn1*",database="vishranthdb")
if mycon.is_connected():
    print("successfully connected")
mycur=mycon.cursor()


def maxqsno():
    q = "select max(qno) from questions"
    mycur.execute(q)
    mydata = mycur.fetchone()
    return (mydata)


def viewdb():

    qnoI = qnoE.get()

    if qnoI == '':
        res = maxqsno()
        qnoI = res[0]

   # print(qnoI)
    q1 = "select * from questions where qno={}".format(qnoI)
    #print(q1)
    mycur.execute(q1)
    mydata = mycur.fetchone()
    print(mydata)

    qdesT1.insert("end-1c",mydata[1])
    optE1.insert(0, mydata[2])
    optE2.insert(0, mydata[3])
    optE3.insert(0, mydata[4])
    optE4.insert(0, mydata[5])
    akE.insert(0, mydata[6])
    subE.insert(0, mydata[7])

def sel():
    global repeat

    repeat = var.get()
    print(repeat)

    if repeat==1:
        qdesT1.delete("1.0", END)
        optE1.delete(0, END)
        optE2.delete(0, END)
        optE3.delete(0, END)
        optE4.delete(0,END)
        akE.delete(0, END)
        subE.delete(0, END)
        subrad2.deselect()
        subrad.select()
        msgbx.place(x=300, y=575)

    if repeat == 0:
        subrad.deselect()
        subrad2.select()

def update_screen(QSNUWindow):
    global qnoE, HeadL2, fetbtn

    global optE1, optE2, optE3, optE4, akE, subE, qdesT1, subrad, subrad2,var,qnoL2,msgbx,msg,qnoL2
    var = IntVar()


    if QSNUWindow is not None:
        QSNUWindow.pack()
        QSNUWindow.place()
        QSNUWindow.tkraise()

    HeadL2 = Label(QSNUWindow,text="Update a Question:)", bg='#0E2B41', fg='white')
    HeadL2.config(font=("ExoBlack",24))
    HeadL2.pack(side=LEFT)
    HeadL2.place(x=250, y=50)

    qnoE = Entry(QSNUWindow, bd=5, width=5)
    qnoE.pack()
    qnoE.place(x=90, y=100)


    fetbtn = Button(QSNUWindow, text="Get", fg='blue', bg='yellow', height="1", width=5, command=lambda:viewdb())
    fetbtn.pack()
    fetbtn.place(x=150, y=100)

    qnoL1 = Label(QSNUWindow, text="Question No: ", bg='#0E2B41', fg='white')
    qnoL1.pack(side=LEFT)
    qnoL1.place(x=0, y=100)


    # to enter question description
    qdesL1 = Label(QSNUWindow, text="Description : ", bg='#0E2B41', fg='white')
    qdesL1.pack(side=LEFT)
    qdesL1.place(x=0, y=150)

    qdesT1 = Text(QSNUWindow, width=30, height=17)
    qdesT1.pack(side=LEFT)
    qdesT1.place(x=70, y=150)

    # receive option A details
    optL1 = Label(QSNUWindow, text="Enter Option A :", bg='#0E2B41', fg='white')
    optL1.pack(side=LEFT)
    optL1.place(x=350, y=150)
    optE1 = Entry(QSNUWindow, bd=5, width=30)
    optE1.pack()
    optE1.place(x=500, y=150)

    # receive Option B details
    optL2 = Label(QSNUWindow, text="Enter Option B :", bg='#0E2B41', fg='white')
    optL2.pack(side=LEFT)
    optL2.place(x=350, y=200)
    optE2 = Entry(QSNUWindow, bd=5, width=30)
    optE2.pack()
    optE2.place(x=500, y=200)

    # receive Option C details
    optL3 = Label(QSNUWindow, text="Enter Option C :", bg='#0E2B41', fg='white')
    optL3.pack(side=LEFT)
    optL3.place(x=350, y=250)
    optE3 = Entry(QSNUWindow, bd=5, width=30)
    optE3.pack()
    optE3.place(x=500, y=250)

    # receive Option D details
    optL4 = Label(QSNUWindow, text="Enter Option D :", bg='#0E2B41', fg='white')
    optL4.pack(side=LEFT)
    optL4.place(x=350, y=300)
    optE4 = Entry(QSNUWindow, bd=5, width=30)
    optE4.pack()
    optE4.place(x=500, y=300)

    # receive Option answerkey details
    akL = Label(QSNUWindow, text="Enter Option answerkey :", bg='#0E2B41', fg='white')
    akL.pack(side=LEFT)
    akL.place(x=350, y=350)
    akE = Entry(QSNUWindow, bd=5, width=30)
    akE.pack()
    akE.place(x=500, y=350)

    # receive Option subject details
    subL = Label(QSNUWindow, text="Enter Option subject :", bg='#0E2B41', fg='white')
    subL.pack(side=LEFT)
    subL.place(x=350, y=400)
    subE = Entry(QSNUWindow, bd=5, width=30)
    subE.pack()
    subE.place(x=500, y=400)

    #Submit all the details of the question
    usubbtn = Button(QSNUWindow,text="Update", fg='blue', bg='yellow', height="1", width=10,command=updatetodb)
    usubbtn.pack()
    usubbtn.place(x=150, y=445)

    subYN = Label(QSNUWindow, text="Do you want to continue adding questions ? : ", bg='#0E2B41', fg='white')
    subYN.pack(side=LEFT)
    subYN.place(x=350, y=445)

    subrad = Radiobutton(QSNUWindow, text="Yes", variable=var, value=1, command=sel)
    subrad.pack(anchor=W)
    subrad.place(x=590, y=445)

    subrad2 = Radiobutton(QSNUWindow, text="No", variable=var, value=0, command=sel)
    subrad2.pack(anchor=W)
    subrad2.place(x=650, y=445)

    msg = StringVar()
    msgbx = Message(QSNUWindow, textvariable=msg, relief=RAISED, justify=CENTER, width=700, bg='red', fg='white')
    msgbx.pack()
    msgbx.place(x=300, y=575)

    exitbtn = Button(QSNUWindow,text="Exit", fg='blue', bg='yellow', height="1", width=5,font=("ExoBlack",12),command=lambda:exitproc2(QSNUWindow))
    exitbtn.pack()
    exitbtn.place(x=700, y=0)


def updatetodb():
    a = qnoE.get()
    b = qdesT1.get('1.0', 'end-1c')
    c = optE1.get()
    d = optE2.get()
    e = optE3.get()
    f = optE4.get()
    g = akE.get()
    h = subE.get()
    #print(a, b, c, d, e, f, g, h)
    if a != ' ' and b != '' and c != '' and d != '' and e != '' and f != '' and g != '' and h != '':
        q = "update questions set qsndescription ='{}', optionA = '{}', optionB = '{}', optionC = '{}', optionD = '{}', answerkey = '{}', subject = '{}' where qno={}".format(b,c,d,e,f,g,h,a)
        #print(q)
        mycur.execute(q)
        mycon.commit()
        msgbx.config(bg='green')
        subrad.deselect()
        subrad2.select()
        msg.set("updated Successfully")
        msgbx.pack()
        msgbx.place(x=300, y=475)


def addtodb():

    #find max no of questions
    res = maxqsno()
    a = res[0] + 1
    b=qdesT1.get('1.0', 'end-1c')
    c=optE1.get()
    d=optE2.get()
    e=optE3.get()
    f=optE4.get()
    g=akE.get()
    h=subE.get()
    #print(a,b,c,d,e,f,g,h)
    if b!='' and c!='' and d!='' and e!='' and f!='' and g!='' and h!='':
        q = "insert into questions(qno,qsndescription,optionA,optionB,optionC,optionD,answerkey,subject) values({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format( a, b, c, d, e, f, g, h)
        mycur.execute(q)
        mycon.commit()
        # find max no of questions
        res = maxqsno()
        a = res[0] + 1
        #print(a)
        qnoL2.config(text=a)
        msgbx.config(bg='green')
        subrad.deselect()
        subrad2.select()
        msg.set("Added Successfully")
        msgbx.pack()
        msgbx.place(x=300, y=475)
    else:
        msg.set("In complete question is not added")
        msgbx.pack()
        msgbx.place(x=300, y=475)

def exitproc(QSNAWindow):
    QSNAWindow.pack_forget()
    QSNAWindow.place_forget()

def exitproc2(QSNUWindow):
    QSNUWindow.pack_forget()
    QSNUWindow.place_forget()



def add_screen(QSNAWindow):

    global optE1, optE2, optE3, optE4, akE, subE, qdesT1, subrad, subrad2,var,a,qnoL2,msgbx,msg,qnoL2
    var = IntVar()

    # find max no of questions
    res = maxqsno()
    a = res[0] + 1

    if QSNAWindow is not None:
        QSNAWindow.pack()
        QSNAWindow.place()
        QSNAWindow.tkraise()

    HeadL = Label(QSNAWindow,text="Add a Question :)", bg='#0E2B41', fg='white',font=("ExoBlack",24))
    HeadL.pack(side=LEFT)
    HeadL.place(x=250, y=50)


    qnoL1 = Label(QSNAWindow, text="Question No.: ",bg='#0E2B41',fg='white')
    qnoL1.pack(side=LEFT)
    qnoL1.place(x=0, y=100)

    qnoL2 = Label(QSNAWindow, text=a,bg='#0E2B41',fg='white')
    qnoL2.pack(side=LEFT)
    qnoL2.place(x=70, y=100)

    #to enter question description
    qdesL1 = Label(QSNAWindow, text="Description : ",bg='#0E2B41',fg='white')
    qdesL1.pack(side=LEFT)
    qdesL1.place(x=0, y=150)

    qdesT1 = Text(QSNAWindow,width=30,height=17)
    qdesT1.pack(side=LEFT)
    qdesT1.place(x=70, y=150)

    #receive option A details
    optL1 = Label(QSNAWindow, text="Enter Option A :",bg='#0E2B41',fg='white')
    optL1.pack(side=LEFT)
    optL1.place(x=350, y=150)
    optE1 = Entry(QSNAWindow,bd=5,width=30)
    optE1.pack()
    optE1.place(x=500,y=150)

    #receive Option B details
    optL2 = Label(QSNAWindow, text="Enter Option B :",bg='#0E2B41',fg='white')
    optL2.pack(side=LEFT)
    optL2.place(x=350, y=200)
    optE2 = Entry(QSNAWindow,bd=5,width=30)
    optE2.pack()
    optE2.place(x=500,y=200)

    # receive Option C details
    optL3 = Label(QSNAWindow, text="Enter Option C :",bg='#0E2B41',fg='white')
    optL3.pack(side=LEFT)
    optL3.place(x=350, y=250)
    optE3 = Entry(QSNAWindow, bd=5, width=30)
    optE3.pack()
    optE3.place(x=500, y=250)

    # receive Option D details
    optL4 = Label(QSNAWindow, text="Enter Option D :",bg='#0E2B41',fg='white')
    optL4.pack(side=LEFT)
    optL4.place(x=350, y=300)
    optE4 = Entry(QSNAWindow, bd=5, width=30)
    optE4.pack()
    optE4.place(x=500, y=300)

    # receive Option answerkey details
    akL = Label(QSNAWindow, text="Enter Option answerkey :",bg='#0E2B41',fg='white')
    akL.pack(side=LEFT)
    akL.place(x=350, y=350)
    akE = Entry(QSNAWindow, bd=5, width=30)
    akE.pack()
    akE.place(x=500, y=350)

    # receive Option subject details
    subL = Label(QSNAWindow, text="Enter Option subject :",bg='#0E2B41',fg='white')
    subL.pack(side=LEFT)
    subL.place(x=350, y=400)
    subE = Entry(QSNAWindow, bd=5, width=30)
    subE.pack()
    subE.place(x=500, y=400)

    #Submit all the details of the question
    asubbtn = Button(QSNAWindow,text="Add", fg='blue', bg='yellow', height="1", width=10,command=addtodb)
    asubbtn.pack()
    asubbtn.place(x=150, y=445)


    subYN = Label(QSNAWindow, text="Do you want to continue adding questions ? : " ,bg='#0E2B41',fg='white')
    subYN.pack(side=LEFT)
    subYN.place(x=350, y=445)

    subrad = Radiobutton(QSNAWindow, text="Yes", variable=var, value=1, command=sel)
    subrad.pack(anchor=W)
    subrad.place(x=590, y=445)

    subrad2 = Radiobutton(QSNAWindow, text="No", variable=var, value=0, command=sel)
    subrad2.pack(anchor=W)
    subrad2.place(x=650, y=445)

    msg = StringVar()
    msgbx = Message(QSNAWindow, textvariable=msg, relief=RAISED,justify=CENTER,width=700,bg='red',fg='white')
    msgbx.pack()
    msgbx.place(x=300, y=575)

    exitbtn = Button(QSNAWindow,text="Exit", fg='blue', bg='yellow', height="1", width=5,font=("ExoBlack",12),command=lambda:exitproc(QSNAWindow))
    exitbtn.pack()
    exitbtn.place(x=700, y=0)






