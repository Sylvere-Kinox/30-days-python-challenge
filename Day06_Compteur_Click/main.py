# App de compteur de clicks
import tkinter as tk
from tkinter import messagebox

# ==================== CONFIGURATION ====================
# Création de la fenêtre principale
root = tk.Tk()
root.title("Compteur de Clicks")
root.geometry("400x300")
root.configure(bg="#dfcfcf")

# Variables globales
counter = 0
OBJECTIF = 20

# ==================== FONCTIONS ====================
def increment_counter():
    global counter
    counter += 1
    update_counter()
    check_objectif()

def decrement_counter():
    global counter
    if counter > 0:
        counter -= 1
    update_counter()

def reset_counter():
    global counter
    counter = 0
    update_counter()

def update_counter():
    """Met à jour l'affichage du compteur avec couleur"""
    counter_label.config(text=f"Compteur: {counter}")
    
    if counter == 0:
        counter_label.config(fg="black")
    elif counter < 10:
        counter_label.config(fg="green")
    else:
        counter_label.config(fg="red")

def check_objectif():
    """Vérifie si l'objectif est atteint"""
    if counter == OBJECTIF:
        messagebox.showinfo(
            "Bravo !",
            f"Objectif de {OBJECTIF} atteint !"
        )

# ==================== WIDGETS ====================
# Titre
title_label = tk.Label(
    root,
    text="Bienvenue dans mon compteur de clicks !",
    font=("Arial", 16),
    bg="#dfcfcf"
)
title_label.pack(pady=20)

# Compteur
counter_label = tk.Label(
    root,
    text=f"Compteur: {counter}",
    font=("Arial", 16),
    bg="#dfcfcf"
)
counter_label.pack(pady=20)

# Boutons
button_increment = tk.Button(
    root,
    text="Cliquez ici !",
    font=("Arial", 12),
    command=increment_counter,
    bg="green",
    fg="white"
)
button_increment.pack(pady=10)

button_decrement = tk.Button(
    root,
    text="Décrémenter",
    font=("Arial", 12),
    command=decrement_counter,
    bg="orange",
    fg="white"
)
button_decrement.pack(pady=10)

button_reset = tk.Button(
    root,
    text="Réinitialiser",
    font=("Arial", 12),
    command=reset_counter,
    bg="red",
    fg="white"
)
button_reset.pack(pady=5)

button_exit = tk.Button(
    root,
    text="Quitter",
    font=("Arial", 12),
    command=root.quit,
    bg="gray",
    fg="white"
)
button_exit.pack(pady=5)

# ==================== LANCEMENT ====================
root.mainloop()