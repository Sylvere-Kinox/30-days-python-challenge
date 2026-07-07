import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

#Stockage des dépenses dans un fichier CSV
FICHIER_DEPENSES = "depenses.csv"

root = tk.Tk()
root.title("Application de Suivi de Dépense")
root.geometry("600x400")
root.config(bg="#f5f5f5")

depenses=[]

def charger_depenses():
    if os.path.exists(FICHIER_DEPENSES):
        with open(FICHIER_DEPENSES, mode='r', newline='', encoding='utf-8') as fichier:
            lecteur_csv = csv.reader(fichier)
            for ligne in lecteur_csv:
                
                depenses.append(ligne)
                depenses_listbox.insert(tk.END, f"{ligne[0]} - {ligne[1]} XOF CFA - {ligne[2]}")
                
def enregistrer_depense():
    with open(FICHIER_DEPENSES, "w", newline='') as fichier:
        ecrivain_csv = csv.writer(fichier)
        for depense in depenses:
            ecrivain_csv.writerow(depense)
def ajouter_depense():
    nom = nom_var.get()
    montant = montant_var.get()
    description = description_var.get()
    
    if not nom or not montant:
        messagebox.showwarning("Attention", "Veuillez remplir le nom et le montant de la dépense.")
        return
    
    try:
        montant_int = int(montant)
    except ValueError:
        messagebox.showwarning("Attention", "Le montant doit être un nombre entier.")
        return
    
    depense = [nom, montant, description]
    depenses.append(depense)
    depenses_listbox.insert(tk.END, f"{nom} - {montant} XOF CFA - {description}")
    calculer_total_depenses()
    enregistrer_depense()
    clear_inputs()
        
def supprimer_depense():
    try:
        index = depenses_listbox.curselection()[0]
        depenses_listbox.delete(index)
        del depenses[index]
        calculer_total_depenses()
        enregistrer_depense()
    except IndexError:
        messagebox.showwarning("Attention", "Veuillez sélectionner une dépense à supprimer.")
        
def calculer_total_depenses():
    total = sum(int(depense[1]) for depense in depenses)
    total_label.config(text=f"Total des Dépenses: {total} XOF CFA") 

def supprimer_toutes_depenses():
    if messagebox.askyesno("Confirmation", "Voulez-vous vraiment supprimer toutes les dépenses ?"):
        depenses.clear()
        depenses_listbox.delete(0, tk.END)
        calculer_total_depenses()
        enregistrer_depense()
    
def clear_inputs():
    nom_var.set("")
    montant_var.set("")
    description_var.set("")

title_label = tk.Label(root, text="Suivi de Dépense", font=("Helvetica", 16), bg="#f5f5f5")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f5f5f5")
input_frame.pack(pady=10)

#Menu déroulant pour sélectionner le nom de la dépense
nom_label = tk.Label(input_frame, text="Nom de la Dépense:", font=("Helvetica", 12), bg="#f5f5f5")
nom_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
nom_var = tk.StringVar(value="Selectionner une dépense")
nom_menu = ttk.Combobox(input_frame, textvariable=nom_var, values=["Alimentation", "Transport", "Logement", "Divertissement", "Santé", "Autres"], state="readonly")
nom_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")

#Montant de la dépense
montant_label = tk.Label(input_frame, text="Montant (XOF CFA):", font=("Helvetica", 12), bg="#f5f5f5")
montant_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
montant_var = tk.StringVar()
montant_entry = tk.Entry(input_frame, textvariable=montant_var, font=("Helvetica", 12))
montant_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")


#Description de la dépense
description_label = tk.Label(input_frame, text="Description:", font=("Helvetica", 12), bg="#f5f5f5")
description_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
description_var = tk.StringVar()
description_entry = tk.Entry(input_frame, textvariable=description_var, font=("Helvetica", 12))
description_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")


#Boutons pour ajouter et supprimer les dépenses
button_frame = tk.Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)
ajouter_button = tk.Button(button_frame, text="Ajouter Dépense", command=ajouter_depense, bg="#4caf50", fg="white", font=("Helvetica", 12))
ajouter_button.grid(row=0, column=0, padx=5)
supprimer_button = tk.Button(button_frame, text="Supprimer Dépense", command=supprimer_depense, bg="#f44336", fg="white", font=("Helvetica", 12))
supprimer_button.grid(row=0, column=1, padx=5)
supprimer_toutes_button = tk.Button(button_frame, text="Supprimer Toutes Dépenses", command=supprimer_toutes_depenses, bg="#f44336", fg="white", font=("Helvetica", 12))
supprimer_toutes_button.grid(row=0, column=2, padx=5)

#Listbox pour afficher les dépenses
listbox_frame = tk.Frame(root, bg="#f5f5f5")
listbox_frame.pack(pady=10)
scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

depenses_listbox = tk.Listbox(listbox_frame, font=("Helvetica", 12), width=50, height=15, yscrollcommand=scrollbar.set)
depenses_listbox.pack(pady=5)

scrollbar.config(command=depenses_listbox.yview)   

#Label pour afficher le total des dépenses
total_label = tk.Label(root, text="Total des Dépenses: 0 XOF CFA", font=("Helvetica", 14), bg="#f5f5f5")
total_label.pack(pady=10)

#charger les dépenses existantes au démarrage de l'application
charger_depenses()
calculer_total_depenses()

#Bouton pour quitter l'application
quitter_button = tk.Button(root, text="Quitter", command=root.destroy, bg="#9e9e9e", fg="white", font=("Helvetica", 12))
quitter_button.pack(pady=10)

root.mainloop()