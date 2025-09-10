import os
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from tkinter import font as tkfont 

# === Global Constants ===
CANVAS_WIDTH            = 1024
CANVAS_HEIGHT           = 600
FRAME_BOUNDARY_WIDTH    = 4
FRAME_PADDING           = 20
FONT_SIZE               = 18
FONT                    = "Oxanium"

# === App Setup ===
app = ttkb.Window(themename="darkly")
app.geometry(f"{CANVAS_WIDTH}x{CANVAS_HEIGHT}")

# === Global Styling (after window!) ===
style = ttkb.Style()
colors = style.colors
app.configure(
    background=colors.bg,
    padx=FRAME_PADDING,
    pady=FRAME_PADDING,
)

# === Font Registration ===
tkfont.Font(root=app, name=FONT,       family=FONT, size=FONT_SIZE)
tkfont.Font(root=app, name=FONT + "Bold", family=FONT, size=FONT_SIZE, weight="bold")
app.option_add("*Font", FONT)

# === Custom Frame Style ===
style.configure("Dashboard.TLabelframe",
    background=colors.bg,
    bordercolor=colors.fg,
    borderwidth=FRAME_BOUNDARY_WIDTH,
    relief="solid"
)
style.configure("Dashboard.TLabelframe.Label",
    foreground=colors.fg,
    background=colors.bg,
    font=(FONT, FONT_SIZE, "normal")
)
style.configure("Dashboard.TFrame", 
    background=colors.bg,
    borderwidth=0
)

# === Layout Container ===
container = ttkb.Frame(app, style="Dashboard.TFrame")
container.pack(fill=BOTH, expand=True)

# === Left and Right Panels ===
left_container  = ttkb.Frame(container, style="Dashboard.TFrame")
right_container = ttkb.Frame(container, style="Dashboard.TFrame")

left_container.pack(side=LEFT,  fill=BOTH, expand=True)
right_container.pack(side=RIGHT, fill=BOTH, expand=True)

# === Engine Frame (Left) ===
engine_frame = ttkb.Labelframe(
    left_container,
    text=" Engine ",
    style="Dashboard.TLabelframe",
    padding=FRAME_PADDING
)
engine_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

# === Batteries Frame (Top Right) ===
batteries_frame = ttkb.Labelframe(
    right_container,
    text=" Batteries ",
    style="Dashboard.TLabelframe"
)
batteries_frame.pack(fill=BOTH, expand=True, padx=10, pady=(10, 5))

# === Tanks Frame (Bottom Right) ===
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
