import tkinter as tk

root = tk.Tk()
root.title("Simple GUI App")
root.geometry("400x300")
root.configure(bg="lightblue")

# Title label
title_label = tk.Label(root, text="Bienvenue dans mon application GUI !", font=("Arial", 16), bg="lightblue")
title_label.pack(pady=20)

#Label Nom
name_label = tk.Label(root, text="Nom:", font=("Arial", 12), bg="lightblue")
name_label.pack(pady=5)

name_entry = tk.Entry(root, font=("Arial", 12))
name_entry.pack(pady=5)

#Label Prénom
surname_label = tk.Label(root, text="Prénom:", font=("Arial", 12), bg="lightblue")
surname_label.pack(pady=5)

surname_entry = tk.Entry(root, font=("Arial", 12))
surname_entry.pack(pady=5)

def greet_user():
    try:
        name = name_entry.get().strip()
        surname = surname_entry.get().strip()
        if name and surname:
            greeting = f"Bonjour, {name} {surname} !"
        elif name:
            greeting = f"Bonjour, {name} ! Veuillez entrer votre prénom."
        elif surname:
            greeting = f"Bonjour, {surname} ! Veuillez entrer votre nom."
        else:
            greeting = "Bonjour ! Veuillez entrer votre nom et prénom."
        greeting_label.config(text=greeting)
    except Exception as e:
        greeting_label.config(text=f"Erreur : {e}")
        raise
        
def reset_fields():
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    greeting_label.config(text="")

# Label pour afficher le message de salutation
greeting_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
greeting_label.pack(pady=10)

greet_button = tk.Button(root, text="Saluer", font=("Arial", 12), command=greet_user, bg="green", fg="white")
greet_button.pack(pady=10)

reset_button = tk.Button(root, text="Réinitialiser", font=("Arial", 12), command=reset_fields, bg="red", fg="white")
reset_button.pack(pady=5)

root.mainloop()
