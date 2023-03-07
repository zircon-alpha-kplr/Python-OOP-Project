def generate_class_def(nom_classe: str, attributs: dict, nom_superclasse: str, args_superclasse: list = []) -> str:
    # Cette fonction génère une définition de classe Python à partir des paramètres passés et retourne une chaîne de caractères représentant la définition de classe générée.

    # Initialisation des variables
    args_constructeur = [] # une liste qui stocke les noms des attributs qui seront utilisés pour créer le constructeur
    definition_constructeur = "" # une chaîne de caractères qui stocke le code qui sera utilisé pour initialiser les attributs de la classe
    has_attributs = False # un booléen qui vérifie si la classe a des attributs ou non
    modele_classe = f"class {nom_classe}" # une chaîne de caractères qui stocke la définition de base de la classe

    # Gestion de la superclasse
    if nom_superclasse: # si la classe a une superclasse
        modele_classe += f"({nom_superclasse})" # ajouter la superclasse à la définition de la classe

    modele_classe += ":\n" # ajouter une nouvelle ligne à la définition de la classe

    # Gestion des attributs
    for nom_attribut in attributs.keys(): # pour chaque attribut dans le dictionnaire d'attributs
        if nom_attribut != "subclasses": # si l'attribut n'est pas une sous-classe
            has_attributs = True # la classe a des attributs
            args_constructeur.append(nom_attribut) # ajouter le nom de l'attribut à la liste des arguments du constructeur
            definition_constructeur += f"\n\t\tself.{nom_attribut} = {nom_attribut}" # ajouter une ligne au code de définition du constructeur pour initialiser l'attribut

    # Gestion du nom de la classe si c'est une classe Product
    if nom_classe == "Product": # si la classe est de type Product
        definition_constructeur += "\n\t\tself.name=type(self).__name__" # ajouter une ligne au code de définition du constructeur pour initialiser le nom de la classe

    # Gestion du constructeur
    if has_attributs: # la classe a des attributs
        modele_constructeur = f"\tdef __init__(self, {', '.join(args_constructeur + args_superclasse)}):" # créer la signature du constructeur en incluant les arguments des attributs et les arguments de la superclasse

        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})" # ajouter une ligne pour initialiser la superclasse

        modele_constructeur += definition_constructeur # ajouter le code d'initialisation des attributs à la définition du constructeur
   
    else: # la classe n'a pas d'attributs
        if len(args_superclasse) > 0: # si la superclasse a des arguments
            modele_constructeur = f"\tdef __init__(self, {', '.join(args_superclasse)}):" # créer la signature du constructeur en incluant les arguments de la superclasse
            modele_constructeur += f"\n\t\tsuper().__init__({', '.join(args_superclasse)})"
      
        else:    
            modele_constructeur = "\tpass"

    return modele_classe + modele_constructeur + "\n\n"


def test_fonction():
    
    attributs = {
    "moteur": "str",
    "nbportes": "int"
    }

    code_classe = generate_class_def("Voiture", attributs, "Vehicule", ["marque", "modele"])
    print(code_classe)

if __name__ == '__main__':
    # Appeler la fonction principale
    test_fonction()