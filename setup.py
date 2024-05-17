import cx_Freeze

executables = [cx_Freeze.Executable("app.py", base='gui', icon="icon.png")]

cx_Freeze.setup(
    name = "Grade-Predictor",
    options = {"build_exe": {"packages":["tkinter"], "include_files":["icon.png","main.py"]}},
    version = "2024.1",
    description = "Predicting and calculating grades for college courses.",
    executables = executables
    )