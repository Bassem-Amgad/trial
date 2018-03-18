from tkinter import *
root=Tk()
# scale (name, from range , to range , orientation,reference to callback fn) 
c= Scale(root,from_=0,to=100,orient=HORIZONTAL,command=update)
c.pack()
def update (duty):
    pwm.ChangeDutyCycle(float(duty))
