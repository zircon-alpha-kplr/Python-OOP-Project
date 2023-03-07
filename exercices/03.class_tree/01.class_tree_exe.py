#import libraries & modules
import os
import json
from unidecode import unidecode
from treelib import Tree

#func to load JSON and convert to dict
def json_dict_from_file():
    local_path = os.path.dirname(os.path.abspath(__file__)) #
    json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb")) #load file JSON
    json_str = json.dumps(json_data) #.dumps to convert to string
    json_data = (unidecode(json_str)) #remove specials
    json_dict = json.loads(json_data)
    return json_dict

# func to create a tree from a dict
def create_tree_from_dict(tree, parent_node_id, parent_dict):
    for key, value in parent_dict.items():
#        if key != ("subclasses"):
            if isinstance(value, dict):
               # Créer un nouveau noeud pour la clé courante du dictionnaire
               new_node_id = f"{parent_node_id}.{key}"
               tree.create_node(tag=key, identifier=new_node_id, parent=parent_node_id)
               create_tree_from_dict(tree, new_node_id, value) # Créer récursivement le sous-arbre pour le dictionnaire courant
 #       else:
 #           continue

# func to create recursive tree

# func MAIN
def main():
    json_dict = json_dict_from_file() #call func "json_dict_from_file() : Load JSON and convert to dict
    my_tree = Tree() #create Tree
    my_tree.create_node(tag="Product Classes Hierarchy", identifier="racine") #create le noeud racine pour l'arbre
    create_tree_from_dict(my_tree, "racine", json_dict) #créer la structure de l'arbre à partir du dictionnaire
    my_tree.show() #Show class tree


# call main function
if __name__ == '__main__':
    main()