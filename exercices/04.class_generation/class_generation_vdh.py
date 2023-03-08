def generate_class_def(class_name: str, class_attributs: dict, superclass_name: str, superclass_args: list = []):
    args_constructeur = []
    definition_constructeur = ""
    has_attributs = False
    modele_classe = f"class {class_name}"

    # Gestion de la superclasse
    if superclass_name:
        modele_classe += f"({superclass_name})"
    
        modele_classe += " :\n"

    # Gestion des class_attributs
    for name_attribut in class_attributs.keys():
        if name_attribut != "subclasses":
            has_attributs = True
            args_constructeur.append(name_attribut)
            definition_constructeur += f"\n\t self.{name_attribut} = {name_attribut}"

    # Gestion de la classe
    if class_name == "Product":
        definition_constructeur += "\n\t\t self.name = type(self).__name__"

    # Gestion constructeur
    if has_attributs:
        modele_constructeur = f"\t def __init__(self, {', '.join(args_constructeur + superclass_args)}) : "

        if len(superclass_args) > 0:
            modele_constructeur += f"\n\t\t super().__init__({', '.join(superclass_args)})"
        
        modele_constructeur += definition_constructeur

    else:
        if len(superclass_args) > 0:
            modele_constructeur = f"\t def __init__(self, {', '.join(superclass_args)}) : "
            modele_constructeur = f"\n\t\t super().__init__({', '.join(superclass_args)})"
    
        else:
            modele_constructeur = "\t pass"

    return modele_classe + modele_constructeur + "\n\n"

"""
def test_fonction():
    class_attributs = {
    "moteur": "str",
    "nbportes": "int"
    }

    code_classe = generate_class_def("Voiture", class_attributs, "Vehicule", ["marque", "modele"])
    print(code_classe)

    
if __name__ == '__main__':
    # Appeler la fonction principale
    test_fonction()

"""