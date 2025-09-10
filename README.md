
# 🛠️ Cockpit Dashboard

A modular, reproducible dashboard built with `tkinter` and `ttkbootstrap`, designed for embedded and desktop environments. Inspired by cockpit-grade clarity, this project separates UI from backend logic and emphasizes introspection, maintainability, and operational sanity.

---

## 📦 Project Structure
cockpit_dashboard/
├── main.py                          # Entry point: launches HomeWindow
├── config/
│   ├── init.py
│   ├── styles.py                    # ttkbootstrap themes, colors, fonts
│   ├── layout.py                    # Grid weights, padding, layout constants
│   └── settings.py                  # App-wide config, paths, flags
├── ui/
│   ├── init.py
│   ├── home_window.py               # HomeWindow class
│   ├── settings_window.py           # SettingsWindow class
│   ├── log_window.py                # LogWindow class
│   ├── engine_panel.py              # EnginePanel class
│   ├── house_panel.py               # HousePanel class
│   └── gauge.py                     # Gauge class (used by RPM + sensors)
├── backend/
│   ├── init.py
│   ├── engine_model.py              # Engine data acquisition + parsing
│   ├── house_model.py               # House sensor data model
│   ├── logger.py                    # Logging, rotation, filtering
│   └── controller.py                # Event handlers, state transitions
├── assets/
│   ├── icons/                       # PNG/SVG icons
│   ├── fonts/                       # Custom fonts
│   └── images/                      # Backgrounds, gauge overlays
├── tests/
│   ├── test_engine_model.py
│   ├── test_gauge_rendering.py
│   └── test_layout_integrity.py
└── README.md


---

## 🚀 Getting Started

### Requirements

- Python 3.10+
- `ttkbootstrap`
- `tkinter` (included with Python)
- Optional: `pytest` for testing

### Launch the Dashboard

```bash
python main.py
