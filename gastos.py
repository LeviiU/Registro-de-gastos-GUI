from tkinter import *
import datetime

def suma(a,b):
	c = a + b
	return c
def mostrar(x):
	print(x)

def hora_y_fecha():
	x = datetime.datetime.now()
	print ("Formato dd/mm/yyyy =  %s/%s/%s" % (x.day, x.month, x.year) )
	print ("Formato hh:mm:ss = %s:%s:%s" % (x.hour, x.month, x.second) )
def no():
	print("no")



_name_ = "_main_"
if _name_ == "_main_":
	ventana = Tk()
	ventana.geometry("700x700")
	una_suma = suma(2,6)
	mostrar(una_suma)
	hora_y_fecha()
	ventana.mainloop()