# Import des modules nécessaires
import json
import os
import re
from unidecode import unidecode

# Get the directory path of the current Python file
local_path = os.path.dirname(os.path.abspath(__file__))
# Chargement des données JSON à partir du fichier dans un dictionnaire python
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))

# il est nécessaire de convertir le dictionnaire en chaine de caractere pour le traiter ensuite
json_str = json.dumps(json_data)

# Utilisation de la fonction unidecode pour enlever les accents et autres caractères spéciaux
json_data = (unidecode(json_str))

# Conversion de la chaine de caractere JSON à nouveau en dictionnaire Python
json_dict = json.loads(json_data)

# nous allons a présent utiliser la classe Tree de la librairie treelib pour construire un arbdre de donnée

from treelib import Tree

def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
        if isinstance(value, dict):
            # Créer un nouveau noeud pour la clé courante du dictionnaire
            new_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
            
            # Créer récursivement le sous-arbre pour le dictionnaire courant
            create_tree_from_dict(tree, new_node_id, value)
        else:
            # Créer un nouveau noeud pour la feuille courante du dictionnaire
            leaf_node_id = f"{parent_node_id}.{key}"
            tree.create_node(tag=f"{key}: {value}", identifier=leaf_node_id, parent=parent_node_id)

# Exemple de dictionnaire
my_dict = {
    "cle1": {
        "souscle1": "valeur1",
        "souscle2": "valeur2",
        "souscle3": "valeur3"
    },
    "cle2": "valeur4",
    "cle3": {
        "souscle4": "valeur5"
    }
}

# Créer un nouvel arbre
my_tree = Tree()

# Créer le noeud racine pour l'arbre
my_tree.create_node(tag="Racine", identifier="racine")

# Créer la structure de l'arbre à partir du dictionnaire
create_tree_from_dict(my_tree, "racine", my_dict)

# Afficher l'arbre
my_tree.show()

"""
- Dans cet exemple, la fonction create_tree_from_dict() parcourt récursivement le dictionnaire d'entrée 
et ajoute chaque paire clé-valeur en tant que noeud dans l'arbre. 

- Si une valeur de dictionnaire est rencontrée, un nouveau noeud est créé pour la clé, 
et la fonction est appelée récursivement pour créer un sous-arbre pour la valeur de dictionnaire. 

- Si une valeur non-dictionnaire est rencontrée, un nouveau noeud est créé pour la paire clé-valeur.

- Une fois que l'arbre est construit, sa méthode show() est appelée pour afficher la structure de l'arbre dans la console. 
"""