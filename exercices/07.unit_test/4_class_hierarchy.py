# Import modules
import os
import json
import re
from unidecode import unidecode
import class_generation_vdh

"""
def trimspaces(data):
    import re
    # Define a regular expression pattern to match quoted substrings
    pattern = r'"[^"]*"'
    # Replace spaces and hyphens with underscore
    #return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), str(unidecode(json.dumps(data))))
    data_s=json.dumps(data)
    return re.sub(pattern, lambda m: m.group(0).replace(" ", "_").replace("-", "_"), data_s)
"""

#load JSON and convert to dict
local_path = os.path.dirname(os.path.abspath(__file__)) #
json_data = json.load(open(os.path.join(local_path, 'json_data.json'), "rb")) #load file JSON
json_str = json.dumps(json_data) #.dumps to convert to string
json_data = (unidecode(json_str)) #remove specials
#json_data = trimspaces(json_data)
json_dict = json.loads(json_data) #.loads : re-assign to json_dict

def generate_class_hierarchy(json_dict :dict, superclass_name:str=None, superclass_args:list=[]):
    # Initialisation de la chaîne de caractères contenant les définitions de classes
    class_defs = ""

    for class_name, class_attrs in json_dict.items():

        class_def = class_generation_vdh.generate_class_def(class_name, class_attrs, superclass_name,superclass_args)
        class_defs += class_def

        if "subclasses" in class_attrs:
            super_attr = (list(class_attrs.keys())+superclass_args)
            super_attr.remove("subclasses")
            subclass_defs = generate_class_hierarchy(class_attrs["subclasses"], class_name, super_attr)
            class_defs += subclass_defs

    return class_defs

# la méthode write_content va nous permet d'écrire le code généré automatiquement des classes dans un fichier Python séparé
def write_content(content,filename):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(content)


# Main Func
if __name__ == '__main__':
    # Appeler la fonction principale
    
    write_content(generate_class_hierarchy(json_dict), local_path+"/product_classes.py")