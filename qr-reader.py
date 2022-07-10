import scan_webcam as sw
import timer
import requests as r
from tkinter import messagebox
t = True
Url = "https://shayan15sa.pythonanywhere.com/qrcheck"
param = {"fn":"","ln":""}
while t:
    dt = sw.scan()
    fn = dt["fn"]
    ln = dt["ln"]
    param["fn"] = fn
    param["ln"] = ln
    if r.get(Url,param).text == "1":
        if not timer.startCountdown(1,0,fn+" "+ln):
            exit()
    else:
        messagebox.showerror("BISHOUR","IT's NOT YOUR TURN!")     