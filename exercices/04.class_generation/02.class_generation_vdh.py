def generate_class_def(nom_classe: str, attributs: dict, nom_superclasse: str, args_superclasse: list = []):
    args_constructeur = []
    definition_constructeur = ""
    has_attributs = False
    modele_classe = f"class {nom_classe}"

    # Gestion de la superclasse
    if nom_superclasse:
        modele_classe += f"({nom_superclasse})"
    
        modele_classe += " :\n"

    # Gestion des attributs
    for nom_attribut in attributs.keys():
        if nom_attribut != "subclasses":
            has_attributs = True
            args_constructeur.append(nom_attribut)
            definition_constructeur += f"\n\t self.{nom_attribut} = {nom_attribut}"

    # Gestion de la classe
    if nom_classe == "Product":
        definition_constructeur += "\n\t\t self.name = type(self).__name__"

    # Gestion constructeur
    if has_attributs:
        modele_constructeur = f"\t def __init__(self, {', '.join(args_constructeur + args_superclasse)}) : "

        if len(args_superclasse) > 0:
            modele_constructeur += f"\n\t\t super().__init__({', '.join(args_superclasse)})"
        
        modele_constructeur += definition_constructeur

    else:
        if len(args_superclasse) > 0:
            modele_constructeur = f"\t def __init__(self, {', '.join(args_superclasse)}) : "
            modele_constructeur = f"\n\t\t super().__init__({', '.join(args_superclasse)})"
    
        else:
            modele_constructeur = "\t pass"

    return modele_classe + modele_constructeur + "\n\n"


if __name__ == '__main__':
    # Appeler la fonction principale
    test_fonction()


def test_fonction():
    attributs = {
    "moteur": "str",
    "nbportes": "int"
    }

    code_classe = generate_class_def("Voiture", attributs, "Vehicule", ["marque", "modele"])
    print(code_classe)