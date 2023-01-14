
from  tkinter import *
from time import strftime


ved= Tk()
ved.title('Clock')



def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)


lbl = Label(ved, font=('calibri', 40, 'bold'),
			background='purple',
			foreground='white')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

mainloop()
