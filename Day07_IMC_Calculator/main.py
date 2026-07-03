import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("IMC Calculator") 
root.geometry("400x400")
root.configure(bg="#f0f4c3")

title_label = tk.Label(root, 
    text="IMC Calculator", 
    font=("Helvetica", 16, "bold"), 
    bg="#f0f4c3"
    )
title_label.pack(pady=10)

weight_label = tk.Label(root,
    text="Poids (kg):",
    font=("Helvetica", 12),
    bg="#f0f4c3"
    )
weight_label.pack(pady=5)

weight_entry = tk.Entry(root, font=("Helvetica", 12))
weight_entry.pack(pady=5)

height_label = tk.Label(root,
    text="Taille (m):",
    font=("Helvetica", 12),
    bg="#f0f4c3"
    )
height_label.pack(pady=5)

height_entry = tk.Entry(root, font=("Helvetica", 12))
height_entry.pack(pady=5)

result_label = tk.Label(root,
    text="",   
    font=("Helvetica", 12),
    bg="#f0f4c3"   
)
result_label.pack(pady=10)

def calculate_imc():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        
        if weight <= 0 or height <= 0:
            raise ValueError("La taille et le poids doivent être des nombres positifs.")
        imc = weight / (height ** 2)
        
        if imc < 18.5:
            status = "Insuffisance pondérale"
            color = "orange"
        elif imc < 25:
            status = "Poids normal"
            color = "green"
        elif imc < 30:
            status = "Surpoids"
            color = "orange"
        else:
            status = "Obésité"
            color = "red"

        result_label.config(
            text=f"IMC : {imc:.2f}\n{status}",
            fg=color
        )
    except ValueError: 
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs valides pour le poids et la taille.")   

calculate_imc_button = tk.Button(root,
    text="Calculer l'IMC", 
    font=("Helvetica", 12),
    command=calculate_imc,
    bg="#8bc34a",
    fg="white"
    )
calculate_imc_button.pack(pady=10)
reset_button = tk.Button(root,
    text="Réinitialiser", 
    font=("Helvetica", 12),
    command=lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text="")],
    bg="#f44336",
    fg="white"
    ) 
reset_button.pack(pady=10)
root.mainloop()      