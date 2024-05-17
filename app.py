import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from main import *

def predict():
    try:
        res = grade_predict(int(pre_co_max.get()),int(pre_co1.get()),int(pre_co2.get()),int(pre_co3.get()),int(pre_co4.get()),int(pre_co5.get()),int(pre_assign.get()))
    except ValueError:
        msgbox.showerror(title='Value Error', message="Invalid Input")
        return
    res_txt = "Predicted Scores to get in Final Exam:\n"
    for i in range(6):
        grade = ['PASS','B','B+','A','A+','O'][i]
        try:
            g_mark = f" : {res[i]:.{2}f}"
        except ValueError:
            g_mark = f" : {res[i]}"
        res_txt = res_txt + grade + g_mark + "\n"
    pre_output.configure(state=tk.NORMAL)
    pre_output.delete(1.0,tk.END)
    pre_output.insert(tk.END, res_txt)
    pre_output.configure(state=tk.DISABLED)
                    
def calculate():
    try:
        res = grade_calc(int(cal_co_max.get()),int(cal_co1.get()),int(cal_co2.get()),int(cal_co3.get()),int(cal_co4.get()),int(cal_co5.get()),int(cal_assign.get()),int(cal_final.get()))
    except ValueError:
        msgbox.showerror(title='Value Error', message="Invalid Input")
        return
    res_txt = f"Total marks : {res[0]}\nGrade : {res[1]}"
    cal_output.configure(state=tk.NORMAL)
    cal_output.delete(1.0,tk.END)
    cal_output.insert(tk.END, res_txt)
    cal_output.configure(state=tk.DISABLED)
    
    
root = tk.Tk()
root.title("Grade-Predictor")

tabs = ttk.Notebook(root)

gp_frame = ttk.Frame(tabs)

pre_co_max_lbl = ttk.Label(gp_frame, text = "Course Outcome Maximum Marks : ")
pre_co_max_lbl.grid(row = 0, column = 0, padx = 5 , pady = 5, sticky = 'e')
pre_co1_lbl = ttk.Label(gp_frame, text = "Course Outcome 1 Marks : ")
pre_co1_lbl.grid(row = 1, column = 0, padx = 5 , pady = 5, sticky = 'e')
pre_co2_lbl = ttk.Label(gp_frame, text = "Course Outcome 2 Marks : ")
pre_co2_lbl.grid(row = 2, column = 0, padx = 5 , pady = 5, sticky = 'e')
pre_co3_lbl = ttk.Label(gp_frame, text = "Course Outcome 3 Marks : ")
pre_co3_lbl.grid(row = 3, column = 0, padx = 5 , pady = 5, sticky = 'e')
pre_co4_lbl = ttk.Label(gp_frame, text = "Course Outcome 4 Marks : ")
pre_co4_lbl.grid(row = 4, column = 0, padx = 5 , pady = 5, sticky = 'e')
pre_co5_lbl = ttk.Label(gp_frame, text = "Course Outcome 5 Marks : ")
pre_co5_lbl.grid(row = 5, column = 0, padx = 5 , pady = 5, sticky = 'e')
pre_assign_lbl = ttk.Label(gp_frame, text = "Assignment Marks : ")
pre_assign_lbl.grid(row = 6, column = 0, padx = 5 , pady = 5, sticky = 'e')

pre_co_max = tk.StringVar()
pre_co1 = tk.StringVar()
pre_co2 = tk.StringVar()
pre_co3 = tk.StringVar()
pre_co4 = tk.StringVar()
pre_co5 = tk.StringVar()
pre_assign = tk.StringVar()

pre_co_max_ent = ttk.Entry(gp_frame, textvariable = pre_co_max)
pre_co_max_ent.grid(row = 0, column = 1, padx = 5 , pady = 5, sticky = 'w')
pre_co1_ent = ttk.Entry(gp_frame, textvariable = pre_co1)
pre_co1_ent.grid(row = 1, column = 1, padx = 5 , pady = 5, sticky = 'w')
pre_co2_ent = ttk.Entry(gp_frame, textvariable = pre_co2)
pre_co2_ent.grid(row = 2, column = 1, padx = 5 , pady = 5, sticky = 'w')
pre_co3_ent = ttk.Entry(gp_frame, textvariable = pre_co3)
pre_co3_ent.grid(row = 3, column = 1, padx = 5 , pady = 5, sticky = 'w')
pre_co4_ent = ttk.Entry(gp_frame, textvariable = pre_co4)
pre_co4_ent.grid(row = 4, column = 1, padx = 5 , pady = 5, sticky = 'w')
pre_co5_ent = ttk.Entry(gp_frame, textvariable = pre_co5)
pre_co5_ent.grid(row = 5, column = 1, padx = 5 , pady = 5, sticky = 'w')
pre_assign_ent = ttk.Entry(gp_frame, textvariable = pre_assign)
pre_assign_ent.grid(row = 6, column = 1, padx = 5 , pady = 5, sticky = 'w')

pre_btn = ttk.Button(gp_frame, text='Predict', command = predict)
pre_btn.grid(row = 7, column = 1, padx = 5 , pady = 5, sticky = 'w')

pre_output = tk.Text(gp_frame, height = 10, width = 50, state = tk.DISABLED)
pre_output.grid(row = 8, column = 0, columnspan=2, padx = 5 , pady = 5)

gp_frame.pack(padx = 5 , pady = 5)

gc_frame = ttk.Frame(tabs)

cal_co_max_lbl = ttk.Label(gc_frame, text = "Course Outcome Maximum Marks : ")
cal_co_max_lbl.grid(row = 0, column = 0, padx = 5 , pady = 5, sticky = 'e')
cal_co1_lbl = ttk.Label(gc_frame, text = "Course Outcome 1 Marks : ")
cal_co1_lbl.grid(row = 1, column = 0, padx = 5 , pady = 5, sticky = 'e')
cal_co2_lbl = ttk.Label(gc_frame, text = "Course Outcome 2 Marks : ")
cal_co2_lbl.grid(row = 2, column = 0, padx = 5 , pady = 5, sticky = 'e')
cal_co3_lbl = ttk.Label(gc_frame, text = "Course Outcome 3 Marks : ")
cal_co3_lbl.grid(row = 3, column = 0, padx = 5 , pady = 5, sticky = 'e')
cal_co4_lbl = ttk.Label(gc_frame, text = "Course Outcome 4 Marks : ")
cal_co4_lbl.grid(row = 4, column = 0, padx = 5 , pady = 5, sticky = 'e')
cal_co5_lbl = ttk.Label(gc_frame, text = "Course Outcome 5 Marks : ")
cal_co5_lbl.grid(row = 5, column = 0, padx = 5 , pady = 5, sticky = 'e')
cal_assign_lbl = ttk.Label(gc_frame, text = "Assignment Marks : ")
cal_assign_lbl.grid(row = 6, column = 0, padx = 5 , pady = 5, sticky = 'e')
cal_final_lbl = ttk.Label(gc_frame, text = "Final Exam Marks : ")
cal_final_lbl.grid(row = 7, column = 0, padx = 5 , pady = 5, sticky = 'e')

cal_co_max = tk.StringVar()
cal_co1 = tk.StringVar()
cal_co2 = tk.StringVar()
cal_co3 = tk.StringVar()
cal_co4 = tk.StringVar()
cal_co5 = tk.StringVar()
cal_assign = tk.StringVar()
cal_final = tk.StringVar()

cal_co_max_ent = ttk.Entry(gc_frame, textvariable = cal_co_max)
cal_co_max_ent.grid(row = 0, column = 1, padx = 5 , pady = 5, sticky = 'w')
cal_co1_ent = ttk.Entry(gc_frame, textvariable = cal_co1)
cal_co1_ent.grid(row = 1, column = 1, padx = 5 , pady = 5, sticky = 'w')
cal_co2_ent = ttk.Entry(gc_frame, textvariable = cal_co2)
cal_co2_ent.grid(row = 2, column = 1, padx = 5 , pady = 5, sticky = 'w')
cal_co3_ent = ttk.Entry(gc_frame, textvariable = cal_co3)
cal_co3_ent.grid(row = 3, column = 1, padx = 5 , pady = 5, sticky = 'w')
cal_co4_ent = ttk.Entry(gc_frame, textvariable = cal_co4)
cal_co4_ent.grid(row = 4, column = 1, padx = 5 , pady = 5, sticky = 'w')
cal_co5_ent = ttk.Entry(gc_frame, textvariable = cal_co5)
cal_co5_ent.grid(row = 5, column = 1, padx = 5 , pady = 5, sticky = 'w')
cal_assign_ent = ttk.Entry(gc_frame, textvariable = cal_assign)
cal_assign_ent.grid(row = 6, column = 1, padx = 5 , pady = 5, sticky = 'w')
cal_final_ent = ttk.Entry(gc_frame, textvariable = cal_final)
cal_final_ent.grid(row = 7, column = 1, padx = 5 , pady = 5, sticky = 'w')

cal_btn = ttk.Button(gc_frame, text='Calculate', command = calculate)
cal_btn.grid(row = 8, column = 1, padx = 5 , pady = 5, sticky = 'w')

cal_output = tk.Text(gc_frame, height = 10, width = 50, state = tk.DISABLED)
cal_output.grid(row = 9, column = 0, columnspan=2, padx = 5 , pady = 5)

gc_frame.pack(padx = 5 , pady = 5)

tabs.add(gp_frame, text = "Grade Predict")
tabs.add(gc_frame, text = "Grade Calculate")
tabs.pack(expand = 1, fill ="both")

root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file="icon.png"))
root.mainloop()