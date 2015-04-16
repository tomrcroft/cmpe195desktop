import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
import tkinter.messagebox
from connection_info import *
from checkin import *
from checkout import *
import tkinter.messagebox


class scan_class:
	
	def __init__(self, master, root, menu_link):
		self.master = master
		self.root = root
		self.my_menu_link = menu_link
		self.result_frame = Frame(self.master, height = 240, width = 300,borderwidth=5,relief=GROOVE)
		self.result_frame.grid_propagate(False)
		self.result_frame.grid(row = 1, column = 0, padx = 10, columnspan = 3, pady = 10, stick = 'nsew')
		
		self.name_label = ttk.Label(master, text = 'Enter ID number: ').grid(row=0, column=0, padx = 3, pady = 3, stick = 'nsew')
		
		self.search_input = ttk.Entry(master, width = 30)
		self.search_input.grid(row=0, column=1, padx = 0, pady = 0, stick = 'nsew')
		
		self.search_button = ttk.Button(master, text="Search", command=self.search_process_function)
		self.search_button.grid(row=0, column= 2, padx = 0, pady = 0, stick = 'nsew')
		
		self.back_button = ttk.Button(master, text = 'Back', command = self.back_button_clicked)
		self.back_button.grid(row = 3, column = 0, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
		
		self.back_button = ttk.Button(master, text = 'Check in', command = self.checkin)
		self.back_button.grid(row = 3, column = 1, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
		
		self.back_button = ttk.Button(master, text = 'Check out', command = self.checkout)
		self.back_button.grid(row = 3, column = 2, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
		
	def back_button_clicked(self):
		self.master.destroy()
		self.my_menu_link.pack()
		
	def convertTrueFalse(self, num):
		if(num == 0):
			return "No"
		else:
			return "Yes"
			
	def convertLocation(self, input):
		if(type(input) == type(None) or input == ''):
			return "Not in Warehouse"
		else:
			converted_input = input
			if(self.result[4] == 34):
				return "Set of Shelves " + converted_input[0] + " Shelf " + converted_input[1] + " Box " + converted_input[2]
			elif(self.result[4] == 26 or self.result[4] == 16):
				return "Row " + converted_input[0] + converted_input[1] + " Shelf " + converted_input[2]
			else:
				return "Row " + converted_input[0] + converted_input[1] + " Level " + converted_input[2] + " Section " + converted_input[3]
		
	def search_process_function(self):	
	
		try:
			if(len(self.search_input.get()) > 1000):
				# popup = Tk()
				# ttk.Label(popup, text = "input is too large").pack()
				tkinter.messagebox.showwarning("Warning","An input is over 200 character, please check and re-try!")
				return
			int(self.search_input.get())
		except Exception as e:
			# popup = Tk()
			# ttk.Label(popup, text = "incorrect input format, must be an integer").pack()
			tkinter.messagebox.showwarning("Warning","search input must be an id number!")
			return
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT * FROM [dbo].[Costume] WHERE Tag_ID = {0}".format(self.search_input.get())
		cur.execute(SQL)
		result = cur.fetchone()
		self.result = result
		
		if(result == None):
			# popup = Tk()
			# ttk.Label(popup, text = "No item associated with that ID number").pack()
			tkinter.messagebox.showwarning("Warning","No item associated with that ID number!")
			return
			
		
		self.result_frame.destroy()
		self.result_frame = Frame(self.master, height = 240, width = 300,borderwidth=5,relief=GROOVE)
		self.result_frame.grid_propagate(False)
		self.result_frame.grid(row = 1, column = 0, padx = 10, columnspan = 3, pady = 10, stick = 'nsew')
		
		self.name_label = ttk.Label(self.result_frame, text = "Name: ")
		self.name_label.grid(row = 0, column = 0, padx = 0, pady = 10, stick = 'nsew')
		
		self.name_value = ttk.Label(self.result_frame, text = result[2], wraplength = 230)
		self.name_value.grid(row = 0, column = 1, padx = 0, pady = 10, stick = 'nsew')
		
		self.desc_label = ttk.Label(self.result_frame, text = "Description: ")
		self.desc_label.grid(row = 1, column = 0, padx = 0, pady = 10, stick = 'nsew')
		
		self.desc_value = ttk.Label(self.result_frame, text = result[3], wraplength = 230)
		self.desc_value.grid(row = 1, column = 1, padx = 0, pady = 10, stick = 'nsew')
		
		self.desc_label = ttk.Label(self.result_frame, text = "Rentable: ")
		self.desc_label.grid(row = 2, column = 0, padx = 0, pady = 10, stick = 'nsew')
		
		self.desc_value = ttk.Label(self.result_frame, text = self.convertTrueFalse(result[18]), wraplength = 230)
		self.desc_value.grid(row = 2, column = 1, padx = 0, pady = 10, stick = 'nsew')
		
		self.desc_label = ttk.Label(self.result_frame, text = "Location: ")
		self.desc_label.grid(row = 3, column = 0, padx = 0, pady = 10, stick = 'nsew')
		
		self.desc_value = ttk.Label(self.result_frame, text = self.convertLocation(result[21]), wraplength = 230)
		self.desc_value.grid(row = 3, column = 1, padx = 0, pady = 10, stick = 'nsew')
		
		cur.close()
		connection.close()
		
	def checkin(self):
		try:
			if(len(self.search_input.get()) == 0):
					# popup = Tk()
					# ttk.Label(popup, text = "there is no input").pack()
					tkinter.messagebox.showwarning("Warning","input is empty!")
					return
			self.master.pack_forget()
			checkin_frame = Frame(self.root, bg='firebrick2')
			checkin_frame.pack()
			add = checkin_class(checkin_frame, self.root, self.my_menu_link, self.result)
		except Exception as e:
			# popup = Tk()
			# ttk.Label(popup, text = "must search for an item by id first").pack()
			tkinter.messagebox.showwarning("Warning","must search for an item first!")
			self.master.pack()
		
	def checkout(self):
		try:
			if(self.result[18] == 0):
				tkinter.messagebox.showwarning("Warning","Item already checked out!")
				return
			#print(self.result)
			if(len(self.search_input.get()) == 0 or len(self.result) == 0):
					# popup = Tk()
					# ttk.Label(popup, text = "there is no input").pack()
					tkinter.messagebox.showwarning("Warning","input is empty!")
					return
			self.master.pack_forget()
			checkin_frame = Frame(self.root, bg='firebrick2')
			checkin_frame.pack()
			add = checkout_class(checkin_frame, self.root, self.my_menu_link, self.result)
		except Exception as e:
			# popup = Tk()
			# ttk.Label(popup, text = "must search for an item by id first").pack()
			
			self.master.pack()