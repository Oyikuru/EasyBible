from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from tkinter import filedialog
#import matplotlib.font_manager
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
from tkinter import filedialog
from ttkbootstrap.tooltip import ToolTip
import sqlite3
import os
import json
import sys
import winreg
import platform
import plistlib

#import imageio
#import threading

class Collection():
	"""docstring for Collection"""
	def __init__(self, family, styles, font):
		super(Collection, self).__init__()
		self.family = family
		self.styles = styles
		self.font = font
		self.color = color
		self.underline = underline
		self.justify = justify
		self.img = img
		self.img_ref = img_ref
		self.file_name = file_name
		self.file_dir = file_dir
		self.object_id = object_id
		

	def tools(root, parent, editor, imgs):
		Collection.family = 'Calibri'
		Collection.styles = 'Paragraph'
		Collection.font = (Collection.family, 14, 'normal', 'roman')
		frame = tk.Frame(parent, background = 'whitesmoke', cursor = 'arrow', pady = 1)
		frame.pack(side = 'top', fill = 'x')

		def selection(e):
			try:
				highlighted = editor.get(SEL_FIRST, SEL_LAST)
				pos = editor.search(highlighted, '1.0')
				end = f"{pos} + {len(highlighted)}c"
				editor.tag_add('sel', pos, end)
				try:
					font = editor.tag_cget(highlighted, 'font')
					Collection.font = font
				except Exception as e:
					Collection.font = ('Calibri', 14, 'normal', 'roman')
			except Exception as e:
				pass

		#editor.bind('<<Selection>>', selection)

		def change_font(e):
			ff = font.get()
			Collection.family = ff
			f_type = Collection.styles
			data = []
			for i in Collection.font:
				data.append(i)
			data[0] = ff

			if f_type == 'Heading 1':
				data[1] = 24
				data[2] = 'bold'
			elif f_type == 'Heading 2':
				data[1] = 22
				data[2] = 'bold'
			elif f_type == 'Heading 3':
				data[1] = 20
				data[2] = 'bold'
			elif f_type == 'Heading 4':
				data[1] = 18
				data[2] = 'bold'
			elif f_type == 'Heading 5':
				data[1] = 16
				data[2] = 'bold'
			elif f_type == 'Heading 6':
				data[1] = 14
				data[2] = 'bold'
			else:
				data[1] = 14
				data[2] = 'normal'

			Collection.font = data
			Collection.styles = data[1]
			Collection.font = data
			
			try:
				highlighted = editor.get(SEL_FIRST, SEL_LAST)
				pos = editor.search(highlighted, '1.0')
				end = f"{pos} + {len(highlighted)}c"
				#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
				editor.tag_add(f'selected{pos}', pos, end)
				editor.tag_configure(f'selected{pos}', font = Collection.font,
				 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

				
			except Exception as e:
				showerror('', 'No text was selected.\n Please select to continue.')

		
		#fonts= matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext = 'ttf')
		#font_n ={matplotlib.font_manager.FontProperties(fname = font_file).get_name() for font_file in fonts}
		
		font_names = ['Agency', 'Algerian', 'Arial', 'Bahnschrift',
		 'Broadway', 'Calibri', 'Cambria', 'Candara', 'Castellar', 
		 'Centaur', 'Century', 'Chiller', 'Consolas', 'Constantia', 'Corbel', 'Dubai',
		 'Ebrima', 'Elephant', 'Forte', 'Gabriola', 'Gadugi', 
		 'Garamond', 'Georgia', 'Gigi', 'Haettenschweiler',
		  'Harrington', 'Impact', 'Jokerman', 'Leelawadee', 'Magneto',
		   'MingLiU-ExtB', 'Mistral','Onyx', 'Papyrus', 'Parchment', 
		   'Perpetua', 'Playbill', 'Pristina', 'Ravie', 'Rockwell',
		    'SimSun', 'SimSun-ExtB', 'Stencil', 'Sylfaen', 'Symbol', 
		     'Tahoma', 'Verdana', 'Vivaldi', 'Webdings', 'Wingdings']


		font = ttk.Combobox(frame, values = font_names, state = 'readonly', height = 30, width =15)
		font.pack(side = 'left', padx = 2, pady = 2)
		font.set(Collection.family)
		font.bind('<<ComboboxSelected>>', change_font)
		ToolTip(font, text = 'Text font')

		def font_type(e):
			f_type = sty.get()
			#ff = Collection.family

			data = []
			for i in Collection.font:
				data.append(i)
			data[1] = 14

			if f_type == 'Heading 1':
				data[1] = 24
				data[2] = 'bold'
			elif f_type == 'Heading 2':
				data[1] = 22
				data[2] = 'bold'
			elif f_type == 'Heading 3':
				data[1] = 20
				data[2] = 'bold'
			elif f_type == 'Heading 4':
				data[1] = 18
				data[2] = 'bold'
			elif f_type == 'Heading 5':
				data[1] = 16
				data[2] = 'bold'
			elif f_type == 'Heading 6':
				data[1] = 14
				data[2] = 'bold'
			else:
				data[1] = 14
				data[2] = 'normal'

			Collection.font = data
			Collection.styles = data[1]
			#Collection.color = 'black'
			#Collection.underline = 0
			#Collection.justify = 'left'

			
			try:
				highlighted = editor.get(SEL_FIRST, SEL_LAST)
				pos = editor.search(highlighted, '1.0')
				end = f"{pos} + {len(highlighted)}c"
				#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
				editor.tag_add(f'selected{pos}', pos, end)
				editor.tag_configure(f'selected{pos}', font = Collection.font,
				 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

				
			except Exception as e:
				showerror('', 'No text was selected.\n Please select to continue.')

		styles = ['Heading 1', 'Heading 2', 'Heading 3', 'Heading 4', 'Heading 5', 'Heading 6', 'Paragraph']
		sty = ttk.Combobox(frame, values = styles, state = 'readonly', width =9)
		sty.pack(side = 'left', padx = 2, pady = 2)
		sty.set(styles[0])
		sty.bind('<<ComboboxSelected>>', font_type)
		ToolTip(sty, text = 'Text style:\n H1, H2, H3, H4, H5, H6 or Paragraph')

		def toggle_bold():
			if var_bold.get() == 1:
				data = []
				for i in Collection.font:
					data.append(i)
				data[2] = 'bold'
				Collection.font = data
				#Collection.color = 'black'
				#Collection.underline = 0
				#Collection.justify = 'left'
				
				try:
					highlighted = editor.get(SEL_FIRST, SEL_LAST)
					pos = editor.search(highlighted, '1.0')
					end = f"{pos} + {len(highlighted)}c"
					#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
					editor.tag_add(f'selected{pos}', pos, end)
					editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

					
				except Exception as e:
					showerror('', 'No text was selected.\n Please select to continue.')
			else:
				data = []
				for i in Collection.font:
					data.append(i)
				data[2] = 'normal'
				Collection.font = data
				#Collection.color = 'black'
				#Collection.underline = 0
				#Collection.justify = 'left'
				try:
					highlighted = editor.get(SEL_FIRST, SEL_LAST)
					pos = editor.search(highlighted, '1.0')
					end = f"{pos} + {len(highlighted)}c"
					#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
					editor.tag_add(f'selected{pos}', pos, end)
					editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

					
				except Exception as e:
					showerror('', 'No text was selected.\n Please select to continue.')

		def toggle_italic():
			if var_italic.get() == 1:
				data = []
				for i in Collection.font:
					data.append(i)
				data[3] = 'italic'
				Collection.font = data
				#Collection.color = 'black'
				#Collection.underline = 0
				#Collection.justify = 'left'
				
				try:
					highlighted = editor.get(SEL_FIRST, SEL_LAST)
					pos = editor.search(highlighted, '1.0')
					end = f"{pos} + {len(highlighted)}c"
					#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
					editor.tag_add(f'selected{pos}', pos, end)
					editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

					
				except Exception as e:
					showerror('', 'No text was selected.\n Please select to continue.')
			else:
				data = []
				for i in Collection.font:
					data.append(i)
				data[3] = 'roman'
				Collection.font = data
				#Collection.color = 'black'
				#Collection.underline = 0
				#Collection.justify = 'left'
				
				try:
					highlighted = editor.get(SEL_FIRST, SEL_LAST)
					pos = editor.search(highlighted, '1.0')
					end = f"{pos} + {len(highlighted)}c"
					#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
					editor.tag_add(f'selected{pos}', pos, end)
					editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

					
				except Exception as e:
					showerror('', f'No text was selected.\n Please select to continue.')
					
		def toggle_underline():
			if var_underline.get() == 1:
				#Collection.font = data
				#Collection.color = 'black'
				Collection.underline = 1
				#Collection.justify = 'left'
				
				try:
					highlighted = editor.get(SEL_FIRST, SEL_LAST)
					pos = editor.search(highlighted, '1.0')
					end = f"{pos} + {len(highlighted)}c"
					#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
					editor.tag_add(f'selected{pos}', pos, end)
					editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

					
				except Exception as e:
					showerror('', f'No text was selected.\n Please select to continue.')

			else:
				#Collection.font = data
				#Collection.color = 'black'
				Collection.underline = 0
				#Collection.justify = 'left'
				try:
					highlighted = editor.get(SEL_FIRST, SEL_LAST)
					pos = editor.search(highlighted, '1.0')
					end = f"{pos} + {len(highlighted)}c"
					#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
					editor.tag_add(f'selected{pos}', pos, end)
					editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

					
				except Exception as e:
					showerror('', f'No text was selected.\n Please select to continue.')
		

		bold_text = ttk.Menubutton(frame, text = 'Text style', style = 'menubutton.TMenubutton')
		bold_text.pack(side = 'left')
		ToolTip(bold_text, text = 'Text style; Bold, Italic, Underline')

		var_bold = tk.IntVar()
		var_italic = tk.IntVar()
		var_underline = tk.IntVar()
		#var_hilight = tk.IntVar()

		items = Menu(tearoff = 0)
		items.add_checkbutton(label = 'Bold', variable = var_bold, command = toggle_bold)
		items.add_checkbutton(label = 'Italic', variable = var_italic, command = toggle_italic)
		items.add_checkbutton(label = 'Underlined', variable = var_underline, command = toggle_underline)
		#items.add_checkbutton(label = 'Hilight')
		bold_text.configure(menu = items)

		def left_align():
			#Collection.font = data
			#Collection.color = 'black'
			#Collection.underline = 0
			Collection.justify = 'left'
			try:
				highlighted = editor.get(SEL_FIRST, SEL_LAST)
				pos = editor.search(highlighted, '1.0')
				end = f"{pos} + {len(highlighted)}c"
				#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
				editor.tag_add(f'selected{pos}', pos, end)
				editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

				
			except Exception as e:
				showerror('', 'No text was selected.\n Please select to continue.')

		def center_align():
			#Collection.font = data
			#Collection.color = 'black'
			#Collection.underline = 0
			Collection.justify = 'center'
			try:
				highlighted = editor.get(SEL_FIRST, SEL_LAST)
				pos = editor.search(highlighted, '1.0')
				end = f"{pos} + {len(highlighted)}c"
				#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
				editor.tag_add(f'selected{pos}', pos, end)
				editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

				
			except Exception as e:
				showerror('', 'No text was selected.\n Please select to continue.')

		def right_align():
			#Collection.font = data
			#Collection.color = 'black'
			#Collection.underline = 0
			Collection.justify = 'right'
			try:
				highlighted = editor.get(SEL_FIRST, SEL_LAST)
				pos = editor.search(highlighted, '1.0')
				end = f"{pos} + {len(highlighted)}c"
				#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
				editor.tag_add(f'selected{pos}', pos, end)
				editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)

				
			except Exception as e:
				showerror('', 'No text was selected.\n Please select to continue.')

		align_text = ttk.Menubutton(frame, text = 'Align text', style = 'menubutton.TMenubutton')
		align_text.pack(side = 'left')
		ToolTip(align_text, text = 'Text align; Left, Center and Right')

		itemss = Menu(tearoff = 0)
		itemss.add_command(label = 'Left', command = left_align)
		itemss.add_command(label = 'Center', command = center_align)
		itemss.add_command(label = 'Right', command = right_align)
		align_text.configure(menu = itemss)

		def open_clr():
			color = askcolor(title='Chose a font color')
			selected_color = color[1]
			#Collection.font = data
			Collection.color = selected_color
			#Collection.underline = 0
			#Collection.justify = 'right'
		
			try:
				highlighted = editor.get(SEL_FIRST, SEL_LAST)
				pos = editor.search(highlighted, '1.0')
				end = f"{pos} + {len(highlighted)}c"
				#tags = ['color', 'bold', 'itatlic', 'font', 'underline', 'size']
				editor.tag_add(f'selected{pos}', pos, end)
				editor.tag_configure(f'selected{pos}', font = Collection.font,
					 foreground = Collection.color, underline = Collection.underline, justify = Collection.justify)
				clr.configure(background = selected_color)
			except Exception as e:
				showerror('', 'No text was selected')

		clr = tk.Button(frame, text = ' ', background = 'red', border = 0,
		 relief = 'flat', padx = 10, command = open_clr)
		clr.pack(side = 'left', padx = 3)
		clr.configure(background = 'red')
		ToolTip(clr, text = 'Text color')

		more = tk.Frame(frame, background = 'whitesmoke')
		more.pack(side = 'right')

		def undo(e):
			editor.configure(undo = True)
			try:
				editor.edit_undo()
			except Exception as e:
				showerror('','Nothing to undo!')

		def redo(e):
			editor.configure(undo = True)
			try:
				editor.edit_redo()
			except Exception as e:
				showerror('','Nothing to redo!')
			
		redo_button = ttk.Button(more, text = 'Redo',
			 compound = 'left', image = imgs[1], style = 'button.TButton')
		redo_button.pack(side = 'right', padx =1)
		redo_button.bind('<Button-1>', redo)
		ToolTip(redo_button, text = 'Redo last action on collection\nKey: Ctrl + Y')

		undo_button = ttk.Button(more, text = 'Undo',
			compound = 'left', image = imgs[0], style = 'button.TButton')
		undo_button.pack(side = 'right', padx =1)
		undo_button.bind('<Button-1>', undo)
		ToolTip(undo_button, text = 'Undo last action on collection\nKey: Ctrl + Z')

		root.bind('<Control-z>', undo)
		root.bind('<Control-y>', redo)


	def title(editor):
		Collection.family = 'Calibri'
		Collection.styles = 'Heading 1'
		Collection.font = (Collection.family, 24, 'bold', 'roman')

		editor.insert('end', '---Your title---\n', ('title'))
		editor.insert('end', 'Your paragraph...\n')
		editor.tag_configure('title', font = Collection.font, justify = 'center')
	
		


	def intro(editor, data):
		Collection.family = 'Calibri'
		Collection.styles = 'Paragraph'
		Collection.font = (Collection.family, 14, 'normal', 'roman')
		editor.insert('end', data, ('paragraph'))
		editor.tag_configure('paragraph', font = Collection.font)
		

	# Function to insert an image at the current cursor position

	def insert_image(parent, img_ref):
		try:
			image_path = filedialog.askopenfilename(defaultextension='.png', filetypes=[('Image files','*')])
			myimage = (Image.open(image_path))
			res = myimage.resize((700,500))
			img = ImageTk.PhotoImage(res)
			
				
			position = parent.index(tk.INSERT)
			parent.image_create(position, image=img)
				
			#Collection.img = img
			try:
				# Store the image creation info
				#The position of the image might change as the user edits the document.
				#make sure to use the retrieved position instead of the inserted one.
				image_info = {
					'name': f'{img}',
					'path': f'{image_path}',
					'position': f'{position}'
				}
					
				img_d = f"{image_path}##|{position}\n"
				Collection.img_ref.append(img_d)
					

			except Exception as e:
				pass
			parent.update_idletasks()
			img_ref.append(img)
			#print(Collection.img_ref)
			#,('JPG files','*.jpg'),('JPEG files','*.jpeg'), ('GIF files','*.gif')])
			# Replace with your image path
		except Exception as e:
			pass

	def save_tags(text_widget, f):
		# Save the tags
		my_tags = []
		for tag in text_widget.tag_names():
		    ranges = text_widget.tag_ranges(tag)
		    for i in range(0, len(ranges), 2):
		        start = ranges[i]
		        end = ranges[i + 1]
		        font = text_widget.tag_cget(tag, 'font')
		        color = text_widget.tag_cget(tag, 'foreground')
		        underline = text_widget.tag_cget(tag, 'underline')
		        justify = text_widget.tag_cget(tag, 'justify')
		        value = (font, color, underline, justify)
		        tag_dict = {
		        	'tag_name': f'{tag}',
		        	'start': f'{start}',
		        	'end': f'{end}',
		        	'value': f'{value}'
		        }
		        f.write(f"{tag}##|{start}##|{end}##|{font}##|{color}##|{underline}##|{justify}\n")


	def save_collection(text):
		text_content = text.get('1.0', 'end')
		if len(Collection.file_dir)>0:
			myfile = Collection.file_dir.pop()
			with open(myfile, 'w') as file:
				file.write('---TEXT---\n')
				file.write(text_content)
				file.write('---TAGS---\n')
				Collection.save_tags(text, file)
				file.write('---IMAGES---\n')
				for img in Collection.img_ref:
					file.write(f'{img}')
			Collection.file_dir.append(myfile)
		else:
			try:
				file_dir = filedialog.asksaveasfilename(defaultextension=".eb", filetypes=[('Easy Bible files','*.eb')])
				with open(file_dir, 'w') as file:
					file.write('---TEXT---\n')
					file.write(text_content)
					file.write('---TAGS---\n')
					Collection.save_tags(text, file)
					file.write('---IMAGES---\n')
					for img in Collection.img_ref:
						file.write(f'{img}')
				Collection.file_dir.append(file_dir)
			except Exception as e:
				pass

	def open_collection(root,text, img_ref):
		#to open the file correctly, there are three things to do
		#1. register the position of the text as you save it
		#2. read the text lines and position and insert them correctly
		#3. solve the issue of the fonts with more than one word. 
		#Research about turning text which resemble a tuple in to a real one.
		## the sel tag once created is also creating problems
		try:
			file_path = filedialog.askopenfilename(defaultextension = '.eb', filetypes = [('Easy Bible files', '*.eb')])
			with open(file_path, 'r') as f:
			    lines = f.readlines()
			
			# Clear the text widget
			text.delete("1.0", tk.END)
			
			# Separate the text and tags
			in_text = False
			in_tags = False
			in_imgs = False
			text_content = []
			tags = []
			images = []
			
			for line in lines:
			    line = line.strip()
			    if line == "---TEXT---":
			        in_text = True
			        in_tags = False
			        in_imgs = False
			    elif line == "---TAGS---":
			        in_text = False
			        in_tags = True
			        in_imgs = False
			    elif line == "---IMAGES---":
			        in_text = False
			        in_tags = False
			        in_imgs = True
			    elif in_text:
			        text_content.append(line)
			    elif in_tags:
			        tags.append(line)
			    elif in_imgs:
			    	images.append(line)
			
			# Insert the text
			text.insert("1.0", "\n".join(text_content))
			
			# Apply the tags
			for tag in tags:
				tag_name, start, end, font, color, underline, justify = tag.split("##|")
				f,s,b,i = font.split(' ')
				#text_widget.tag_add(tag_name, start, end)

				r_font = (f, int(s), b, i)
				try:
				    text.tag_add(tag_name, start, end)
				    text.tag_configure(tag_name, font = r_font, foreground = color, underline = underline, justify = justify)
				except Exception as e:
				    pass

			for image_data in images:
				image_path, position = image_data.split('##|')

				myimage = (Image.open(image_path))
				res = myimage.resize((700,500))
				img = ImageTk.PhotoImage(res)

				try:
					position = text.index(tk.INSERT)
					text.image_create(position, image=img)
					img_ref.append(img)
				except Exception as e:
					showerror('', 'Failed to open images')

			Collection.file_dir.append(file_path)
			root.title(f'Easy Bible - {file_path}')
		except Exception as e:
			pass

	def read(text, img_ref):
		try:
			file_path = Collection.file_dir.pop()
			with open(file_path, 'r') as f:
			    lines = f.readlines()
			
			# Clear the text widget
			text.delete("1.0", tk.END)
			
			# Separate the text and tags
			in_text = False
			in_tags = False
			in_imgs = False
			text_content = []
			tags = []
			images = []
			
			for line in lines:
			    line = line.strip()
			    if line == "---TEXT---":
			        in_text = True
			        in_tags = False
			        in_imgs = False
			    elif line == "---TAGS---":
			        in_text = False
			        in_tags = True
			        in_imgs = False
			    elif line == "---IMAGES---":
			        in_text = False
			        in_tags = False
			        in_imgs = True
			    elif in_text:
			        text_content.append(line)
			    elif in_tags:
			        tags.append(line)
			    elif in_imgs:
			    	images.append(line)
			
			# Insert the text
			text.insert("1.0", "\n".join(text_content))
			
			# Apply the tags
			for tag in tags:
				tag_name, start, end, font, color, underline, justify = tag.split("##|")
				f,s,b,i = font.split(' ')
				#text_widget.tag_add(tag_name, start, end)

				r_font = (f, int(s), b, i)
				try:
				    text.tag_add(tag_name, start, end)
				    text.tag_configure(tag_name, font = r_font, foreground = color, underline = underline, justify = justify)
				except Exception as e:
				    pass

			for image_data in images:
				image_path, position = image_data.split('##|')

				myimage = (Image.open(image_path))
				res = myimage.resize((700,500))
				img = ImageTk.PhotoImage(res)

				try:
					position = text.index(tk.INSERT)
					text.image_create(position, image=img)
					img_ref.append(img)
				except Exception as e:
					showerror('', 'Failed to open images')

			Collection.file_dir.append(file_path)
			root.title(f'Easy Bible - {file_path}')
		except Exception as e:
			#showerror('', 'No file is opened!')
			pass

	def opening_logic(root, text, file_path):
			with open(file_path, 'r') as f:
			    lines = f.readlines()
			
			# Clear the text widget
			text.delete("1.0", tk.END)
			
			# Separate the text and tags
			in_text = False
			in_tags = False
			in_imgs = False
			text_content = []
			tags = []
			images = []
			
			for line in lines:
			    line = line.strip()
			    if line == "---TEXT---":
			        in_text = True
			        in_tags = False
			        in_imgs = False
			    elif line == "---TAGS---":
			        in_text = False
			        in_tags = True
			        in_imgs = False
			    elif line == "---IMAGES---":
			        in_text = False
			        in_tags = False
			        in_imgs = True
			    elif in_text:
			        text_content.append(line)
			    elif in_tags:
			        tags.append(line)
			    elif in_imgs:
			    	images.append(line)
			
			# Insert the text
			text.insert("1.0", "\n".join(text_content))
			
			# Apply the tags
			for tag in tags:
				tag_name, start, end, font, color, underline, justify = tag.split("##|")
				f,s,b,i = font.split(' ')
				#text_widget.tag_add(tag_name, start, end)

				r_font = (f, int(s), b, i)
				try:
				    text.tag_add(tag_name, start, end)
				    text.tag_configure(tag_name, font = r_font, foreground = color, underline = underline, justify = justify)
				except Exception as e:
				    pass

			for image_data in images:
				image_path, position = image_data.split('##|')

				myimage = (Image.open(image_path))
				res = myimage.resize((700,500))
				img = ImageTk.PhotoImage(res)

				try:
					position = text.index(tk.INSERT)
					text.image_create(position, image=img)
					img_ref.append(img)
				except Exception as e:
					showerror('', 'Failed to open images')

			Collection.file_dir.append(file_path)
			root.title(f'Easy Bible - {file_path}')
		

	def file_opening(root, state, text):
		# file opening.
		system=platform.system()
		if system == 'Windows':
			def register_file_association(file_extension, app_name, app_path):
			    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, file_extension)
			    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, app_name)

			    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, app_name)
			    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, "EasyBible")

			    key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, app_name + "\\shell\\open\\command")
			    winreg.SetValueEx(key, None, 0, winreg.REG_SZ, f'"{app_path}" "%1"')

			# Handle the file opening
			def main():
			    if len(sys.argv) > 1:
			        file_path = sys.argv[1]
			        state.configure(text = f'Opening {file_path} ...')
			        Collection.opening_logic(root, text, file_path)
			        time.sleep(5)
			        
			        state.configure(text = '')
			    else:
			        tate.configure(text = 'No file found')
			        Collection.opening_logic(root, text, file_path)
			        time.sleep(5)

			if __name__ == "__main__":
			    # Register the file association
			    register_file_association('.eb', "EasyBible", sys.executable)

			    # Handle the file opening
			    main()

		elif system == 'Darwin':
			# *macOS (via plist file)*


			# Create a plist file
			def create_plist_file(file_extensions):
			    plist_data = {
			        "CFBundleDocumentTypes": [
			            {
			                "CFBundleTypeExtensions": file_extensions,
			                "CFBundleTypeName": "Easy Bible file",
			                "CFBundleTypeRole": "Editor",
			            }
			        ]
			    }

			    with open("Info.plist", "wb") as f:
			        plistlib.dump(plist_data, f)

			# Handle the file opening
			def main():
			    if len(sys.argv) > 1:
			    	file_path = sys.argv[1]
			    	state.configure(text = f'Opening {file_path} ...')
			    	    
			    	time.sleep(5)
			    	Collection.opening_logic(root, text, file_path)
			    	state.configure(text = '')
			    	
			    else:
			        tate.configure(text = 'No file found')
			        Collection.opening_logic(root, text, file_path)
			        time.sleep(5)

			if __name__ == "__main__":
			    # Create a plist file
			    create_plist_file([".eb"])

			    # Handle the file opening
			    main()
		elif system == 'Linux':
			# *Linux*

			# 1. *Create a desktop file*: Create a `.desktop` file to declare the file types your application supports.

			def create_desktop_file(file_extensions):
			    desktop_data = f"""
			[Desktop Entry]
			Name=My Application
			Exec=EasyBible.exe %f
			Terminal=false
			Type=Application
			MimeType=application/x-eb;
			"""

			    with open("myapp.desktop", "w") as f:
			        f.write(desktop_data)

			# Handle the file opening
			def main():
			    if len(sys.argv) > 1:
			        file_path = sys.argv[1]
			        state.configure(text = f'Opening {file_path} ...')
			        Collection.opening_logic(root, text, file_path)
			        time.sleep(5)
			  
			        state.configure(text = '')
			    else:
			        state.configure(text = 'No file found')
			        Collection.opening_logic(root, text, file_path)
			        time.sleep(5)

			if __name__ == "__main__":
			    # Create a desktop file
			    create_desktop_file([".eb"])

			    # Handle the file opening
			    main()

		else:
			showerror('', 'Your opereating system does not support this file type.')



Collection.font = ('Calibri', 14, 'normal', 'roman')
Collection.color = 'black'
Collection.underline = 0
Collection.justify = 'left'	


		    
	
	    
