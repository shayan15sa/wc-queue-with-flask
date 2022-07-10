import time
from tkinter import *
from tkinter import messagebox
from functools import partial
from turtle import color



f = ("Arial",370)

ws = Tk()
ws.geometry("1280x720")
ws.title("Timer")
ws.config(bg='#345')

#hour=StringVar()
minute=StringVar()
second=StringVar()
#hour.set("00")
minute.set("00")
second.set("00")

# hour_tf= Entry(
# 	ws, 
# 	width=2, 
# 	font=f,
# 	textvariable=hour
# 	)

# hour_tf.place(x=80,y=290)

mins_tf= Label(
	ws, 
	width=2, 
	font=f,
	textvariable=minute)

mins_tf.place(x=20,y=50)

sec_tf = Label(
	ws, 
	width=2, 
	font=f,
	textvariable=second)

sec_tf.place(x=650,y=50)
def finsh():
    messagebox.showinfo("", "Time's Up")
    return messagebox.askyesno("is Next person ready?","Are you ready next person?")
n_s = StringVar()
n_s.set("MR & MS")
n_l = Label(ws,font=35,textvariable=n_s,bg='#345',fg="white")
n_l.place(x=630,y=10)

def startCountdown(min,sec,name):
    n_s.set(name)
    messagebox.showwarning("ARE YOU READY?","Press OK to start")
    userinput = int(min)*60 + int(sec)
    while userinput >-1:
        mins,secs = divmod(userinput,60) 
	
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

	
        ws.update()
        time.sleep(1)

	
        if (userinput == 0):
          return finsh()

        userinput -= 1
    ws.mainloop()

finish_btn = Button(
	ws, 
	text='FINISH', 
	bd='5',
	command= finsh
	)

finish_btn.place(x = 610,y = 650)


