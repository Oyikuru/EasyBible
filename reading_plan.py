from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
# import customtkinter as ctk
from books import get_psalms, get_rand_verse
#from ttkwidgets import *
#from ttkwidgets import tooltips
#from tkinter.messagebox import *

class Plan(Toplevel):
	"""docstring for Plan"""
	def __init__(self):
		super().__init__()
		self.title('Easy Bible - Daily Psalms')
		self.attributes('-topmost', True)
		#self.geometry('600x600')
		
		

	def plan(img):
		root = Plan()
		frame = ttk.Frame(root)
		frame.pack(side = 'top', fill = 'both', expand=1)

		verse = get_psalms().split(']')

		ref = ttk.Label(frame, text = f"{verse[0]}]", font = ('roboto', 20))
		ref.pack(side = 'top', fill = 'x')

		label = tk.Message(frame, text = verse[1], font = ('roboto', 24), justify = 'center', aspect = 300)
		label.pack(fill = 'both', expand = 1)

		plans = ttk.Frame(frame)
		plans.pack(side = 'top', fill = 'x')

		
		next_b = ttk.Button(plans, text = 'Next', command = lambda: Plan.next_step(label, ref))
		next_b.pack(side='right', padx = 10, pady = 10)

		cancel = ttk.Button(plans, text = 'Close', command = root.destroy)
		cancel.pack(side='right', padx = 10, pady =10)

		root.iconphoto(False, img)
		
		#root.mainloop()

	def next_step(label, ref):
		verse = get_psalms().split(']')
		label.configure(text = verse[1])
		ref.configure(text = f'{verse[0]}]')


class PlanB(Toplevel):
	"""docstring for Plan"""
	def __init__(self):
		super().__init__()
		self.title('Easy Bible - Daily verses')
		self.attributes('-topmost', True)
		#self.geometry('600x600')
		
		

	def plan(img):
		root = Plan()
		frame = ttk.Frame(root)
		frame.pack(side = 'top', fill = 'both', expand=1)

		verse = get_rand_verse().split(']')

		ref = ttk.Label(frame, text = f"{verse[0]}]", font = ('roboto', 20))
		ref.pack(side = 'top', fill = 'x')

		label = tk.Message(frame, text = verse[1], font = ('roboto', 24), justify = 'center', aspect = 300)
		label.pack(fill = 'both', expand = 1)

		plans = ttk.Frame(frame)
		plans.pack(side = 'top', fill = 'x')

		
		next_b = ttk.Button(plans, text = 'Next', command = lambda: PlanB.next_step(label, ref))
		next_b.pack(side='right', padx = 10, pady = 10)

		cancel = ttk.Button(plans, text = 'Cancel', command = root.destroy)
		cancel.pack(side='right', padx = 10, pady =10)

		root.iconphoto(False, img)


		
		#root.mainloop()

	def next_step(label, ref):
		verse = get_rand_verse().split(']')
		label.configure(text = verse[1])
		ref.configure(text = f'{verse[0]}]')

#Plan.plan()
