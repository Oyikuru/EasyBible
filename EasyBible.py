"""
Python 3.12
I did not document or comment on everything because most of the functions and the variable names
describes the code well enough to understand.

This program, I wrote it with the intention to learn as taking the opportunity to spread
the bible by providing a platform for studying it.

Most of my intentions were not met due to the limitations of my knowledge in programming
especially in the collection section of the program. I wanted a text editor that could be 
used easily without difficult. The purpose is to avoid moving out of the program to look for another apps
to write study notes. I also wanted the text editor to have the ability to convert or save the text as document
and pdf or even html. all these things I failed to achieve.
What I have now can basically do some little formating playing around with tags.
The user experience is definitely not okay. Me as the programmer can use the text editor very well and get what i want but
a user who knows nothing about how the text editor was programmed will achieve nothing.

The notes taken by the user on verses are saved in a sqlite database which the user can extract all in text format.
this is already implemented. The format of the text file is in a way that it will be easy to create with it another database table
in the original structure. The intention was to make a file out of the notes that can be shared so that those with this
application will be able to open it and read it verse by verse just like how the notes are read now
that if a user select a verse by placing the cursor on it, he can read the notes on that verse by clicking on the read note icon
or from the context menu or from the menu bar in tools

The reason why I am explaining all this is to get someone who can help me achieve my childhood dream
of making a powerful bible program. I have to teach my self programming for this dream and this is what I can achieve
so far. I am a self-taught programmer that is also some of the reasons why my knowledge in programming is so much limited as
most of the things I get from tutorials or stackoverflow. I need to see how someone experienced and knowledgeable approaches
and whites a whole application like this.

Anyone who is willing can improve the program and make it better without changing my intentions of the app.
You can change how the interface look and the general accessibility without taking out an existing feature.
You can add any feature as long as it will make studying the bible easy.
You can add other bible versions
Identify bugs and fix.
Improve existing codes and functions.
NOTE: PLEASE, WHERE POSIBLE COMMENT YOUR CODE WELL AND GENERALLY MAKE IT EASY TO UNDERSTAND.

For this program, I used tkinter, ttkbootstap for the gui, python 3.12
You can use any other gui python library you are flexible as long as you will be able to achieve the same thing as my intention
If you feel like rewriting the program in another language, C++, C#, C or Java can do. But you will have to let me know why first.

This application is meant to be free and open source. Please when you improve this program, make it available for free
and make the source code available at community platforms.
When you improve the program, let me know as well so that I can read and also improve my skills.
If you feel like giving me a credit for this, please feel free. I will appreciate is so much.



This is software by the Heavenly City Community. Heavenly city community is a christian community or groups of people
living in a christian lifestyle. As the leader, I have always dreamed of this application to support us in our
bible studies. You can support us by improving it.

I am OYIKURU EMMANUEL
Live in Gulu City, Uganda
Email: emmaoyikuru@gmail.com
Phone: +256786319064

GOD BLESS YOU
"""

from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.tooltip import ToolTip
from tkinter import filedialog
# import customtkinter as ctk
from books import get_bible_paraphrase, get_bible_ch,get_bible
import pythonbible as my_bible
#import matplotlib.font_manager
from hilights import Hilights, Notes
from collects import Collection
from reading_plan import Plan, PlanB
# from to_cvs import Ttext
from dictionary import dictionary
from present import slide_show, to_projector, present_bg
# from to_pdf import Pdf
# from audio import AudioPlayer
# from PIL import Image, ImageTk
import os
# from pathlib import Path
# import shutil
import webbrowser
#from tkinter import ttk
import sqlite3
# import sys
# import winreg
import platform
# import plistlib
# import appdirs
# import time
import subprocess

root = Tk()
root.title('Easy Bible')
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.wm_attributes('-fullscreen', False)
#root.geometry(str(sw)+'x'+str(sh))
# ctk.set_appearance_mode("light")
# ctk.set_default_color_theme('blue')

class History:
	"""docstring for History"""
	def __init__(self, theme, ref_bk, ref_ch):
		super(History, self).__init__()
		self.ref_bk = ref_bk 
		self.ref_ch = ref_ch

# class texttouadio(object):
# 	"""docstring for tta"""
# 	def __init__(self, arg):
# 		super(texttouadio, self).__init__()
#
# 	def converter(self):
# 		system=platform.system()
# 		if system=='Linux':
#
# 			#for linux
# 			# subprocess.run(['gedit', file_dir], check=True)
# 			showerror('System error', 'Converter does not exist on this system.\nIts available only in windows 10 or 11.')
# 		elif system =='Darwin':
# 			#for mac
# 			# subprocess.run(['open', '-a', 'TextEdit',file_dir])
# 			showerror('System error', 'Converter does not exist on this system.\nIts available only in windows 10 or 11.')
# 		elif system=='Windows':
# 			#for windows
# 			subprocess.run(['Speaker-TTS.exe'], check=True)
# 		else:
# 			showerror('System error', 'Converter does not exist on this system.\nIts available only in windows 10 or 11.')
# root.bind('<Control-k>', texttouadio.converter)

def save_history():
	a = bk.get()
	b = ch.get()
	conn = sqlite3.connect('hilights.db')
	c = conn.cursor()
	sql = 'UPDATE history set books = ?, chapter = ?'
	c.execute(sql, (a, b,))
	conn.commit()

conn = sqlite3.connect('hilights.db')
c = conn.cursor()

sq = 'SELECT * from history'
r = c.execute(sq).fetchall()

if r[0][1] == '':
	History.ref_bk = 'Genesis'
	History.ref_ch = 1
else:
	History.ref_bk = r[0][1]
	History.ref_ch = r[0][2]

#the program's styles and themes
style = ttk.Style()
style.configure('custom.Treeview', font =('Comic Sans', 12), rowheight = 30)
style.configure('TButton', background = 'whitesmoke', foreground = 'black')
style.configure('close.TButton', background = 'red',
 foreground = 'whitesmoke', padx =0, pady = 0, border =0, relief = 'flat')
style.configure('button.TButton', borderwidth=0, background = 'white', foreground = 'black')
style.configure('menubutton.TMenubutton', background = 'white', borderwidth = 0, foreground = 'black')
#style.configure('TMenu', font = ('roboto', 13, 'bold'))
style.configure('TCombobox', font = ('roboto', 16, 'bold'), pady = 10, 
	padx = 10, border = 0, relief = 'flat', background = 'white')
#style.configure('TListbox', font = ('Calibri', 12, 'bold'))
History.theme = 'cosmo'

#to handle themes properly,the highlighted section category tabs is created in two functions
# tab_fx() and tab_fy()
def tabs_fx():
	td = tabs.winfo_children()

	def hover1(obj):
		for item in td:
			item.configure(border = 0)
		obj.configure(border = 1)

	def blur(e):
		for item in td:
			item.configure(border = 0)
	tabs.bind('<Leave>', blur)

	td[0].bind('<Enter>', lambda obj: hover1(td[0]))
	td[1].bind('<Enter>', lambda obj: hover1(td[1]))
	td[2].bind('<Enter>', lambda obj: hover1(td[2]))
	td[3].bind('<Enter>', lambda obj: hover1(td[3]))
	td[4].bind('<Enter>', lambda obj: hover1(td[4]))
	td[5].bind('<Enter>', lambda obj: hover1(td[5]))
	td[6].bind('<Enter>', lambda obj: hover1(td[6]))

	td[0].bind('<Button-1>', lambda obj: filter(td[0]))
	td[1].bind('<Button-1>', lambda obj: filter(td[1]))
	td[2].bind('<Button-1>', lambda obj: filter(td[2]))
	td[3].bind('<Button-1>', lambda obj: filter(td[3]))
	td[4].bind('<Button-1>', lambda obj: filter(td[4]))
	td[5].bind('<Button-1>', lambda obj: filter(td[5]))
	td[6].bind('<Button-1>', lambda source: populate_hilight(all_hilights()))
	td[6].configure(text = 'All', foreground = 'black')

def tab_fy():
	for item in tabs.winfo_children():
		item.destroy()

	tab_color = ['yellowgreen','yellow', 'lightblue', 'lightgreen', 'pink', 'orange', 'whitesmoke']
	for cl in tab_color:
		label = tk.Label(tabs, background = cl, pady= 10, relief = 'solid', border =0)
		label.pack(side = 'left', fill = 'x', expand = 1)
		label.configure(background = cl)
		ToolTip(label, text = 'Filter hilights for this color')

#handling the the different themes, cosmo, flatly, darkly and superehero

def cosmo():
	style.theme_use('cosmo')
	style.configure('button.TButton', borderwidth=0, background = 'white', foreground = 'black')
	style.configure('menubutton.TMenubutton', background = 'white', borderwidth = 0, foreground = 'black')
	style.configure('Treeview', rowheight = 30,
	 font = ('roboto', 11), border = 0, relief = 0)
	
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

def flatly():
	style.theme_use('flatly')
	style.configure('button.TButton', borderwidth=0, background = 'white', foreground = 'black')
	style.configure('menubutton.TMenubutton', background = 'white', borderwidth = 0, foreground = 'black')
	style.configure('Treeview', rowheight = 30,
	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	History.theme = 'flatly'
	present_bg()

def darkly():
	style.theme_use('darkly')
	style.configure('button.TButton', borderwidth=0, background = '#222222', foreground = 'white')
	style.configure('menubutton.TMenubutton', background = '#222222', borderwidth = 0, foreground = 'white')
	style.configure('Treeview', rowheight = 30,
	 font = ('roboto', 11), border = 0, relief = 0)
	
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

def superhero():
	style.theme_use('superhero')
	style.configure('button.TButton', borderwidth=0, background = '#2b3e50', foreground = 'white')
	style.configure('menubutton.TMenubutton', background = '#2b3e50', borderwidth = 0, foreground = 'white')
	style.configure('Treeview', rowheight = 30,
 	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

def morph():
	style.theme_use('morph')
	style.configure('button.TButton', borderwidth=0, background = '#D9E3F1', foreground = '#7B8AB8')
	style.configure('menubutton.TMenubutton', background = '#D9E3F1', borderwidth = 0, foreground = '#7B8AB8')
	style.configure('Treeview', rowheight = 30,
 	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

def cerculean():
	style.theme_use('cerculean')
	style.configure('button.TButton', borderwidth=0, background = 'white', foreground = '#4bb1ea')
	style.configure('menubutton.TMenubutton', background = 'white', borderwidth = 0, foreground = '#4bb1ea')
	style.configure('Treeview', rowheight = 30,
 	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

# def siplex():
# 	style.theme_use('siplex')
# 	style.configure('button.TButton', borderwidth=0, background = '#284d6b', foreground = 'white')
# 	style.configure('menubutton.TMenubutton', background = '#284d6b', borderwidth = 0, foreground = 'white')
# 	style.configure('Treeview', rowheight = 30,
#  	 font = ('roboto', 11), border = 0, relief = 0)
	
# 	tab_fy()
# 	tabs_fx()
# 	hi_tool.configure(background = 'yellow')

def yeti():
	style.theme_use('yeti')
	style.configure('button.TButton', borderwidth=0, background = 'white', foreground = 'black')
	style.configure('menubutton.TMenubutton', background = 'white', borderwidth = 0, foreground = 'black')
	style.configure('Treeview', rowheight = 30,
 	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

# def united():
# 	style.theme_use('united')
# 	style.configure('button.TButton', borderwidth=0, background = '#284d6b', foreground = 'white')
# 	style.configure('menubutton.TMenubutton', background = '#284d6b', borderwidth = 0, foreground = 'white')
# 	style.configure('Treeview', rowheight = 30,
#  	 font = ('roboto', 11), border = 0, relief = 0)
	
# 	tab_fy()
# 	tabs_fx()
# 	hi_tool.configure(background = 'yellow')

# def sandston():
# 	style.theme_use('sandstone')
# 	style.configure('button.TButton', borderwidth=0, background = '#284d6b', foreground = 'white')
# 	style.configure('menubutton.TMenubutton', background = '#284d6b', borderwidth = 0, foreground = 'white')
# 	style.configure('Treeview', rowheight = 30,
#  	 font = ('roboto', 11), border = 0, relief = 0)
	
# 	tab_fy()
# 	tabs_fx()
# 	hi_tool.configure(background = 'yellow')

# def pulse():
# 	style.theme_use('pulse')
# 	style.configure('button.TButton', borderwidth=0, background = '#284d6b', foreground = 'white')
# 	style.configure('menubutton.TMenubutton', background = '#284d6b', borderwidth = 0, foreground = 'white')
# 	style.configure('Treeview', rowheight = 30,
#  	 font = ('roboto', 11), border = 0, relief = 0)
	
# 	tab_fy()
# 	tabs_fx()
# 	hi_tool.configure(background = 'yellow')

# def minty():
# 	style.theme_use('minty')
# 	style.configure('button.TButton', borderwidth=0, background = '#284d6b', foreground = 'white')
# 	style.configure('menubutton.TMenubutton', background = '#284d6b', borderwidth = 0, foreground = 'white')
# 	style.configure('Treeview', rowheight = 30,
#  	 font = ('roboto', 11), border = 0, relief = 0)
	
# 	tab_fy()
# 	tabs_fx()
# 	hi_tool.configure(background = 'yellow')

# def lumen():
# 	style.theme_use('lumen')
# 	style.configure('button.TButton', borderwidth=0, background = '#284d6b', foreground = 'white')
# 	style.configure('menubutton.TMenubutton', background = '#284d6b', borderwidth = 0, foreground = 'white')
# 	style.configure('Treeview', rowheight = 30,
#  	 font = ('roboto', 11), border = 0, relief = 0)
	
# 	tab_fy()
# 	tabs_fx()
# 	hi_tool.configure(background = 'yellow')

# def journal():
# 	style.theme_use('journal')
# 	style.configure('button.TButton', borderwidth=0, background = '#284d6b', foreground = 'white')
# 	style.configure('menubutton.TMenubutton', background = '#284d6b', borderwidth = 0, foreground = 'white')
# 	style.configure('Treeview', rowheight = 30,
#  	 font = ('roboto', 11), border = 0, relief = 0)
	
# 	tab_fy()
# 	tabs_fx()
# 	hi_tool.configure(background = 'yellow')

def solar():
	style.theme_use('solar')
	style.configure('button.TButton', borderwidth=0, background = '#002b36', foreground = 'white')
	style.configure('menubutton.TMenubutton', background = '#002b36', borderwidth = 0, foreground = 'white')
	style.configure('Treeview', rowheight = 30,
 	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

def cyborg():
	style.theme_use('cyborg')
	style.configure('button.TButton', borderwidth=0, background = '#060606', foreground = 'white')
	style.configure('menubutton.TMenubutton', background = '#060606', borderwidth = 0, foreground = 'white')
	style.configure('Treeview', rowheight = 30,
 	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	History.theme = 'cyborg'
	present_bg()

def vapor():
	style.theme_use('vapor')
	style.configure('button.TButton', borderwidth=0, background = '#190831', foreground = '#26d8e2')
	style.configure('menubutton.TMenubutton', background = '#190831', borderwidth = 0, foreground = '#26d8e2')
	style.configure('Treeview', rowheight = 30,
 	 font = ('roboto', 11), border = 0, relief = 0)
	
	tab_fy()
	tabs_fx()
	hi_tool.configure(background = 'yellow')
	present_bg()

#the program's images or icons	

book_img = PhotoImage(file = 'book.png')
folder = PhotoImage(file = 'open.png')
document = PhotoImage(file = 'page_add.png')
rem_b = PhotoImage(file = 'delete.png')
edit_b = PhotoImage(file = 'b_edit.png')
copy_b = PhotoImage(file = 'copy.png')
more = PhotoImage(file = 'plus.png')
# check = PhotoImage(file = 'check.png')
filter_img = PhotoImage(file = 'filter.png')
save_img = PhotoImage(file = 'save.png')
# web_img = PhotoImage(file = 'world1.png')
drop_img = PhotoImage(file = 'b_drop.png')
help_img = PhotoImage(file = 'help.png')
doc_img = PhotoImage(file = 'b_docs.png')
back_img = PhotoImage(file = 'b_undo.png')
forward_img = PhotoImage(file = 'redo.png')
# pdf_img = PhotoImage(file = 'b_pdfdoc.png')
view_img = PhotoImage(file = 's_views.png')
bk_img = PhotoImage(file = 'b_bookmark.png')
minus = PhotoImage(file = 'minus.png')
share = PhotoImage(file = 'reload.png')
right_side = PhotoImage(file = 'b_nextpage.png')
left_side = PhotoImage(file = 'b_prevpage.png')
upside = PhotoImage(file = 's_asc.png')
downside = PhotoImage(file = 'b_more.png')
eb = PhotoImage(file = 'eb.png')
addd = PhotoImage(file = 'add.png')
text_b = PhotoImage(file = 'text.png')
view2 = PhotoImage(file = 'b_views.png')
slide = PhotoImage(file = 'slide.png')

#connected database path.
# def db_path():

# 	try:
# 		# Get the AppData directory path
# 		appdata_path = Path(os.getenv('APPDATA'))

# 		# Create a directory for your application
# 		app_dir = appdata_path / 'EasyBible'
# 		app_dir.mkdir(parents=True, exist_ok=True)

# 		try:
# 			shutil.copy2('hilights.db', app_dir)
# 			file_path = app_dir / 'hilights.db'
# 		except Exception as e:
# 			return app_dir / 'hilights.db'
# 		return app_dir/'hilights.db'
# 	except Exception as e:
# 		pass

img_list = [back_img, forward_img]

root.iconphoto(False, eb)

#the program's main frame
#sw and sh are the screen's width and height respectively. see top.
main = ttk.Frame(root)
main.pack(fill = 'both', side = 'top', expand = 1)
h = (sh/100)*90 # 90% of screen's height
pane = ttk.PanedWindow(main, orient = 'horizontal')
pane.pack(fill='both', side = 'top', expand = 1, anchor = 'n')

left = Frame(pane)
pane.add(left)

w = (sw/100)*20 # 20% of screen's width

bible_pane = ttk.PanedWindow(left, orient = 'vertical', width = int(w))
bible_pane.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)

bible_frame = tk.Frame(bible_pane)
bible_pane.add(bible_frame)


icons_tool = ttk.LabelFrame(bible_frame, text = 'Resources')
icons_tool.pack(side = 'top', fill = 'x')
#icons_tool.bind('<Leave>', blur_icons)

# functions to get the differnt commentaries. Commentaries are pdf files that I at the moment chose to open in browsers
#this may change later if I or anyone reading this code decides to write a reader for them
def matthew():
	path = os.path.abspath('VOL01.pdf')
	webbrowser.open(f'file://{path}')

def mark():
	path = os.path.abspath('VOL02.pdf')
	webbrowser.open(f'file://{path}')

def acts():
	path = os.path.abspath('VOL03B.pdf')
	webbrowser.open(f'file://{path}')

def john():
	path = os.path.abspath('VOL04.pdf')
	webbrowser.open(f'file://{path}')

def romans():
	path = os.path.abspath('VOL05.pdf')
	webbrowser.open(f'file://{path}')

def timothy():
	path = os.path.abspath('VOL09.pdf')
	webbrowser.open(f'file://{path}')

def ecclesiastes():
	path = os.path.abspath('VOL09OT.pdf')
	webbrowser.open(f'file://{path}')

def revelation():
	path = os.path.abspath('VOL12.pdf')
	webbrowser.open(f'file://{path}')

def staff():
	path = os.path.abspath('The Shepherd\'s Staff.pdf')
	webbrowser.open(f'file://{path}')

comm = ttk.Menubutton(icons_tool, text = 'Commentaries', compound = 'top',
  bootstyle = 'primary', style = 'menubutton.TMenubutton')
comm.pack(side = 'left', padx = 1)
ToolTip(comm, text = "Books and commentaries")

# text_to_audio = ttk.Button(icons_tool, text = 'Converter', command = lambda: texttouadio.converter(None))
# text_to_audio.pack(side = 'left')
# ToolTip(text_to_audio, text = 'Convert text to audio')

comm_menu = Menu()
# comm_menu.add_command(label = 'From CSV file notes')
# comm_menu.add_command(label = 'From Text file notes')
comm_menu.add_command(label = 'The Shepherd\'s Staff', command = staff)
comm_menu.add_separator()
comm_menu.add_command(label = 'The book of Matthew', command = matthew)
comm_menu.add_command(label = 'The book of Mark, 1 and 2 Peter', command = mark)
comm_menu.add_command(label = 'The Acts of Apostles', command = acts)
comm_menu.add_command(label = 'The Gospel of John, 1, 2 & 3 John', command = john)
comm_menu.add_command(label = 'The book of Romans', command = romans)
comm_menu.add_command(label = 'The book of 1 Timothy, Titus & 2 Timothy', command = timothy)
comm_menu.add_command(label = 'The book of Ecclesiastes', command = ecclesiastes)
comm_menu.add_command(label = 'The book of Revelation', command = revelation)
comm.configure(menu = comm_menu)
#website.bind('<Enter>', lambda obj: hover_icons(website))

# video_ico = ttk.Menubutton(icons_tool, text = 'Channel', compound = 'top',
# image = video)
# video_ico.pack(side = 'left', padx = 1)
# #video_ico.bind('<Enter>', lambda obj: hover_icons(video_ico))

# def audio_(e):
# 	images = [audio_guide,fav1,play,next_, prev, stop,vol,pause, list_, cog_]
# 	AudioPlayer.page(eb, audio, right_side, shuffle, folder_, live, filter_img, web_img, fav, images)

# audio_ic = ttk.Menubutton(icons_tool, text = 'Audios', compound = 'top',
# image = audio)
# audio_ic.pack(side = 'left', padx = 1)
# audio_ic.bind('<Button-1>', audio_)

# this is to get the different bible versions
#this is specifically to handle from the menu. the treeview has its own functions to do the same thing
# if anyone reading this code has the bility to make the two 
#functions into one that handle both the menu and the treeview i'll be grateful.
class Version(object):
	"""to make the version accesible at all scope"""
	def __init__(self, verion):
		super(Version, self).__init__()
		self.verion = verion


def kjv():
	ver.configure(text = 'KJV')
	Version.verion = 'kjv'

def akjv():
	ver.configure(text = 'AKJV')
	Version.verion = 'akjv'

def kjv():
	ver.configure(text = 'KJV')
	Version.verion = 'kjv'

def ylt():
	ver.configure(text = 'YLT')
	Version.verion = 'ylt'

def asv():
	ver.configure(text = 'ASV')
	Version.verion = 'asv'

def web():
	ver.configure(text = 'WEB')
	Version.verion = 'web1'

def erv():
	ver.configure(text = 'ERV')
	Version.verion = 'erv'

def wrv():
	ver.configure(text = 'WRV')
	Version.verion = 'web'
# this is the second part that handle the treeview
def get_version():
	try:
		if bk_list.selection():
			for item in bk_list.selection():
				var = bk_list.item(item)
				v = var['values'][0]
				
				if v == 'King James Version':
					Version.verion = 'kjv'
					va = 'KJV'
				elif v == 'American King James Version':
					Version.verion = 'akjv'
					va = 'AKJV'
				elif v == 'Young Literal Translation':
					Version.verion = 'ylt'
					va = 'YLT'
				elif v == 'American Standard Version':
					Version.verion='asv'
					va = 'ASV'
				elif v == 'World Edition Bible':
					Version.verion = 'web1'
					va = 'WEB'
				elif v == 'English Revised Version':
					Version.verion = 'erv'
					va = 'ERV'
				elif v == 'World Revised Version':
					Version.verion = 'web'
					va = 'WRV'

		else:
			Version.verion ='kjv'
			va = 'KJV'
		ver.configure(text=va)

		return Version.verion
	except Exception as e:
		pass

# bible version treeview

books = {'King James Version':'KJV', 'American King James Version':'AKJV',
 'Young Literal Translation':'YLT','American Standard Version':'ASV', 
 'World Edition Bible':'WEB','English Revised Version':'ERV','World Revised Version':'WRV'}
columns = ('image', 'name')
bk_list = ttk.Treeview(bible_frame, columns=columns)
bk_list.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES, anchor = tk.N)
ToolTip(bk_list, text = 'Bible versions')

bk_list.heading('#0', text = 'Books', anchor='center')
bk_list.heading('#1', text='Bible book versions')


bk_list.column('#0', width=110, anchor='w')
bk_list.column('#1', width=300, anchor = 'w')

# populating the bible versions

for book,abr in books.items():
	bk_list.insert('',tk.END, value =(book,), image =bk_img, text =abr)

bk_list.bind('<<TreeviewSelect>>',lambda event: get_version())
# bk_list.configure(style ='Custom.Treeview')
# the default style for the default theme
style.configure('Treeview', rowheight = 30,
 font = ('roboto', 11), border = 0, relief = 0)

# for the highlight and notes section
tool_pane = tk.Frame(bible_pane)
bible_pane.add(tool_pane)

my_tools = ttk.Notebook(tool_pane)
my_tools.pack(side = 'top', fill = 'both', expand = 1)

highlit_page = tk.Frame(my_tools)
note_page = tk.Frame(my_tools)

my_tools.add(highlit_page, text = 'Highlights')
my_tools.add(note_page, text = 'Notes')

my_tools.enable_traversal()

#the highlights page
tabs = tk.Frame(highlit_page)
tabs.pack(side = 'top', fill = 'x')

def all_hilights():
	conn = sqlite3.connect('hilights.db')
	c = conn.cursor()
	sql = "SELECT* from hilights order by ID DESC"
	result = c.execute(sql).fetchall()
	return result

def sorted_hilights(color):
	conn = sqlite3.connect('hilights.db')
	c = conn.cursor()
	sql = "SELECT* from hilights where COLOR = ? order by ID DESC"
	result = c.execute(sql, (color,)).fetchall()
	return result


def populate_hilight(source):
	for item in frame.winfo_children():
		item.destroy()

	#h = all_hilights()
	for i in source:
		ref = i[2].split(']')
		#print(ref[1])
		Hilights.verse(frame, i[1], f"{ref[0]}]", ref[1], i[0], minus)

# this sorts the highlights according to color
def filter(obj):
	color = obj.cget('background')
	populate_hilight(sorted_hilights(color))

#highlights tabs are placed in functions towards the beginning to easy working with differnt themes
tab_fy()
tabs_fx()


frame = ScrolledFrame(highlit_page, width = 400)
frame.pack(side = 'top', fill = 'both', expand = 1)


populate_hilight(all_hilights())


np = ScrolledFrame(note_page)
np.pack(side = 'left', fill = 'both', expand = 1)
#note_holder.window_create('end', window = np)

# n_bg = tk.Label(np, background = 'whitesmoke')
# n_bg.pack(side = TOP, fill = BOTH, expand = 1)
# n_bg.configure(background = 'whitesmoke')

def my_notes():
	conn = sqlite3.connect('hilights.db')
	c = conn.cursor()
	sql = "SELECT REF,TITLE from notes order by ID DESC"
	result = c.execute(sql).fetchall()
	return result


right = tk.Frame(pane)
pane.add(right)

# this is to toggle between the appeance of note reading pane and collection pane 
def toggle_window(pane, ref, variable):
	var = variable.get()
	try:
		if var == 1:
			pane.add(ref)
			#reader.pack()
		else:
			pane.forget(ref)

	except Exception as e:
		pass

# the pane that contains the scripture, notes and collections
right_pane = ttk.PanedWindow(right, orient = 'horizontal')
right_pane.pack(fill='both', side = 'top', expand = 1)

# the reader contains the scripture and notes
reader = tk.Frame(right_pane)
right_pane.add(reader)

scripture = tk.Frame(reader)
scripture.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)

scripture_tool = ttk.LabelFrame(scripture, text = 'Bible refference')
scripture_tool.pack(side=tk.TOP, fill=tk.X)

ver = ttk.Label(scripture_tool,text='', font=('roboto',14,'bold'))

ver.pack(side=tk.LEFT, padx=10)
ToolTip(ver, text = 'Bible version on use')

Version.verion = get_version()

bks = ['Genesis', 'Exodus', 'Leviticus', 'Numbers',
				'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel','2 Samuel', '1 Kings', '2 Kings',
				'1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalm', 'Proverbs', 'Ecclesiastes',
				'Song of Solomon', 'Isaiah', 'Jeremiah','Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah',
				'Jonah','Micah','Nahum','Habakkuk','Zephaniah', 'Haggai', 'Zechariah','Malachi','Matthew', 'Mark','Luke',
				'John','Acts','Romans','1 Corinthians', '2 Corinthians','Galatians', 'Ephesians', 'Philippians','Colossians',
				'1 Thessalonians', '2 Thessalonians','1 Timothy','2 Timothy','Titus','Philemon','Hebrews','James','1 Peter',
				'2 Peter', '1 John', '2 John', '3 John','Jude','Revelation' ]
def change_books(e):
	global chs
	# version =get_version()
	book = bk.get()
	chs = my_bible.count_chapters(book)
	sel_book = get_bible_ch(Version.verion,f"%{book}%")
	scripture_book.delete('1.0',END)
	for sel in sel_book:
		
		scripture_book.insert(END, sel+'\n\n')

	ch.configure(value=[x for x in range(1, chs+1)])
	vs.set('1')
	ch.set('1')
	save_history()

def next_book():
	try:
		b = bks.index(bk.get())
		if b < len(bks):
			b += 1
			bk.set(bks[b])
			change_books(None)
		elif b > len(bks):
			b = 0
			bk.set(bks[b])
			change_books(None)
		else:
			b = 0
			bk.set(bks[b])
			change_books(None)
	except Exception as e:
		pass

def prev_book():
	try:
		b = bks.index(bk.get())
		if b < len(bks):
			b -= 1
			bk.set(bks[b])
			change_books(None)
		elif b > len(bks):
			b = 0
			bk.set(bks[b])
			change_books(None)
		else:
			b = 0
			bk.set(bks[b])
			change_books(None)
	except Exception as e:
		pass

prev_tool1 = ttk.Button(scripture_tool, image = left_side, command = prev_book, style = 'button.TButton')
prev_tool1.pack(side = LEFT)
ToolTip(prev_tool1, text = 'Previous book\n Key: Down')


bk = ttk.Combobox(scripture_tool, values = bks, height = 30,
 state ='readonly', width = 30)
bk.pack(side=tk.LEFT, padx = 5)
bk.set(History.ref_bk)
ToolTip(bk, text = 'Select a book')
#bk.current(0)
#bk.configure(style = 'TCombobox')
chs = my_bible.count_chapters('Genesis')


bk.bind('<<ComboboxSelected>>',change_books)

#search bible 
def search_bible(e):
	version =Version.verion
	scripture_book.delete('1.0',END)
	txt = search_entry.get()
	if ':' in txt:
		v = get_bible_ch(version,f"%{txt}%")
	else:
		v = get_bible_paraphrase(version,f"%{txt}%")
	for verse in v:
		
		scripture_book.insert('end', verse+'\n\n')
		try:
			pos = scripture_book.search(txt, '1.0', nocase = 1, exact = False)
			end = f"{pos} + {len(txt)}c"
			scripture_book.tag_add('color', pos, end)
			scripture_book.tag_configure('color', foreground = 'orange') 
		except Exception as e:
			pass

verse_list = []
for x in range(1, chs +1):
	verse_list.append(x)

nxt_tool1 = ttk.Button(scripture_tool, image = right_side, command = next_book, style = 'button.TButton')
nxt_tool1.pack(side = LEFT)
ToolTip(nxt_tool1, text = 'Next book\n Key: Up')

ch = ttk.Combobox(scripture_tool, values=[str(x) for x in range(1, chs+1)],
 height =30, state = 'readonly', width =5)
ch.pack(side=tk.LEFT, padx = 5)
ch.set(History.ref_ch)
ToolTip(ch, text = 'Selected book chapter')
#ch.current(0)
#ch.configure(style = 'TCombobox')

def get_verse_num(e):
	version = Version.verion
	b = bk.get()
	c = ch.get()
	ref = f"{b} {c}"
	v = my_bible.count_verses(ref)
	vs.configure(value=[x for x in range(1, v+1)])
	vs.set('1')
	#vse = get_bible(version, f"%{ref}%")

	text = get_bible_ch(version, f"%{b} {c}:%")
	scripture_book.delete('1.0', tk.END)
	for txt in text:
		scripture_book.insert(tk.END, txt +'\n\n')
	save_history()
ch.bind('<<ComboboxSelected>>', get_verse_num)

def get_verse(e):
	try:
		version = Version.verion
		b = bk.get()
		chapter = ch.get()
		v = vs.get()
		ref = f"{b} {chapter}:{v}"
		vse = get_bible(version, f"%{ref}%")
		pos = scripture_book.search(vse, '1.0')
		# scripture_book.delete('1.0', tk.END)
		scripture_book.see(pos)
		end = f"{pos} + {len(vse)}chapter"
		scripture_book.tag_add('sele', pos, end)
		scripture_book.tag_configure('sele', background='#d9e3f1', foreground='black')
	except Exception as e:
		pass
vs = ttk.Combobox(scripture_tool, value=[x for x in range(1, 2)],
 height =30, state = 'readonly', width = 5)
vs.pack(side=LEFT)
vs.current(0)
vs.bind('<<ComboboxSelected>>', get_verse)
vs.configure(style = 'TCombobox')
ToolTip(vs, text = 'Verses')


search_label = ttk.Label(scripture_tool, image = filter_img,
 font = ('roboto', 10))
search_label.pack(side=tk.LEFT)
search_entry = ttk.Entry(scripture_tool)
search_entry.pack(side=tk.LEFT, fill=tk.X, expand=tk.YES, padx = 10)
search_entry.bind('<KeyRelease>',search_bible)
ToolTip(search_entry, text = 'Search for scripture\nfor text or paraphrase.\nAlso search for scripture reference\ne.g. Proverbs 9:10')

scripture_pane = ttk.PanedWindow(scripture, orient = 'vertical')
scripture_pane.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

#THE CONTAINER FOR THE SCRIPTURE BOOK AND ITS TOOLS
s_b = ttk.Frame(scripture)
scripture_pane.add(s_b)

scripture_book = tk.Text(s_b, font =('Comic Sans', 14),
 wrap = WORD, width=13, height = 15, padx =20,
 border = 0, relief = 'sunken')
scripture_book.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)

# these are to handle the icon tools on the right of the scripture_book
scrip_book_tool = ttk.Frame(s_b)
scrip_book_tool.pack(side = 'left', fill = 'y')

def looking():
	hilighted_text(scripture_book)

search_tool = ttk.Button(scrip_book_tool, image = filter_img, command = looking, style = 'button.TButton')
search_tool.pack(side = TOP)
ToolTip(search_tool, text = 'Search selected text')

def ccp():
	copy_text()

copy_tool = ttk.Button(scrip_book_tool, image = copy_b, command = ccp, style = 'button.TButton')
copy_tool.pack(side = TOP)
ToolTip(copy_tool, text = 'Copy selected text.\nKey: Ctrl + C')

def coll():
	get_current_line()

add_collection_tool = ttk.Button(scrip_book_tool, image = text_b, command = coll, style ='button.TButton')
add_collection_tool.pack(side = TOP)
ToolTip(add_collection_tool, text ='Add the verse where the cursor is to collection.\nKey: Ctrl + M')

def wrt_note():
	write_note()

wr_tool = ttk.Button(scrip_book_tool, image = edit_b, command = wrt_note, style = 'button.TButton')
wr_tool.pack(side = TOP)
ToolTip(wr_tool, text = 'Write a note on the verse where the cursor is.\nKey: Ctrl + W')

def my_notes_view():
	view_notes()

read_tool = ttk.Button(scrip_book_tool, image = view2, command = my_notes_view, style = 'button.TButton')
read_tool.pack(side = TOP)
ToolTip(read_tool, text = 'Read note of the verse where the cursor is.\nKey: Ctrl + R')

# copy_tool1 = ttk.Button(scrip_book_tool, image = copy2)
# copy_tool1.pack(side = TOP)

def dictionary_look(e):
	try:
		word = scripture_book.selection_get()
		meaning = dictionary.meaning(word)
		read.configure(state = 'normal', font = ('roboto', 12))
		read.delete('1.0', END)
		for line in meaning:
			wrd = line[0]
			pos = line[1]
			definition = line[2]
			read.insert('end', f'{wrd}:', ('font3'))
			read.insert('end', f'{pos}\n', ('font4'))
			read.insert('end', f'{definition}\n\n')
			read.tag_configure('font3', font = ('Calibre Light', 12, 'bold'))
			read.tag_configure('font4', font = ('roboto', 12, 'normal', 'italic'), foreground = 'orange')
		read.configure(state = 'disabled')
	except Exception as e:
		pass

dict_tool = ttk.Button(scrip_book_tool, image = view_img, command = lambda: dictionary_look(None), style = 'button.TButton')
dict_tool.pack(side = TOP)
ToolTip(dict_tool, text = 'Search the meaning of selected text from dictionary.\nKey: Ctrl + F')
root.bind('<Control-f>',dictionary_look)

def coloring(e):
	hilighted_box()

hi_tool = tk.Label(scrip_book_tool, text = '', padx = 18,
 background = 'yellow', border = 1, relief = 'solid')
hi_tool.pack(side = TOP, pady = 1)
hi_tool.bind('<Button-1>', coloring)
hi_tool.configure(background = 'yellow')
ToolTip(hi_tool, text = 'Highlight a verse\nKey: Ctrl + H')

def load_history():
	scripture_book.delete('1.0',END)
	get_verse_num(None)
load_history()
#next chapter
def next_ch():
	try:
		chapters = my_bible.count_chapters(bk.get())
		x = int(ch.get())
		if x <= chapters:
			x += 1
			if x > chapters:
				# showinfo('', 'You are on the last chapter')
				x = 1
				next_book()
			ch.set(x)
			get_verse_num(None)

				
	except Exception as e:
		pass
# previous chapter
def prev_ch():
	try:
		chapters = my_bible.count_chapters(bk.get())
		x = int(ch.get())
		if 0 < x <= chapters+1:
			x -= 1
			if x == 0:
				x = 1
				# showinfo('', 'Your, on the first chapter')
				prev_book()
			ch.set(x)
			get_verse_num(None)
	except Exception as e:
		pass


next_tool = ttk.Button(scrip_book_tool, image = right_side, command = next_ch, style = 'button.TButton')
next_tool.pack(side = BOTTOM, anchor = S)
ToolTip(next_tool, text = 'Next chapter\nKey: Right')

prev_tool = ttk.Button(scrip_book_tool, image = left_side, command = prev_ch, style = 'button.TButton')
prev_tool.pack(side = BOTTOM, anchor = S)
ToolTip(prev_tool, text = 'Previous chapter\nKey: Left')

# change font size of the scripture_book
def change_font(Event = None):
	try:
		f = font_size.get()
		scripture_book.configure(font = ('Comic Sans', int(f)))
		font_la.configure(text = int(f))
	except Exception as e:
		pass

font_size = ttk.Scale(scrip_book_tool, orient = VERTICAL, from_ = 50, to = 10,
 value = 10, command = change_font, cursor = 'hand2')
font_size.pack(side = BOTTOM, anchor = S)
ToolTip(font_size, text = 'Bible font size:\nDrag the handle up to increase the font size\nand down to decrease.\nKey: + to add font\nKey: - to reduce font')
font_size.set(14)
#font label
font_la = ttk.Label(scrip_book_tool, text = '14')
font_la.pack(side = BOTTOM, anchor = S)

def add_font(e):
	f = font_size.get()
	font_size.set(int(f) +1)
	change_font()

def reduce_font(e):
	f = font_size.get()
	font_size.set(int(f) -1)
	change_font()
root.bind('-', reduce_font)
root.bind('+', add_font)

#syy = tk.Scrollbar(scripture_book, orient ='vertical',
 #command = scripture_book.yview, cursor = 'arrow')
#scripture_book.configure(yscrollcommand = syy.set)
#syy.pack(side=tk.RIGHT, fill=tk.Y, expand=1, anchor=tk.E)

#the notes section begins here
notes = tk.Frame(scripture)
scripture_pane.add(notes)

note_tool = tk.Frame(notes)
note_tool.pack(side = tk.TOP, fill=tk.X)


copy = ttk.Button(note_tool, text = 'Copy', image = copy_b, compound = 'top', style = 'button.TButton')
copy.pack(side = 'left')
ToolTip(copy, text = 'Copy notes')

# when selecting a text from the read text area
def sel_data(e):
	search_sel.configure(state = 'active')
	# the highlighted text2(source) function searches the bible for the text selected from source.
	# it creates a top level window with the results.
	# the function is written below. continue reading you will get it
	search_sel.bind('<Button-1>', lambda source: hilighted_text2(read))
	search_sel.configure(state = 'active')
	present_verse.configure(state = 'active', command=lambda: present_highlighted_text(None))
	present_verse.bind('<Button-1>', present_highlighted_text)
	# live_tools()

search_sel = ttk.Button(note_tool, text = 'Find', compound = 'top',
	image = filter_img, state = 'disabled', style = 'button.TButton')
search_sel.pack(side = 'left')
ToolTip(search_sel, text = 'Search the bible for selected text from note')

dic = ttk.Button(note_tool, text = 'Dictionary', compound = 'top',
	image = view_img, style = 'button.TButton', command = lambda: dictionary_look(None))
dic.pack(side = 'left')
ToolTip(dic, text = 'Find the meaning of text selected!\nKey: Ctrl + F')

def search_dictionary(e):
	text = search_box.get()
	if text == '':
		word = 'a'
	else:
		word = text
	try:
		meaning = dictionary.meaning(word)
		read.configure(state = 'normal', font = ('roboto', 12))
		read.delete('1.0', END)
		for line in meaning:
			wrd = line[0]
			pos = line[1]
			definition = line[2]
			read.insert('end', f'{wrd}:', ('font3'))
			read.insert('end', f'{pos}\n', ('font4'))
			read.insert('end', f'{definition}\n\n')
			read.tag_configure('font3', font = ('Calibre Light', 12, 'bold'))
			read.tag_configure('font4', font = ('roboto', 12, 'normal', 'italic'), foreground = 'orange')
		read.configure(state = 'disabled')
	except Exception as e:
		pass

search_box = ttk.Entry(note_tool)
search_box.pack(side = LEFT)
search_box.bind('<KeyRelease>', search_dictionary)
to_projector()

def present_highlighted_text(e):
	try:
		text = read.selection_get()

		diction = text.split('\n')
		ref, body = diction[0], diction[1]
		slide_show(body, ref)

	except Exception as e:
		text = read.selection_get()
		slide_show(text, '')

def presentation(e):
	try:
		v = current_line().split(']')
		ref, verse = v[0], v[1]
		slide_show(verse, ref.strip('['))

	except Exception as e:
		pass


present_verse = ttk.Button(note_tool, text = 'Present', compound = 'left',
	image = slide, style = 'button.TButton', command = lambda: presentation(None))
present_verse.pack(side = 'left')

ToolTip(present_verse, text = 'Project the selected verse to secondary screen.\nKey: Ctrl + J')
root.bind('<Control-j>', presentation)

mode = IntVar()
def change_mode():
	var = mode.get()
	if var == 1:
		present_verse.configure(state='disabled')
		return True

	else:
		present_verse.configure(state='active')
		return False

def on_presentation_mode(e):
	if change_mode() == True:
		presentation(None)
	else:
		pass
scripture_book.bind('<Button-1>', on_presentation_mode)

present_mode = ttk.Checkbutton(note_tool, text='Presentation mode', variable= mode, command= change_mode)
present_mode.pack(side = LEFT, padx = 10)
ToolTip(present_mode, text='Toggle presentation mode. Once set on,\n Clicking on a verse will present it to the secondary screen')

def clear_presentation():
	slide_show('','')

clear_button = ttk.Button(note_tool, text = 'Clear presentation', command= clear_presentation, style = 'button.TButton',
						  image=drop_img, compound='left')
clear_button.pack(side = RIGHT, padx = 10)
ToolTip(clear_button, 'Clear presentation text')

def live_tools(e):
	def remove(e):
		bar.place_forget()

	x_pos, y_pos = root.winfo_pointerxy()
	bar = tk.Frame(root, background='whitesmoke', border=1, relief='solid')
	bar.place(x = x_pos, y = y_pos)
	bar.configure(background='whitesmoke', border=1, relief='solid')

	cc = ttk.Button(bar, text = 'Copy', command= ccp, style='button.TButton', image= copy_b, compound= TOP)
	cc.pack(side = LEFT)
	cc.bind('<Button-1>', copy_text)

	se = ttk.Button(bar, text='Search', command=lambda source: hilighted_text2(read), style='button.TButton', image=filter_img, compound=TOP)
	se.pack(side=LEFT)
	se.bind('<Button-1>', lambda source: hilighted_text2(read))

	dc = ttk.Button(bar, text='Dictionary', command=lambda: dictionary_look(None) , style='button.TButton', image=view_img, compound=TOP)
	dc.pack(side=LEFT)
	dc.bind('<Button-1>', dictionary_look)

	pr = ttk.Button(bar, text='Present', command=lambda: present_highlighted_text(None), style='button.TButton', image=slide, compound=TOP)
	pr.pack(side=LEFT)
	pr.bind('<Button-1>',present_highlighted_text)

	root.bind('<Button-1>', remove)

# the text area to read notes
read = tk.Text(notes, state = 'disabled', border =0, relief = 'sunken', wrap = WORD)
read.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
read.bind('<<Selection>>', sel_data)
read.bind('<Button-1>', live_tools)
# populate the scripture book with scriptures.
# the get_bible_ch function generates a bible chapters given the bible version and book.
# if an empty string is given instead of a book, it generates the whole bible.
# the function is imported from the book module
# cur = bk.get()
# bible_text = get_bible_ch(Version.version, f"% %")
# for verses in bible_text:
# 	scripture_book.insert('end', verses +'\n\n')
	#print(verses)
#scripture_book.configure(state = 'disabled')
def disable_backspace(e):
	return 'break'
scripture_book.bind('<BackSpace>', disable_backspace)

#get the cursor position and return the line of text
#current line
def current_line():
	cursor_position = scripture_book.index("insert").split('.')[0]
	line_text = scripture_book.get(f"{cursor_position}.0",f"{cursor_position}.end")
	return line_text

def get_current_line(event = None):	
	#reference_book.insert(tk.END, current_line()+'\n\n')
	Collection.intro(reference_book, current_line()+'\n\n')
#scripture_book.bind('<Button-1>', get_current_line)
#scripture_book.bind('<KeyRelease>', get_current_line)
#shortcut for collections
root.bind('<Control-m>', get_current_line)
#add context menu
def show_context_menu(event):
	context_menu.post(event.x + 350, event.y)

def copy_text(event=None):
	try:
		selected_text = scripture_book.selection_get()
		root.clipboard_clear()
		root.clipboard_append(selected_text)
	except Exception as e:
		# selected_text = scripture_book.selection_get()
		root.clipboard_clear()
		root.clipboard_append(current_line())
	
#shortcut for copying verse
root.bind('<Control-c>', copy_text)

#highlits colors. Highlighting verses
def hilighted_box(event = None):
	x_pos, y_pos = root.winfo_pointerxy()
	box = tk.Frame(root, background = 'whitesmoke', border = 1, relief = 'solid')
	box.place(x = x_pos-390, y = y_pos-50)

	top = tk.Frame(box, background = 'lightgray')
	top.pack(side = 'top', fill = 'x')

	tt = tk.Label(top, text = f'Highlight styles - {current_line().split(']')[0]}]',
	 font = ('roboto', 12, 'bold'), background = 'lightgray')
	tt.pack(side= 'left')

	cl = tk.Button(top, text = 'X', foreground = 'red',
	 background = 'whitesmoke', relief = 'solid', border = 0,
	 command = box.destroy)
	cl.pack(side = 'right')
	ToolTip(cl, text = 'Close')

	tool2 = tk.Frame(box, padx =10, pady = 10)
	tool2.pack(side = 'top', fill = 'both')

	def selected_color(obj):
		try:
			if current_line():
				clr = obj.cget('background')
				pos = scripture_book.search(current_line(), '1.0')
				end = f"{pos} + {len(current_line())}c"
				scripture_book.tag_add(f'clr{pos}', pos, end)
				scripture_book.tag_configure(f'clr{pos}', background = clr)
				tag_pos = f'clr{pos}|{pos}|{end}|{clr}'
				#print(pos,end)
				#SAVE HILIGHTS TO DATABASE
				conn =  sqlite3.connect('hilights.db')
				c = conn.cursor()

				sql = 'INSERT INTO hilights (COLOR, REF,TAG) values (?, ?, ?)'
				c.execute(sql, (clr, current_line(), tag_pos))
				conn.commit()

				populate_hilight(all_hilights())
			else:
				showerror('Selection error','No verse was selected! Click on a verse to select')
		except Exception as e:
			raise e

	colors = ['yellowgreen','yellow', 'lightblue', 'lightgreen', 'pink', 'orange']
	for color in colors:
		label = tk.Label(tool2, background = color, pady = 20, padx = 30, border = 0, relief = 'solid')
		label.pack(side = 'left')
		label.configure(background = color)
		#label.bind('<Button-1>', lambda obj: selected_color(label))

	butt = tool2.winfo_children()
	butt[0].bind('<Button-1>', lambda obj: selected_color(butt[0]))
	butt[1].bind('<Button-1>', lambda obj: selected_color(butt[1]))
	butt[2].bind('<Button-1>', lambda obj: selected_color(butt[2]))
	butt[3].bind('<Button-1>', lambda obj: selected_color(butt[3]))
	butt[4].bind('<Button-1>', lambda obj: selected_color(butt[4]))
	butt[5].bind('<Button-1>', lambda obj: selected_color(butt[5]))


	def hover(obj):
		for item in butt:
			item.configure(border = 0)
		obj.configure(border = 1)

	butt[0].bind('<Enter>', lambda obj: hover(butt[0]))
	butt[1].bind('<Enter>', lambda obj: hover(butt[1]))
	butt[2].bind('<Enter>', lambda obj: hover(butt[2]))
	butt[3].bind('<Enter>', lambda obj: hover(butt[3]))
	butt[4].bind('<Enter>', lambda obj: hover(butt[4]))
	butt[5].bind('<Enter>', lambda obj: hover(butt[5]))
# writing notes on selected verses. selected verses are where the cursor is
def write_note(event = None):
	title = current_line().split(']')[0]
	def save_notes():
		note = text.get('1.0', 'end')
		tt = inp.get()
		ref = f"{title}]"
		conn = sqlite3.connect('hilights.db')
		c = conn.cursor()
		try:
			sql = "INSERT INTO notes (REF, TITLE, NOTES) values (?, ?, ?)"
			c.execute(sql, (ref, tt, note,))
			conn.commit()
		except Exception as e:
			showerror('','permission error')
		frame.destroy()
		for item in np.winfo_children():
			item.destroy()
		for note in my_notes():
			Notes.notes(root, np, read, note[0], note[1], rem_b, edit_b)

	frame = ttk.Label(root)
	x_pos, y_pos = sw/4, sh/4#root.winfo_pointerxy()
	frame.place(x = x_pos, y = y_pos)
	frame.configure(background = 'whitesmoke')

	la = ttk.Label(frame, text = 'Write notes', font = ('roboto', 16, 'bold'), justify = 'left')
	la.pack(side = 'top', fill = 'x')

	inp = ttk.Entry(frame, font = ('roboto', 18, 'bold'))
	inp.pack(side = 'top', fill = 'x', pady = 10, padx =10)
	inp.insert('end', f'{title}]')

	text = ttk.Text(frame, border = 2, relief = 'sunken', height = 10,
	 padx = 10, pady =10, wrap = 'word', font = ('roboto', 13))
	text.pack(side = 'top', fill = 'both', padx =10)

	text.insert('end', f"{current_line()}\n\n")

	tool = ttk.Label(frame)
	tool.pack(side = tk.TOP, fill= tk.X)
	tool.configure(background = 'whitesmoke')

	save = ttk.Button(tool, text = 'Save', command = save_notes)
	save.pack(side = 'left', padx = 10, pady = 10)
	ToolTip(save, text = 'Save notes')

	clo = ttk.Button(tool, text = 'Close', command = frame.destroy)
	clo.pack(side = 'left', padx = 5, pady = 10)
	ToolTip(clo, text = 'Close without saving')

root.bind('<Control-w>', write_note)

# read the notes of a verse where the cursor is
def view_notes(event = None):
	title = current_line().split(']')[0]
	ref = f'{title}]'
	conn = sqlite3.connect('hilights.db')
	c = conn.cursor()
	sql = "SELECT TITLE, NOTES from notes where REF = ?"
	result = c.execute(sql, (ref,)).fetchall()
	read.configure(state = 'normal')
	read.delete('1.0', 'end')

	for data in result:
		
		read.insert('end', f'{data[0]}\n\n', ('font'))
		read.insert('end', f'{data[1]}', ('font1'))

		read.tag_configure('font', font = ('roboto', 16, 'bold'))
		read.tag_configure('font1', font = ('root', 12,))
		read.configure(state = 'disabled', padx =10, wrap = 'word', font = ('roboto', 12))

for note in my_notes():
	Notes.notes(root,np, read, note[0], note[1], rem_b, edit_b)

def copy_note(event=None):
	source = read.get('1.0', 'end')
	root.clipboard_clear()
	root.clipboard_append(source)
	showinfo('Success', 'Note copied!')

root.bind('<Control-r>', view_notes)

context_menu = tk.Menu(scripture_book, tearoff=0)
context_menu.add_command(label = 'Next book', accelerator = 'Up', command = next_book)
context_menu.add_command(label = 'Previous book', accelerator = 'Down', command = prev_book)
context_menu.add_command(label = 'Next chapter', accelerator = 'Right', command = next_ch)
context_menu.add_command(label = 'Previous chapter', accelerator = 'Left', command = prev_ch)
context_menu.add_separator()
context_menu.add_command(label= 'Search selected text', command = lambda: hilighted_text(scripture_book))
context_menu.add_command(label= 'Copy verse to clipbord', accelerator = 'Ctrl + C', command=copy_text)
context_menu.add_command(label= 'Dictionary meaning of selected word', accelerator = 'Ctrl + F', 
	command = lambda: dictionary_look(None))
context_menu.add_separator()
#context_menu.add_command(label= 'Add verse to bookmark', accelerator = 'Ctrl + D')
context_menu.add_command(label= 'Add to collections', accelerator = 'Ctrl + M', command = get_current_line)
context_menu.add_separator()
context_menu.add_command(label= 'Write notes', accelerator = 'Ctrl + W', command = write_note)
context_menu.add_command(label= 'Read notes', accelerator = 'Ctrl + R', command = view_notes)
context_menu.add_command(label= 'Copy notes', accelerator = 'Ctrl + Shift + C', command = copy_note)
context_menu.add_separator()
context_menu.add_command(label= 'Highlight verse', accelerator = 'Ctrl + H', command = hilighted_box)
context_menu.add_separator()
context_menu.add_command(label='Present', accelerator='Ctrl + J', command=lambda: presentation(None))
context_menu.add_checkbutton(label='Presentation mode', variable= mode, command= change_mode)

root.bind('<Control-h>', hilighted_box)
copy.bind('<Button-1>', copy_note)
root.bind('<Control-Shift-c>', copy_note)
scripture_book.bind('<Button-3>', show_context_menu)
#get highlighted text
# unlike hilighted_text2(source), hilighted_text(source) gets the result of any text selected.

def hilighted_text(source):
	version =Version.verion
	top = Toplevel()
	top.iconphoto(False, eb)
	#top.geometry('700x700')
	text =  tk.Text(top, padx = 10, pady =10, font = ('Calibri Light', 14, 'bold'), wrap = 'word')
	text.pack(fill = 'both', side = 'left', expand = 1)
	syy = tk.Scrollbar(top, orient ='vertical',
	 command = text.yview, cursor = 'arrow')
	text.configure(yscrollcommand = syy.set)
	syy.pack(side=tk.RIGHT, fill=tk.Y, expand=1)
	try:
		highlighted = source.get(SEL_FIRST, SEL_LAST)
		#do something
		
		var = get_bible_paraphrase(version,f"%{highlighted}%")
		text.delete('1.0','end')
		vss =[]
		for v in var:
			vss.append(v)
			text.insert(END, v+'\n\n')
		
		#num.configure(text=f"{len(vss)} verses found.")
		top.title(f"Easy Bible - {highlighted}. {len(vss)} verses found")
	except TclError:
		pass

# this function only gets searches for scripture reffernces 
def hilighted_text2(source):
	version =Version.verion
	top = Toplevel()
	top.iconphoto(False, eb)
	#top.geometry('700x700')
	text =  tk.Text(top, padx = 10, pady =10, font = ('Calibri Light', 14, 'bold'), wrap = 'word')
	text.pack(fill = 'both', side = 'left', expand = 1)
	syy = tk.Scrollbar(top, orient ='vertical',
	 command = text.yview, cursor = 'arrow')
	text.configure(yscrollcommand = syy.set)
	syy.pack(side=tk.RIGHT, fill=tk.Y, expand=1)
	try:
		highlighted = source.get(SEL_FIRST, SEL_LAST)
		#do something
		var = get_bible_ch(version,f"%{highlighted}%")
		text.delete('1.0','end')
		vss =[]
		for v in var:
			vss.append(v)
			text.insert(END, v+'\n\n')
		#num.configure(text=f"{len(vss)} verses found.")
		top.title(f"Easy Bible - {highlighted}. {len(vss)} verses found")
	except TclError:
		pass
#scripture_book.bind('<ButtonRelease>', lambda source: hilighted_text(scripture_book))
#read.bind('<ButtonRelease>', lambda source: hilighted_text2(read))

# this function does not work as intended. 
# The intention is to highlight or in other words add tags to the the scripture_book
# the moment it loads the text
# the all_hlights() fuction returns a list of all the scripter verses that were highlighted with the color used
# the intention was to search all the scripture book for the text in the highlight and add a tag to it with bacground as color
# please if you can achieve this help me
def initialize_hilights():
	try:
		for hilight in all_hilights():
			tag = hilight[3].split('|')
			scripture_book.tag_add(tag[0], tag[1], tag[2])
			scripture_book.tag_configure(tag[0], background = tag[3])

	except Exception as e:
		raise e
# initialize_hilights()

# the ref or reference section are things to do with collections
# the collect.py is the source code that works with most functions here

reference = tk.Frame(right_pane)
right_pane.add(reference)

reference_tool = tk.Frame(reference)
reference_tool.pack(side=tk.TOP, fill=tk.X)

goto = tk.Label(reference_tool, text='Your collections', font =('Comic Sans', 14))
goto.pack(side=tk.LEFT)

num = tk.Label(reference_tool, text='', font=('Comic Sans', 13, 'bold'))
num.pack(side=tk.LEFT, padx=10)


def new_collection(Event = None):
	try:
		file_dir = filedialog.asksaveasfilename(defaultextension=".eb", filetypes=[('Easy Bible files','*.eb')])
		file = file_dir.split('/').pop()
		with open(file_dir, 'w') as f:
			f.write('')
		Collection.file_name = file
		Collection.file_dir.append(file_dir)

		Collection.title(reference_book)
		root.title(f'Easy Bible - {file_dir}')
	except Exception as e:
		pass

root.bind('<Control-n>', new_collection)

def open_collection(Event = None):
	Collection.open_collection(root, reference_book, img_ref)
root.bind('<Control-o>', open_collection)


ref_menu = tk.Frame(reference_tool)
ref_menu.pack(side ='right', padx = 10)


open_ref = ttk.Button(ref_menu, text = 'Open',
compound = 'top',
image = folder,
style = 'button.TButton'
#command = open_collection
)
open_ref.pack(side = 'right')
open_ref.bind('<Button-1>', open_collection)
ToolTip(open_ref, text = 'Open saved collection\nKey: Ctrl + O')


new_ref = ttk.Button(ref_menu, text = 'New',
compound = 'top',
image = document,
style = 'button.TButton'
#command = new_collection
)
new_ref.pack(side = 'right', padx =1)
new_ref.bind('<Button-1>', new_collection)
ToolTip(new_ref, text = 'New collection\nKey: Ctrl + N')

def mytext():
	Collection.intro(reference_book, 'Text here...')

add_button = ttk.Menubutton(reference_tool, image = more,
	text = 'Add item', compound = 'top', style = 'menubutton.TMenubutton')
add_button.pack(side = 'right', padx =4)
ToolTip(add_button, text = 'Add Title or paragraph to collection')

def my_image():
	Collection.insert_image(reference_book,img_ref)

img_ref = []	
Collection.img_ref = []
def add_title():
	Collection.title(reference_book)
	def update():
		num.configure(text = '')
	num.configure(text = 'Saved')
	root.after(5000, update)

items = Menu(tearoff = 0)
items.add_command(label = 'Add title', command = add_title)
items.add_command(label = 'Add text paragraph', command = mytext)
#items.add_command(label = 'Add image', command = my_image)
#items.add_command(label = 'Add audio')
#items.add_command(label = 'Add video', command = my_video)
add_button.configure(menu = items)

Collection.file_dir = []
def save_collection(Event = None):
	Collection.save_collection(reference_book)

root.bind('<Control-s>', save_collection)

def read_collection(Event = None):
	top = Toplevel()
	top.iconphoto(False, eb)
	#top.geometry('700x700')
	frame = tk.Frame(top, background = 'white')
	frame.pack(side = 'top', fill = 'both', expand =1)
	text =  tk.Text(frame, padx = 10, pady =10, cursor = 'hand2',
	 font = ('Calibri Light', 14, 'normal'), wrap = 'word', border = 0, relief = 'flat')
	text.pack(fill = 'both', side = 'left', expand = 1)
	syy = tk.Scrollbar(frame, orient ='vertical',
	 command = text.yview, cursor = 'arrow')
	text.configure(yscrollcommand = syy.set)
	syy.pack(side=tk.RIGHT, fill=tk.Y, expand=1, anchor = tk.E)
	Collection.read(text, img_ref) 
	text.configure(state = 'disabled')
	size = ttk.Sizegrip(top)
	size.pack(side = 'bottom', anchor = 'se')
root.bind('<Control-t>', read_collection)

# def read_pdf():
# 	try:
# 		Pdf.read(Collection.file_dir.pop())
# 	except Exception as e:
# 		showerror('', 'Collection file was not selected or opened!')
# 		#raise e


read_button = ttk.Menubutton(reference_tool, image = view_img,
	text = 'Read', compound = 'top', style = 'menubutton.TMenubutton')
read_button.pack(side = 'right', padx =4)
ToolTip(read_button, text = 'Read or save collection')

itemses = Menu(tearoff = 0)
itemses.add_command(label = 'Read collection', command = read_collection, accelerator = 'Ctrl + T')
itemses.add_command(label = 'Save collection', accelerator = 'Ctrl + S', command = save_collection, compound = 'left', image = save_img)
# itemses.add_command(label = 'Read collection as PDF', compound = 'left', image = pdf_img, command = read_pdf)
# itemses.add_command(label = 'Read collection as MS Word')
#itemses.add_command(label = 'Read collection as HTML')

read_button.configure(menu = itemses)

'''
def tabs(parent, label):
	frame = tk.Frame(parent, background = 'whitesmoke')
	frame.pack(side = 'left', padx = 1, pady =1, fill = 'x', expand = 1)

	text = tk.Label(frame, text = label, background = 'whitesmoke')
	text.pack(side = 'left', padx = 10, pady = 2)

	close = tk.Button(frame, text = 'x', background = 'whitesmoke', border =1,
		foreground= 'gray', relief = 'flat')
	close.pack(side = 'right', padx = 5)
tab_list = []
'''

ref_tab = tk.Frame(reference, background = 'lightgray')
ref_tab.pack(side = 'top', fill = 'x')

#tab_holder = tk.Frame(ref_tab)
#tab_holder.pack(side = 'left', fill = 'x', expand = 0)
'''
for tab in tab_list:
	tabs(tab_holder, tab)
overflow = tk.Frame(ref_tab)
overflow.pack(side = 'right')
ref_overflow = ttk.Menubutton(overflow, text = 'All')
ref_overflow.pack(side = 'right', padx =3)

ref_overflow_menu = Menu(tearoff = 0)
for tab in tab_list:
	ref_overflow_menu.add_command(label = tab)
ref_overflow.configure(menu = ref_overflow_menu)
'''
# the ref or reference section are things to do with collections
# the collect.py is the source code that works with most functions here
ref_cover = tk.Frame(reference, background = 'white')
ref_cover.pack(side = 'top', fill = 'both', expand =1, anchor = 'center')

ref_book = tk.Frame(ref_cover)
ref_book.pack(side = 'left', fill = 'both', expand = 1)

reference_book = tk.Text(ref_book, wrap=WORD, font=('Comic Sans', 11), 
	padx = 40, pady =20, undo = True,
	 border = 0, relief = 'flat', takefocus = True)
reference_book.pack(side=TOP, fill=BOTH, expand=1, anchor = CENTER, padx =50)
syy = ttk.Scrollbar(ref_cover, orient ='vertical',
 command = reference_book.yview, cursor = 'arrow')
reference_book.configure(yscrollcommand = syy.set)
syy.pack(side=tk.RIGHT, fill=tk.Y, expand=1, anchor = tk.E)

reference_book.edit_modified(True)
Collection.tools(root,ref_tab, reference_book, img_list)

def contextMenu(e):
	def close_menu(e):
		frame.destroy()

	def hover(obj):
		for item in frame.winfo_children():
			item.configure(background = '', foreground = '')
		obj.configure(background = '#284d6b', foreground = 'white')

	def select_all(event=None):
		reference_book.tag_add('sel', '1.0', 'end')
		close_menu(None)

	def copy_text(event):
		try:
			selected_text=reference_book.selection_get()
			root.clipboard_clear()
			root.clipboard_append(selected_text)
			close_menu(None)
		except Exception as e:
			close_menu(None)
			showerror('', 'No text selected')

	def paste_text(event):
		try:
			text_to_paste = root.clipboard_get()
			reference_book.insert(INSERT, text_to_paste)
			close_menu(None)
		except Exception as e:
			close_menu(None)
			showerror('', 'Nothing found on clipboard')

	def cut_text(event):
		try:
			selected_text= reference_book.selection_get()
			reference_book.delete(SEL_FIRST, SEL_LAST)
			root.clipboard_clear()
			root.clipboard_append(selected_text)
			close_menu(None)
		except Exception as e:
			close_menu(None)
			showerror('', 'No text selected')

	x_pos, y_pos = root.winfo_pointerxy()
	frame = ttk.Label(root, width = 300, padding = 1)
	frame.place(x = x_pos-100, y = y_pos-30)
	frame.configure(background = '#8ba0b1')

	select = ttk.Label(frame, text = '    Select all',padding = 5,
	 width = 30, justify = LEFT)
	select.pack(side = 'top', fill = 'x', pady = 1, padx = 1)
	select.bind('<Enter>', lambda obj: hover(select))
	select.bind('<Button-1>', select_all)

	copy = ttk.Label(frame, text = '    Copy', padding = 5,
	 width = 30, justify = LEFT)
	copy.pack(side = 'top', fill = 'x', pady = 1, padx = 1)
	copy.bind('<Enter>', lambda obj: hover(copy))
	copy.bind('<Button-1>', copy_text)

	cut = ttk.Label(frame, text = '    Cut',padding = 5,
	 width = 30, justify = LEFT)
	cut.pack(side = 'top', fill = 'x', pady = 1, padx = 1)
	cut.bind('<Enter>', lambda obj: hover(cut))
	cut.bind('<Button-1>', cut_text)

	paste = ttk.Label(frame, text = '    Paste',padding = 5,
	 width = 30, justify = LEFT)
	paste.pack(side = 'top', fill = 'x', pady = 1, padx = 1)
	paste.bind('<Enter>', lambda obj: hover(paste))
	paste.bind('<Button-1>', paste_text)

	root.bind('<Button-1>', close_menu)
	root.bind('<Button-3>', close_menu)


reference_book.bind('<Button-3>', contextMenu)


bott = ttk.Frame(main)
bott.pack(side = 'top', fill = 'x', anchor = 's')


# this is now the status bar below the gui page
la = ttk.Label(bott, text = 'Easy Bible - Software by the Heveanly City Community', font = ('roboto', 11))
la.pack(side = 'left', padx = 10)

state = ttk.Label(bott, text = '')
state.pack(side = LEFT, padx = 10)

# this another fuctions that seems to be duplicates
# a similar was already implemented but using menus as the triger point
# this time it buttons to organize the gui by toggling off and on some sections i.e. notes and collections
class Toggle():
	"""variables for toggle status"""
	def __init__(self, col_var, not_var):
		super(Toggle, self).__init__()
		self.col_var = col_var
		self.not_var = not_var
		
Toggle.col_var = True
Toggle.not_var = True

def toggle_view_col(source, page, butt):
	try:
		try:
			if Toggle.col_var == True:
				source.forget(page)
				butt.configure(image = left_side, compound = 'left', text = 'Show collection')
				Toggle.col_var = False

			else:
				source.add(page)
				butt.configure(image = right_side, compound = 'right', text = 'Hide collection')
				Toggle.col_var = True
		except Exception as e:
			source.add(page)
			butt.configure(image = right_side, compound = 'right', text = 'Hide collection')
			Toggle.col_var = True
	except Exception as e:
		pass

def toggle_view_note(source, page, butt):
	try:
		try:
			if Toggle.not_var == True:
				source.forget(page)
				butt.configure(image = upside, text = 'Show notes')
				Toggle.col_var = False

			else:
				source.add(page)
				butt.configure(image = downside, text = 'Hide notes')
				Toggle.col_var = True

		except Exception as e:
			source.add(page)
			butt.configure(image = downside, text = 'Hide notes')
			Toggle.col_var = True
	except Exception as e:
		pass

coll_butt = ttk.Button(bott, text = 'Hide collection',
 image = right_side, compound = 'right',
 command = lambda: toggle_view_col(right_pane, reference, coll_butt), style = 'button.TButton')
coll_butt.pack(side = 'right', anchor = 'e')
ToolTip(coll_butt, text = 'Hide or show collection')

note_butt = ttk.Button(bott, text = 'Hide notes',
 image = downside, compound = 'left',
 command = lambda: toggle_view_note(scripture_pane, notes, note_butt), style = 'button.TButton')
note_butt.pack(side = 'right', anchor = 'e', padx = 2)
ToolTip(note_butt, text = 'Hide or show notes')


class AppVersion(Toplevel):
	"""docstring for Version"""
	def __init__(self):
		super().__init__()
		self.title('Easy Bible - Version 1.01 - 2025')
		self.geometry('400x300')
		self.attributes('-topmost', True)
		self.resizable(False, False)
		self.iconphoto(False, eb)

	
		try:
			frame = ttk.Frame(self)
			frame.pack(fill = 'both', expand = 1, ipadx = 20, ipady = 20)

			mytextt = """A Software application by the Heavenly City Community. This application is free to use and the source code can be got from github. Do with the app whatever you please as long as you credit those who worked on it before you.
			"""

			label = ttk.Label(frame, text = 'Easy Bible', font = ('Roboto', 24))
			label.pack(side = 'top', fill = 'x')

			label1 = ttk.Label(frame, text = 'Version 1.01 - 2025', font = ('Roboto', 18))
			label1.pack(side = 'top', fill = 'x')

			message = tk.Message(frame, aspect = 240, justify = 'left',
		 text = mytextt, font = ('Roboto', 12), pady =10, padx =10)
			message.pack(side = TOP, fill = BOTH, expand = 1)

			# check = ctk.CTkButton(frame, text = 'Check for new release.')
			# check.pack(side = 'bottom', pady = 10)
		except Exception as e:
			pass

# showing random psalms and bible verses in topleves
# the source codes are in reading_plan.py
daily = ttk.Menubutton(bott, text = 'Daily verses', style = 'menubutton.TMenubutton')
daily.pack(side = 'right', anchor = 'center')
daily_menu = Menu()
daily_menu.add_command(label = 'From random Psalms', command = lambda: Plan.plan(eb))
daily_menu.add_command(label = 'From random verses', command = lambda: PlanB.plan(eb))
# daily_menu.add_command(label = 'Topical devotionals')
# daily_menu.add_command(label = 'Verses with notes')
daily.configure(menu = daily_menu)
ToolTip(daily, text = 'Daily Psalm or Random bible verses')

def q():
	quit(None)
menu_bar = tk.Menu(root) 
filemenu = Menu(menu_bar)
filemenu.add_command(label = 'New collection', accelerator = 'Ctrl + N', command = new_collection)
filemenu.add_command(label = 'Open collection', accelerator = 'Ctrl + O', command = open_collection)
filemenu.add_separator()
filemenu.add_command(label = 'Save collection', accelerator = 'Ctrl + S', command = save_collection, compound = 'left', image = save_img)
# filemenu.add_command(label = 'Export collection to PDF', compound = 'left', image = pdf_img, command = read_pdf)
# filemenu.add_command(label = 'Export collection to MS Word file')
#filemenu.add_command(label = 'Share collection to community page', compound = 'left', image = share)
filemenu.add_separator()
# filemenu.add_command(label = 'Export notes to plain text', command = Ttext)
#filemenu.add_command(label = 'Export notes to word')
# filemenu.add_command(label = 'Export notes to CSV (Excel)', command = Cvs)
# filemenu.add_command(label = 'Text to audio converter', accelerator = 'Ctrl + K', command = lambda: texttouadio.converter(None))
filemenu.add_separator()
filemenu.add_command(label = 'Quit', accelerator = 'Ctrl + Q', command = q, compound = 'left', image = drop_img)
menu_bar.add_cascade(label="File", menu=filemenu)

var_notes = tk.IntVar()
var_collections = tk.IntVar()

viewmenu = Menu(menu_bar)
viewmenu.add_checkbutton(label = 'View notes', variable = var_notes, command = lambda:toggle_window(scripture_pane,notes, var_notes))
viewmenu.add_checkbutton(label = 'View collections', variable = var_collections, command = lambda:toggle_window(right_pane, reference, var_collections))
#viewmenu.add_command(label = 'View collections on a separate window')
menu_bar.add_cascade(label = 'View', menu = viewmenu)

def nbk(e):
	next_book()

def pbk(e):
	prev_book()

root.bind('<Up>', nbk)
root.bind('<Down>', pbk)
def nc(e):
	next_ch()

def pc(e):
	prev_ch()

root.bind('<Right>', nc)
root.bind('<Left>', pc)

toolmenu = Menu(menu_bar)
toolmenu.add_command(label = 'Next book', accelerator = 'Up', command = next_book)
toolmenu.add_command(label = 'Previous book', accelerator = 'Down', command = prev_book)
toolmenu.add_command(label = 'Next chapter', accelerator = 'Right', command = next_ch)
toolmenu.add_command(label = 'Previous chapter', accelerator = 'Left', command = prev_ch)
toolmenu.add_separator()
toolmenu.add_command(label = 'Copy selected text', accelerator = 'Ctrl + C', command = ccp)
toolmenu.add_command(label = 'Search selected text', command =lambda: hilighted_text(scripture_book))
toolmenu.add_command(label = 'Dictionary meaning of selected word', command =lambda: dictionary_look(None),
	accelerator = 'Ctrl + F')
toolmenu.add_separator()
toolmenu.add_command(label = 'Add verse to collection', accelerator = 'Ctrl M', command = get_current_line)
toolmenu.add_separator()
toolmenu.add_command(label = 'Write notes', accelerator = 'Ctrl + W', command = write_note)
toolmenu.add_command(label = 'Read notes', accelerator = 'Ctrl + R', command = view_notes)
toolmenu.add_command(label= 'Copy notes', accelerator = 'Ctrl + Shift + C', command = copy_note)
toolmenu.add_separator()
toolmenu.add_command(label='Present', accelerator='Ctrl + J', command=lambda: presentation(None))
toolmenu.add_checkbutton(label='Presentation mode', variable= mode, command= change_mode)
# toolmenu.add_command(label = 'Highlights', command = hilight_box)
menu_bar.add_cascade(label = 'Tools', menu = toolmenu)

resource = Menu(menu_bar)
# resource.add_command(label = 'Online books')
# resource.add_command(label = 'Bible commentaries')
# resource.add_separator()
guides = Menu(resource)
guides.add_command(label = 'King James Version', command = kjv)
guides.add_command(label = 'American Standard Version', command = asv)
guides.add_command(label = 'Young Literal Translation', command = ylt)
guides.add_command(label = 'American King James Version', command = akjv)
guides.add_command(label = 'World Edition Bible', command = web)
guides.add_command(label = 'English Revised Version', command = erv)
guides.add_command(label = 'World Revised Version', command = wrv)
# guides.add_command(label = 'Bible study groups')
# guides.add_separator()
# guides.add_command(label= 'Study guide')
#guides.add_command(label = 'Bible reading plans', command = Plan.plan)
resource.add_cascade(label = 'Bible versions', menu = guides)
commentaries = Menu(resource)
commentaries.add_command(label = 'The Shepherd\'s Staff', command = staff)
commentaries.add_separator()
commentaries.add_command(label = 'The book of Matthew', command = matthew)
commentaries.add_command(label = 'The book of Mark, 1 and 2 Peter', command = mark)
commentaries.add_command(label = 'The Acts of Apostles', command = acts)
commentaries.add_command(label = 'The Gospel of John, 1, 2 & 3 John', command = john)
commentaries.add_command(label = 'The book of Romans', command = romans)
commentaries.add_command(label = 'The book of 1 Timothy, Titus & 2 Timothy', command = timothy)
commentaries.add_command(label = 'The book of Ecclesiastes', command = ecclesiastes)
commentaries.add_command(label = 'The book of Revelation', command = revelation)
resource.add_cascade(label = 'Comentaries', menu = commentaries)

devotionals = Menu(resource)
devotionals.add_command(label = 'Daily Psalms', command =lambda:  Plan.plan(eb))
devotionals.add_command(label = 'Daily verse', command =lambda: PlanB.plan(eb))
# devotionals.add_command(label = 'Topical devotionals')
# devotionals.add_command(label = 'From verses with notes')
# devotionals.add_separator()
# devotionals.add_command(label = 'Daily quotes from community')
# devotionals.add_command(label = 'Daily sermons')
devotionals.add_separator()
# devotionals.add_command(label = 'Video devotionals')
# devotionals.add_command(label = 'Audio devotionals')
resource.add_cascade(label = 'Devotionals', menu = devotionals)
# resource.add_separator()
# resource.add_command(label = 'Questions and answers')
# resource.add_command(label = 'Ask Questions')
menu_bar.add_cascade(label = 'Resources', menu = resource)

def open_documentation(Event = None):
	mypath = os.path.abspath('docs/app documentation.pdf')
	webbrowser.open('file://'+ mypath)

def our_web():
	webbrowser.open('https://heavenlycity.mystrikingly.com/')

def report():
	# webbrowser.open('https://heavenlycity.mystrikingly.com/')
	pass

def improve():
	# webbrowser.open('https://heavenlycity.mystrikingly.com/')
	pass

root.bind('<F1>', open_documentation)
# th = ['morph', 'litera', 'cerculean','siplex','yeti','united','sandston','pulse','minty','lumen','journal',
# 'solar','cyborg','vapor',]
root.bind('<F10>', lambda e: cerculean())
root.bind('<F11>', lambda e: cosmo())
root.bind('<F12>', lambda e: yeti())
root.bind('<F2>', lambda e: flatly())
root.bind('<F3>', lambda e: darkly())
root.bind('<F4>', lambda e: superhero())
root.bind('<F6>', lambda e: morph())
root.bind('<F7>', lambda e: solar())
root.bind('<F8>', lambda e: cyborg())
root.bind('<F9>', lambda e: vapor())

thememenu = Menu()
thememenu.add_command(label = 'Cosmo (Light)', command = cosmo, accelerator = 'F11')
thememenu.add_command(label = 'Flatly (Light)', command = flatly, accelerator = 'F2')
thememenu.add_command(label = 'Darkly (Dark)', command = darkly, accelerator = 'F3')
thememenu.add_command(label = 'Superhero', command = superhero, accelerator = 'F4')
thememenu.add_command(label = 'Morph', command = morph, accelerator = 'F6')
# thememenu.add_command(label = 'Litera', command = litera)
thememenu.add_command(label = 'Cerculean', command = cerculean, accelerator = 'F10')
# thememenu.add_command(label = 'Siplex', command = siplex)
thememenu.add_command(label = 'Yeti', command = yeti, accelerator = 'F12')
# thememenu.add_command(label = 'United', command = united)
# thememenu.add_command(label = 'Sandstone', command = sandston)
# thememenu.add_command(label = 'Pulse', command = pulse)
# thememenu.add_command(label = 'Minty', command = minty)
# thememenu.add_command(label = 'Lumen', command = lumen)
# thememenu.add_command(label = 'Journal', command = journal)
thememenu.add_command(label = 'Solar', command = solar, accelerator = 'F7')
thememenu.add_command(label = 'Cyborg', command = cyborg, accelerator = 'F8')
thememenu.add_command(label = 'Vapor', command = vapor, accelerator = 'F9')
#thememenu.add_separator()
#thememenu.add_command(label = 'Plain window (Vista)', command = run_main)
menu_bar.add_cascade(label = 'Theme', menu = thememenu)


def fullscreenmode(e):
	root.wm_attributes('-fullscreen', True)
	root.attributes('-topmost', False)

def not_fullscreen(e):
	root.wm_attributes('-fullscreen', False)
	root.attributes('-topmost', False)

root.bind('<F5>', fullscreenmode)
root.bind('<Escape>', not_fullscreen)

windowmenu = Menu()
windowmenu.add_command(label = 'Enter fullscreen mode', accelerator = 'F5', command = lambda: fullscreenmode(None))
windowmenu.add_command(label = 'Leave fullscreen mode', accelerator = 'Esc', command = lambda: not_fullscreen(None))
menu_bar.add_cascade(label = 'Window', menu = windowmenu)

helpmenu = Menu(menu_bar)
helpmenu.add_command(label = 'Documentation', accelerator = 'F1', compound = 'left', image = doc_img, command = open_documentation)
helpmenu.add_separator()
# helpmenu.add_command(label = 'About us')
helpmenu.add_command(label = 'Our website', command = our_web)
# helpmenu.add_command(label = 'Feedback')
# helpmenu.add_command(label = 'Support us')
# helpmenu.add_command(label = 'Partner with us')
helpmenu.add_separator()
# helpmenu.add_command(label = 'Report a problem', command = report)
# helpmenu.add_command(label = 'Improve our application', command = improve)
helpmenu.add_command(label = 'Application version', command = AppVersion)
menu_bar.add_cascade(label = 'Help', menu = helpmenu)

Collection.file_opening(root, state, reference_book)

root.state('zoomed')
root.update_idletasks()
def quit(e):
	save_history()
	# fr = tk.Frame(root)
	# # fr.place(x = sw/2.6, y = sh/2.8)
	# gb = tk.Label(fr, text = 'Good bye!', font = ('roboto', 24, 'bold'))
	# gb.pack(side = TOP, pady = 50, padx = 50)
	# fr.configure(background = 'whitesmoke')
	# gb.configure(background = 'whitesmoke')
	# fr.place(x = sw/2.6, y = sh/2.8)
	
	# time.sleep(3)
	root.destroy()
	
root.bind('<Control-q>',quit)
root.config(menu = menu_bar)

root.mainloop()