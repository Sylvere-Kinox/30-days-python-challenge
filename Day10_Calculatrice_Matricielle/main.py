import numpy as np

#Fonction pour prendre les entrées de l'utilisateur

def get_user_input():
    try:
        rows = int(input("Entrez le nombre de lignes de la matrice: "))
        cols = int(input("Entrez le nombre de colonnes de la matrice: "))
        print("Entrez les éléments de la matrice ligne par ligne:")
        elements = []
        for i in range(rows):
            row_elements = list(map(float, input(f"Ligne {i + 1}: ").split()))
            if len(row_elements) != cols:
                raise ValueError("Le nombre d'éléments dans la ligne ne correspond pas au nombre de colonnes spécifié.")
            elements.append(row_elements)
        return np.array(elements)
    except ValueError as e:
        print(f"Erreur: {e}")
        return None
    
#Operations matricielles
def operations_matricielles(A, B):
    print("=== Opérations Matricielles ===")
    print("Matrice A:", A)
    print("Matrice B:", B)
    
    try:
        print("\nAddition:\n", A + B)
    except ValueError:
        print("Erreur: Les matrices doivent avoir les mêmes dimensions pour l'addition.")
        
    try:
        print("\nSoustraction:\n", A - B)
    except ValueError:
        print("Erreur: Les matrices doivent avoir les mêmes dimensions pour la soustraction.")
        
    try:
        print("\nMultiplication:\n", np.dot(A, B))
    except ValueError:
        print("Erreur: Les matrices doivent avoir des dimensions compatibles pour la multiplication.")
    
    print("\nTransposée de A:\n", A.T)
    print("\nTransposée de B:\n", B.T)    
        
    try:
        print("\nDeterminant de A:", np.linalg.det(A))
    except np.linalg.LinAlgError:
        print("Erreur: La matrice A n'est pas inversible.")

    try:
        print("\nInverse de A:\n", np.linalg.inv(A))
    except np.linalg.LinAlgError:
        print("Erreur: La matrice A n'est pas inversible.")
        
        
#Programme principal
def main():
    print("=== Calculatrice Matricielle ===")
    print("Entrez les éléments de la première matrice (A):")
    A = get_user_input()
    if A is None:
        return
    
    print("\nEntrez les éléments de la deuxième matrice (B):")
    B = get_user_input()
    if B is None:
        return
    
    operations_matricielles(A, B)
if __name__ == "__main__":
    main()