from tkinter import *
from PIL import Image, ImageTk
class window (Frame):
     #creating the window
     def __init__(self,master=None):
          Frame.__init__(self,master)
          self.master = master
          self.init_window()
     # window properties
     def init_window(self):
          self.master.title("GUI")
          self.pack(fill=BOTH,expand=1)
          # creating button
          quitbutton=Button(self,text="Quit",command = self.client_exit)
          quitbutton.place(x=200,y=150)
          # creating menu
          menu = Menu(self.master)
          self.master.config(menu=menu)
               # addiing item to menu
          file = Menu(menu)
          file.add_command(label='new')
          file.add_command(label='save')
          file.add_command(label='exit',command = self.client_exit)
          menu.add_cascade(label='File',menu=file)
          edit = Menu(menu)
          edit.add_command(label='Show Image',command = self.client_Showimg)
          edit.add_command(label='Show Text',command = self.client_Showtxt)
          # client_Showimg() will initially put pictures without clicking command
          menu.add_cascade(label='Edit',menu=edit)
     def client_exit(self):
          exit()
     def client_Showimg(self):
          load = Image.open('photo.jpg')
          render = ImageTk.PhotoImage(load)
          img = Label(self,image=render)
          img.image = render
          img.place(x=0,y=0)
     def client_Showtxt(self):
          text = Label(self,text='Hiii there')
          text.pack()
          
root=Tk()
root.geometry("400x300")
app=window(root)
root.mainloop()
