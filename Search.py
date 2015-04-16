import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
from functools import partial
from editItem import *
import tkinter.messagebox
from connection_info import *


class search_class:
	
	def __init__(self, master, root, menu_link):
		self.master = master
		self.root = root
		self.my_menu_link = menu_link
		self.results = list()
		self.start_index = 0
		self.result_frame = Frame(self.master,  height = 350, width = 700,borderwidth=5,relief=GROOVE)
		self.result_frame.grid(row = 1, column = 0,columnspan = 3, padx = 10, pady = 10, stick = 'nsew')
		
		self.search_button = ttk.Button(master, text="Search", command=self.search_process_function)
		self.search_button.grid(row=0, column= 2, padx = 10, pady = 10, stick = 'nsew')
		
		self.back_button = ttk.Button(master, text = 'Back', command = self.back_button_clicked)
		self.back_button.grid(row = 3, column = 0, columnspan = 3, padx = 10, pady = 10, stick = 'nsew')
		
		self.prev_button = ttk.Button(master, text = 'Previous', command = self.previous_button_clicked)
		self.prev_button.grid(row = 2, column = 0, columnspan = 1, padx = 10, pady = 10, stick = 'w')
		
		self.next_button = ttk.Button(master, text = 'Next', command = self.next_button_clicked)
		self.next_button.grid(row = 2, column = 2, columnspan = 1, padx = 10, pady = 10, stick = 'e')
		
		self.search_input = ttk.Entry(master, width = 30)
		self.search_input.grid(row=0, column=0,columnspan = 1, padx = 10, pady = 10, stick = 'nsw')
		
		self.category = StringVar()
		self.category_input = ttk.Combobox(master, textvariable = self.category)
		self.category_input.grid(row = 0, column = 1, padx = 10, pady = 10, stick = 'nsew')
		self.category_input.config(values = ('All', 'Group', 'Accessories', 'Belt', 'Bloomers', 'Blouse', 'Bodice', 'Bra', 'Breeches / Knickers', 'Cape', 'Coat', 'Collar / Jabbot', 'Crown / Tiara', 'Cuffs', 'Cumberbund', 'Dance Dress - Leotard', 'Dress', 'Hat', 'Jacket', 'Leotard', 'Other', 'Panier / Bustle', 'Pants / Sacks', 'Robe', 'Romantic Tutu', 'Scarf', 'Shirt', 'Shoes', 'Skirt', 'Suit Jacket', 'Tie', 'Tights', 'Tutu', 'Unitard / Jumpsuit', 'Vest', 'Wig'))
		
	def back_button_clicked(self):
		self.master.destroy()
		self.my_menu_link.pack()
		
	def search_process_function(self):	
		self.result_frame.destroy()
		self.result_frame = Frame(self.master, height = 350, width = 700,borderwidth=5,relief=GROOVE)
		self.result_frame.grid_propagate(False)
		self.result_frame.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, stick = 'nsew')
		self.current_result_desc = []
		self.result_buttons = list()
		self.start_index = 0;
	
		cur = sql_info()[0]
		connection = sql_info()[1]
		
		SQL = self.get_SQL()
		
		
		cur.execute(SQL)
		
		self.results = cur.fetchall()

		if(len(self.results) == 0):
			tkinter.messagebox.showwarning("Warning","No results found")
			return
		self.result_name_column = ttk.Label(self.result_frame, text = "Name", background='white')
		self.result_desc_column = ttk.Label(self.result_frame, text = "Description", background='white')
		self.result_select_column = ttk.Label(self.result_frame, text = "More Info", background='white')
		self.result_name_column.grid(row=0, column=0, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
		self.result_desc_column.grid(row=0, column=1, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
		self.result_select_column.grid(row=0, column= 2, padx = 0,columnspan = 2,pady = 0, stick = 'nsew')

		for i in range(10):
			if i > (len(self.results) - 1):
				break
			self.current_result_name = ttk.Label(self.result_frame,width = 30, text = self.results[self.start_index + i][2], wraplength = 100)
			self.current_result_desc = ttk.Label(self.result_frame,width = 60, text = self.results[self.start_index + i][3], wraplength = 350)
			self.select_button = ttk.Button(self.result_frame, text="Edit/View", command=partial(self.select_process_function, self.results[self.start_index + i]))
			self.delete_button = ttk.Button(self.result_frame, text="Delete", command=partial(self.delete_process_function, self.results[self.start_index + i]))
			self.delete_button.grid(row=i+1, column= 3, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
			self.current_result_name.grid(row=i +1, column=0, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
			self.current_result_desc.grid(row=i +1, column=1, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
			self.select_button.grid(row=i+1, column= 2, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')

		self.prev_button.config(state = 'disabled')
		if(len(self.results) < 11):
			self.next_button.config(state = 'disabled')
		else:
			self.next_button.config(state = 'normal')
		
		cur.close()
		connection.close()
		
	def get_SQL(self):
		SQL = ""
		if((self.category.get() == 'All') or (len(self.category.get()) == 0)):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0"
		elif(self.category.get() == 'Group'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE Costume_Group LIKE '%"+self.search_input.get()+"%' AND Source_Deleted = 0"
		elif(self.category.get() == 'Accessories'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 1"
		elif(self.category.get() == 'Belt'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 2"
		elif(self.category.get() == 'Bloomers'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 3"
		elif(self.category.get() == 'Blouse'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 4"
		elif(self.category.get() == 'Bodice'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 5"
		elif(self.category.get() == 'Bra'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 6"
		elif(self.category.get() == 'Breeches / Knickers'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 7"
		elif(self.category.get() == 'Cape'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 8"
		elif(self.category.get() == 'Coat'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 9"
		elif(self.category.get() == 'Collar / Jabbot'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 10"
		elif(self.category.get() == 'Crown / Tiara'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 11"
		elif(self.category.get() == 'Cuffs'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 12"
		elif(self.category.get() == 'Cumberbund'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 13"
		elif(self.category.get() == 'Dance Dress - Leotard'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 14"
		elif(self.category.get() == 'Dress'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 15"
		elif(self.category.get() == 'Hat'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 16"
		elif(self.category.get() == 'Jacket'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 17"
		elif(self.category.get() == 'Leotard'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 18"
		elif(self.category.get() == 'Other'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 19"
		elif(self.category.get() == 'Panier / Bustle'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 20"
		elif(self.category.get() == 'Pants / Sacks'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 21"
		elif(self.category.get() == 'Robe'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 22"
		elif(self.category.get() == 'Romantic Tutu'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 23"
		elif(self.category.get() == 'Scarf'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 24"
		elif(self.category.get() == 'Shirt'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 25"
		elif(self.category.get() == 'Shoes'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 26"
		elif(self.category.get() == 'Skirt'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 27"
		elif(self.category.get() == 'Suit Jacket'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 28"
		elif(self.category.get() == 'Tie'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 29"
		elif(self.category.get() == 'Tights'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 30"
		elif(self.category.get() == 'Tutu'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 31"
		elif(self.category.get() == 'Unitard / Jumpsuit'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 32"
		elif(self.category.get() == 'Vest'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 33"
		elif(self.category.get() == 'Wig'):
			SQL = "SELECT top 100 * FROM [dbo].[Costume] WHERE (Costume_Name LIKE '%"+self.search_input.get()+"%' OR Costume_Description LIKE '%"+self.search_input.get()+"%') AND Source_Deleted = 0 AND Costume_Type_Key = 34"
		else:
			tkinter.messagebox.showwarning("Warning","The search category input in incorrect")
			return
		return SQL
		
	def delete_process_function(self, row):
		result = tkinter.messagebox.askquestion("Delete", "Are You Sure?")
		if result == 'yes':
			cur = sql_info()[0]
			connection = sql_info()[1]

			SQL = "EXECUTE cmt.[dbo].[Delete_Costume] @Costume_Key = {0}, @Username = 'Warehouse Computer', @Is_Deleted = yes".format(row[0])
			# popup = Tk()
			# pop = ttk.Entry(popup, width = 30)
			# pop.insert(0, SQL)

			# pop.pack()
			cur.execute(SQL)
			
			cur.commit()
			cur.close()
			connection.close()
		else:
			pass
		
	def select_process_function(self, row):
		#print(str(id))
		self.master.pack_forget()
		search_frame = Frame(self.root, bg='firebrick2')
		search_frame.pack()
		add = EditItem(search_frame, self.root, self.my_menu_link, row)
		
	def previous_button_clicked(self):
		self.next_button.config(state = 'normal')
		self.result_frame.destroy()
		self.result_frame = Frame(self.master, height = 350, width = 700,borderwidth=5,relief=GROOVE)
		self.result_frame.grid_propagate(False)
		self.result_frame.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, stick = 'nsew')
		self.current_result_desc = []
		self.result_buttons = list()
		if(self.start_index == 9):
			self.start_index -= 9
			self.prev_button.config(state = 'disabled')
		else:
			self.start_index -= 10
			
		self.result_name_column = ttk.Label(self.result_frame, text = "Name", background='white')
		self.result_desc_column = ttk.Label(self.result_frame, text = "Description", background='white')
		self.result_select_column = ttk.Label(self.result_frame, text = "More Info", background='white')
		self.result_name_column.grid(row=0, column=0, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
		self.result_desc_column.grid(row=0, column=1, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
		self.result_select_column.grid(row=0, column= 2, padx = 0,columnspan = 2,pady = 0, stick = 'nsew')
		
		for i in range(10):
			self.current_result_name = ttk.Label(self.result_frame,width = 30, text = self.results[self.start_index + i][2], wraplength = 100)
			self.current_result_desc = ttk.Label(self.result_frame,width = 60, text = self.results[self.start_index + i][3], wraplength = 350)
			self.select_button = ttk.Button(self.result_frame, text="Edit/View", command=partial(self.select_process_function, self.results[self.start_index + i]))
			self.delete_button = ttk.Button(self.result_frame, text="Delete", command=partial(self.delete_process_function, self.results[self.start_index + i]))
			self.delete_button.grid(row=i+1, column= 3, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
			self.current_result_name.grid(row=i +1, column=0, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
			self.current_result_desc.grid(row=i +1, column=1, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
			self.select_button.grid(row=i+1, column= 2, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
		
	def next_button_clicked(self):
		# print(type(self.prev_button['state']))
		# if (not (self.start_index - i < 0)):
			# print("there")
			# self.prev_button['state'] = 'normal'
		# print(self.prev_button['state'])

		self.result_frame.destroy()
		self.result_frame = Frame(self.master, height = 350, width = 700,borderwidth=5,relief=GROOVE)
		self.result_frame.grid_propagate(False)
		self.result_frame.grid(row = 1, column = 0, columnspan = 3, padx = 10, pady = 10, stick = 'nsew')
		self.current_result_desc = []
		self.result_buttons = list()
		if(self.start_index == 0):
			self.start_index += 9
		else:
			self.start_index += 10
			
		self.result_name_column = ttk.Label(self.result_frame, text = "Name", background='white')
		self.result_desc_column = ttk.Label(self.result_frame, text = "Description", background='white')
		self.result_select_column = ttk.Label(self.result_frame, text = "More Info", background='white')
		self.result_name_column.grid(row=0, column=0, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
		self.result_desc_column.grid(row=0, column=1, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
		self.result_select_column.grid(row=0, column= 2, padx = 0,columnspan = 2,pady = 0, stick = 'nsew')
			
		for i in range(10):
			if self.start_index + i > (len(self.results) - 1):
				self.next_button.config(state = 'disabled')
				break
			if(self.start_index > 0):
				self.prev_button.config(state = 'enabled')
			self.current_result_name = ttk.Label(self.result_frame,width = 30, text = self.results[self.start_index + i][2], wraplength = 100)
			self.current_result_desc = ttk.Label(self.result_frame, width = 60, text = self.results[self.start_index + i][3], wraplength = 350)
			self.select_button = ttk.Button(self.result_frame, text="Edit/View", command=partial(self.select_process_function, self.results[self.start_index + i]))
			self.delete_button = ttk.Button(self.result_frame, text="Delete", command=partial(self.delete_process_function, self.results[self.start_index + i]))
			self.delete_button.grid(row=i+1, column= 3, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
			self.current_result_name.grid(row=i +1, column=0, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
			self.current_result_desc.grid(row=i +1, column=1, padx = 0, pady = 0, columnspan = 1, stick = 'nsew')
			self.select_button.grid(row=i+1, column= 2, columnspan = 1, padx = 0, pady = 0, stick = 'nsew')
		
		
		