from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.tooltip import ToolTip
from tkinter import filedialog
import sqlite3

class Hilights():
	"""docstring for Hilights"""
	def __init__(self, arg):
		super(Hilights, self).__init__()
		self.arg = arg

	def verse(parent, color, ref, scripture, id_ref):
		def delete_hilight():
			par = top.winfo_children()
			idd = par[1].cget('text')
			conn = sqlite3.connect('hilights.db')
			c = conn.cursor()
			sql = 'DELETE from hilights where ID = ?'
			c.execute(sql, (idd,))
			conn.commit()
			verse_frame.destroy()

		def hover(f1):
			for item in parent.winfo_children():
				item.configure(border = 0, relief = 'solid')
			f1.configure(border =1, relief = 'solid')

		def blur(f1):
			for item in parent.winfo_children():
				item.configure(border = 0, relief = 'solid')

		verse_frame = tk.Frame(parent, background = color, padx = 5, pady =5)
		verse_frame.pack(side = 'top', pady = 5, fill = 'x', expand = 1)
		verse_frame.bind('<Enter>', lambda f1: hover(verse_frame))
		verse_frame.bind('<Leave>', lambda f1: blur(verse_frame))
		verse_frame.configure(background = color)

		top = tk.Frame(verse_frame, background = color)
		top.pack(side = 'top', fill = 'x', expand = 1)
		top.configure(background = color)

		reff = tk.Label(top, background = color, font = ('Arial', 14, 'bold'), text = ref)
		reff.pack(side = 'left')
		reff.configure(background = color, foreground = 'black')

		id_reff = tk.Label(top, background = color, font = ('Arial', 14, 'bold'), text = id_ref, foreground = color)
		id_reff.pack(side = 'left')
		id_reff.configure(background = color, foreground = color)

		rem = tk.Button(top, text = 'X',background = color, border = 1, relief = 'solid', command = delete_hilight)
		rem.pack(side = 'right', padx = 10)
		rem.configure(background = color, cursor = 'hand2', foreground = 'red')
		ToolTip(rem, text = 'Delete hilight')
		#x = lambda: rem.configure(tooltip ='Delete this hilight')

		script = tk.Message(verse_frame, text = scripture, background = color,
		 font = ('roboto', 12), aspect = 200, takefocus = True,
		 justify = 'left')
		script.pack(side = 'top', fill = 'both', expand =1)

		# script = ttk.Label(verse_frame, text = scripture, background = color, font = ('roboto', 12),
		#  justify = 'left', foreground = 'black')
		# script.pack(side = 'top', fill = 'both', expand =1)
		# script.configure(background = color, foreground = 'black')
		ToolTip(script, text = scripture)

class Notes():
	"""docstring for Notes"""
	def __init__(self, arg):
		super(Notes, self).__init__()
		self.arg = arg

	def notes(root, parent, read, ref, title, img1, img2):
		#parent.configure(background = 'white')

		def read_note(e):
			try:
				x = frame.winfo_children()[0]
				tit = x.winfo_children()[0].cget('text')
				conn = sqlite3.connect('hilights.db')
				c = conn.cursor()
				sql = "SELECT NOTES from notes where TITLE = ?"
				result = c.execute(sql, (tit,)).fetchone()
				read.configure(state = 'normal')
				read.delete('1.0', 'end')
				
				read.insert('end', f'{tit}\n\n', ('font'))
				read.insert('end', result[0], ('font1'))

				read.tag_configure('font', font = ('Arial', 16, 'bold'))
				read.tag_configure('font1', font = ('Arial', 12,))
				read.configure(state = 'disabled', padx =10, wrap = 'word')
			except Exception as e:
				pass

		def hover(obj):
			for item in parent.winfo_children():
				item.configure(border = 0, relief = 'solid')
			obj.configure(border = 1, relief = 'solid')

		def blur(obj):
			for item in parent.winfo_children():
				item.configure(border = 0, relief = 'solid')
			obj.configure(border = 0, relief = 'solid')

		def edit_notes(obj):
			def save_notes():
				tl = inp.get()
				txt = text.get('1.0', 'end')
				conn = sqlite3.connect('hilights.db')
				c = conn.cursor()
				sql = "UPDATE notes set TITLE = ?, NOTES = ? where REF = ?"
				c.execute(sql, (tl, txt, tit))
				conn.commit()
				frame.destroy()

			def on_press(event):
				start_x = event.x
				start_y = event.y
				orig_x = root.winfo_x()
				orig_y = root.winfo_y()
				return (orig_x, orig_y)

			def on_drag(event):
				orig_x, orig_y = on_press(event)
				new_x = orig_x + event.x# - start_x
				new_y = orig_y + event.y# - start_y
				#print(event.x, event.y, start_x, start_y)
				frame.place(x = new_x, y = new_y)
			

			x = obj.winfo_children()[0]
			tit = x.winfo_children()[1].cget('text')

			conn = sqlite3.connect('hilights.db')
			c = conn.cursor()
			sql = "SELECT TITLE, NOTES from notes where REF = ? limit 1"
			result = c.execute(sql, (tit,)).fetchone()

			frame = ttk.Label(root, background = 'whitesmoke')
			x_pos, y_pos = root.winfo_pointerxy()
			frame.place(x = x_pos, y = y_pos-400)
			frame.bind('<ButtonPress-1>', on_press)
			frame.bind('<B1-Motion>', on_drag)
			frame.configure(background = 'whitesmoke')

			la = ttk.Label(frame, text = 'Edit notes', font = ('roboto', 16, 'bold'), justify = 'left')
			la.pack(side = 'top', fill = 'x')
			la.configure(background = 'whitesmoke')

			inp = ttk.Entry(frame, font = ('Arial', 18, 'bold'))
			inp.pack(side = 'top', fill = 'x', pady = 20, padx =10)
			inp.insert('end', result[0])

			text = ttk.Text(frame, border = 2, relief = 'sunken', height = 10,
			 padx = 10, pady =10, wrap = 'word', font = ('Arial', 13))
			text.pack(side = 'top', fill = 'both', padx = 10)

			text.insert('end', f"{result[1]}\n\n")

			tool = ttk.Label(frame)
			tool.pack(side = tk.TOP, fill= tk.X)
			tool.configure(background = 'whitesmoke')

			save = ttk.Button(tool, text = 'Save', command = save_notes)
			save.pack(side = 'left', pady =10, padx=10)
			ToolTip(save, text = 'Save notes')

			clo = ttk.Button(tool, text = 'Close', command = frame.destroy)
			clo.pack(side = 'left', padx =10, pady =10)
			ToolTip(clo, text = 'Close without saving')

		def delete_note(obj):
			response = askyesno('Confirm action', 'Are you sure you want to delete the note?')
			if response:
				x = obj.winfo_children()[0]
				tit = x.winfo_children()[0].cget('text')

				conn = sqlite3.connect('hilights.db')
				c = conn.cursor()
				sql = "DELETE from notes where TITLE = ?"
				c.execute(sql, (tit,))
				conn.commit()
				obj.destroy()
			else:
				pass
			
		
		frame = tk.Frame(parent, background = 'white', pady =3)
		frame.pack(side = 'top', fill='x', pady =5)
		frame.bind('<Enter>', lambda obj: hover(frame))
		frame.bind('<Leave>', lambda obj: blur(frame))
		frame.bind('<Button-1>', read_note)
		#parent.configure(background = 'whitesmoke')
		

		tf = tk.Frame(frame, background = 'white')
		tf.pack(side = 'left', fill = 'x', anchor = W)

		label = tk.Label(tf, text = title, background = 'white', font = ('roboto', 13), justify = LEFT)
		label.pack(side = 'top', padx = 5, anchor = W)
		label.bind('<Button-1>', read_note)

		fr = ttk.Label(tf, text = ref, font = ('roboto', 11), foreground = 'gray', justify = LEFT)
		fr.pack(side = 'top', padx = 5, anchor = W)
		fr.configure(foreground = 'gray')
		fr.bind('<Button-1>', read_note)

		ttf = tk.Frame(frame, background = 'white')
		ttf.pack(side = 'right', fill = 'x')

		rem = ttk.Button(ttf, text = '', image = img1, style = 'button.TButton')
		rem.pack(side = 'right', padx = 5)
		rem.bind('<Button-1>', lambda obj: delete_note(frame))
		ToolTip(rem, text = 'Delete notes')

		edit = ttk.Button(ttf, text = '', image = img2, style = 'button.TButton')
		edit.pack(side = 'right', padx = 5)
		edit.bind('<Button-1>', lambda obj: edit_notes(frame))
		ToolTip(edit, text = 'Edit notes')
		
