import sys
from tkinter import *
from tkinter import ttk
from Menu import *
import pypyodbc 
import traceback
from connection_info import *
import tkinter.messagebox


# import pymssql


class Login:
	
	#constructor
	#
	def __init__(self, master, root):
		self.master = master
		self.root = root
		
		photo = PhotoImage(file = 'black.png')
		# rphoto = PhotoImage(file = 'red.png')
		# bphoto = PhotoImage(file = 'blue.png')
		
		self.image_frame = Frame(master)
		# self.rimage_frame = Frame(master, height = 100, width = 100)
		# self.bimage_frame = Frame(master)
		
		
		self.image_label = ttk.Label(self.image_frame)
		self.image_label.config(image = photo)
		self.image_label.pack()
		self.image_label.image = photo
		self.image_frame.grid(row = 0, column = 1, padx = 0, pady = 10, columnspan = 1, stick = 'ns')
		
		# self.rimage_label = ttk.Label(self.rimage_frame)
		# self.rimage_label.config(image = rphoto)
		# self.rimage_label.pack()
		# self.rimage_label.image = rphoto
		# self.rimage_frame.grid(row = 0, column = 1, padx = 10, pady = 10, columnspan = 1, stick = 'ns')
		
		# self.bimage_label = ttk.Label(self.bimage_frame)
		# self.bimage_label.config(image = bphoto)
		# self.bimage_label.pack()
		# self.bimage_label.image = bphoto
		# self.bimage_frame.grid(row = 0, column = 2, padx = 10, pady = 10, columnspan = 1, stick = 'ns')
		
		
	
		self.username_label = ttk.Label(master, text = "Username: ").grid(row = 1, column = 0, padx = 0, pady = 10, columnspan = 1, stick = 'nswe')
		#self.username_label.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
		
		self.password_label = ttk.Label(master, text = 'Password: ')
		self.password_label.grid(row=2, column=0, padx = 0, pady = 10, columnspan = 1, stick = 'nswe')
		
		self.login_button = ttk.Button(master, text="Login", command=self.login_function)
		self.login_button.grid(row=3, column= 0, padx = 10, pady = 10, columnspan=3, stick = 'nsew')
		
		self.username_input = ttk.Entry(master, width = 30)
		self.username_input.grid(row=1, column=1, padx = 0, pady = 10, columnspan=2, stick = 'nsew')
		
		self.password_input = ttk.Entry(master, width=30)
		self.password_input.config(show = '*')
		self.password_input.grid(row=2, column=1, padx = 0, pady = 10, columnspan=2, stick = 'nsew')
		
		
	def login_function(self):
		try:
			if((len(self.username_input.get()) == 0)):
				# popup = Tk()
				# ttk.Label(popup, text = "Passwords do not match or you did not enter a password").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
				tkinter.messagebox.showwarning("Warning","Username field empty!")
				return
			
			if((len(self.password_input.get()) == 0)):
				# popup = Tk()
				# ttk.Label(popup, text = "Passwords do not match or you did not enter a password").grid(row=2, column=0, padx = 10, pady = 10, columnspan = 1, stick = 'nsew')
				tkinter.messagebox.showwarning("Warning","Password field empty!")
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
			cur = sql_info()[0]
			connection = sql_info()[1]
			
			SQL = 'select password from cmt..desktop_user WHERE username=\'' + self.username_input.get()+ '\''
			
			cur.execute(SQL)
			row = cur.fetchone()
			if(row == None):
				# popup = Tk()
				# ttk.Label(popup, text = "Username does not exist").pack()
				tkinter.messagebox.showwarning("Warning","Username does not exist!")
			else:
				password = row[0]
				if(password == self.password_input.get()):
					menu_frame = Frame(self.root, bg='firebrick2')
					menu_frame.pack()
					menu = Menu(menu_frame, self.root, self.master)
					self.master.pack_forget()
				else:
					# popup = Tk()
					# ttk.Label(popup, text = "incorrect password").pack()
					tkinter.messagebox.showwarning("Warning","Incorrect Password!")
				cur.close()
				connection.close()
		except Exception as e:
			popup = Tk()
			ttk.Label(popup, text = "DB connection error" + traceback.format_exc()).pack()
			
			
		
		
		
		
def main():

	root = Tk()
	prog = Login(root)
	root.mainloop()

if __name__ == "__main__": main()
