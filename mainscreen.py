from Menu_Options import *


window = Tk()

background_image = PhotoImage(file=".\\Photos\\dailyquiz1.gif")
cv = Canvas(window,width=400, height=250)
cv.create_image(0,0, image=background_image, anchor='nw')
cv.pack(side='top', fill='both', expand='yes')
window.title('Quiz Project')
#geometry("window width x window height + position right + position down")

window.geometry('746x500+250+150')
window.positionfrom()
window.resizable(FALSE,FALSE)


btn=Button(window, text="Quiz Master", fg='blue', bg='yellow',height="1",width=15,command=lambda :show_Newscreen(window,"All"))
btn.pack()
btn.place(x=300, y=450)


window.mainloop()





