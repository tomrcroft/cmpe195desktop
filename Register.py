import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
from connection_info import *
import tkinter.messagebox


class Register:
	
	def __init__(self, master, root, menu_link):
		self.master = master
		self.root = root
		self.my_menu_link = menu_link
		
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
		
		self.username_label = ttk.Label(master, text = "Username: ")
		self.username_label.grid(row = 1, column = 0, padx = 0, pady = 10, columnspan = 1, stick = 'nsew')
		
		self.password_label = ttk.Label(master, text = 'Password: ')
		self.password_label.grid(row=2, column=0, padx = 0, pady = 10, columnspan = 1, stick = 'nsew')
		
		self.login_button = ttk.Button(master, text="Register", command=self.register_process_function)
		self.login_button.grid(row=4, column= 1, padx = 10, pady = 10, stick = 'nsew')
		
		self.back_button = ttk.Button(master, text = 'Back', command = self.back_button_clicked)
		self.back_button.grid(row = 4, column = 0, padx = 10, pady = 10, stick = 'nsew')
		
		self.username_input = ttk.Entry(master, width = 30)
		self.username_input.grid(row=1, column=1, padx = 0, pady = 10, stick = 'nsew')
		
		self.password_input = ttk.Entry(master, width=30)
		self.password_input.config(show = '*')
		self.password_input.grid(row=2, column=1, padx = 0, pady = 10, stick = 'nsew')
		
		self.repeat_password_input = ttk.Entry(master, width=30)
		self.repeat_password_input.config(show = '*')
		self.repeat_password_input.grid(row=3, column=1, padx = 0, pady = 10, stick = 'ns')
		
		self.repeat_password_label = ttk.Label(master, text = 'Repeat Password: ')
		self.repeat_password_label.grid(row=3, column=0, padx = 0, pady = 10, columnspan = 1, stick = 'nsew')
		
	def back_button_clicked(self):
		# menu_frame = ttk.Frame(self.root)
		# menu_frame.pack()
		# menu_link = Menu(menu_frame, self.root)
		self.master.destroy()
		self.my_menu_link.pack()
		
	def register_process_function(self):
		if((len(self.username_input.get()) == 0)):
			# popup = Tk()
			# ttk.Label(popup, text = "Passwords do not match or you did not enter a password").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			tkinter.messagebox.showwarning("Warning","Username field empty!")
			return
	
		if(len(self.username_input.get()) > 200):
			# popup = Tk()
			# ttk.Label(popup, text = "Username input is too large").pack()
			tkinter.messagebox.showwarning("Warning","Username input is too large!")
			return
		if(len(self.password_input.get()) > 200):
			# popup = Tk()
			# ttk.Label(popup, text = "Password input is too large").pack()
			tkinter.messagebox.showwarning("Warning","Password input is too large!")
			return
			
		if(len(self.repeat_password_input.get()) > 200):
			# popup = Tk()
			# ttk.Label(popup, text = "Repeat password input is too large").pack()
			tkinter.messagebox.showwarning("Warning","Repeat password is too large!")
			return
			
		if((len(self.password_input.get()) == 0)):
			# popup = Tk()
			# ttk.Label(popup, text = "Passwords do not match or you did not enter a password").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			tkinter.messagebox.showwarning("Warning","Password field empty!")
			return
			
		if((self.password_input.get() != self.repeat_password_input.get())):
			# popup = Tk()
			# ttk.Label(popup, text = "Passwords do not match or you did not enter a password").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			tkinter.messagebox.showwarning("Warning","Password field does not match repeat password!")
			return
	
		cur = sql_info()[0]
		connection = sql_info()[1]

		SQL = "SELECT [Username] FROM [CMT].[dbo].[Desktop_User] WHERE username='"+self.username_input.get()+"'"
		cur.execute(SQL)
		row = cur.fetchone()
		if(row != None):
			# popup = Tk()
			# ttk.Label(popup, text = "Username already exists!").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			tkinter.messagebox.showwarning("Warning","Username already exists!")
			return
			
		SQL = "EXECUTE cmt.[dbo].[Add_Or_Update_Desktop_User] @Username = '"+ self.username_input.get() +"',@Password = \'"+self.password_input.get()+"'"
		
		cur = connection.cursor()
		if(cur.execute(SQL) == None):
			# popup = Tk()
			# ttk.Label(popup, text = "Error inserting into DB").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			tkinter.messagebox.showwarning("Error inserting into DB!")
			connection.close()
		else:
			cur.commit()
			cur.close()
			connection.close()
			# popup = Tk()
			# ttk.Label(popup, text = "Succesful registration!").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			tkinter.messagebox.showwarning("Warning","Successful registration!")
			self.master.destroy()
			# new_menu_frame = ttk.Frame(self.root)
			# new_menu_frame.pack()
			# popup = Tk()
			# ttk.Label(popup, text = "wtf").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
			# ttk.Label(self.root, text = "wtf").pack()
			#new_menu_link = Menu(new_menu_frame, self.root)
			self.my_menu_link.pack()
			