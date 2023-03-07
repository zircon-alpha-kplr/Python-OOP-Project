# Import des modules nécessaires
import json
import os
import re
from unidecode import unidecode
from treelib import Tree

# Get the directory path of the current Python file
local_path = os.path.dirname(os.path.abspath(__file__))
# Load JSON from file in a dictionary
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb"))

# Convert the dictionary in string
json_str = json.dumps(json_data)

# Use unidecode to remove special character
json_data = (unidecode(json_str))

# Convert string to the dictionary again
json_dict = json.loads(json_data)


# Function to create Tree
def create_tree_from_dict(tree, parent_node_id, parent_dict):
    """
    Cette fonction crée un arbre à partir d'un dictionnaire.
    Elle est appelée récursivement pour chaque sous-dictionnaire.

    Args:
        tree (Tree): un objet Tree de la bibliothèque treelib pour représenter l'arbre
        parent_node_id (str): l'identifiant du noeud parent dans l'arbre
        parent_dict (dict): le dictionnaire Python contenant les données à insérer dans l'arbre
    """
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

def main():
    """
    Cette fonction est la fonction principale qui orchestre toutes les autres.
    Elle charge les données JSON depuis un fichier, crée un objet Tree de la bibliothèque treelib,
    et crée un arbre à partir des données JSON.

    Elle affiche ensuite l'arbre créé.
    """
    my_tree = Tree()
    # Créer le noeud racine pour l'arbre
    my_tree.create_node(tag="Racine", identifier="racine")

    # Charger les données JSON depuis un fichier et créer la structure de l'arbre à partir du dictionnaire
    create_tree_from_dict(my_tree, "racine", json_dict)

    # Afficher l'arbre
    my_tree.show()

if __name__ == '__main__':
    # Appeler la fonction principale
    main()
