import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
from tkinter.filedialog import askopenfilename
import os
from connection_info import *
from checkin import *
import tkinter.messagebox


class AddItem:
	
	def __init__(self, master, root, menu_link):
		self.master = master
		self.root = root
		self.inputs = list()
		self.required_inputs = list()
		self.type_list = list()
		self.color_list = list()
		self.specialeffects_list = list()
		self.cleaning_code_list = list()
		self.my_menu_link = menu_link
		self.must_be_decimal = list()
		
		
		left_frame = Frame(master, bg='firebrick2')
		left_frame.grid(row=0, column=0, padx = 10, pady = 10, stick = 'nsew')
		right_frame = Frame(master, bg='firebrick2')
		right_frame.grid(row=0, column=1, padx = 10, pady = 10, stick = 'nsew')
		
		#name
		self.name_label = ttk.Label(left_frame, text = '*Name: ').grid(row=0, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.name_input = ttk.Entry(left_frame, width = 30)
		self.name_input.grid(row=0, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.name_input)
		self.required_inputs.append(self.name_input)
		
		#description
		self.description_label = ttk.Label(left_frame, text = '*Description: ').grid(row=1, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.description_input = ttk.Entry(left_frame, width = 30)
		self.description_input.grid(row=1, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.description_input)
		self.required_inputs.append(self.description_input)
		
		#color
		self.color_label = ttk.Label(left_frame, text = '*Color: ').grid(row=2, column=0, padx = 0, pady = 0, stick = 'nsew')
		color = StringVar()
		self.color_input = ttk.Combobox(left_frame, textvariable = color)
		self.color_input.grid(row=2, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.color_list = self.get_colorlist()
		self.color_input.config(values = self.color_list)
		self.inputs.append(color)
		self.required_inputs.append(color)
		
		#type
		self.type_label = ttk.Label(left_frame, text = '*Type: ').grid(row=3, column=0, padx = 0, pady = 0, stick = 'nsew')
		type = StringVar()
		self.type_input = ttk.Combobox(left_frame, textvariable = type)
		self.type_input.grid(row=3, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.type_list = self.get_typelist()
		self.type_input.config(values = self.type_list)
		self.required_inputs.append(type)
		self.inputs.append(type)
		
		#group
		self.group_label = ttk.Label(left_frame, text = 'Group: ').grid(row=4, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.group_input = ttk.Entry(left_frame, width = 30)
		self.group_input.grid(row=4, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.group_input)
		
		#fabric
		self.fabric_label = ttk.Label(left_frame, text = '*Fabric: ').grid(row=5, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.fabric_input = ttk.Entry(left_frame, width = 30)
		self.fabric_input.grid(row=5, column=1, padx = 0, pady =0, stick = 'nsew')
		self.inputs.append(self.fabric_input)
		self.required_inputs.append(self.fabric_input)
		
		#time period
		self.timeperiod_label = ttk.Label(left_frame, text = 'Time Period: ').grid(row=6, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.timeperiod_input = ttk.Entry(left_frame, width = 30)
		self.timeperiod_input.grid(row=6, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.timeperiod_input)
		
		#special effects
		self.specialeffects_label = ttk.Label(left_frame, text = 'Special Effects: ').grid(row=7, column=0, padx = 0, pady = 0, stick = 'nsew')
		specialeffect = StringVar()
		self.specialeffects_input = ttk.Combobox(left_frame, textvariable = specialeffect)
		self.specialeffects_input.grid(row=7, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.specialeffects_list = self.get_specialeffects()
		self.specialeffects_input.config(values = self.specialeffects_list)
		self.inputs.append(specialeffect)
		
		#adult of child
		self.adult_or_child_label = ttk.Label(left_frame, text = '*Adult or Child: ')
		self.adult_or_child_label.grid(row = 8, column = 0, padx = 0, pady = 0, stick = 'nsew')
		adult_or_child = StringVar()
		self.adult_or_child_input = ttk.Combobox(left_frame, textvariable = adult_or_child)
		self.adult_or_child_input.grid(row = 8, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.adult_or_child_input.config(values = ('Adult', 'child'))
		self.inputs.append(adult_or_child)
		self.required_inputs.append(adult_or_child)
		
		#size
		self.size_label = ttk.Label(left_frame, text='*Size: ')
		self.size_label.grid(row = 9, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.size_input = ttk.Entry(left_frame, width = 30)
		self.size_input.grid(row = 9, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.size_input)
		self.required_inputs.append(self.size_input)
		
		#gender
		self.gender_label = ttk.Label(left_frame, text = '*Gender: ')
		self.gender_label.grid(row = 10, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.gender_input = ttk.Entry(left_frame, width = 30)
		self.gender_input.grid(row = 10, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.gender_input)
		self.required_inputs.append(self.gender_input)
		
		#designer
		self.designer_label = ttk.Label(left_frame, text='Designer: ')
		self.designer_label.grid(row = 11, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.designer_input = ttk.Entry(left_frame, width = 30)
		self.designer_input.grid(row = 11, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.designer_input)
		
		#source
		self.source_label = ttk.Label(left_frame, text='Source: ')
		self.source_label.grid(row = 12, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.source_input = ttk.Entry(left_frame, width = 30)
		self.source_input.grid(row = 12, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.source_input)
		
		#creation cost
		self.creation_cost_label = ttk.Label(left_frame, text='Creation Cost: ')
		self.creation_cost_label.grid(row = 13, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.creation_cost_input = ttk.Entry(left_frame, width = 30)
		self.creation_cost_input.grid(row = 13, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.creation_cost_input)
		self.must_be_decimal.append(self.creation_cost_input)
		
		#replacement cost
		self.replacement_cost_label = ttk.Label(left_frame, text='*Replacement Cost: ')
		self.replacement_cost_label.grid(row = 14, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.replacement_cost_input = ttk.Entry(left_frame, width = 30)
		self.replacement_cost_input.grid(row = 14, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.replacement_cost_input)
		self.required_inputs.append(self.replacement_cost_input)
		self.must_be_decimal.append(self.replacement_cost_input)
		
		#rentable
		self.rentable_label = ttk.Label(left_frame, text = '*Rentable: ')
		self.rentable_label.grid(row = 15, column = 0, padx = 0, pady = 0, stick = 'nsew')
		rentable = StringVar()
		self.rentable_input = ttk.Combobox(left_frame, textvariable = rentable)
		self.rentable_input.grid(row = 15, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.rentable_input.config(values = ('Yes', 'No'))
		self.inputs.append(rentable)
		self.required_inputs.append(rentable)
		
		#rental cost
		self.rental_cost_label = ttk.Label(left_frame, text='*Rental Cost: ')
		self.rental_cost_label.grid(row = 16, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.rental_cost_input = ttk.Entry(left_frame, width = 30)
		self.rental_cost_input.grid(row = 16, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.rental_cost_input)
		self.required_inputs.append(self.rental_cost_input)
		self.must_be_decimal.append(self.rental_cost_input)
		
		#begin right frame
		
		#cleaning code
		self.cleaning_code_label = ttk.Label(right_frame, text = '*Cleaning Code: ').grid(row=0, column=0, padx = 0, pady = 0, stick = 'nsew')
		cleaning_code = StringVar()
		self.cleaning_code_input = ttk.Combobox(right_frame, textvariable = cleaning_code)
		self.cleaning_code_input.grid(row=0, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.cleaning_code_list = self.get_cleaning_codelist()
		self.cleaning_code_input.config(values = self.cleaning_code_list)
		self.required_inputs.append(cleaning_code)
		self.inputs.append(cleaning_code)
		
		#needs repair
		self.needs_repair_label = ttk.Label(right_frame, text = '*Needs Repair: ')
		self.needs_repair_label.grid(row = 1, column = 0, padx = 0, pady = 0, stick = 'nsew')
		needs_repair = StringVar()
		self.needs_repair_input = ttk.Combobox(right_frame, textvariable = needs_repair)
		self.needs_repair_input.grid(row = 1, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.needs_repair_input.config(values = ('Yes', 'No'))
		self.inputs.append(needs_repair)
		self.required_inputs.append(needs_repair)
		
		#repair description
		self.repair_description_label = ttk.Label(right_frame, text = '*Repair Description (could type "none"): ').grid(row=2, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.repair_description_input = ttk.Entry(right_frame, width = 30)
		self.repair_description_input.grid(row=2, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.repair_description_input)
		self.required_inputs.append(self.repair_description_input)
		
		#chest
		self.chest_label = ttk.Label(right_frame, text='Chest: ')
		self.chest_label.grid(row = 3, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.chest_input = ttk.Entry(right_frame, width = 30)
		self.chest_input.grid(row = 3, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.chest_input)
		self.must_be_decimal.append(self.chest_input)
		
		#waist
		self.waist_label = ttk.Label(right_frame, text='Waist: ')
		self.waist_label.grid(row = 4, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.waist_input = ttk.Entry(right_frame, width = 30)
		self.waist_input.grid(row = 4, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.waist_input)
		self.must_be_decimal.append(self.waist_input)
		
		#hips
		self.hips_label = ttk.Label(right_frame, text='Hips: ')
		self.hips_label.grid(row = 5, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.hips_input = ttk.Entry(right_frame, width = 30)
		self.hips_input.grid(row = 5, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.hips_input)
		self.must_be_decimal.append(self.hips_input)
		
		#girth
		self.girth_label = ttk.Label(right_frame, text='Girth: ')
		self.girth_label.grid(row = 6, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.girth_input = ttk.Entry(right_frame, width = 30)
		self.girth_input.grid(row = 6, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.girth_input)
		self.must_be_decimal.append(self.girth_input)
		
		#neck
		self.neck_label = ttk.Label(right_frame, text='Neck: ')
		self.neck_label.grid(row = 7, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.neck_input = ttk.Entry(right_frame, width = 30)
		self.neck_input.grid(row = 7, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.neck_input)
		self.must_be_decimal.append(self.neck_input)
		
		#sleeves
		self.sleeves_label = ttk.Label(right_frame, text='Sleeves: ')
		self.sleeves_label.grid(row = 8, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.sleeves_input = ttk.Entry(right_frame, width = 30)
		self.sleeves_input.grid(row = 8, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.sleeves_input)
		self.must_be_decimal.append(self.sleeves_input)
		
		#neck_to_waist
		self.neck_to_waist_label = ttk.Label(right_frame, text='Neck To Waist: ')
		self.neck_to_waist_label.grid(row = 9, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.neck_to_waist_input = ttk.Entry(right_frame, width = 30)
		self.neck_to_waist_input.grid(row = 9, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.neck_to_waist_input)
		self.must_be_decimal.append(self.neck_to_waist_input)
		
		#waist_to_hem
		self.waist_to_hem_label = ttk.Label(right_frame, text='Waist To Hem: ')
		self.waist_to_hem_label.grid(row = 10, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.waist_to_hem_input = ttk.Entry(right_frame, width = 30)
		self.waist_to_hem_input.grid(row = 10, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.waist_to_hem_input)
		self.must_be_decimal.append(self.waist_to_hem_input)
		
		#inseam
		self.inseam_label = ttk.Label(right_frame, text='Inseam: ')
		self.inseam_label.grid(row = 11, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.inseam_input = ttk.Entry(right_frame, width = 30)
		self.inseam_input.grid(row = 11, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.inseam_input)
		self.must_be_decimal.append(self.inseam_input)
		
		#notes
		self.notes_label = ttk.Label(right_frame, text='*Notes: ')
		self.notes_label.grid(row = 12, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.notes_input = ttk.Entry(right_frame, width = 30)
		self.notes_input.grid(row = 12, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.notes_input)
		self.required_inputs.append(self.notes_input)
		
		#ensemble
		self.ensemble_label = ttk.Label(right_frame, text='Ensemble: ')
		self.ensemble_label.grid(row = 13, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.ensemble_input = ttk.Entry(right_frame, width = 30)
		self.ensemble_input.grid(row = 13, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.ensemble_input)
		
		#image
		self.image_label = ttk.Label(right_frame, text='*Image: ')
		self.image_label.grid(row = 14, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.image_button = ttk.Button(right_frame, text='Select Image')
		self.image_button.grid(row = 14, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.image_button.config(command = self.select_image_function)
		
		#selected image
		self.selected_image = ttk.Label(right_frame, text='Selected Image: ')
		self.selected_image.grid(row = 15, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.selected_image_label = ttk.Entry(right_frame, width= 30)
		self.selected_image_label.grid(row = 15, column = 1, padx = 0, pady = 0, stick = 'nsew')
		
		#back button
		self.back_button = ttk.Button(left_frame, text = 'Back')
		self.back_button.grid(row = 17, column = 0, padx = 0, pady = 30, stick = 'nsew')
		self.back_button.config(command = self.back_button_clicked)
		
		#submit button
		# self.selected_image = ttk.Label(right_frame, text='')
		# self.selected_image.grid(row = 16, column = 0, padx = 0, pady = 20, stick = 'nsew')
		self.submit_button = ttk.Button(right_frame, text = 'Add')
		self.submit_button.grid(row = 17, column = 1, padx = 0, pady = 50, stick = 'nsew')
		self.submit_button.config(command = self.submit_button_function)
		
		#*explained
		self.selected_image = ttk.Label(self.master, text='*Required Input ')
		self.selected_image.grid(row = 19, column = 1, columnspan = 1, padx = 0, pady = 0, stick = 'nsw')
		
	def back_button_clicked(self):
		self.master.destroy()
		self.my_menu_link.pack()
		
	def add_item_function(self):
	
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Username] FROM [CMT].[dbo].[Desktop_User] WHERE username='"+self.username_input.get()+"'"
		cur.execute(SQL)
		row = cur.fetchone()
		if(row != None):
			popup = Tk()
			ttk.Label(popup, text = "Username already exists!").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			return
			
		SQL = "EXECUTE cmt.[dbo].[Add_Or_Update_Desktop_User] @Username = '"+ self.username_input.get() +"',@Password = \'"+self.password_input.get()+"'"
		
		cur = sql_info()[1]
		if(cur.execute(SQL) == None):
			popup = Tk()
			ttk.Label(popup, text = "Error inserting into DB").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			connection.close()
		else:
			cur.commit()
			cur.close()
			connection.close()
			popup = Tk()
			ttk.Label(popup, text = "Succesful registration!").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			self.master.destroy()
			
			
	def get_colorlist(self):
		output = list()
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Costume_Color_Key],[Costume_Color] FROM [CMT].[dbo].[Dic_Costume_Color]"
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output.append(row[1])
			
		cur.close()
		connection.close()
		return output
		
	def get_typelist(self):
		output = list()
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Costume_Type_Key],[Costume_Type] FROM [CMT].[dbo].[Dic_Costume_Type]"
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output.append(row[1])
			
		cur.close()
		connection.close()
		return output
		
	def get_specialeffects(self):
		output = list()
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Special_Effects_Key],[Special_Effects]FROM [CMT].[dbo].[Dic_Special_Effects]"
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output.append(row[1])
			
		cur.close()
		connection.close()
		return output
		
	def get_cleaning_codelist(self):
		output = list()
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Cleaning_Code] ,[Cleaning_Code_Description] FROM [CMT].[dbo].[Dic_Cleaning_Codes]"
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output.append(row[1])
			
		cur.close()
		connection.close()
		return output
		
	def select_image_function(self):
		self.filename = askopenfilename()
		# self.filename = self.filename.replace('/', '\\')
		# popup = Tk()
		# ttk.Label(popup, text = self.filename).pack()
		self.selected_image_label.insert(0, self.filename)
		f = open(self.filename, 'rb')
		# ablob = pypyodbc.Binary(f.read())
		img = f.read()
		# self.inputs.append(self.selected_image_label)
		self.inputs.append(img)
		self.required_inputs.append(self.selected_image_label)
		
	def submit_button_function(self):
		#for i in range(len(self.inputs)):
		
		#check to protect data input size
		for i in range(len(self.inputs) - 1):
			if(isinstance(self.inputs[i], int)):
				if(self.inputs[i] > 10000000000000000):
					# popup = Tk()
					# ttk.Label(popup, text = "An input is over 200 characters, please check and re-try").pack()
					tkinter.messagebox.showwarning("Warning","An input is over 200 character, please check and re-try!")
					return
			else:
				try:
					if(len(self.inputs[i].get()) > 200):
						# popup = Tk()
						# ttk.Label(popup, text = "An input is over 200 characters, please check and re-try").pack()
						tkinter.messagebox.showwarning("An input is over 200 characters, please check and re-try!")
						return
					skip = False
					if('\'' in self.inputs[i].get()):
						for x in range(len(self.inputs[i].get())):
							if(skip):
								skip = False
								continue
							if(self.inputs[i].get()[x] == "\'"):
								if(x == len(self.inputs[i].get()) - 1):
									newString  = self.inputs[i].get() + "\'"
									self.inputs[i].delete(0, END)
									self.inputs[i].insert(0, newString)
								else:
									# newString = self.inputs[i].get()[0:x - 1] + "\'" + self.inputs[i].get()[x:]
									self.inputs[i].insert(x, "\'")
									skip = True
				except AttributeError:
					pass
					# popup = Tk()
					# ttk.Label(popup, text = type(self.inputs[i])).pack()
		#check if required is not empty
		for i in range(len(self.required_inputs)):
			if(len(self.required_inputs[i].get()) == 0):
				# popup = Tk()
				# ttk.Label(popup, text = "A required input has not been entered, please check and re-try").pack()
				tkinter.messagebox.showwarning("Warning","A required input has not been entered, please check and re-try!")
				return
			if(len(self.inputs) < 32):
				# popup = Tk()
				# ttk.Label(popup, text = "No selected image, please check and re-try").pack()
				tkinter.messagebox.showwarning("Warning","No selected image!")
				return
		#check if size is a number
		# try:
			# if(isinstance(self.inputs[9], int)):
				# pass
			# else:
				# self.inputs[9] = int(self.inputs[9].get())
		# except ValueError:
			# popup = Tk()
			# ttk.Label(popup, text = "size must be a number").pack()
			# return
		#check if all need to be decimals
		for i in range(len(self.must_be_decimal)):
			try:
				if(isinstance(self.must_be_decimal[i], float)):
					pass
				else:
					self.must_be_decimal[i] = float(self.must_be_decimal[i].get())
			except ValueError:
				# popup = Tk()
				# ttk.Label(popup, text = "incorrect data types, money and measurements must be a decimal").pack()
				tkinter.messagebox.showwarning("Warning","Incorrect data types, money and measurements must be a decimal!")
				return
		#check to convert yes or no in rentable and needs repair
		if(self.inputs[15].get() == "Yes"):
			#self.inputs[15] = str(1)
			pass
		elif(self.inputs[15].get() == "No"):
			#self.inputs[15] = str(0)
			pass
		else:
			# popup = Tk()
			# ttk.Label(popup, text = "incorrect input for rentable, must be one selected").pack()
			tkinter.messagebox.showwarning("Warning","Incorrect input for rentable, must be one selected!")
			return	
		if(self.inputs[18].get() == "Yes"):
			#self.inputs[18] = str(1)
			pass
		elif(self.inputs[18].get() == "No"):
			#self.inputs[18] = str(0)
			pass
		else:
			popup = Tk()
			ttk.Label(popup, text = "incorrect input for needs repair, must be one selected").pack()
			tkinter.messagebox.showwarning("Warning","incorrect input for needs repair, must be one selected!")
			return
		

		cur = sql_info()[0]
		connection = sql_info()[1]
		
		#prepare file path 
		# popup = Tk()
		# ttk.Label(popup, text = "before: " + self.inputs[31].get()).pack()
		# for i in range(len(self.inputs[31].get())):
			# if(self.inputs[31].get()[i] == "\\"):
				# popup = Tk()
				# ttk.Label(popup, text = "found a \\").pack()
				# output = insert_dash(self.inputs[31].get(), i)
				# self.selected_image_label.insert(0, output)
		# self.inputs[31].insert(0, os.path.normpath(self.inputs[31].get()))
		# popup = Tk()
		# ttk.Label(popup, text = "after: " + self.inputs[31].get()).pack()
		# popup = Tk()
		# ttk.Label(popup, text = self.inputs[30].get()).pack()
		# SQL = "				EXECUTE cmt.[dbo].[Add_Costume] 				   @Costume_Name = '{0:s}'				  ,@Costume_Description = '{1:s}'				  ,@Costume_Type = '{3:s}' 				  ,@Costume_Color = '{2:s}' 				  ,@Costume_Group = '{4:s}'				  ,@Costume_Fabric = '{5:s}'				  ,@Costume_Time_Period = '{6:s}'				  ,@Special_Effects = '{7:s}' 				  ,@Adult_or_Child = '{8:s}'				  ,@Costume_Size = '{9:d}'				  ,@Costume_Gender = '{10:s}'				  ,@Costume_Designer = '{11:s}'				  ,@Costume_Source = '{12:s}'				  ,@Date_Acquired = null				  ,@Creation_or_Buy_Cost = '{13:s}'				  ,@Replacement_Cost = '{14:s}'				  ,@Rentable = '{15:s}'				  ,@Rental_Fee = '{16:s}'				  ,@Cleaning_Code = '{17:s}' 				  ,@Storage_Location = null				  ,@Current_Location = null				  ,@Needs_Repair = '{18:s}'				  ,@Repair_Description = '{19:s}'				  ,@Chest = '{20:s}'				  ,@Waist = '{21:s}'				  ,@Hips = '{22:s}'				  ,@Girth = '{23:s}'				  ,@Neck = '{24:s}'				  ,@Sleeves = '{25:s}'				  ,@Neck_to_Waist = '{26:s}'				  ,@Waist_to_Hem = '{27:s}'				  ,@Inseam = '{28:s}'				  ,@Notes = '{29:s}'				  ,@Ensemble = '{30:s}'				  ,@Costume_Image = {31:s}			  ,@Username = null\n				".format(self.inputs[0].get(), self.inputs[1].get(), self.inputs[2].get(), self.inputs[3].get(), self.inputs[4].get(), self.inputs[5].get(), self.inputs[6].get(), self.inputs[7].get(), self.inputs[8].get(), self.inputs[9], self.inputs[10].get(), self.inputs[11].get(), self.inputs[12].get(), self.inputs[13].get(), self.inputs[14].get(), self.inputs[15].get(),self.inputs[16].get(), self.inputs[17].get(), self.inputs[18].get(), self.inputs[19].get(), self.inputs[20].get(), self.inputs[21].get(),self.inputs[22].get(), self.inputs[23].get(), self.inputs[24].get(), self.inputs[25].get(), self.inputs[26].get(), self.inputs[27].get(), self.inputs[28].get(), self.inputs[29].get(), self.inputs[30].get(), str(self.inputs[31]))

		
		SQL = "				EXECUTE cmt.[dbo].[Add_Costume] 				   @Costume_Name = '{0:s}'				  ,@Costume_Description = '{1:s}'				  ,@Costume_Type = '{3:s}' 				  ,@Costume_Color = '{2:s}' 				  ,@Costume_Group = '{4:s}'				  ,@Costume_Fabric = '{5:s}'				  ,@Costume_Time_Period = '{6:s}'				  ,@Special_Effects = '{7:s}' 				  ,@Adult_or_Child = '{8:s}'				  ,@Costume_Size = '{9:s}'				  ,@Costume_Gender = '{10:s}'				  ,@Costume_Designer = '{11:s}'				  ,@Costume_Source = '{12:s}'				  ,@Date_Acquired = null				  ,@Creation_or_Buy_Cost = '{13:s}'				  ,@Replacement_Cost = '{14:s}'				  ,@Rentable = '{15:s}'				  ,@Rental_Fee = '{16:s}'				  ,@Cleaning_Code = '{17:s}' 				  ,@Storage_Location = null				  ,@Current_Location = null				  ,@Needs_Repair = '{18:s}'				  ,@Repair_Description = '{19:s}'				  ,@Chest = '{20:s}'				  ,@Waist = '{21:s}'				  ,@Hips = '{22:s}'				  ,@Girth = '{23:s}'				  ,@Neck = '{24:s}'				  ,@Sleeves = '{25:s}'				  ,@Neck_to_Waist = '{26:s}'				  ,@Waist_to_Hem = '{27:s}'				  ,@Inseam = '{28:s}'				  ,@Notes = '{29:s}'				  ,@Ensemble = '{30:s}'				  ,@Costume_Image = null			  ,@Username = null\n				".format(self.inputs[0].get(), self.inputs[1].get(), self.inputs[2].get(), self.inputs[3].get(), self.inputs[4].get(), self.inputs[5].get(), self.inputs[6].get(), self.inputs[7].get(), self.inputs[8].get(), self.inputs[9].get(), self.inputs[10].get(), self.inputs[11].get(), self.inputs[12].get(), self.inputs[13].get(), self.inputs[14].get(), self.inputs[15].get(),self.inputs[16].get(), self.inputs[17].get(), self.inputs[18].get(), self.inputs[19].get(), self.inputs[20].get(), self.inputs[21].get(),self.inputs[22].get(), self.inputs[23].get(), self.inputs[24].get(), self.inputs[25].get(), self.inputs[26].get(), self.inputs[27].get(), self.inputs[28].get(), self.inputs[29].get(), self.inputs[30].get())
		
		# popup = Tk()
		# pop = ttk.Entry(popup, width = 30)
		# pop.insert(0, SQL)

		# pop.pack()
		
		cur.execute(SQL)
		cur.commit()
		
		SQL = "SELECT * FROM [CMT].[dbo].[Costume] where Costume_Name = '{0}' and Costume_Description = '{1}'".format(self.inputs[0].get(), self.inputs[1].get())
		cur.execute(SQL)
		
		results = cur.fetchone()
		
		insertSQL = """UPDATE [dbo].[Costume] SET [Costume_Image] = ? WHERE Costume_Key = ?"""
		inputimg = list()
		inputimg.append(pypyodbc.Binary(self.inputs[31]))
		inputimg.append(results[0])
		cur.execute(insertSQL, inputimg)
		
		cur.commit()
		
		# SQL = "UPDATE [CMT].[dbo].[Costume] SET       [Costume_Image] = ? WHERE (Costume_name = '"+self.inputs[0].get()+"' AND Costume_Description = '"+self.inputs[1].get()+"'"
		# cur.execute(SQL, self.inputs[31])
		
		# cur.commit()
		cur.close()
		connection.close()
		
		self.master.pack_forget()
		checkin_frame = Frame(self.root, bg='firebrick2')
		checkin_frame.pack()
		add = checkin_class(checkin_frame, self.root, self.my_menu_link, results)
		
		# self.master.destroy()
		#self.my_menu_link.pack()
		
	def insert_dash(string, index):
		output = string[:index] + "\\" + string[index:]
		
		return output
		