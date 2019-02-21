#!usr/bin/python2  
import tkinter as tk
from tkinter import ttk
import tk_tools

import matplotlib 
import matplotlib.pyplot as plt 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

import urllib
import json
import pandas as pd
import numpy as np

FONT = ("Verdana", 9)
FONT_TITLE  = ("TkLabelFont", 12)
plt.style.use(['bmh'])

f = Figure(figsize = (3,3), dpi = 75)
a = f.add_subplot(111)

def animate(i):
	pullData = open("sampleData.txt", "r").read()

	dataList = pullData.split("\n")
	xList = []
	yList = []
	for eachLine in dataList:
		if len(eachLine)>1:
			x, y = eachLine.split(',')
			xList.append(int(x))
			yList.append(int(y))

	a.clear()
	a.plot(xList, yList)

class mainApplication(tk.Tk):
		
		def __init__(self, *args, **kwargs):
			
			tk.Tk.__init__(self, *args, **kwargs)

			#tk.Tk.wm_iconbitmap(self, "clienticon.gif")

			container = tk.Frame(self)
			container.pack(side = "top", fill = "both", expand = True)
			container.grid_rowconfigure(0, weight = 1)
			container.grid_columnconfigure(0, weight = 1)
			
			self.frames = {}

			for F in (init_page,
					  analysis_opts,
					  spacho_page,
					  temp_page,
					  gps_page,
					  graph_page):
			
				frame = F(container, self)
			
				self.frames[F] = frame
			
				frame.grid(row = 0, column = 0, sticky = "nsew")
			
			self.show_frame(init_page)

		def show_frame(self, cont):
			
			frame = self.frames[cont]
			frame.tkraise()



class init_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label_main = tk.Label(self, text = "Onboard Vehicle Analysis Ver.0.0.1", font = FONT)
		label_main.pack(pady = 10,  padx =10)

		init_button = tk.Button(self, text = "Initialize Vehicle Analysis" ,command = lambda: controller.show_frame(analysis_opts), font = FONT)
		init_button.pack()

class analysis_opts(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		opts_label = tk.Label(self, text = "Analysis Library", font = FONT)
		opts_label.pack(pady = 10, padx = 10)
		spacho_button = tk.Button(self, text = "Velocty/Accleration", command = lambda: controller.show_frame(spacho_page), font = FONT)
		spacho_button.pack()
		temp_button = tk.Button(self, text = "Engine Temperature", command = lambda: controller.show_frame(temp_page), font = FONT)
		temp_button.pack()
		gps_button = tk.Button(self, text = "GPS Location", command = lambda: controller.show_frame(gps_page), font = FONT)
		gps_button.pack()
		graph_button = tk.Button(self, text = "Graphical Feed", command = lambda: controller.show_frame(graph_page), font = FONT)
		graph_button.pack()
		back_button = tk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(init_page), font = FONT)
		back_button.pack()

class spacho_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		spacho_label  = tk.Label(self, text = "Velocity | Acceleration | Horespower", font = FONT)
		spacho_label.pack(padx = 10, pady = 10)
		backops_button = tk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(analysis_opts), font = FONT)
		backops_button.pack()
		# gauge = tk_tools.Gauge(self, max_value=100.0, label='speed', unit='km/h')
		# gauge.pack()
		# gauge.set_value(10)
		self.led_func(120)
		
		# if bin == 1:
		# 	led1 = tk_tools.Led(self, size = 20)
		# 	led1.to_green(on = True)
		# 	led1.pack()
		# else: 



#If the velocity is equal to 0 |less than 10, call row 0. [0,:]
#If the velocity is equal to 10 |less than 20 , call row 1. [1,:]...etc until 100.
	
	def led_func(self, vel):
		
		# light_matrix = np.array([[0,0,0,0,0,0,0,0,0,0],
		# 						 [0,0,0,0,0,0,0,0,0,0],
		# 					 	 [1,0,0,0,0,0,0,0,0,0],
		# 					 	 [1,1,0,0,0,0,0,0,0,0],
		# 			 		 	 [1,1,1,0,0,0,0,0,0,0],
		# 					 	 [1,1,1,1,0,0,0,0,0,0],
		# 					 	 [1,1,1,1,1,0,0,0,0,0],
		# 					 	 [1,1,1,1,1,1,0,0,0,0],
		# 					 	 [1,1,1,1,1,1,1,0,0,0],
		# 					 	 [1,1,1,1,1,1,1,1,0,0],
		# 					 	 [1,1,1,1,1,1,1,1,1,0],
		# 					 	 [1,1,1,1,1,1,1,1,1,1]])

		# [False False False False False False False False False False]
		# [ True False False False False False False False False False]
		# [ True  True False False False False False False False False]
		# [ True  True  True False False False False False False False]
		# [ True  True  True  True False False False False False False]
		# [ True  True  True  True  True False False False False False]
		# [ True  True  True  True  True  True False False False False]
		# [ True  True  True  True  True  True  True False False False]
		# [ True  True  True  True  True  True  True  True False False]
		# [ True  True  True  True  True  True  True  True  True False]


		m = np.tril(np.arange(0, 110, dtype=np.float).reshape(11,10))
		boolmatrix = np.arange(m.shape[0])[:,None] > np.arange(m.shape[1])


		increment = 10

		# if vel > 100 or vel < 0:
		# 	vel = 100
		# return(vel)

		for i in range(0,110,increment):

			if vel == i or vel < (i+increment) and vel > i:
				led_row = boolmatrix[int(i/increment),:]
				print(led_row)
			elif vel > 100:
				print("Velocity exceeds measurement limits")
				led_row = boolmatrix[int(10),:]
				print(led_row)
				return(led_row)
			else:
				print("Velocity outside of range")

		return(led_row)





			# led1 = tk_tools.Led(self, size = 20)
			# led1.pack()
			# led2 = tk_tools.Led(self, size = 20)
			# led2.pack()	



class temp_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		temp_label  = tk.Label(self, text = "Temperature | Humidity", font = FONT)
		temp_label.pack(padx = 10, pady = 10)
		backops_button = tk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(analysis_opts), font = FONT)
		backops_button.pack()


class gps_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		gps_label  = tk.Label(self, text = "GPS | Coordinates", font = FONT)
		gps_label.pack(padx = 10, pady = 10)
		backops_button = tk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(analysis_opts), font = FONT)
		backops_button.pack()


class graph_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		graph_label  = tk.Label(self, text = "Graph", font = FONT)
		graph_label.pack(padx = 10, pady = 10)
		backops_button = tk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(analysis_opts), font = FONT)
		backops_button.pack()

		# f = Figure(figsize = (3,3), dpi = 75)
		# a = f.add_subplot(111)
		# a.plot([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])

		canvas = FigureCanvasTkAgg(f,self)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

		# toolbar = NavigationToolbar2TkAgg(canvas, self)
		# toolbar.update()
		# canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


def main():
	
	app = mainApplication()
	app.title("O.V.D.S")
	#app.resizable(0,0)
	app.geometry("480x320")
	img = tk.PhotoImage(file='clienticon.png')
	app.tk.call('wm', 'iconphoto', app._w, img)
	ani = animation.FuncAnimation(f,animate, interval = 1000)
	app.mainloop()

if __name__ == "__main__":
	main()