#!usr/bin/python2  
import Tkinter as tk

FONT = ("TkLabelFont", 13)

class mainApplication(tk.Tk):
		
		def __init__(self, *args, **kwargs):
			
			tk.Tk.__init__(self, *args, **kwargs)
			container = tk.Frame(self)
			container.pack(side = "top", fill = "both", expand = True)
			container.grid_rowconfigure(0, weight = 1)
			container.grid_columnconfigure(0, weight = 1)
			
			self.frames = {}

			for F in (init_page, analysis_opts):
			
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

		init_button = tk.Button(self, text = "Initialize Vehicle Analysis", command = lambda: controller.show_frame(analysis_opts), font = FONT)
		init_button.pack()

class analysis_opts(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		opts_label = tk.Label(self, text = "Analysis Library", font = FONT)
		opts_label.pack(pady = 10, padx = 10)
		spacho_button = tk.Button(self, text = "Speed/Accleration", command = lambda: controller.show_frame(spacho_page), font = FONT)
		spacho_button.pack()
		temp_button = tk.Button(self, text = "Engine Temperature", command = lambda: controller.show_frame(init_page), font = FONT)
		temp_button.pack()
		gps_button = tk.Button(self, text = "GPS Location", command = lambda: controller.show_frame(init_page), font = FONT)
		gps_button.pack()
		graph_button = tk.Button(self, text = "Graphical Feed", command = lambda: controller.show_frame(init_page), font = FONT)
		graph_button.pack()
		back_button = tk.Button(self, text = "Back to Home", command = lambda: controller.show_frame(init_page), font = FONT)
		back_button.pack()

class spacho_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		spacho_label  = tk.Label(self, text = "Speed | Acceleration | Horespower", font = FONT)
		spacho_label.pack(padx = 10, pady = 10)

class temp_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		temp_label  = tk.Label(self, text = "Temperature | Humidity", font = FONT)
		temp_label.pack(padx = 10, pady = 10)

class gps_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		gps_label  = tk.Label(self, text = "GPS | Coordinates", font = FONT)
		gps_label.pack(padx = 10, pady = 10)


class spacho_page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		spacho_label  = tk.Label(self, text = "Speed | Acceleration | Horespower", font = FONT)
		spacho_label.pack(padx = 10, pady = 10)



def main():
	
	app = mainApplication()
	app.mainloop()

if __name__ == "__main__":
	main()