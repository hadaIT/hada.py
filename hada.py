from tkinter import *
import requests
root = Tk()
root.geometry('700x400')
def myclick():
 link = requests.get(input1.get())
 mylink = link.text
 mytext.insert(1.0, mylink)
 

def clean():
  mytext.delete(1.0, END)
  
border = Label(root, text="g",borderwidth=5,bg='#010101',width=100,height=100)
border.place(x=0,y=0)


loginmsg = Label(root,text=" ༒ Welcome To Home Dragon ༒  ",font=10,bg='#010101',fg='#FFD700')
loginmsg.place(x=250,y=13)


nwsenakanm1 = Label(root,text="Url  : ",font=10,bg='#010101',fg='#FFD700')
nwsenakanm1.place(x=80,y=50)


input1 = Entry(root,font=10,borderwidth=3,relief="ridge",bg='#010101',fg='#FFD700', width=50)
input1.place(x=150,y=50)


mytext = Text(root, height=15, width=56,fg='#FFD700',bg='#3C3B42')
mytext.place(x=150,y=100)

button = Button(root, text="Requests.get",font=8,borderwidth=2,relief="groove",width =15,bg='#010101',fg='#FFD700', command=myclick)
button.place(x=150,y=350)


button = Button(root, text="Clean",font=8,borderwidth=2,relief="groove",width =15,bg='#010101',fg='#FFD700', command=clean)
button.place(x=305,y=350)

button = Button(root, text="Exit",font=8,borderwidth=2,relief="groove",width =15,bg='#010101',fg='#FFD700', command=root.destroy)
button.place(x=458,y=350)
root.mainloop()


////////////////


from tkinter import *
from tkinter import filedialog

root = Tk()
root.geometry('500x500')

def saveFile():
 file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("بە شێوەی تێکست",".txt"),("بە شێوەی هتمل",".html"),("هەموو جۆریک بە دەست خۆم", ".*"),])
 filetext = str(mytext.get(1.0,END))
 file.write(filetext)
 file.close()
 
mybutton = Button(root,text="Xaznkrdn",command=saveFile)
mybutton.place(x=0,y=450)

mytext = Text(root,height=25,width=60,bg="red",fg="white")
mytext.place(x=0,y=0)

root.mainloop()



//////////////



