# Date
# Category
# Amount
# Description

import csv
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

def log_expense(date, category, amount, description):
	with open('expenses.csv', 'a', newline="") as file:
		writer = csv.writer(file)
		writer.writerow([date, category, amount, description])



def load_expenses():
    return pd.read_csv(
        "expenses.csv",
        names=["Date", "Categorie", "Compte", "Description"],
        encoding="latin-1"
    )

def summarize_expenses(df):
	summary = df.groupby("Categorie")["Compte"].sum()
	print("\n Résumé des dépenses:")
	print(summary)




def plot_expenses_by_category(df):
	summary = df.groupby("Categorie")["Compte"].sum()
	summary.plot(kind="pie", autopct="%1.1f%%", figsize=(8,8), title="Dépenses par catégorie")
	plt.ylabel("")
	plt.show()


def plot_monthly_trends(df):
	df["Date"] = pd.to_datetime(df["Date"])
	df["Mois"] = df["Date"].dt.to_period("M")
	monthly_summary = df.groupby("Mois")["Compte"].sum()
	monthly_summary.plot(kind="bar", figsize=(10, 6), title="Tendances Mensuelles des Dépenses")
	plt.xlabel("Mois")
	plt.ylabel("Dépenses Totales")
	plt.xticks(rotation=45)
	plt.show()





def main():
    df = load_expenses()
    while True:
        print("\nMenu :")
        print("1. Ajouter une dépense")
        print("2. Résumer les dépenses par catégorie")
        print("3. Afficher un graphique des dépenses par catégorie")
        print("4. Afficher les tendances mensuelles des dépenses")
        print("5. Quitter")

        choix = input("Entrez le numéro correspondant à votre choix : ")

        if choix == "1":
            date = input("Entrez la date (YYYY-MM-DD) : ")
            category = input("Entrez la catégorie : ")
            amount = float(input("Entrez le montant : "))
            description = input("Entrez la description : ")
            log_expense(date, category, amount, description)
            df = load_expenses()  # Recharger les données après l'ajout
        elif choix == "2":
            summarize_expenses(df)
        elif choix == "3":
            plot_expenses_by_category(df)
        elif choix == "4":
            plot_monthly_trends(df)
        elif choix == "5":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
            
if __name__ == "__main__":
    main()