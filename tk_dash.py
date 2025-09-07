import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import font as tkfont

# === Global Constants ===
BGR_COLOR               = "#323232"
PRIMARY_COLOR           = "#A06000"
TEXT_COLOR              = "#DEDEDE"

CANVAS_WIDTH            = 1024
CANVAS_HEIGHT           = 600

FRAME_BOUNDARY_WIDTH    = 4
FRAME_BOUNDARY_ROUNDING = 8
FRAME_PADDING           = 20

FONT_SIZE               = 18
FONT                    = "Helvetica"

# === App Setup ===
app = ttkb.Window(themename="darkly")
app.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")
app.configure(background=BGR_COLOR, padx=FRAME_PADDING, pady=FRAME_PADDING)

# === Font Registration ===
default_font = tkfont.Font(family=FONT, size=FONT_SIZE)
app.option_add("*Font", default_font)

# === Custom Frame Style ===
style = ttkb.Style()
style.configure("Dashboard.TLabelframe",
    background=BGR_COLOR,
    bordercolor=TEXT_COLOR,
    borderwidth=FRAME_BOUNDARY_WIDTH,
    relief="solid"
)
style.configure("Dashboard.TLabelframe.Label",
    foreground=TEXT_COLOR,
    background=BGR_COLOR,
    font=(FONT, FONT_SIZE, "bold")
)


style.configure("Dashboard.TFrame", 
    background=BGR_COLOR,
    borderwidth=0
)

# === Layout Container ===
container = ttkb.Frame(app)
container.configure(style="Dashboard.TFrame")
container.pack(fill=BOTH, expand=True)

# === Left and Right Containers ===
left_container = ttkb.Frame(container, style="Dashboard.TFrame")
right_container = ttkb.Frame(container, style="Dashboard.TFrame")

left_container.pack(side=LEFT, fill=BOTH, expand=True)
right_container.pack(side=RIGHT, fill=BOTH, expand=True)

# === Engine Frame (Left) ===
engine_frame = ttkb.Labelframe(
    left_container,
    text=" Engine ",
    style="Dashboard.TLabelframe",
    padding=FRAME_PADDING
)
engine_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# === Batteries Frame ===
batteries_frame = ttkb.Labelframe(
    right_container,
    text=" Batteries ",
    style="Dashboard.TLabelframe"
)
batteries_frame.pack(fill=BOTH, expand=True, padx=10, pady=(10, 5))

# === Tanks Frame ===
tanks_frame = ttkb.Labelframe(
    right_container,
    text=" Tanks ",
    style="Dashboard.TLabelframe"
)
tanks_frame.pack(fill=BOTH, expand=True, padx=10, pady=(5, 10))

# === Responsive Grid ===
for col in range(3):
    container.columnconfigure(col, weight=1)
container.rowconfigure(0, weight=1)

app.mainloop()
