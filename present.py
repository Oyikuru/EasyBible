from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import ctypes.wintypes


# BACKGROUND_IMG = ''
OUTLINE_COLOR = 'black'
ALIGNMENT = 'center'
FONT_FAMILY = 'Arial'
FONT_SIZE = 32
FONT_COLOR = 'white'

def slide_show(slide_text, ref):
    canvas.itemconfigure(l, text = slide_text)
    canvas.itemconfigure(l_outline, text = slide_text)
    canvas.itemconfigure(bref, text = ref)
    canvas.itemconfigure(bref_outline, text = ref)

def present_bg():
    canvas.configure(background= 'blue')

def to_projector():
    def get_monitors_info():
        """Obtain all monitors information and return information for the second monitor"""
        """Windows only - using user32 eliminates the need to install the pywin32 software package"""
        user32 = ctypes.windll.user32

        def _get_monitors_resolution():
            monitors = []
            monitor_enum_proc = ctypes.WINFUNCTYPE(
                ctypes.c_int, ctypes.c_ulong, ctypes.c_ulong, ctypes.POINTER(ctypes.wintypes.RECT), ctypes.c_double)

            # Callback function,to obtain information for each display
            def callback(hMonitor, hdcMonitor, lprcMonitor, dwData):
                monitors.append((lprcMonitor.contents.left, lprcMonitor.contents.top,
                                 lprcMonitor.contents.right - lprcMonitor.contents.left,
                                 lprcMonitor.contents.bottom - lprcMonitor.contents.top))
                return 1

            # Enumerate all Monitors
            user32.EnumDisplayMonitors(None, None, monitor_enum_proc(callback), 0)
            return monitors

        # All monitors information
        monitors = _get_monitors_resolution()
        return monitors

    class MyApp:
        def __init__(self, master):
            self.master = master
            master.title("Easy Bible Presentation")
            monitors = get_monitors_info()
            if len(monitors) >= 2:
                x1 = monitors[1][0]
                y1 = monitors[1][1]
                w1 = monitors[1][2]
                h1 = monitors[1][3]
                # print("%dx%d+%d+%d" % (w1, h1, x1, y1))
                "Can move the window via project.geometry, but it cannot be moved to full screen on the secondary monitor via project.wm_attributes('-fullscreen',True) either"
                "The fullscreen top-level window created with overrideredirect(1) can be fullscreen on the secondary screen after moving the position。"
                project.geometry("%dx%d+%d+%d" % (w1, h1, x1, y1))
                # project.wm_attributes('-fullscreen', True)
                project.overrideredirect(1)
                # project.attributes("-topmost", True)
            else:
                w1 = monitors[0][2]
                h1 = monitors[0][3]
                project.geometry("%dx%d+%d+%d" % (w1, h1, 0, 0))
                project.overrideredirect(1)
            master.bind('<Double-Button-1>', self.toggle_fullscreen)
            master.bind("<F11>", self.toggle_fullscreen)
            master.bind('<Escape>', self.close)

        def toggle_fullscreen(self, event=None):
            overrideredirect_value = project.overrideredirect()
            if (overrideredirect_value):
                project.overrideredirect(0)
            else:
                project.overrideredirect(1)

        def close(self, event=None):
            # set the running flag False to stop updating the image
            self.running = False
            # close the window
            self.master.destroy()

    project = Toplevel()
    sw = project.winfo_screenwidth()
    sh = project.winfo_screenheight()
    project.title('Easy Bible Presentation')
    icon = PhotoImage(file='slide.png')
    project.iconphoto(False, icon)
    global canvas, l, l_outline, bref, bref_outline

    canvas = ttk.Canvas(project, width=sw, height=sh, background='green')
    # background = PhotoImage(file=bg_background)
    # canvas.create_image(0, 0, anchor=NW, image=BACKGROUND_IMG)
    # my_img = canvas.create_image(0, 0, anchor=NW)

    canvas.pack(side=LEFT, fill=BOTH, expand=1)
    l_outline = canvas.create_text((sw / 4) - 1, (sh / 3) - 1, anchor='center', width=sw / 2.5,
                                   text=' ', fill=OUTLINE_COLOR,
                                   font=(FONT_FAMILY, FONT_SIZE, 'bold'), justify=ALIGNMENT)
    l = canvas.create_text(sw / 4, sh / 3, anchor='center', width=sw / 2.5,
                           text=' ', fill=FONT_COLOR,
                           font=(FONT_FAMILY, FONT_SIZE, 'bold'), justify=ALIGNMENT)

    bref_outline = canvas.create_text((sw / 4) - 1, 49, fill=OUTLINE_COLOR, font=(FONT_FAMILY, 22, 'bold'), text=' ',
                                      justify=ALIGNMENT, width=sw/2.5, anchor='center')
    bref = canvas.create_text(sw / 4, 50, fill=FONT_COLOR, font=(FONT_FAMILY, 22, 'bold'), text=' ',
                              justify=ALIGNMENT, width=sw/2.5, anchor='center')
    canvas.configure(background='blue')

    #

    app = MyApp(project)

