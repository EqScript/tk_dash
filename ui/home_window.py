###########################################################
# 
# @file     home_window.py
# @dir      ./ui
# @brief    Home Window module of the HMI Display project
# @author   Sergio @EqScript Belenkoff
# @date     10 Sep, 2025
#
############################################################


import tkinter as tk
from ttkbootstrap import Style

# Constants
DEFAULT_PADX = 10
DEFAULT_PADY = 20

# Style globals
style = Style(theme="darkly")
color_primary = style.colors.primary
color_secondary = style.colors.secondary
color_bg = style.colors.bg
color_fg = style.colors.fg
color_warning = style.colors.warning


class HomeWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard - Home")
        self.geometry("1024x600")
        self.style = Style(theme="darkly")

        # Grid config: 3 rows (Top, Middle, Bottom), 
        # 3 Columns (Left, Center, Right) in Middle Row
        for r, weight in enumerate((1, 3, 1)):
            self.rowconfigure(r, weight=1)
        for c, weight in range(3):
            self.columnconfigure(c, weight=1)

        # Top bar frames
        for col in range(3):
            tk.Frame(self, bg=color_bg).grid(row=0, column=col,
                sticky="nsew", padx=DEFAULT_PADX, pady=DEFAULT_PADY)

        # Middle row panels
        self.engine_panel = EnginePanel(self)
        self.engine_panel.grid(row=1, column=0, sticky="nsew", padx=DEFAULT_PADX, pady=DEFAULT_PADY)

        self.rpm_meter = RpmMeter(self, gauge_type="RPM")
        self.rpm_meter.grid(row=1, column=1, sticky="nsew", padx=DEFAULT_PADX, pady=DEFAULT_PADY)

        self.house_panel = HousePanel(self)
        self.house_panel.grid(row=1, column=2, sticky="nsew", padx=DEFAULT_PADX, pady=DEFAULT_PADY)

        # Bottom row panels
        tk.Frame(self, bg=color_bg).grid(row=2, column=0, sticky="nsew", padx=DEFAULT_PADX, pady=DEFAULT_PADY)
        tk.Frame(self, bg=color_bg).grid(row=2, column=1, sticky="nsew", padx=DEFAULT_PADX, pady=DEFAULT_PADY)
        tk.Frame(self, bg=color_bg).grid(row=2, column=2, sticky="nsew", padx=DEFAULT_PADX, pady=DEFAULT_PADY)