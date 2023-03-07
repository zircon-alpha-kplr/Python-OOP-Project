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
def create_tree_from_dict(json_dict):
    # define the tree
    global tree 
    tree = Tree()

    # define the root node
    root_node_id = "root"
    root_node_name = "Product Classes Hierarchy"
    tree.create_node(root_node_name, root_node_id)

    #traverse json data and creathe other node
    recursive_tree_from_dict(json_dict, root_node_id)

    return tree


def recursive_tree_from_dict(json_dict, parent_node_id):
    for class_name, class_attrs in json_dict.items():
            class_node_id = class_name
            class_node_name = class_name

            # Add the class node to the tree
            tree.create_node(class_node_name, class_node_id, parent=parent_node_id)

            # Traverse any subclasses
            if "subclasses" in class_attrs:
                recursive_tree_from_dict(class_attrs["subclasses"], class_node_id)


# func MAIN
def main():
    json_dict = json_dict_from_file() #call func "json_dict_from_file() : Load JSON and convert to dict
    my_tree = create_tree_from_dict(json_dict)
    my_tree.show() #Show class tree


# call main function
if __name__ == '__main__':
    main()
