from tkinter import *


def showuserresult(resframe):
    import pickle

    total = 0

    if resframe is not None:
        resframe.pack()
        resframe.place()
        resframe.tkraise()


    resheadL = Label(resframe,text="Quiz Result", bg='#0E2B41', fg='white',font=("ExoBlack",24))
    resheadL.pack(side=LEFT)
    resheadL.place(x=250, y=25)

    resT1 = Text(resframe,width=400,height=60,wrap=WORD,bg='#0E2B41',fg='white',font=("ExoBlack",12))
    resT1.pack(side=LEFT)
    resT1.place(x=0, y=70)
    resT1.insert("end-1c", '*********************************************************************************************************************')
    resT1.insert("end-1c", '\n')
    headline = ("%10s" %"Q.No", "%5s" %"*****","%15s" %"UserAnswer", "%5s" %"*****","%19s" %"CorrectAnswer", "%5s" %"*****","%10s" %'Scores')
    resT1.insert("end-1c",headline)
    resT1.insert("end-1c", '\n')
    resT1.insert("end-1c", '*********************************************************************************************************************')
    resT1.insert("end-1c", '\n')

    exitbtn = Button(resframe,text="Exit", fg='yellow', bg='#0E2B41', height="1", width=5,font=("ExoBlack",12),command=lambda:exitproc4(resframe))
    exitbtn.pack()
    exitbtn.place(x=700, y=0)


    f=open("username.dat","rb")
    res=pickle.load(f)
    for i in res:
        t = ("%14s" % i[0], "%5s" %"*****", "%25s" % i[1], "%5s" %"*****","%30s" % i[2], "%5s" %"*****","%15s" % i[3])
        resT1.insert("end-1c", t)
        resT1.insert("end-1c", '\n')
        total += int(t[6])
    f.close()
    resT1.insert("end-1c", '\n')
    resT1.insert("end-1c", 'Total Score is:')
    resT1.insert("end-1c", total)



def exitproc4(resframe):
    resframe.pack_forget()
    resframe.place_forget()



