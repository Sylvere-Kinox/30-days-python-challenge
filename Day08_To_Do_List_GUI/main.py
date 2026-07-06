import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.config(bg="#e3f2fd")

def ajouter_tache():
    tache = entry_tache.get()
    if tache:
        listbox_taches.insert(tk.END, tache)
        entry_tache.delete(0, tk.END)
    else:
        messagebox.showwarning("Attention", "Veuillez entrer une tâche.")
        
def supprimer_tache():
    try:
        index = listbox_taches.curselection()[0]
        listbox_taches.delete(index)
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une tâche à supprimer.")
        
def effacer_taches():
    listbox_taches.delete(0, tk.END)
    
title_label = tk.Label(root, text="Ma Liste de Tâches", font=("Helvetica", 16), bg="#e3f2fd")
title_label.pack(pady=10)

entry_tache = tk.Entry(root, width=30, font=("Helvetica", 14))
entry_tache.pack(pady=10)

button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=10)

ajouter_button = tk.Button(button_frame, text="Ajouter", command=ajouter_tache, bg="#4caf50", fg="white", font=("Helvetica", 12))
ajouter_button.grid(row=0, column=0, padx=5)

supprimer_button = tk.Button(button_frame, text="Supprimer", command=supprimer_tache, bg="#f44336", fg="white", font=("Helvetica", 12))
supprimer_button.grid(row=0, column=1, padx=5)

effacer_button = tk.Button(button_frame, text="Effacer Tout", command=effacer_taches, bg="#2196f3", fg="white", font=("Helvetica", 12))
effacer_button.grid(row=0, column=2, padx=5)

frame=tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_taches = tk.Listbox(frame, width=40, height=15, font=("Helvetica", 14), yscrollcommand=scrollbar.set)
listbox_taches.pack(pady=10)

scrollbar.config(command=listbox_taches.yview)

sorti_button = tk.Button(root, text="Sortir", command=root.destroy, bg="#9e9e9e", fg="white", font=("Helvetica", 12))
sorti_button.pack(pady=10)

root.mainloop()