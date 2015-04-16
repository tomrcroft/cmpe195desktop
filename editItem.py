import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
from tkinter.filedialog import askopenfilename
import os
from connection_info import *
import tkinter.messagebox



class EditItem:
	
	def __init__(self, master, root, menu_link, info):
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
		self.info = info
		
		left_frame = Frame(master, bg='firebrick2')
		left_frame.grid(row=1, column=0, padx = 10, pady = 10, stick = 'nsew')
		right_frame = Frame(master, bg='firebrick2')
		right_frame.grid(row=1, column=1, padx = 10, pady = 10, stick = 'nsew')
		
		#tag
		self.name_label = ttk.Label(master, text = 'ID number: ' + str(self.info[1]),background='firebrick2',font = "Helvetica 24 bold").grid(row=0, column=1, padx = 0, pady = 0, stick = 'nsew')
		# self.name_input = ttk.Label(master, text = self.info[1], font = "Helvetica 16 bold")
		# self.name_input.grid(row=0, column=2, padx = 0, pady = 0, stick = 'nsew')
		
		
		#name
		self.name_label = ttk.Label(left_frame, text = '*Name: ').grid(row=1, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.name_input = ttk.Entry(left_frame, width = 30)
		self.name_input.grid(row=1, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.name_input)
		self.required_inputs.append(self.name_input)
		self.name_input.insert(0, self.info[2])
		
		#description
		self.description_label = ttk.Label(left_frame, text = '*Description: ').grid(row=2, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.description_input = ttk.Entry(left_frame, width = 30)
		self.description_input.grid(row=2, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.description_input)
		self.required_inputs.append(self.description_input)
		self.description_input.insert(0, self.info[3])
		
		#color
		self.color_label = ttk.Label(left_frame, text = '*Color: ').grid(row=3, column=0, padx = 0, pady = 0, stick = 'nsew')
		color = StringVar()
		self.color_input = ttk.Combobox(left_frame, textvariable = color)
		self.color_input.grid(row=3, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.color_list = self.get_colorlist()
		self.color_input.config(values = self.color_list)
		self.inputs.append(color)
		self.required_inputs.append(color)
		color.set(self.convert_color(info[5]))
		
		#type
		self.type_label = ttk.Label(left_frame, text = '*Type: ').grid(row=4, column=0, padx = 0, pady = 0, stick = 'nsew')
		type = StringVar()
		self.type_input = ttk.Combobox(left_frame, textvariable = type)
		self.type_input.grid(row=4, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.type_list = self.get_typelist()
		self.type_input.config(values = self.type_list)
		self.required_inputs.append(type)
		self.inputs.append(type)
		type.set(self.convert_type(info[4]))
		
		#group
		self.group_label = ttk.Label(left_frame, text = 'Group: ').grid(row=5, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.group_input = ttk.Entry(left_frame, width = 30)
		self.group_input.grid(row=5, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.group_input)
		# self.group_input.insert(0, bytes(self.info[6], "utf-8").decode("unicode_escape"))
		# print()
		if(self.info[6] == None):
			self.group_input.insert(0, "")
		else:
			self.group_input.insert(0, self.info[6])
		
		#fabric
		self.fabric_label = ttk.Label(left_frame, text = '*Fabric: ').grid(row=6, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.fabric_input = ttk.Entry(left_frame, width = 30)
		self.fabric_input.grid(row=6, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.fabric_input)
		self.required_inputs.append(self.fabric_input)
		self.fabric_input.insert(0, self.info[7])
		
		#time period
		self.timeperiod_label = ttk.Label(left_frame, text = 'Time Period: ').grid(row=7, column=0, padx = 0, pady = 0, stick = 'nsew')
		self.timeperiod_input = ttk.Entry(left_frame, width = 30)
		self.timeperiod_input.grid(row=7, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.timeperiod_input)
		self.timeperiod_input.insert(0, self.info[8])
		
		#special effects
		self.specialeffects_label = ttk.Label(left_frame, text = 'Special Effects: ').grid(row=8, column=0, padx = 0, pady = 0, stick = 'nsew')
		specialeffect = StringVar()
		self.specialeffects_input = ttk.Combobox(left_frame, textvariable = specialeffect)
		self.specialeffects_input.grid(row=8, column=1, padx = 0, pady = 0, stick = 'nsew')
		self.specialeffects_list = self.get_specialeffects()
		self.specialeffects_input.config(values = self.specialeffects_list)
		self.inputs.append(specialeffect)
		specialeffect.set(self.convert_special_effect(info[9]))
		
		#adult of child
		self.adult_or_child_label = ttk.Label(left_frame, text = '*Adult or Child: ')
		self.adult_or_child_label.grid(row = 9, column = 0, padx = 0, pady = 0, stick = 'nsew')
		adult_or_child = StringVar()
		self.adult_or_child_input = ttk.Combobox(left_frame, textvariable = adult_or_child)
		self.adult_or_child_input.grid(row = 9, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.adult_or_child_input.config(values = ('Adult', 'child'))
		self.inputs.append(adult_or_child)
		self.required_inputs.append(adult_or_child)
		adult_or_child.set(info[10])
		
		#size
		self.size_label = ttk.Label(left_frame, text='*Size: ')
		self.size_label.grid(row = 10, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.size_input = ttk.Entry(left_frame, width = 30)
		self.size_input.grid(row = 10, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.size_input)
		self.required_inputs.append(self.size_input)
		self.size_input.insert(0, info[11])
		
		#gender
		self.gender_label = ttk.Label(left_frame, text = '*Gender: ')
		self.gender_label.grid(row = 11, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.gender_input = ttk.Entry(left_frame, width = 30)
		self.gender_input.grid(row = 11, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.gender_input)
		self.required_inputs.append(self.gender_input)
		self.gender_input.insert(0, info[12])
		
		#designer
		self.designer_label = ttk.Label(left_frame, text='Designer: ')
		self.designer_label.grid(row = 12, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.designer_input = ttk.Entry(left_frame, width = 30)
		self.designer_input.grid(row = 12, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.designer_input)
		self.designer_input.insert(0, self.info[13])
		
		#source
		self.source_label = ttk.Label(left_frame, text='Source: ')
		self.source_label.grid(row = 13, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.source_input = ttk.Entry(left_frame, width = 30)
		self.source_input.grid(row = 13, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.source_input)
		self.source_input.insert(0, self.info[14])
		
		#creation cost
		self.creation_cost_label = ttk.Label(left_frame, text='Creation Cost: ')
		self.creation_cost_label.grid(row = 14, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.creation_cost_input = ttk.Entry(left_frame, width = 30)
		self.creation_cost_input.grid(row = 14, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.creation_cost_input)
		self.must_be_decimal.append(self.creation_cost_input)
		self.creation_cost_input.insert(0, info[16])
		
		#replacement cost
		self.replacement_cost_label = ttk.Label(left_frame, text='*Replacement Cost: ')
		self.replacement_cost_label.grid(row = 15, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.replacement_cost_input = ttk.Entry(left_frame, width = 30)
		self.replacement_cost_input.grid(row = 15, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.replacement_cost_input)
		self.required_inputs.append(self.replacement_cost_input)
		self.must_be_decimal.append(self.replacement_cost_input)
		self.replacement_cost_input.insert(0, info[17])
		
		#rentable
		self.rentable_label = ttk.Label(left_frame, text = '*Rentable: ')
		self.rentable_label.grid(row = 16, column = 0, padx = 0, pady = 0, stick = 'nsew')
		rentable = StringVar()
		if(info[18] == 1):
			rentable.set("Yes")
		elif(info[18] == 0):
			rentable.set("No")
		else:
			popup = Tk()
			ttk.Label(popup, text = "incorrect rentable from DB").pack()
		self.rentable_input = ttk.Combobox(left_frame, textvariable = rentable)
		self.rentable_input.grid(row = 16, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.rentable_input.config(values = ('Yes', 'No'))
		self.inputs.append(rentable)
		self.required_inputs.append(rentable)
		
		
		#rental cost
		self.rental_cost_label = ttk.Label(left_frame, text='*Rental Cost: ')
		self.rental_cost_label.grid(row = 17, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.rental_cost_input = ttk.Entry(left_frame, width = 30)
		self.rental_cost_input.grid(row = 17, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.rental_cost_input)
		self.required_inputs.append(self.rental_cost_input)
		self.must_be_decimal.append(self.rental_cost_input)
		self.rental_cost_input.insert(0, info[19])
		
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
		cleaning_code.set(self.convert_cleaning_code(info[20]))
		
		#needs repair
		self.needs_repair_label = ttk.Label(right_frame, text = 'Needs Repair: ')
		self.needs_repair_label.grid(row = 1, column = 0, padx = 0, pady = 0, stick = 'nsew')
		needs_repair = StringVar()
		if(info[23] == 1):
			needs_repair.set("Yes")
		elif(info[23] == 0):
			needs_repair.set("No")
		else:
			popup = Tk()
			ttk.Label(popup, text = "*incorrect needs repair from DB").pack()
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
		self.repair_description_input.insert(0, self.info[24])
		
		#chest
		self.chest_label = ttk.Label(right_frame, text='Chest: ')
		self.chest_label.grid(row = 3, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.chest_input = ttk.Entry(right_frame, width = 30)
		self.chest_input.grid(row = 3, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.chest_input)
		self.must_be_decimal.append(self.chest_input)
		self.chest_input.insert(0, info[25])
		
		#waist
		self.waist_label = ttk.Label(right_frame, text='Waist: ')
		self.waist_label.grid(row = 4, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.waist_input = ttk.Entry(right_frame, width = 30)
		self.waist_input.grid(row = 4, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.waist_input)
		self.must_be_decimal.append(self.waist_input)
		self.waist_input.insert(0, info[26])
		
		#hips
		self.hips_label = ttk.Label(right_frame, text='Hips: ')
		self.hips_label.grid(row = 5, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.hips_input = ttk.Entry(right_frame, width = 30)
		self.hips_input.grid(row = 5, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.hips_input)
		self.must_be_decimal.append(self.hips_input)
		self.hips_input.insert(0, info[27])
		
		#girth
		self.girth_label = ttk.Label(right_frame, text='Girth: ')
		self.girth_label.grid(row = 6, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.girth_input = ttk.Entry(right_frame, width = 30)
		self.girth_input.grid(row = 6, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.girth_input)
		self.must_be_decimal.append(self.girth_input)
		self.girth_input.insert(0, info[28])
		
		#neck
		self.neck_label = ttk.Label(right_frame, text='Neck: ')
		self.neck_label.grid(row = 7, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.neck_input = ttk.Entry(right_frame, width = 30)
		self.neck_input.grid(row = 7, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.neck_input)
		self.must_be_decimal.append(self.neck_input)
		self.neck_input.insert(0, info[29])
		
		#sleeves
		self.sleeves_label = ttk.Label(right_frame, text='Sleeves: ')
		self.sleeves_label.grid(row = 8, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.sleeves_input = ttk.Entry(right_frame, width = 30)
		self.sleeves_input.grid(row = 8, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.sleeves_input)
		self.must_be_decimal.append(self.sleeves_input)
		self.sleeves_input.insert(0, info[30])
		
		#neck_to_waist
		self.neck_to_waist_label = ttk.Label(right_frame, text='Neck To Waist: ')
		self.neck_to_waist_label.grid(row = 9, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.neck_to_waist_input = ttk.Entry(right_frame, width = 30)
		self.neck_to_waist_input.grid(row = 9, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.neck_to_waist_input)
		self.must_be_decimal.append(self.neck_to_waist_input)
		self.neck_to_waist_input.insert(0, info[31])
		
		#waist_to_hem
		self.waist_to_hem_label = ttk.Label(right_frame, text='Waist To Hem: ')
		self.waist_to_hem_label.grid(row = 10, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.waist_to_hem_input = ttk.Entry(right_frame, width = 30)
		self.waist_to_hem_input.grid(row = 10, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.waist_to_hem_input)
		self.must_be_decimal.append(self.waist_to_hem_input)
		self.waist_to_hem_input.insert(0, info[32])
		
		#inseam
		self.inseam_label = ttk.Label(right_frame, text='Inseam: ')
		self.inseam_label.grid(row = 11, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.inseam_input = ttk.Entry(right_frame, width = 30)
		self.inseam_input.grid(row = 11, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.inseam_input)
		self.must_be_decimal.append(self.inseam_input)
		self.inseam_input.insert(0, info[33])
		
		#notes
		self.notes_label = ttk.Label(right_frame, text='*Notes: ')
		self.notes_label.grid(row = 12, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.notes_input = ttk.Entry(right_frame, width = 30)
		self.notes_input.grid(row = 12, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.notes_input)
		self.required_inputs.append(self.notes_input)
		self.notes_input.insert(0, self.info[34])
		
		#ensemble
		self.ensemble_label = ttk.Label(right_frame, text='Ensemble: ')
		self.ensemble_label.grid(row = 13, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.ensemble_input = ttk.Entry(right_frame, width = 30)
		self.ensemble_input.grid(row = 13, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.inputs.append(self.ensemble_input)
		self.ensemble_input.insert(0, self.info[35])
		
		#image
		self.image_label = ttk.Label(right_frame, text='Image: ')
		self.image_label.grid(row = 14, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.image_button = ttk.Button(right_frame, text='Select Image')
		self.image_button.grid(row = 14, column = 1, padx = 0, pady = 0, stick = 'nsew')
		self.image_button.config(command = self.select_image_function)
		
		#selected image
		self.selected_image = ttk.Label(right_frame, text='Selected Image: ')
		self.selected_image.grid(row = 15, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.selected_image_label = ttk.Entry(right_frame, width= 30)
		self.selected_image_label.grid(row = 15, column = 1, padx = 0, pady = 0, stick = 'nsew')
		# self.selected_image_label.insert(0, "0x89504E470D0A1A0A0000000D49484452000002C8000005990802000000EFBC74FD00")
		self.selected_image_label.insert(0, "no new image")
		self.imageValue = info[36]
		self.inputs.append(self.imageValue)
		self.required_inputs.append(self.selected_image_label)
		#back button
		self.back_button = ttk.Button(left_frame, text = 'Cancel')
		self.back_button.grid(row = 18, column = 0, padx = 0, pady = 10, stick = 'nsew')
		self.back_button.config(command = self.back_button_clicked)
		
		#submit button
		# self.selected_image = ttk.Label(right_frame)
		# self.selected_image.grid(row = 16, column = 0, padx = 0, pady = 0, stick = 'nsew')
		self.submit_button = ttk.Button(right_frame, text = 'Edit')
		self.submit_button.grid(row = 18, column = 1, padx = 0, pady = 30, stick = 'nsew')
		self.submit_button.config(command = self.submit_button_function)
		
		#*explained
		self.selected_image = ttk.Label(self.master, text='*Required Input ')
		self.selected_image.grid(row = 19, column = 1, columnspan = 1, padx = 0, pady = 20, stick = 'nsw')
		
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
		
		if(cur.execute(SQL) == None):
			popup = Tk()
			ttk.Label(popup, text = "Error inserting into DB").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			connection.close()
		else:
			cur.commit()
			cur.close()
			connection.close()
			popup = Tk()
			ttk.Label(popup, text = "Succesful insert!").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			self.master.destroy()
			# new_menu_frame = ttk.Frame(self.root)
			# new_menu_frame.pack()
			# popup = Tk()
			# ttk.Label(popup, text = "wtf").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			# ttk.Label(self.root, text = "wtf").pack()
			#new_menu_link = Menu(new_menu_frame, self.root)
			#self.my_menu_link.pack()
			
	def get_colorlist(self):
		output = list()
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Costume_Color_Key],[Costume_Color] FROM [CMT].[dbo].[Dic_Costume_Color]"
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output.append(str(row[1]))
			
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
			output.append(str(row[1]))
			
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
			output.append(str(row[1]))
			
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
			output.append(str(row[1]))
			
		cur.close()
		connection.close()
		return output
		
	def select_image_function(self):
		self.filename = askopenfilename()
		self.selected_image_label.delete(0, 'end')
		self.selected_image_label.insert(0, self.filename)
		f = open(self.filename, 'rb')
		# ablob = pypyodbc.Binary(f.read())
		img = f.read()
		self.inputs[31] = img
		
		
	def convert_color(self, index):
		output = ""
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Costume_Color] FROM [CMT].[dbo].[Dic_Costume_Color] WHERE Costume_Color_Key = "+str(index)
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output = row[0]
			
		cur.close()
		connection.close()
		return output
		
	def convert_type(self, index):
		output = ""
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Costume_Type] FROM [CMT].[dbo].[Dic_Costume_Type] WHERE Costume_Type_Key = "+str(index)
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output = row[0]
			
		cur.close()
		connection.close()
		return output
	
	def convert_special_effect(self, index):
		output = ""
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Special_Effects] FROM [CMT].[dbo].[Dic_Special_Effects] WHERE Special_Effects_Key = "+str(index)
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output = row[0]
			
		cur.close()
		connection.close()
		return output
		
	def convert_cleaning_code(self, index):
		output = ""
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Cleaning_Code_Description] FROM [CMT].[dbo].[Dic_Cleaning_Codes] WHERE Cleaning_Code = "+str(index)
		cur.execute(SQL)
		
		rows = cur.fetchall()
		for row in rows:
			output = row[0]
			
		cur.close()
		connection.close()
		return output
		
	def submit_button_function(self):
		#u
		
		#check to protect data input size
		for i in range(len(self.inputs) - 1):
			if(isinstance(self.inputs[i], int)):
				if(self.inputs[i] > 10000000000000000):
					# popup = Tk()
					# ttk.Label(popup, text = "An input is over 200 characters, please check and re-try").pack()
					tkinter.messagebox.showwarning("An input is over 200 characters, please check and re-try!")
					return
			else:
				try:
					if(len(self.inputs[i].get()) > 200):
						# popup = Tk()
						# ttk.Label(popup, text = "An input is over 200 characters, please check and re-try").pack()
						tkinter.messagebox.showwarning("Warning","An input is over 200 characters, please check and re-try!")
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
							
				except Exception as e:
					popup = Tk()
					ttk.Label(popup, text = self.inputs[i].get() + str(e)).pack()
		#check if required is not empty
		for i in range(len(self.required_inputs)):
			if(len(self.required_inputs[i].get()) == 0):
				# popup = Tk()
				# ttk.Label(popup, text = "A required input has not been entered, please check and re-try").pack()
				tkinter.messagebox.showwarning("Warning","A required input has not been entered, please check and re-try!")
				return
			if(len(self.selected_image_label.get()) < 1):
				# popup = Tk()
				# ttk.Label(popup, text = "No selected image, please check and re-try").pack()
				tkinter.messagebox.showwarning("Warning","No image selected!")
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
		if(self.inputs[15].get() == "Yes" or self.inputs[15].get() == 1):
			#self.inputs[15] = str(1)
			pass
		elif(self.inputs[15].get() == "No" or self.inputs[15].get() == 0):
			#self.inputs[15] = str(0)
			pass
		else:
			# popup = Tk()
			# ttk.Label(popup, text = "incorrect input for rentable, must be one selected").pack()
			tkinter.messagebox.showwarning("Warning","incorrect input for rentable, must be one selected!")
			return	
		if(self.inputs[18].get() == "Yes" or self.inputs[18].get() == 1):
			#self.inputs[18] = str(1)
			pass
		elif(self.inputs[18].get() == "No" or self.inputs[18].get() == 0):
			#self.inputs[18] = str(0)
			pass
		else:
			# popup = Tk()
			# ttk.Label(popup, text = "incorrect input for needs repair, must be one selected").pack()
			tkinter.messagebox.showwarning("Warning","incorrect input for needs repair, must be one selected!")
			return
		
		
		cur = sql_info()[0]
		connection = sql_info()[1]
		
		
			
		# print(self.info[36])
		# for i in range(len(self.inputs)):
			# if(isinstance(self.inputs[i], int)):
				# print(str(i) +" "+ str(self.inputs[i]))
			# else:
				# print(str(i) +" "+ str(self.inputs[i].get()))
				
		# for i in range(len(self.info)):
			# if(isinstance(self.info[i], int)):
				# print(str(i) +" "+ str(type(self.info[i])))
			# else:
				# print(str(i) +" "+ str(type(self.info[i])))
		SQL = "EXECUTE cmt.[dbo].[Update_Costume] 			@Costume_Key = {31:s}				  ,@Costume_Name = '{0:s}'				  ,@Costume_Description = '{1:s}'				  ,@Costume_Type = '{3:s}' 				  ,@Costume_Color = '{2:s}'			  ,@Costume_Group = '{4:s}'				  ,@Costume_Fabric = '{5:s}'				  ,@Costume_Time_Period = '{6:s}'				  ,@Special_Effects = '{7:s}' 				  ,@Adult_or_Child = '{8:s}'				  ,@Costume_Size = '{9:s}'				  ,@Costume_Gender = '{10:s}'				  ,@Costume_Designer = '{11:s}'				  ,@Costume_Source = '{12:s}'				  ,@Date_Acquired = null				  ,@Creation_or_Buy_Cost = '{13:s}'				  ,@Replacement_Cost = '{14:s}'				  ,@Rentable = '{15:s}'				  ,@Rental_Fee = '{16:s}'				  ,@Cleaning_Code = '{17:s}' 				  ,@Storage_Location = null				  ,@Current_Location = null				  ,@Needs_Repair = '{18:s}'				  ,@Repair_Description = '{19:s}'				  ,@Chest = '{20:s}'				  ,@Waist = '{21:s}'				  ,@Hips = '{22:s}'				  ,@Girth = '{23:s}'				  ,@Neck = '{24:s}'				  ,@Sleeves = '{25:s}'				  ,@Neck_to_Waist = '{26:s}'				  ,@Waist_to_Hem = '{27:s}'				  ,@Inseam = '{28:s}'				  ,@Notes = '{29:s}'				  ,@Ensemble = '{30:s}'				  ,@Costume_Image = null				  ,@Username = null\n				".format(self.inputs[0].get(), self.inputs[1].get(), self.inputs[2].get(), self.inputs[3].get(), self.inputs[4].get(), self.inputs[5].get(), self.inputs[6].get(), self.inputs[7].get(), self.inputs[8].get(), self.inputs[9].get(), self.inputs[10].get(), self.inputs[11].get(), self.inputs[12].get(), self.inputs[13].get(), self.inputs[14].get(), self.inputs[15].get(),self.inputs[16].get(), self.inputs[17].get(), self.inputs[18].get(), self.inputs[19].get(), self.inputs[20].get(), self.inputs[21].get(),self.inputs[22].get(), self.inputs[23].get(), self.inputs[24].get(), self.inputs[25].get(), self.inputs[26].get(), self.inputs[27].get(), self.inputs[28].get(), self.inputs[29].get(), self.inputs[30].get(), str(self.info[0]))

		
		# popup = Tk()
		# pop = ttk.Entry(popup, width = 30)
		# pop.pack()
		# pop.insert(0, SQL)
		
		cur.execute(SQL)
		
		cur.commit()
		
		
		
		insertSQL = """UPDATE [dbo].[Costume] SET [Costume_Image] = ? WHERE Costume_Key = ?"""
		inputimg = list()
		inputimg.append(pypyodbc.Binary(self.inputs[31]))
		inputimg.append(self.info[0])
		cur.execute(insertSQL, inputimg)
		
		cur.commit()
		
		cur.close()
		connection.close()
		
		self.master.destroy()
		self.my_menu_link.pack()
		
	def insert_dash(string, index):
		output = string[:index] + "\\" + string[index:]
		return output
		
	
		