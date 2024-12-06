from tkinter import *
import tkinter as tk
from tkinter import ttk
# import customtkinter as ctk
from tkinter.messagebox import *
from tkinter import filedialog
import sqlite3
import os
import csv
from pathlib import Path
import shutil
import appdirs

class Ttext(Toplevel):
	"""docstring for Cvs"""
	def __init__(self):
		super().__init__()
		self.title('Easy Bible - Export notes to cvs')
		#self.geometry('600x400')
		book_img = PhotoImage(file = 'icons/eb.png')
		self.attributes('-topmost', True)
		self.resizable(False, False)
		self.iconphoto(False, book_img)

		frame = ttk.Frame(self)
		frame.pack(fill = 'both', expand = 1, ipadx = 20, ipady = 20)

		label = ttk.Label(frame, text = 'Notes to Text file (.txt)', font = ('Roboto', 24))
		label.pack(side = 'top', fill = 'x', pady = 20)

		form = ttk.Frame(frame)
		form.pack(side = 'top', fill = 'both', expand = 1)

		mytext = """Text file is simple text data without formating but can be very useful. Just like csv files, text files can easily be accessed and programed to produce powerful things. With this application, we decided to export the notes to text format file because they can be reused. In the next release, you will be able to share your notes with friends in a simple text file but when they open it with this application, everything will be fitted just as it appears to you in your computer where you can access them verse by verse."""

		label1 = tk.Message(form, aspect = 400, justify = 'left',
		 text = mytext, font = ('Roboto', 12), background = 'white')
		label1.pack(fill = 'both', side = 'top', expand =1)


		buttons = ttk.Frame(frame)
		buttons.pack(side = 'top', fill = 'x')

		export = ttk.Button(buttons, text = 'Export', command = self.export_file)
		export.pack(side = 'right', pady = 5, padx = 10)

		close = ttk.Button(buttons, text = 'Cancel', command = self.destroy)
		close.pack(side = 'right', pady = 5, padx = 10)


	def export_file(self):
		def db_path():

			try:
				# Get the AppData directory path
				appdata_path = Path(os.getenv('APPDATA'))

				# Create a directory for your application
				app_dir = appdata_path / 'EasyBible'
				app_dir.mkdir(parents=True, exist_ok=True)

				try:
					shutil.copy2('hilights.db', app_dir)
					file_path = app_dir / 'hilights.db'
				except Exception as e:
					return app_dir / 'hilights.db'
				return app_dir/'hilights.db'
			except Exception as e:
				app_dir = appdirs.user_data_dir('EasyBible', 'HCC')
				path = Path(app_dir)
				shutil.copy2(db, path)
				file_path = path / db
				return file_path
		try:
			file_name = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[('Text file','*.txt')])
			conn = sqlite3.connect(db_path())
			c = conn.cursor()
			sql = "SELECT REF, TITLE, NOTES from notes"
			result = c.execute(sql).fetchall()

			with open(file_name, 'w') as file:
			    
			    for row in result:
			    	file.write( 'REF\n')
			    	file.write(row[0] + '\n')
			    	file.write( 'TITLE\n')
			    	file.write(row[1] + '\n')
			    	file.write( 'NOTES\n')
			    	file.write(row[2] + '\n')
			    	file.write( 'END\n')

			showinfo('Notice', f'Your notes were exported to Text file to\n {file_name}\n successfully.')                          
			self.destroy()
		except Exception as e:
			showerror('', f'Failed to save Text file! Please try again.\n{e}')
			self.attributes('-topmost', True)