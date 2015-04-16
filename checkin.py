import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
from functools import partial
from editItem import *
import tkinter.messagebox
from connection_info import *


class checkin_class:
	
	def __init__(self, master, root, menu_link, data):
		self.master = master
		self.root = root
		self.data = data
		self.my_menu_link = menu_link
		self.inputs = list()
		self.result_frame = Frame(self.master,borderwidth=5,relief=GROOVE)
		self.result_frame.grid(row = 0, column = 0, padx = 10, columnspan = 3, pady = 10, stick = 'nsew')
		
		#back button
		self.back_button = ttk.Button(self.master, text = 'Cancel')
		self.back_button.grid(row = 8, column = 0, padx = 3, pady = 3, stick = 'nsew')
		self.back_button.config(command = self.back_button_clicked)
		
		#Check in button
		self.checkin_button = ttk.Button(self.master, text = 'Check in')
		self.checkin_button.grid(row = 8, column = 2, padx = 3, pady = 3, stick = 'nsew')
		self.checkin_button.config(command = self.checkin_function)
		
		if(self.data[4] == 34):
			self.create_wig_ui()
		elif(self.data[4] == 26 or self.data[4] == 16):
			self.create_shelf_ui()
		else:
			self.create_rack_ui()
			
		
	def back_button_clicked(self):
		self.master.destroy()
		self.my_menu_link.pack()
		
	def rack_function(self):
		try:
			cur = sql_info()[0]
			connection = sql_info()[1]
			input = self.inputs[0].get() + self.inputs[1].get() + self.inputs[2].get()
			
			SQL = "SELECT [Name],[isfull] FROM [CMT].[dbo].[Racks]"
			
			cur.execute(SQL)
			result = cur.fetchall()
			
			not_correct_input = True
			for i in range(len(result)):
				if(result[i][0] == input):
					if(result[i][1] == 1):
						# popup = Tk()
						# ttk.Label(popup, text = "Cannot store in that location because that location is full").pack()
						tkinter.messagebox.showwarning("Warning","Cannot store in that location because that location is full!")
						return
					not_correct_input = False
					break
			
			if(not_correct_input):
				# popup = Tk()
				# ttk.Label(popup, text = "That storage location does not exist").pack()
				tkinter.messagebox.showwarning("Warning","That storage location does not exist!")
				return
				
			result = tkinter.messagebox.askquestion("Correct?", "Did that location work?")
			if result == 'yes':
				SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 1,[Storage_Location] = '{0}',[Current_Location] = '{1}' WHERE Tag_ID = {2}".format(input, input, self.data[1])
				
				cur.execute(SQL)
				cur.commit()
				
				cur.close()
				connection.close()
				
				result2 = tkinter.messagebox.askquestion("Is it now full?", "Is that location now full?")
				if(result2 == 'yes'):
					SQL = "UPDATE [CMT].[dbo].[Racks] SET [isfull] = 1 WHERE Name = '{0}'".format(input)
					cur = sql_info()[0]
					connection = sql_info()[1]
					cur.execute(SQL)
					cur.commit()
					
					cur.close()
					connection.close()
				else:
					pass
			else:
				result2 = tkinter.messagebox.askquestion("Why?", "Is that location full?")
				if(result2 == 'yes'):
					SQL = "UPDATE [CMT].[dbo].[Racks] SET [isfull] = 1 WHERE Name = '{0}'".format(input)

					cur.execute(SQL)
					cur.commit()
					
					cur.close()
					connection.close()
					return
				else:
					return
			
			# SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 1,[Storage_Location] = '{0}',[Current_Location] = '{1}' WHERE Tag_ID = {2}".format(input, input, self.data[1])
			
			# cur.execute(SQL)
			# cur.commit()
			
			# cur.close()
			# connection.close()
			self.master.destroy()
			self.my_menu_link.pack()
			
		except Exception as e:
			popup = Tk()
			ttk.Label(popup, text = "DB connection error" + str(e)).pack()
			
	def wig_function(self):
		try:
			cur = sql_info()[0]
			connection = sql_info()[1]
			input = self.inputs[0].get() + self.inputs[1].get() + self.inputs[2].get()
			
			SQL = "SELECT [Name],[isfull] FROM [CMT].[dbo].[Controlled_Climate]"
			
			cur.execute(SQL)
			result = cur.fetchall()
			
			not_correct_input = True
			for i in range(len(result)):
				if(result[i][0] == input):
					if(result[i][1] == 1):
						# popup = Tk()
						# ttk.Label(popup, text = "Cannot store in that location because that location is full").pack()
						tkinter.messagebox.showwarning("Warning","Cannot store in that location because that location is full!")
						return
					not_correct_input = False
					break
			
			if(not_correct_input):
				# popup = Tk()
				# ttk.Label(popup, text = "That storage location does not exist").pack()
				tkinter.messagebox.showwarning("Warning","That storage location does not exist!")
				return
				
			result = tkinter.messagebox.askquestion("Correct?", "Did that location work?")
			if result == 'yes':
				SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 1,[Storage_Location] = '{0}',[Current_Location] = '{1}' WHERE Tag_ID = {2}".format(input, input, self.data[1])
				
				cur.execute(SQL)
				cur.commit()
				
				cur.close()
				connection.close()
				
				result2 = tkinter.messagebox.askquestion("Is it now full?", "Is that location now full?")
				if(result2 == 'yes'):
					SQL = "UPDATE [CMT].[dbo].[Controlled_Climate] SET [isfull] = 1 WHERE Name = '{0}'".format(input)
					cur = sql_info()[0]
					connection = sql_info()[1]
					cur.execute(SQL)
					cur.commit()
					
					cur.close()
					connection.close()
				else:
					pass
			else:
				result2 = tkinter.messagebox.askquestion("Why?", "Is that location full?")
				if(result2 == 'yes'):
					SQL = "UPDATE [CMT].[dbo].[Controlled_Climate] SET [isfull] = 1 WHERE Name = '{0}'".format(input)

					cur.execute(SQL)
					cur.commit()
					
					cur.close()
					connection.close()
				else:
					pass
			
			# SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 1,[Storage_Location] = '{0}',[Current_Location] = '{1}' WHERE Tag_ID = {2}".format(input, input, self.data[1])
			
			# cur.execute(SQL)
			# cur.commit()
			
			# cur.close()
			# connection.close()
			self.master.destroy()
			self.my_menu_link.pack()
			
		except Exception as e:
			popup = Tk()
			ttk.Label(popup, text = "DB connection error" + str(e)).pack()
			
	def shelf_function(self):
		try:
			cur = sql_info()[0]
			connection = sql_info()[1]
			input = self.inputs[0].get() + self.inputs[1].get()
			
			SQL = "SELECT [Name],[isfull] FROM [CMT].[dbo].[Shelves]"
			
			cur.execute(SQL)
			result = cur.fetchall()
			
			not_correct_input = True
			for i in range(len(result)):
				if(result[i][0] == input):
					if(result[i][1] == 1):
						# popup = Tk()
						# ttk.Label(popup, text = "Cannot store in that location because that location is full").pack()
						tkinter.messagebox.showwarning("Warning","Cannot store in that location because that location is full!")
						return
					not_correct_input = False
					break
			
			if(not_correct_input):
				# popup = Tk()
				# ttk.Label(popup, text = "That storage location does not exist").pack()
				tkinter.messagebox.showwarning("Warning","That storage location does not exist!")
				return
				
			result = tkinter.messagebox.askquestion("Correct?", "Did that location work?")
			if result == 'yes':
				SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 1,[Storage_Location] = '{0}',[Current_Location] = '{1}' WHERE Tag_ID = {2}".format(input, input, self.data[1])
				
				cur.execute(SQL)
				cur.commit()
				
				cur.close()
				connection.close()
				
				result2 = tkinter.messagebox.askquestion("Is it now full?", "Is that location now full?")
				if(result2 == 'yes'):
					SQL = "UPDATE [CMT].[dbo].[Shelves] SET [isfull] = 1 WHERE Name = '{0}'".format(input)
					cur = sql_info()[0]
					connection = sql_info()[1]
					cur.execute(SQL)
					cur.commit()
					
					cur.close()
					connection.close()
				else:
					pass
			else:
				result2 = tkinter.messagebox.askquestion("Why?", "Is that location full?")
				if(result2 == 'yes'):
					SQL = "UPDATE [CMT].[dbo].[Shelves] SET [isfull] = 1 WHERE Name = '{0}'".format(input)

					cur.execute(SQL)
					cur.commit()
					
					cur.close()
					connection.close()
				else:
					pass
			
			# SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 1,[Storage_Location] = '{0}',[Current_Location] = '{1}' WHERE Tag_ID = {2}".format(input, input, self.data[1])
			
			# cur.execute(SQL)
			# cur.commit()
			
			# cur.close()
			# connection.close()
			self.master.destroy()
			self.my_menu_link.pack()
			
		except Exception as e:
			popup = Tk()
			ttk.Label(popup, text = "DB connection error" + str(e)).pack()
		
	def checkin_function(self):
		if(self.data[4] == 34):
			self.wig_function()
		elif(self.data[4] == 26 or self.data[4] == 16):
			self.shelf_function()
		else:
			self.rack_function()
			
	def create_shelf_ui(self):
		#labels
		self.suggestion_label = ttk.Label(self.result_frame, text = "Suggested Placement: ")
		self.suggestion = ttk.Label(self.result_frame, text = self.get_shelf_suggestion())
		self.info_label = ttk.Label(self.result_frame, text = "Where are you storing the item?")
		self.rack_row_label = ttk.Label(self.result_frame, text = "Shelf: ")
		self.rack_level_label = ttk.Label(self.result_frame, text = "Row: ")
		
		self.suggestion_label.grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.suggestion.grid(row=2, column=1, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.info_label.grid(row=3, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_row_label.grid(row=4, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_level_label.grid(row=5, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		
		#row input
		row = StringVar()
		self.rack_row_input = ttk.Combobox(self.result_frame, textvariable = row)
		self.rack_row_input.grid(row = 4, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_row_input.config(values = ('1', '2', '3', '4', '5', '6', '7', '8', '9'))
		
		
		#level input
		level = StringVar()
		self.rack_level_input = ttk.Combobox(self.result_frame, textvariable = level)
		self.rack_level_input.grid(row = 5, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_level_input.config(values = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'))
		self.inputs.append(level)
		self.inputs.append(row)
		
		
		
	def create_rack_ui(self):
		#labels
		self.suggestion_label = ttk.Label(self.result_frame, text = "Suggested Placement: ")
		self.suggestion = ttk.Label(self.result_frame, text = self.get_rack_suggestion())
		self.info_label = ttk.Label(self.result_frame, text = "Where are you storing the item?")
		self.rack_row_label = ttk.Label(self.result_frame, text = "Row: ")
		self.rack_level_label = ttk.Label(self.result_frame, text = "*Level: ")
		self.rack_section_label = ttk.Label(self.result_frame, text = "Section: ")
		self.rack_explanation_label = ttk.Label(self.result_frame, text = "*only level 3 for rack rows 17-20")
		
		self.suggestion_label.grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.suggestion.grid(row=2, column=1, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.info_label.grid(row=3, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_row_label.grid(row=4, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_level_label.grid(row=5, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_section_label.grid(row=6, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_explanation_label.grid(row=7, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		
		#row input
		row = StringVar()
		self.rack_row_input = ttk.Combobox(self.result_frame, textvariable = row)
		self.rack_row_input.grid(row = 4, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_row_input.config(values = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'))
		self.inputs.append(row)
		
		#level input
		level = StringVar()
		self.rack_level_input = ttk.Combobox(self.result_frame, textvariable = level)
		self.rack_level_input.grid(row = 5, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_level_input.config(values = ('1', '2', '3'))
		self.inputs.append(level)
		
		#section input
		section = StringVar()
		self.rack_section_input = ttk.Combobox(self.result_frame, textvariable = section)
		self.rack_section_input.grid(row = 6, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_section_input.config(values = ('1', '2', '3', '4', '5', '6'))
		self.inputs.append(section)
		
	def create_wig_ui(self):
		#labels
		self.suggestion_label = ttk.Label(self.result_frame, text = "Suggested Placement: ")
		self.suggestion = ttk.Label(self.result_frame, text = self.get_wig_suggestion())
		self.info_label = ttk.Label(self.result_frame, text = "Where are you storing the item?")
		self.rack_row_label = ttk.Label(self.result_frame, text = "Set of shelves: ")
		self.rack_level_label = ttk.Label(self.result_frame, text = "Level: ")
		self.rack_section_label = ttk.Label(self.result_frame, text = "Box: ")
		
		self.suggestion_label.grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.suggestion.grid(row=2, column=1, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.info_label.grid(row=3, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_row_label.grid(row=4, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_level_label.grid(row=5, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_section_label.grid(row=6, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		
		#row input
		row = StringVar()
		self.rack_row_input = ttk.Combobox(self.result_frame, textvariable = row)
		self.rack_row_input.grid(row = 4, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_row_input.config(values = ('1', '2'))
		self.inputs.append(row)
		
		#level input
		level = StringVar()
		self.rack_level_input = ttk.Combobox(self.result_frame, textvariable = level)
		self.rack_level_input.grid(row = 5, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_level_input.config(values = ('1', '2', '3', '4', '5'))
		self.inputs.append(level)
		
		#section input
		section = StringVar()
		self.rack_section_input = ttk.Combobox(self.result_frame, textvariable = section)
		self.rack_section_input.grid(row = 6, column = 1, padx = 3, pady = 3, stick = 'nsew')
		self.rack_section_input.config(values = ('1', '2', '3'))
		self.inputs.append(section)
		
	def get_rack_suggestion(self):
		cur = sql_info()[0]
		connection = sql_info()[1]
		output = ""
			
		SQL = "SELECT [Name],[isfull] FROM [CMT].[dbo].[Racks]"
			
		cur.execute(SQL)
		result = cur.fetchall()
		
		for i in range(len(result)):
			if(result[i][1] == 0):
				output =  result[i][0]
				break
		
		cur.close()
		connection.close()
		
		return "Row: " + output[0] + output[1] + " Level: " + output[2] + " Section: " + output[3]
		
	def get_shelf_suggestion(self):
		cur = sql_info()[0]
		connection = sql_info()[1]
		output = ""
			
		SQL = "SELECT [Name],[isfull] FROM [CMT].[dbo].[Shelves]"
			
		cur.execute(SQL)
		result = cur.fetchall()
		
		for i in range(len(result)):
			if(result[i][1] == 0):
				output =  result[i][0]
				break
		
		cur.close()
		connection.close()
		
		return "Row: " + output[0] + output[1] + " Shelf: " + output[2]
		
	def get_wig_suggestion(self):
		cur = sql_info()[0]
		connection = sql_info()[1]
		output = ""
			
		SQL = "SELECT [Name],[isfull] FROM [CMT].[dbo].[Controlled_Climate]"
			
		cur.execute(SQL)
		result = cur.fetchall()
		
		for i in range(len(result)):
			if(result[i][1] == 0):
				output =  result[i][0]
				break
		
		cur.close()
		connection.close()
		
		return "Set of helves: " + output[0] + " Shelf: " + output[1] + " Box: " + output[2]