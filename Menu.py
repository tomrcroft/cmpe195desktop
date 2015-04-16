import sys
from tkinter import *
from tkinter import ttk
from Register import *
from addItem import *
from Search import *
from scan import *

class Menu:
	
	#constructor
	#
	def __init__(self, master, root, login):
		self.master = master
		self.root = root
		self.login = login
		
		photo = PhotoImage(file = 'black.png')
		rphoto = PhotoImage(file = 'red.png')
		bphoto = PhotoImage(file = 'blue.png')
		
		self.image_frame = Frame(master, bg='firebrick2')
		# self.rimage_frame = Frame(master, height = 100, width = 100)
		# self.bimage_frame = Frame(master)
		
		
		self.image_label = ttk.Label(self.image_frame)
		self.image_label.config(image = photo)
		self.image_label.pack(side = LEFT)
		self.image_label.image = photo
		
		self.rimage_label = ttk.Label(self.image_frame)
		self.rimage_label.config(image = rphoto)
		self.rimage_label.pack(side = TOP)
		self.rimage_label.image = rphoto
		
		self.bimage_label = ttk.Label(self.image_frame)
		self.bimage_label.config(image = bphoto)
		self.bimage_label.pack(side = RIGHT)
		self.bimage_label.image = bphoto
		self.image_frame.grid(row = 0, column = 0, padx = 10, pady = 10, rowspan = 5, stick = 'ns')

		
		self.register_button = ttk.Button(master, text="Register New User", command=self.register_function)
		self.register_button.grid(row=0, column= 1, padx = 10, pady = 10, stick = 'nsew')
		
		self.add_new_item_button = ttk.Button(master, text="Add New Item", command=self.addItem_function)
		self.add_new_item_button.grid(row=1, column= 1, padx = 10, pady = 10, stick = 'nsew')
		
		self.scan_item_button = ttk.Button(master, text="Check in/out Item", command=self.scan_function)
		self.scan_item_button.grid(row=2, column= 1, padx = 10, pady = 10, stick = 'nsew')
		
		self.search_item_button = ttk.Button(master, text="Search Items", command=self.search_function)
		self.search_item_button.grid(row=3, column= 1, padx = 10, pady = 10, stick = 'nsew')
		
		self.logout_button = ttk.Button(master, text="Logout", command=self.logout_function)
		self.logout_button.grid(row=4, column= 1, padx = 10, pady = 10, stick = 'nsew')
		
		
	def register_function(self):
		self.master.pack_forget()
		register_frame = Frame(self.root, bg='firebrick2')
		register_frame.pack()
		# popup = Tk()
		# ttk.Label(popup, text = type(register_frame)).grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		register = Register(register_frame, self.root, self.master)
		
	def addItem_function(self):
		self.master.pack_forget()
		addItem_frame = Frame(self.root, bg='firebrick2')
		addItem_frame.pack()
		# popup = Tk()
		# ttk.Label(popup, text = type(register_frame)).grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		add = AddItem(addItem_frame, self.root, self.master)
		
	def logout_function(self):
		self.master.destroy()
		# login_frame = Frame(self.root)
		# login_frame.pack()
		# popup = Tk()
		# ttk.Label(popup, text = type(register_frame)).grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.login.pack()

	def search_function(self):
		self.master.pack_forget()
		search_frame = Frame(self.root, bg='firebrick2')
		search_frame.pack()
		add = search_class(search_frame, self.root, self.master)
		
	def scan_function(self):
		self.master.pack_forget()
		scan_frame = Frame(self.root, bg='firebrick2')
		scan_frame.pack()
		add = scan_class(scan_frame, self.root, self.master)
