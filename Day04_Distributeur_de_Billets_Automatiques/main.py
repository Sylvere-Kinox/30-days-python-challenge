#Mini distributeur de billets automatique
class Compte_bancaire :
    def __init__(self, num_compte, pin, solde=0):
        self.num_compte = num_compte
        self.__pin = pin
        self.__solde = solde
        
    def validation_pin (self, pin_entrer):
        return pin_entrer == self.__pin

    def verifiation_solde(self):
        print(f"Le solde courant est {self.__solde}")
        
    def depot(self, montant2depot):
        if montant2depot > 0:
            self.__solde += montant2depot
            print(f"Vous venez de faire un dépôt de {montant2depot}, votre solde courant est {self.__solde}.")
        else:
            print(f"Montant invalide, veuillez entrez un montant raisonnable.")
        
    def retrait(self, montant2retrait):
        if montant2retrait > self.__solde :
            print(f"Solde insuffisant")
        elif montant2retrait > 0:
            self.__solde -= montant2retrait
            print(f"Vous venez de faire un retrait de {montant2retrait}, votre solde courant est {self.__solde}.")
        else:
            print(f"Montant invalide, veuillez entrez un montant raisonnable.")
            
    def modif_pin(self, old_pin, new_pin):
        if self.validation_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("Code pin changer avec succes.")
        else:
            print("Echec du changement du code Pin.")
            
            
class ATM:
    def __init__(self,):
        self.compte = {}
        
    def creer_compte(self) :
        num_compte = input("Entrez un numero de compte :")
        pin = input("Créer un code pin à 4 chiffres :")
        if len(pin) == 4 and pin.isdigit():
            if num_compte in self.compte:
                    print("Ce numéro de compte existe déjà.")
                    return
            else:
                self.compte[num_compte] = Compte_bancaire(num_compte, pin)
                print("Compte créer avec succes.")
        else :
            print("Code Pin invalide. Veuillez entrez un code à 4 chiffres.")            
            
    def authent_coompte(self) :
        num_compte = input("Entrez un numero de compte :")
        pin = input("Entrez votre code pin :")

        compte = self.compte.get(num_compte)
        if compte and compte.validation_pin(pin):
            print("Authentification réussie.")
            self.menu_compte(compte)
        else:   
            print("Numéro de compte ou code pin incorrect.")
            
    def menu_compte(self, compte):
        while True:
            print("\n=== Menu du Compte ===")
            print("1. Vérifier le solde")
            print("2. Déposer de l'argent")
            print("3. Retirer de l'argent")
            print("4. Changer le code pin")
            print("5. Déconnexion")

            choix = input("Choisissez une option : ")

            if choix == "1":
                compte.verifiation_solde()
            elif choix == "2":
                try:
                    montant2depot = float(input("Entrez le montant à déposer : "))
                    compte.depot(montant2depot)
                except ValueError:
                    print("Montant invalide. Veuillez entrer un nombre.")
            elif choix == "3":
                try:
                    montant2retrait = float(input("Entrez le montant à retirer : "))
                    compte.retrait(montant2retrait)
                except ValueError:
                    print("Montant invalide. Veuillez entrer un nombre.")
            elif choix == "4":
                old_pin = input("Entrez votre ancien code pin : ")
                new_pin = input("Entrez votre nouveau code pin à 4 chiffres : ")
                compte.modif_pin(old_pin, new_pin)
            elif choix == "5":
                print("Déconnexion du compte.")
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")
        
    #Programme principal
    def main_menu(self):
        while True:
            print("\n=== Menu Principal ===")
            print("1. Créer un compte")
            print("2. Se connecter à un compte")
            print("3. Quitter")
        
            choix = input("Choisissez une option : ")
        
            if choix == "1":
                self.creer_compte()
            elif choix == "2":
                self.authent_coompte()
            elif choix == "3":
                print("Merci d'avoir utiliser le ditributeur automatique. Au revoir!")
                break
            else:
                print("Option invalide. Veuillez choisir une option valide.")
            
if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()
    