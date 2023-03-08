def generate_class_def(nom_classe: str, attributs: dict, nom_superclasse: str, args_superclasse: list = [])
    args_constructeur = []
    definition_constructeur = ""
    has_attributs = False
    modele_classe = f"class {nom_classe}"

# Gestion de la superclasse
if nom_superclasse:
    modele_classe += " :\n"

# Gestion de la classe
if nom_classe == "Product":
    definition_constructeur += "\n\t\t self.name = type(self).__name__"

# Gestion constructeur
if has_attributs:
    modele_constructeur = f"\t def __init__(self, {", ".join(args_constructeur + args_superclasse)}) : "

    if len(args_superclasse) > 0:
        modele_constructeur += definition_constructeur

else:
    if len(args_superclasse) > 0:
        modele_constructeur = f"\t def __init__(self, {", ".join(args_superclasse)}) : "
        modele_constructeur = f"\n\t\t super().__init__({", ".join(args_superclasse)})"