# Cosinus & Sinus 

from tkinter import*
from tkinter.messagebox import*
import math
import sys
import time

def sinus():
    sin_a = sin.get()
    sin_b = math.radians(float(sin_a))
    sin_c = math.sin(sin_b)
    print("Sin: ", sin_c)
    showinfo("Синус", sin_c)
    
def cosinus():
    cos_a = cos_entr.get()
    cos_b = math.radians(float(cos_a))
    cos_c = math.cos(cos_b)
    print("Cos: ",cos_c)
    showinfo("Косинус", cos_c)
    
def Exit():
    showinfo("Bye", "Bye!")
    root.destroy()
    time.sleep(1)
    sys.exit()
    
# Window root
root = Tk()
root.geometry("450x250")
root.title("Sinus & cosinus program")

# Sinus
text1 = Label(root, text="Синус:") # Text sinus
text1.place(x=100, y=10)
sin = Entry(root, width=25) # Entry sin
sin.place(x=100, y=30)
butt = Button(root, text="Розрахувати синус", bg="cyan", command=sinus) # Button sinus
butt.place(x=120, y=55)

# Cosinus
text2 = Label(root, text="Косинус:") # Text cosinus
text2.place(x=100, y=100)
cos_entr = Entry(root, width=25) # Entry cos
cos_entr.place(x=100, y= 120)
butt_cos = Button(root, text="Розрахувати косинус", bg="orange", command=cosinus) # Button cosinus
butt_cos.place(x=114, y=150)

# EXIT
ext = Button(root, text="Exit", bg="red", command=Exit)
ext.place(x=380, y=200)

root.mainloop()