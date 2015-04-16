import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
from functools import partial
from editItem import *
import tkinter.messagebox
from connection_info import *


class checkout_class:
	
	def __init__(self, master, root, menu_link, data):
		self.master = master
		self.root = root
		self.data = data
		self.my_menu_link = menu_link
		
		#back button
		self.back_button = ttk.Button(self.master, text = 'Cancel')
		self.back_button.grid(row = 5, column = 0, padx = 3, pady = 3, stick = 'nsw')
		self.back_button.config(command = self.back_button_clicked)
		
		#Done button
		self.done_button = ttk.Button(self.master, text = 'Done')
		self.done_button.grid(row = 5, column = 1, padx = 3, pady = 3, stick = 'nse')
		self.done_button.config(command = self.done_button_clicked)
		
		self.rack_section_label = ttk.Label(self.master, text = "Items Location: ")
		self.rack_explanation_label = ttk.Label(self.master, text = self.getInfo())
		
		self.rack_section_label.grid(row=3, column=0, padx = 0, pady = 10, columnspan = 1, stick = 'nsew')
		self.rack_explanation_label.grid(row=3, column=1, padx = 0, pady = 10, columnspan = 1, stick = 'nsew')
		
		photo = PhotoImage(file = 'black.png')
		# rphoto = PhotoImage(file = 'red.png')
		# bphoto = PhotoImage(file = 'blue.png')
		
		self.image_frame = Frame(master)
		# self.rimage_frame = Frame(master, height = 100, width = 100)
		# self.bimage_frame = Frame(master)
		
		
		self.image_label = ttk.Label(self.image_frame)
		self.image_label.config(image = photo)
		self.image_label.pack()
		self.image_label.pack(side = TOP)
		self.image_label.image = photo
		self.image_frame.grid(row = 0, column = 0, padx = 0, pady = 10, columnspan = 2, stick = 'ns')
		
	def back_button_clicked(self):
		self.master.destroy()
		self.my_menu_link.pack()
		
	def getInfo(self):
		try:
			if(self.data[4] == 34):
				return "Set of Shelves " + self.data[21][0] + " Shelf " + self.data[21][1] + " Box" + self.data[21][2]
			elif(self.data[4] == 26 or self.data[4] == 16):
				return "Row " + self.data[21][0] + self.data[21][1] + " Shelf " + self.data[21][2]
			else:
				return "Row " + self.data[21][0] + self.data[21][1] + " Level " + self.data[21][2] + " Section" + self.data[21][3]
		except Exception as e:
			popup = Tk()
			ttk.Label(popup, text = "location not in correct form, possible corrupt database" + traceback.format_exc()).pack()
			
	def done_button_clicked(self):
		if(self.data[4] == 34):
			self.wig_checkout()
		elif(self.data[4] == 26 or self.data[4] == 16):
			self.shelf_checkout()
		else:
			try:
				cur = sql_info()[0]
				connection = sql_info()[1]
				
				SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 0,[Storage_Location] = '',[Current_Location] = '' WHERE Tag_ID = {0}".format(self.data[1])
				
				cur.execute(SQL)
				cur.commit()
				
				SQL = "UPDATE [CMT].[dbo].[Racks] SET [isfull] = 0 WHERE Name = '{0}'".format(self.data[21])
				
				cur.execute(SQL)
				cur.commit()
				
				cur.close()
				connection.close()
				
				self.master.destroy()
				self.my_menu_link.pack()
			except Exception as e:
				popup = Tk()
				ttk.Label(popup, text = "error updating item location" + str(e)).pack()
			
	def shelf_checkout(self):
		try:
			cur = sql_info()[0]
			connection = sql_info()[1]
			
			SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 0,[Storage_Location] = '',[Current_Location] = '' WHERE Tag_ID = {0}".format(self.data[1])
			
			cur.execute(SQL)
			cur.commit()
				
			SQL = "UPDATE [CMT].[dbo].[Shelves] SET [isfull] = 0 WHERE Name = '{0}'".format(self.data[21])
				
			cur.execute(SQL)
			cur.commit()
			
			cur.close()
			connection.close()
				
			self.master.destroy()
			self.my_menu_link.pack()
		except Exception as e:
			print("error: " + str(e))
			
	def wig_checkout(self):
		try:
			cur = sql_info()[0]
			connection = sql_info()[1]
			
			SQL = "UPDATE [CMT].[dbo].[Costume] SET [Rentable] = 0,[Storage_Location] = '',[Current_Location] = '' WHERE Tag_ID = {0}".format(self.data[1])
			
			cur.execute(SQL)
			cur.commit()
				
			SQL = "UPDATE [CMT].[dbo].[Controlled_Climate] SET [isfull] = 0 WHERE Name = '{0}'".format(self.data[21])
				
			cur.execute(SQL)
			cur.commit()
			
			cur.close()
			connection.close()
				
			self.master.destroy()
			self.my_menu_link.pack()
		except Exception as e:
			print("error: " + str(e))