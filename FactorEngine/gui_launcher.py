import tkinter as tk
from tkinter import messagebox
import subprocess


def run_pipeline():
    try:
        subprocess.run(["python", "main.py"], check=True)
        messagebox.showinfo("Pipeline", "PrimeEngineAI pipeline launched successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))


app = tk.Tk()
app.title("PrimeEngineAI GUI")
app.geometry("400x200")

label = tk.Label(app, text="PrimeEngineAI Launcher", font=("Arial", 16))
label.pack(pady=20)

start_btn = tk.Button(
    app, text="Run Pipeline", command=run_pipeline, height=2, width=20
)
start_btn.pack(pady=10)

app.mainloop()
